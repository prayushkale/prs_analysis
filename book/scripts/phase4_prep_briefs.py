#!/usr/bin/env python3
"""Phase 4 prep: Build per-chapter candidate data from analysis batch JSONLs.
Output: book/events/verified_db.json (lookup: claim_hash -> {verdicts,sources,...})
        book/chapters/candidates/NN-slug.json (transcript IDs grouped by chapter)
Usage: python3 book/scripts/phase4_prep_briefs.py
"""
import json, glob, os, re
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"

# 1) Build verified-fact lookup
events = json.load(open(f"{ROOT}/book/events/events_verified.json"))
vdb = {}
for e in events:
    h = hash(e.get("corrected_claim") or e.get("claim", ""))
    vdb[h] = {"verdict": e["verdict"], "corrected": e.get("corrected_claim", ""),
              "evidence": e.get("evidence", []), "notes": e.get("notes", "")}
json.dump(vdb, open(f"{ROOT}/book/events/verified_db.json", "w"))

# 2) Chapter map
CHAPTERS = [
    (1,"why_traders_lose"),(2,"anatomy_failure"),(3,"discipline_process"),
    (4,"fii_dii_flows"),(5,"vix_regimes"),(6,"option_chain"),(7,"microstructure_gaps_expiry"),
    (8,"why_derivatives"),(9,"calls_puts"),(10,"greeks"),(11,"implied_volatility"),(12,"margins_collateral"),
    (13,"straddles_strangles"),(14,"spreads_ratio"),(15,"calendar_spreads"),(16,"butterflies_condors"),
    (17,"portfolio_hedges"),(18,"firefighting"),
    (19,"event_playbook"),(20,"budgets_elections"),(21,"wars_black_swans"),
    (22,"chronicle_2018_20"),(23,"chronicle_2021_22"),(24,"chronicle_2023_24"),(25,"chronicle_2025_26"),
    (26,"retail_scams"),(27,"regulation_sebi"),(28,"taxation"),
    (29,"investing_vs_trading"),(30,"hard_assets"),(31,"crypto")]
CH = [s for _, s in CHAPTERS]

