#!/usr/bin/env python3
"""Scan all analysis batch JSONLs, compile per-chapter source candidates.
Output: book/chapters/sources_per_chapter.json {ch_num: [{id,date,summary,lessons,chapter_targets,themes,strategies,events,quotes,subtype}]}
Also produce compact per-chapter brief template files."""
import json, glob, sys

ROOT = "/home/ubuntu/repos/prs_analysis"

# Scan all analysis records
records = []
for f in sorted(glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl")):
    for l in open(f, encoding="utf-8"):
        try:
            r = json.loads(l)
            records.append(r)
        except:
            pass
print("total analysis records:", len(records))

# Chapter map from editorial
ch_map = {
    1: "why traders lose",
    2: "anatomy of failure",
    3: "discipline/process",
    4: "FII/DII flows",
    5: "VIX regimes",
    6: "option chain",
    7: "microstructure",
    8: "why derivatives exist",
    9: "calls and puts",
    10: "greeks",
    11: "implied volatility",
    12: "margins/collateral",
    13: "short straddles/strangles",
    14: "spreads and ratio spreads",
    15: "calendar spreads",
    16: "butterflies/condors",
    17: "portfolio hedges",
    18: "firefighting/adjustments",
    19: "event playbook",
    20: "budgets/elections",
    21: "wars/black swans",
    22: "chronicle 2018-2020",
    23: "chronicle 2021-2022",
    24: "chronicle 2023-2024",
    25: "chronicle 2025-2026",
    26: "retail scams",
    27: "regulation",
    28: "taxation",
    29: "investing vs trading",
    30: "real assets",
    31: "crypto",
}

# Map each record to its best chapter
sources = {k: {"title": v, "records": []} for k, v in ch_map.items()}
unmapped = 0
for r in records:
    # Check chapter_targets field first
    ct = r.get("chapter_targets", [])
    if isinstance(ct, int):
        ct = [ct]
    if ct and isinstance(ct[0], int):
        for ch in ct:
            if ch in sources:
                sources[ch]["records"].append(r)
        continue
    # Try matching by theme keywords
    t = (r.get("type","") + " " + " ".join(r.get("themes",[]) + [r.get("subtype","")])).lower()
    # simple heuristic mapping
    if any(k in t for k in ["why no to trading","failure","psychology","discipline","gambling"]):
        sources[1]["records"].append(r)
    elif any(k in t for k in ["fil dii","flow","institutional"]):
        sources[4]["records"].append(r)
    elif any(k in t for k in ["vix","volatility index","implied volatility","iv rank"]):
        sources[5]["records"].append(r)
    elif any(k in t for k in ["open interest","option chain","max oi","pcr", "put call ratio"]):
        sources[6]["records"].append(r)
    elif any(k in t for k in ["gap","expiry","microstructure","index construction","etf rebalancing"]):
        sources[7]["records"].append(r)
    elif any(k in t for k in ["mission options","derivative","futures","forward"]):
        sources[8]["records"].append(r)
    elif any(k in t for k in ["calls","puts","itm","atm","otm","strike","payoff"]):
        sources[9]["records"].append(r)
    elif any(k in t for k in ["delta","gamma","vega","theta","greeks","option greeks"]):
        sources[10]["records"].append(r)
    elif any(k in t for k in ["straddle","strangle"]):
        sources[13]["records"].append(r)
    elif any(k in t for k in ["ratio","spread"]):
        sources[14]["records"].append(r)
    elif any(k in t for k in ["calendar"]):
        sources[15]["records"].append(r)
    elif any(k in t for k in ["butterfly","condor"]):
        sources[16]["records"].append(r)
    elif any(k in t for k in ["hedge","hedging","protective put","collar","insurance"]):
        sources[17]["records"].append(r)
    elif any(k in t for k in ["firefight","adjustment","rescue","recover"]):
        sources[18]["records"].append(r)
    elif any(k in t for k in ["event","playbook","binary"]):
        sources[19]["records"].append(r)
    elif any(k in t for k in ["budget","election"]):
        sources[20]["records"].append(r)
    elif any(k in t for k in ["war","black swan","crash","pandemic","geopolitics"]):
        sources[21]["records"].append(r)
    elif any(k in t for k in ["scam","fraud","broker cheat","loophole","manipulation"]):
        sources[26]["records"].append(r)
    elif any(k in t for k in ["sebi","regulation","ban","margin rule","rule change","expiry change"]):
        sources[27]["records"].append(r)
    elif any(k in t for k in ["tax","stt","audit","itr","income tax"]):
        sources[28]["records"].append(r)
    elif any(k in t for k in ["invest","stock pick","value","momentum","sip","mf","mutual fund","etf"]):
        sources[29]["records"].append(r)
    elif any(k in t for k in ["real estate","gold","bond","reit","invi", "fd"]):
        sources[30]["records"].append(r)
    elif any(k in t for k in ["crypto","bitcoin","btc","ethereum","eth"]):
        sources[31]["records"].append(r)
    else:
        unmapped += 1
        # Auto-assign to chronicle or general by type
        if r.get("type") in ("pre_market","post_market","weekly"):
            yr = (r.get("date") or "2020")[:4]
            if yr in ("2018","2019","2020"):
                sources[22]["records"].append(r)
            elif yr in ("2021","2022"):
                sources[23]["records"].append(r)
            elif yr in ("2023","2024"):
                sources[24]["records"].append(r)
            else:
                sources[25]["records"].append(r)
        else:
            sources[3]["records"].append(r)  # default: discipline/process

print("unmapped:", unmapped)
for k, v in sources.items():
    recs = v["records"]
    # Deduplicate by id
    seen = set()
    unique = []
    for r in recs:
        if r.get("id") not in seen:
            seen.add(r.get("id"))
            unique.append(r)
    v["records"] = unique
    v["count"] = len(unique)
    print(f"  ch {k:02d} {v['title']:25s}: {len(unique)} sources")

# Write compact version with just what compiler needs
compact = {}
for k, v in sources.items():
    recs = []
    for r in v["records"]:
        recs.append({
            "id": r.get("id"),
            "date": r.get("date"),
            "subtype": r.get("subtype"),
            "summary": r.get("summary","")[:100],
            "themes": (r.get("themes") or [])[:4],
            "lessons": (r.get("lessons") or [])[:3],
            "events": (r.get("event_claims") or r.get("events") or [])[:2],
            "strategies": bool(r.get("strategies")),
            "quality": r.get("quality", 3),
        })
    compact[k] = {"title": v["title"], "source_count": v["count"], "sources": recs}
json.dump(compact, open(f"{ROOT}/book/chapters/sources_per_chapter.json","w"), indent=1)