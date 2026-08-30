#!/usr/bin/env python3
"""Phase 4: Chapter brief compiler — scans all analysis JSONs, groups by chapter, writes briefs."""
import json, glob, os, re
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"
CHAPTERS = json.load(open(f"{ROOT}/book/editorial/chapter_map.json")) if os.path.exists(f"{ROOT}/book/editorial/chapter_map.json") else None
# embedded chapter map fallback
CHAPTER_NAMES = {
    1: "Why Most Traders Lose", 2: "Anatomy of a Trader's Failure", 3: "Discipline, Process, and Surviving First",
    4: "FII/DII Flows", 5: "Volatility as a Regime", 6: "Reading the Option Chain", 7: "Microstructure: Gaps, Expiries, Last Half Hour",
    8: "Why Derivatives Exist", 9: "Calls and Puts", 10: "The Greeks, Demystified", 11: "Implied Volatility", 12: "Margins, Collateral, Machinery",
    13: "Short Straddles & Strangles", 14: "Spreads & Ratio Spreads", 15: "Calendar Spreads", 16: "Butterflies & Condors",
    17: "Portfolio Hedges", 18: "Firefighting & Adjustments",
    19: "The Event Playbook", 20: "Budgets and Elections", 21: "Wars, Crashes and Black Swans",
    22: "Chronicle 2018-2020", 23: "Chronicle 2021-2022", 24: "Chronicle 2023-2024", 25: "Chronicle 2025-2026",
    26: "How Retail Gets Cheated", 27: "The Regulator's Dilemma", 28: "Taxes",
    29: "Investing vs Trading", 30: "Hard Assets", 31: "Crypto as a Satellite",
}
PART_NAMES = {1: "I The Trader's Mind", 2: "II How This Market Works", 3: "III Options from First Principles",
              4: "IV The Strategy Library", 5: "V Trading the Events", 6: "VI Market Chronicle 2018-2026",
              7: "VII Predators & Protectors", 8: "VIII Wealth Beyond the Screen"}
PART_OF = {1:1,2:1,3:1, 4:2,5:2,6:2,7:2, 8:3,9:3,10:3,11:3,12:3, 13:4,14:4,15:4,16:4,17:4,18:4,
           19:5,20:5,21:5, 22:6,23:6,24:6,25:6, 26:7,27:7,28:7, 29:8,30:8,31:8}

# Per-chapter collections
ch_data = defaultdict(lambda: {"ids": [], "lessons": [], "themes": [], "strategies": [],
                                "enhance": [], "events": [], "quality": 0, "n": 0,
                                "daily_summaries": [], "weekly_summaries": []})