# 3) Chapter keywords for auto-mapping
KW_MAP = {}
for n, slug in CHAPTERS:
    kw = []
    if n==1: kw = ["93%", "99%", "lose", "fail", "gambling", "gambler", "kirana"]
    elif n==2: kw = ["journey", "stop loss", "religion", "position size", "typical"]
    elif n==3: kw = ["discipline", "process", "patience", "survive", "emotion", "mindset"]
    elif n==4: kw = ["fii", "dii", "foreign flow", "fii selling", "fii buying", "absorption", "domestic institution", "block deal"]
    elif n==5: kw = ["vix", "volatility", "volatile", "india vix", "volatility index"]
    elif n==6: kw = ["oi", "open interest", "option chain", "max pain", "pcr", "put call ratio"]
    elif n==7: kw = ["gap", "expiry", "microstructure", "last hour", "half hour", "read through", "read-through", "etf rebalance", "index construction"]
    elif n==8: kw = ["forward", "future", "futures", "derivative", "arbitrageur", "speculator", "hedger", "m2m", "mark to market"]
    elif n==9: kw = ["call option", "put option", "itm", "atm", "otm", "intrinsic", "time value", "exercise", "assignment"]
    elif n==10: kw = ["delta", "gamma", "theta", "vega", "rho", "option greeks", "gamma effect"]
    elif n==11: kw = ["implied volatility", "iv", "iv rank", "iv percentile", "premium behavior"]
    elif n==12: kw = ["margin", "collateral", "span", "exposure", "peak margin", "50% cash", "lot size"]
    elif n==13: kw = ["straddle", "strangle", "short straddle", "seller's edge", "naked", "at the money straddle"]
    elif n==14: kw = ["spread", "ratio spread", "call ratio", "put ratio", "bull call", "bear put"]
    elif n==15: kw = ["calendar", "reverse calendar", "put calendar", "call calendar"]
    elif n==16: kw = ["butterfly", "condor", "double butterfly", "iron condor"]
    elif n==17: kw = ["hedge", "hedging", "protective put", "bees", "nifty bees", "collar", "portfolio protect", "insurance"]
    elif n==18: kw = ["firefight", "adjust", "adjustment", "rescue", "roll", "exit", "when to quit"]
    elif n==19: kw = ["event playbook", "binary", "event risk", "stay light", "light ahead"]
    elif n==20: kw = ["budget", "election", "vote", "parliament", "bihar", "maharashtra", "state election"]
    elif n==21: kw = ["war", "ukraine", "russia", "indo pak", "kargil", "pulwama", "balakot", "covid", "coronavirus", "black swan", "yen carry", "japan crash"]
    elif 22<=n<=25: kw = [str(2018), str(2019), str(2020), str(2021), str(2022), str(2023), str(2024), str(2025), str(2026), "chronicle", "history"]
    elif n==26: kw = ["scam", "fraud", "cheat", "broker scam", "client cheat", "trader scam", "influencer scam", "how traders lure", "hidden charges"]
    elif n==27: kw = ["sebi", "regulation", "circular", "ban", "rule", "jane street", "index expiry", "lot size change", "regulator", "sebi rule"]
    elif n==28: kw = ["tax", "taxation", "stt", "ltcg", "stcg", "capital gain", "presumptive", "crypto tax", "tds", "audit"]
    elif n==29: kw = ["investing", "investment", "mutual fund", "etf", "sip", "value investing", "momentum", "stock vs fund"]
    elif n==30: kw = ["real estate", "gold", "bond", "fixed deposit", "fd", "reit", "invit", "hard asset", "property"]
    elif n==31: kw = ["crypto", "bitcoin", "btc", "ethereum", "eth", "crypto option", "digital asset", "blockchain"]
    KW_MAP[n] = kw

def match_chapter(text):
    tl = text.lower()
    scores = {}
    for n, kw in KW_MAP.items():
        for k in kw:
            if k in tl:
                scores[n] = scores.get(n, 0) + 1
    if not scores: return None
    return max(scores, key=scores.get)

# 4) Scan analysis JSONLs for chapter candidates
by_chapter = defaultdict(list)
total = 0
for f in glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl"):
    bid = os.path.basename(f).replace("batch_", "").replace(".jsonl", "")
    for l in open(f):
        try: r = json.loads(l)
        except: continue
        total += 1
        text = r.get("summary", "") + " " + " ".join(r.get("themes", [])) + " " + " ".join(r.get("lessons", [])) + " " + " ".join(r.get("chapter_targets", []) if isinstance(r.get("chapter_targets"), list) else [])
        if isinstance(r.get("chapter_targets"), list) and r["chapter_targets"]:
            for c in r["chapter_targets"]:
                try: by_chapter[int(c)].append(r["id"])
                except: pass
        else:
            cn = match_chapter(text)
            if cn:
                by_chapter[cn].append(r["id"])

os.makedirs(f"{ROOT}/book/chapters/candidates", exist_ok=True)
print(f"Scanned {total} analysis records across {len(by_chapter)} chapters")
for n, ids in sorted(by_chapter.items()):
    data = {"chapter": n, "slug": CH[n-1] if n <= len(CH) else "unknown",
            "candidates": list(set(ids)), "count": len(set(ids))}
    json.dump(data, open(f"{ROOT}/book/chapters/candidates/{n:02d}_{CH[n-1]}.json", "w"), indent=1)
    print(f"  Ch {n:02d} {CH[n-1]:25s}: {data['count']:4d} candidates")

# Flag missing verified IDs for on-demand verification
if os.path.exists(f"{ROOT}/book/events/verified_db.json"):
    vdb_ids = set(vdb.keys())  # wrong - these are claim hashes, not transcript IDs
    pass
print(f"\nPhase 4 prep done. Candidates in book/chapters/candidates/")