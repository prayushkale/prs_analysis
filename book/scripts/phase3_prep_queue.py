#!/usr/bin/env python3
"""Phase 3 prep (no LLM): extract event claims from completed batch JSONLs,
parse prior events from PR_Sundar_Market_History.md, dedupe into a verification queue."""
import json, re, glob, hashlib
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"

# 1) claims from new analysis
claims = []
for f in glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl"):
    for l in open(f, encoding="utf-8"):
        try:
            r = json.loads(l)
        except Exception:
            continue
        src = r.get("id")
        date = r.get("date")
        for e in r.get("events", []) or []:
            if isinstance(e, dict) and e.get("claim"):
                claims.append({"source_id": src, "date": date, "claim": e["claim"], "verify": e.get("verify", True)})
        for s in r.get("strategies", []) or []:
            pass  # strategies verified differently (internal math)

# 2) prior events from Market_History.md
prior = []
cur = None
for line in open(f"{ROOT}/PR_Sundar_Market_History.md", encoding="utf-8"):
    if line.startswith("### "):
        if cur: prior.append(cur)
        cur = {"title": line[4:].strip(), "fields": {}}
    elif cur is not None:
        m = re.match(r"- \*\*(.+?):\*\* (.*)", line.strip())
        if m:
            cur["fields"][m.group(1)] = m.group(2)
        elif line.startswith("- **Source video:**"):
            pass
if cur: prior.append(cur)
print("new claims:", len(claims), "| prior events:", len(prior))

def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ₹$%.]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def keyf(text, date):
    nums = re.findall(r"\d[\d,\.]*", text)
    toks = [w for w in norm(text).split() if len(w) > 4]
    return (date or "", "|".join(sorted(set(nums))[:8]), "|".join(sorted(set(toks))[:8]))

# 3) dedupe: bucket by (approx-date, strongest numeric signature) then fuzzy
buckets = defaultdict(list)
for c in claims:
    k = keyf(c["claim"], c["date"])
    buckets[k].append(c)

queue = []
for k, group in buckets.items():
    best = max(group, key=lambda c: len(c["claim"]))
    queue.append({
        "claim": best["claim"],
        "date": best["date"],
        "sources": sorted({c["source_id"] for c in group if c["source_id"]}),
        "times_seen": len(group),
    })

# merge prior events (title+what happened) as additional queue items
for p in prior:
    what = p["fields"].get("What happened", "")
    d = p["fields"].get("Source video", "")
    md = re.search(r"\((\d{1,2} \w+ \d{4}|[\d–\- ]+ \w* ?20\d\d[^)]*)\)", p["title"])
    date = None
    if md:
        raw = md.group(1)
        m2 = re.search(r"(\d{4})", raw)
        mon = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)", raw, re.I)
        if m2 and mon:
            months = {m.lower(): i+1 for i, m in enumerate(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])}
            day = re.search(r"(\d{1,2})\s+" + mon.group(1), raw, re.I)
            date = f"{m2.group(1)}-{months[mon.group(1).lower()]:02d}-{int(day.group(1)):02d}" if day else f"{m2.group(1)}-{months[mon.group(1).lower()]:02d}"
    queue.append({
        "claim": (p["title"] + " — " + what[:300]).strip(),
        "date": date,
        "sources": ["prior_history"],
        "times_seen": 1,
        "prior": True,
    })

# final dedupe by normalized title head
seen = {}
final = []
for q in queue:
    h = hashlib.md5(norm(q["claim"])[:180].encode()).hexdigest()
    if h in seen:
        seen[h]["sources"] = sorted(set(seen[h]["sources"] + q["sources"]))
        seen[h]["times_seen"] += 1
    else:
        seen[h] = q
        final.append(q)

json.dump(final, open(f"{ROOT}/book/events/queue_deduped.json", "w"), indent=1)
print("deduped verification queue:", len(final))
dated = sum(1 for q in final if q["date"])
print("with parsed date:", dated)