# Scan all analysis JSONLs
for f in sorted(glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except: continue
        rtype = r.get("type", "")
        rid = r.get("id")
        # Map to chapters
        targets = r.get("chapter_targets", [])
        if targets:
            for ch in targets:
                ch = int(ch)
                if 1 <= ch <= 31:
                    ch_data[ch]["ids"].append(rid)
                    ch_data[ch]["n"] += 1
                    for l in r.get("lessons", []):
                        if l and len(l) > 10: ch_data[ch]["lessons"].append(f"[{rid}] {l}")
                    for t in r.get("themes", []):
                        if t: ch_data[ch]["themes"].append(t)
                    for s in r.get("strategies", []):
                        if s: ch_data[ch]["strategies"].append(s)
                    for e in r.get("enhance", []):
                        if e: ch_data[ch]["enhance"].append(e)
                    for ev in r.get("event_claims", []):
                        if ev: ch_data[ch]["events"].append(ev)
                    q = r.get("quality", 3)
                    ch_data[ch]["quality"] += q
        # Dailies feed chronicle (ch 22-25) by year
        if rtype in ("pre_market", "post_market", "weekly") and r.get("summary"):
            dt = r.get("date", "")
            if dt:
                yr = dt[:4]
                ch_map = {"2018":22, "2019":22, "2020":22, "2021":23, "2022":23, "2023":24, "2024":24, "2025":25, "2026":25}
                ch = ch_map.get(yr, 22)
                ch_data[ch]["ids"].append(rid)
                ch_data[ch]["n"] += 1
                ch_data[ch]["daily_summaries"].append(f"[{rid}|{dt}] {r.get('summary','')[:80]}")
                for ev in r.get("events", []):
                    if ev: ch_data[ch]["events"].append(ev)
                for l in r.get("lessons", []):
                    if l and len(l) > 10: ch_data[ch]["lessons"].append(f"[{rid}] {l}")
        # Daily summaries for mechanics chapters (4-7)
        if rtype in ("pre_market", "post_market", "weekly") and r.get("summary"):
            ch_data[4]["daily_summaries"].append(f"[{rid}|{r.get('date','')}] {r.get('summary','')[:100]}")
            ch_data[5]["daily_summaries"].append(f"[{rid}|{r.get('date','')}] {r.get('summary','')[:100]}")
            ch_data[6]["daily_summaries"].append(f"[{rid}|{r.get('date','')}] {r.get('summary','')[:100]}")
            ch_data[7]["daily_summaries"].append(f"[{rid}|{r.get('date','')}] {r.get('summary','')[:100]}")
            if r.get("levels", {}).get("vix"): ch_data[5]["n"] += 1

# Load verified events
verified = []
if os.path.exists(f"{ROOT}/book/events/events_verified.jsonl"):
    for line in open(f"{ROOT}/book/events/events_verified.jsonl"):
        try: verified.append(json.loads(line))
        except: pass

# Write briefs
os.makedirs(f"{ROOT}/book/chapters/briefs", exist_ok=True)
for ch in sorted(ch_data.keys()):
    d = ch_data[ch]
    name = CHAPTER_NAMES.get(ch, f"Chapter {ch}")
    part = PART_OF.get(ch, 0)
    part_name = PART_NAMES.get(part, "")
    avg_q = d["quality"] / max(d["n"], 1)
    top_lessons = sorted(set(d["lessons"]), key=lambda x: -len(x))[:10]
    top_themes = sorted(set(d["themes"]), key=lambda x: -len(x))[:10]
    strategies = d["strategies"][:5]
    enhance = list(set(d["enhance"]))[:5]
    daily = d["daily_summaries"]
    # Sort by date
    daily.sort(key=lambda x: x.split("|")[1] if "|" in x else "")
    # Pick ~10 most representative dailies
    step = max(len(daily)//10, 1)
    sample_daily = daily[::step][:10]

    brief = f"""# Chapter {ch}: {name}
Part: {part_name}

## Source count
- Transcripts directly mapped: {d['n']}
- Unique IDs: {len(set(d['ids']))}

## Top themes
{chr(10).join(f'- {t}' for t in top_themes)}

## Key lessons
{chr(10).join(f'- {l}' for l in top_lessons)}

## Strategies (if applicable)
{chr(10).join(f'- {json.dumps(s)}' for s in strategies)}

## Enhancement candidates
{chr(10).join(f'- {e}' for e in enhance)}

## Representative daily/weekly entries
{chr(10).join(f'- {s}' for s in sample_daily)}

## Verified events (relevant)
{chr(10).join(f'- {v.get("claim","")[:100]} ({v.get("verdict","")})' for v in verified[:3])}

## Source IDs
{chr(10).join(sorted(set(str(x) for x in d['ids']))[:30])}
"""
    # Chronicle chapters get all dailies references
    if ch in (22,23,24,25):
        brief += f"\n## All daily transcript references\n{chr(10).join(f'- {s}' for s in daily[:60])}\n"

    slug = name.lower().replace(' ','_').replace('/','_').replace('?','').replace(',','')[:40]
    with open(f"{ROOT}/book/chapters/briefs/{ch:02d}_{slug}.md", "w") as fh:
        fh.write(brief)
    print(f"Wrote chapter {ch:02d}: {name} ({d['n']} sources, {len(top_lessons)} lessons)")

print("\nDone. All chapter briefs written.")