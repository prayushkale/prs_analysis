#!/usr/bin/env python3
"""Phase 5 writer - runs chapter generation with concurrent workers.
Adjust CONCURRENT to manage API load.
"""
import json, glob, os, requests, sys, time, re
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = "/home/ubuntu/repos/prs_analysis"
API_KEY = "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"
MODEL = "deepseek/deepseek-v4-flash"
CONCURRENT = 3

CHAPTER_NAMES = {
    1:"Why Most Traders Lose", 2:"The Anatomy of Failure", 3:"Discipline, Process, and Survival",
    4:"The Engine Room: FII/DII Flows", 5:"Volatility as a Regime", 6:"Reading the Option Chain",
    7:"Microstructure: Gaps, Expiries, and the Last Half Hour",
    8:"Why Derivatives Exist", 9:"Calls and Puts", 10:"The Greeks, Demystified",
    11:"Implied Volatility", 12:"Margins, Collateral and the Machinery",
    13:"The Seller's Edge: Short Straddles & Strangles", 14:"Controlled Direction: Spreads & Ratio Spreads",
    15:"Time Is the Trade: Calendar Spreads", 16:"Butterflies & Condors",
    17:"Portfolio Protection: Hedges That Work", 18:"Firefighting: Rescue and Adjustment",
    19:"The Event Playbook", 20:"Budgets and Elections: Case Files", 21:"Wars, Crashes and Black Swans",
    22:"2018-2020: From Tariff Tantrums to the Pandemic", 23:"2021-2022: Liquidity Boom and Inflation Bust",
    24:"2023-2024: The Bull Run and Its First Crack", 25:"2025-2026: Tariffs, Jane Street and the New Regime",
    26:"How Retail Gets Cheated", 27:"The Regulator's Dilemma", 28:"Taxes: The Trader's Real Opponent",
    29:"Investing vs Trading: Choosing Your Game", 30:"The Hard Assets Debate", 31:"Crypto as a Satellite"
}

verified = json.load(open(f"{ROOT}/book/events/events_verified.json"))

def call_api(prompt):
    resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers={
        "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"
    }, json={"model": MODEL, "messages": [{"role":"user","content":prompt}],
             "temperature": 0.3, "max_tokens": 4096}, timeout=120)
    return resp.json()["choices"][0]["message"]["content"]

def load_analysis_for(ids):
    result = {}
    for f in glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl"):
        for l in open(f):
            try: r = json.loads(l); result[r["id"]] = r
            except: pass
    return {i: result[i] for i in ids if i in result}

def write_chapter(cn, brief_text, part_name):
    title = CHAPTER_NAMES[cn]
    cand_paths = glob.glob(f"{ROOT}/book/chapters/candidates/{cn:02d}_*.json")
    ids = json.load(open(cand_paths[0])).get("candidates",[]) if cand_paths else []
    analysis = load_analysis_for(ids[:20])
    
    summaries = []
    for aid, r in list(analysis.items())[:10]:
        s = r.get("summary","") or ""
        l = "; ".join((r.get("lessons") or [])[:2])
        st = ""
        if r.get("strategies"):
            st = "; ".join(f'{s.get("name","")}[{s.get("numbers","")}]' for s in r["strategies"][:2] if isinstance(s,dict))
        summaries.append(f"[{aid}] {s[:150]}{' | '+l[:150] if l else ''}{' | '+st[:150] if st else ''}")
    
    vfacts = json.dumps([e for e in verified if e["verdict"]!="unverifiable"][:8], indent=1)
    
    prompt = f"""You are a book writer. Write ONE CHAPTER for a book about Indian stock markets by "Dhanraj".

VOICE: Third-person teaching, occasional first-person "I" for anecdotes attributed to Dhanraj. Direct, clear, plain English. No hero worship, no identity, no politics, no sales pitch. Use ₹ and crore/lakh.

CHAPTER: Chapter {cn}: "{title}" | Part: "{part_name}"

PART BRIEF: {brief_text[:2000]}

KEY SOURCE ANALYSIS: 
{' '.join(summaries)[:2000]}

VERIFIED FACTS: {vfacts[:1500]}

INSTRUCTIONS:
1. Write ~2000-4000 words of engaging, book-quality prose
2. Start with a hook (a real market moment)
3. Build from first principles; use analogies
4. If complex topic, include a worked example with numbers
5. End with 3-5 bullet-point "Key Takeaways"
6. No references to original channel/person/videos/platform
7. No political opinions
8. Markdown formatting. OUTPUT ONLY the chapter content."""

    content = call_api(prompt)
    content = re.sub(r"^```.*?\n", "", content)
    content = re.sub(r"\n```.*$", "", content)
    slug = re.sub(r'[^a-z0-9]+','_',title.lower())[:40]
    out = f"{ROOT}/book/chapters/ch{cn:02d}_{slug}.md"
    with open(out,"w") as f: f.write(content)
    return cn, len(content)

briefs = {}
for f in glob.glob(f"{ROOT}/book/chapters/briefs/part_*.md"):
    briefs[os.path.basename(f).split(".md")[0]] = open(f).read()

PARTS = [
    (1,"part_01_the_trader's_mind",[1,2,3],"The Trader's Mind"),
    (2,"part_02_how_this_market_works",[4,5,6,7],"How This Market Works"),
    (3,"part_03_options_from_first_principles",[8,9,10,11,12],"Options from First Principles"),
    (4,"part_04_the_strategy_library",[13,14,15,16,17,18],"The Strategy Library"),
    (5,"part_05_trading_the_events",[19,20,21],"Trading the Events"),
    (6,"part_06_market_chronicle",[22,23,24,25],"A Market Chronicle 2018-2026"),
    (7,"part_07_predators_&_protectors",[26,27,28],"Predators & Protectors"),
    (8,"part_08_wealth_beyond_the_screen",[29,30,31],"Wealth Beyond the Screen"),
]

target_part = int(sys.argv[1]) if len(sys.argv)>1 else None
filtered = PARTS if not target_part else [p for p in PARTS if p[0]==target_part]

with ThreadPoolExecutor(max_workers=CONCURRENT) as pool:
    futures = []
    for pnum, bkey, chs, pn in filtered:
        bt = briefs.get(bkey, "")
        for cn in chs:
            if os.path.exists(f"{ROOT}/book/chapters/ch{cn:02d}_*.md"):
                # check if slug file already exists
                slug = re.sub(r'[^a-z0-9]+','_',CHAPTER_NAMES[cn].lower())[:40]
                existing = [f for f in glob.glob(f"{ROOT}/book/chapters/ch{cn:02d}_*.md")]
                if existing:
                    # don't redo if already written (for resumption)
                    pass
            futures.append(pool.submit(write_chapter, cn, bt, pn))
    for f in as_completed(futures):
        cn, length = f.result()
        print(f"  Ch {cn:02d}: {length:5d} chars")

print("\nPhase 5 done. Checking chapters:")
chapters = sorted(glob.glob(f"{ROOT}/book/chapters/ch*.md"))
print(f"  {len(chapters)} files")
total = sum(len(open(f).read()) for f in chapters)
print(f"  Total: ~{total//1000}K chars ({(total//350)//1000}K words est)")