#!/usr/bin/env python3
"""Phase 3 prep v2: number-aware clustering of event claims into unique verification groups."""
import json, re, glob
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"

def salient_numbers(text):
    t = text.replace(",", "")
    nums = []
    for m in re.finditer(r"\d+(?:\.\d+)?", t):
        s = m.group(0)
        if len(s) >= 3 or float(s) < 1900:  # skip years when short
            nums.append(s.rstrip("."))
    # drop pure years unless accompanied
    return [n for n in nums if n not in ("2018","2019","2020","2021","2022","2023","2024","2025","2026")][:6]

def normtext(t):
    t = t.lower()
    t = re.sub(r"[₹$%]", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

STOP = set("""the a an of in on at to for with by from and or is are was were be been it its this that these those market markets nifty bank index points point crore lakh per cent percent day days week weeks month year""".split())

def keywords(text, k=6):
    toks = [w for w in normtext(text).split() if w not in STOP and len(w) > 3]
    freq = {}
    for w in toks: freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: -x[1])[:k]]

claims = []
for f in glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl"):
    for l in open(f, encoding="utf-8"):
        try: r = json.loads(l)
        except Exception: continue
        for e in r.get("events", []) or []:
            if isinstance(e, dict) and e.get("claim") and len(e["claim"]) > 20:
                claims.append({"claim": e["claim"], "date": r.get("date"), "src": r.get("id")})

# prior events
prior = []
title = None
for line in open(f"{ROOT}/PR_Sundar_Market_History.md", encoding="utf-8"):
    if line.startswith("### "):
        if title: prior.append(title)
        title = {"title": line[4:].strip(), "what": ""}
    elif title and line.strip().startswith("- **What happened:**"):
        title["what"] = line.strip()[len("- **What happened:**"):].strip()
if title: prior.append(title)
for p in prior:
    claims.append({"claim": p["title"] + " :: " + p["what"][:280], "date": None, "src": "prior_history"})

# cluster: same year-month (from claim date or source date) + >=2 shared salient numbers
def month_of(c):
    if c["date"]: return c["date"][:7]
    return None

clusters = []
used = [False] * len(claims)
info = []
for c in claims:
    info.append({"nums": set(salient_numbers(c["claim"])), "kw": set(keywords(c["claim"], 8)), "mon": month_of(c)})

order = sorted(range(len(claims)), key=lambda i: -len(info[i]["nums"]))
for i in order:
    if used[i]: continue
    cluster = [i]; used[i] = True
    for j in order:
        if used[j]: continue
        a, b = info[i], info[j]
        shared_nums = a["nums"] & b["nums"]
        shared_kw = a["kw"] & b["kw"]
        same_time = (a["mon"] == b["mon"]) or (a["mon"] is None) or (b["mon"] is None)
        if same_time and len(shared_nums) >= 2 and len(shared_kw) >= 2:
            cluster.append(j); used[j] = True
    members = [claims[k] for k in cluster]
    longest = max(members, key=lambda m: len(m["claim"]))
    clusters.append({
        "claim": longest["claim"],
        "date": next((m["date"] for m in members if m["date"]), None),
        "sources": sorted({str(m["src"]) for m in members if m["src"]}),
        "times_seen": len(members),
        "salient_numbers": sorted(info[i]["nums"]),
    })

json.dump(clusters, open(f"{ROOT}/book/events/queue_clusters.json", "w"), indent=1)
print("raw:", len(claims), "clusters:", len(clusters))
big = sum(1 for c in clusters if c["times_seen"] >= 3)
print("clusters seen >=3x:", big)
from collections import Counter
print("size dist:", dict(Counter(min(c["times_seen"],10) for c in clusters)))
