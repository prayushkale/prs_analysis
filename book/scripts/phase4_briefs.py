#!/usr/bin/env python3
"""Phase 4: Generate chapter briefs from analysis data + verified facts.
Output: book/chapters/briefs/NN-slug.md per chapter.
"""
import json, os, glob
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"
META = os.path.join(ROOT, "book/meta/metadata.jsonl")
EVENTS = os.path.join(ROOT, "book/events/events_verified.jsonl")
BRIEFS = os.path.join(ROOT, "book/chapters/briefs")
CANDIDATES = os.path.join(ROOT, "book/chapters/chapter_candidates.json")

ch_map = """1 Why Most Traders Lose
2 The Anatomy of a Trader's Failure
3 Discipline, Process, and Surviving First
4 The Engine Room: FII/DII Flows
5 Volatility Is a Regime, Not a Number
6 Reading the Option Chain
7 Microstructure: Gaps, Expiries and the Last Half Hour
8 Why Derivatives Exist
9 Calls and Puts
10 The Greeks, Demystified
11 Implied Volatility: The Real Price of Options
12 Margins, Collateral and the Machinery
13 The Seller's Edge: Short Straddles & Strangles
14 Controlled Direction: Spreads & Ratio Spreads
15 Time Is the Trade: Calendar Spreads
16 Butterflies & Condors
17 Portfolio Protection: Hedges That Actually Hedge
18 Firefighting: Rescue and Adjustment
19 The Event Playbook
20 Budgets and Elections: Case Files
21 Wars, Crashes and Black Swans
22 2018-2020: Tariff Tantrums to Pandemic
23 2021-2022: Liquidity Boom, Inflation Bust
24 2023-2024: Bull Run and Its First Crack
25 2025-2026: Tariffs, Jane Street and New Regime
26 How Retail Gets Cheated
27 The Regulator's Dilemma
28 Taxes: The Trader's Real Opponent
29 Investing vs Trading: Choosing Your Game
30 The Hard Assets Debate
31 Crypto as a Satellite"""
ch_names = [l.split(" ", 1)[1] for l in ch_map.strip().split("\n")]
ch_by_num = {i+1: n for i,n in enumerate(ch_names)}

def load_analysis():
    """Return dict id->{record} for all analysis"""
    idx = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "book/analysis/batch_*.jsonl"))):
        for l in open(f):
            if l.strip():
                try: r = json.loads(l); idx[r.get("id")] = r
                except: pass
    return idx

def load_events():
    """Return list of verified events"""
    events = []
    if os.path.exists(EVENTS):
        for l in open(EVENTS):
            if l.strip():
                try: events.append(json.loads(l))
                except: pass
    return events

def build_brief(ch_num, analysis_idx, candidates, events):
    """Write one chapter brief."""
    slug = f"{ch_num:02d}-" + ch_names[ch_num-1].lower().replace(":", "").replace(" ", "-").replace("--", "-").replace("---", "-")
    meta = candidates.get(slug, [])
    ids = [m["id"] for m in meta]
    records = [analysis_idx[i] for i in ids if i in analysis_idx]
    
    # extract key content
    lessons = []
    strategies = []
    events_mentioned = []
    themes = set()
    for r in records:
        if r.get("lessons"): lessons.extend(r["lessons"])
        if r.get("strategies"): strategies.extend(r["strategies"])
        if r.get("event_claims"): events_mentioned.extend([e["claim"] for e in r["event_claims"] if isinstance(e, dict)])
        if r.get("themes"): themes.update(r["themes"])
        if r.get("enhance"): pass  # flagged for enhancement
    # dedupe
    lessons = list(dict.fromkeys(lessons))[:15]
    themes = list(dict.fromkeys(themes))[:10]
    
    brief = f"""# Chapter {ch_num}: {ch_names[ch_num-1]}

## Source transcripts ({len(records)})
""" + "\n".join(f"- {r.get('id','?')}: {r.get('summary','')[:80]}" for r in records[:8]) + (f"\n+ {len(records)-8} more" if len(records) > 8 else "") + f"""

## Key themes
{' — '.join(themes)}

## Core lessons to feature
""" + "\n".join(f"{i+1}. {l}" for i,l in enumerate(lessons[:8])) + """

## Strategy content (if applicable)
""" + ("\n".join(f"- **{s.get('name','strategy')}**: {s.get('construction','')[:100]} — {s.get('best_regime','')} — risk: {s.get('risks','')[:60]}" for s in strategies[:4]) if strategies else "None.") + """

## Enhancement candidates (worked examples/tables needed)
""" + ("\n".join(f"- {r.get('enhance',[''])}" for r in records if r.get('enhance'))) + """

## Event claims relevant to this chapter
""" + "\n".join(f"- {(e[:120] if len(e)>120 else e)}" for e in events_mentioned[:6]) + """

## Redundancy / deduplication notes
""" + (f"- {len(records)} source transcripts; dedupe repeated pre/post coverage to strongest statement." if len(records) > 5 else "- Low volume; use all sources.") + """

## Enhancement instructions
- Add worked numerical examples where concepts are abstract.
- Include payoff tables for strategies.
- Dated levels are illustrative of method, not evergreen advice.
- For chronicle chapters (22-25): verified events from events_verified.jsonl are authoritative; any discrepancy with source analysis should follow the verified fact.
- For Parts V-VII: cross-reference between chapters (e.g., a scam in ch.26 that SEBI addressed in ch.27).
"""
    return brief, slug

def main():
    os.makedirs(BRIEFS, exist_ok=True)
    analysis_idx = load_analysis()
    candidates = json.load(open(CANDIDATES))
    events = load_events()
    print(f"analysis records loaded: {len(analysis_idx)}")
    print(f"events loaded: {len(events)}")
    
    for ch_num in range(1, 32):
        brief, slug = build_brief(ch_num, analysis_idx, candidates, events)
        path = os.path.join(BRIEFS, f"{slug}.md")
        open(path, "w").write(brief)
        print(f"  -> {slug}.md")
    print(f"Wrote {31} chapter briefs to {BRIEFS}/")

if __name__ == "__main__":
    main()