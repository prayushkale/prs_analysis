#!/usr/bin/env python3
"""Phase 3b: fetch REST summaries for key entities and also query Google News RSS."""

import json, time, urllib.request, urllib.parse, re

ROOT = "/home/ubuntu/repos/prs_analysis"

ENTITIES = [
    "2024 Indian general election",
    "2019 Indian general election",
    "2025 Bihar Legislative Assembly election",
    "Nirmala Sitharaman",
    "2022 Union budget of India",
    "2024 Union budget of India",
    "Cryptocurrency and taxation in India",
    "Hindenburg Research",
    "Adani Group",
    "Madhabi Puri Buch",
    "Life Insurance Corporation of India",
    "HDFC Bank",
    "Hyundai Motor India",
    "Russian invasion of Ukraine",
    "2020 stock market crash",
    "NIFTY 50",
    "2024 United States presidential election",
    "August 2024 global stock selloff",
    "2019 Pulwama attack",
    "2016 Uri attack",
    "Kargil War",
    "China–United States trade war",
    "2022 Federal Reserve",
    "China Evergrande Group",
    "GameStop short squeeze",
    "Yes Bank",
    "IL&FS",
    "Franklin Templeton Investments",
    "Vauld",
]

def rest_summary(title):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(title.replace(" ", "_"))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as r:
            d = json.loads(r.read().decode("utf-8"))
            return {"title": d.get("title"), "extract": (d.get("extract") or "")[:600]}
    except Exception as e:
        return {"title": title, "error": str(e)}

out = []
existing = set()
try:
    for line in open(f"{ROOT}/book/events/evidence_raw.jsonl"):
        row = json.loads(line)
        existing.add(row.get("entity"))
        out.append(row)
except FileNotFoundError:
    pass

added = 0
for e in ENTITIES:
    if e in existing:
        continue
    res = rest_summary(e)
    out.append({"query": "REST " + e, "entity": e, "result": [{"title": res.get("title") or e, "snippet": res.get("extract", "")}], "ts": time.time()})
    added += 1
    time.sleep(0.15)

with open(f"{ROOT}/book/events/evidence_raw.jsonl", "w") as f:
    for row in out:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"rows: {len(out)} (added {added} REST)")

# Google News RSS check for a couple of critical items
def news(q):
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q + " when:2y")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as r:
            xml = r.read().decode("utf-8")
        titles = re.findall(r"<title>(.*?)</title>", xml)[1:6]
        return titles
    except Exception as e:
        return [f"err:{e}"]

for q in ["Jane Street SEBI penalty 2025", "SEBI contract size 15 lakh 2024", "Nifty 26300 September 2024"]:
    print("\nNEWS:", q)
    print(json.dumps(news(q), ensure_ascii=False, indent=1))
    time.sleep(0.3)