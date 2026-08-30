#!/usr/bin/env python3
"""Phase 2 batch generator: create batch manifests + wave JS files for parallel analysis."""
import json, os

ROOT = "/home/ubuntu/repos/prs_analysis"
META = f"{ROOT}/book/meta/metadata.jsonl"
AN = f"{ROOT}/book/analysis"
JS = f"{ROOT}/book/scripts"

rows = [json.loads(l) for l in open(META, encoding="utf-8")]
# exclusions: first-pass + reader-flagged
EXTRA_EXCLUDE = {"2923"}
rows = [r for r in rows if not r.get("excluded_firstpass") and r["id"] not in EXTRA_EXCLUDE]
print("to analyze:", len(rows))

ASR = """gif nifty/GIF-50/GIFT->GIFT Nifty (SGX Nifty only pre-Jul-2023) | Sabi/CB/semi/say B->SEBI | RBA->RBI |
FAs/FIA/FAS/F&I/APIs/FA->FIIs | DAAs/DAI's/DIA->DIIs | Bagnifty/Bang nifty/Bagniti->Bank Nifty | if-in-nifty->FinNifty |
global queues->global cues | stock covering->short covering | shorter up->shot up | MSA->MSCI | CPA->CPI |
Wix/weeks/Bix->VIX | Toji->Doji | ICSA->ICICI Bank | Industin/Indus and Bank->IndusInd | Quotac/Kotaik->Kotak Bank |
trunk->Trump | gargle war->Kargil war | pull-up attack->Pulwama | hidden bar/Hind bet->Hindenburg | Lull Street->Dalal Street |
taxbeddy->TaxBuddy | 'Delta dot exchange' variants->Delta Exchange | Struggles->straddles | piano->P&L | bees/BeES->ETF (e.g. Nifty BeES)"""

DAILY_PROMPT = """You are an analyst extracting structured data from transcripts of an Indian stock-market trading educator for an anonymized book. Rules: (1) NEVER output the speaker's real name or any identity string - where you see one, note it in `leaks` only. (2) Apply these transcription corrections when interpreting (do not echo the errors): {asr}. (3) Be factual - only what the transcript says; mark uncertain numbers.

Read each transcript below IN FULL (read tool). For EACH, emit exactly ONE line of JSON (no markdown fences) with schema:
{{"id":"...","date":"YYYY-MM-DD or null","type":"pre_market|post_market|weekly","summary":"<=50 words: what happened in the market and what the speaker focused on","levels":{{"nifty":null,"banknifty":null,"vix":null,"fii_cr":null,"dii_cr":null}},"events":[{{"claim":"specific factual market/policy/corporate event asserted with numbers/dates","verify":true/false}}],"lessons":["<=25 words each, max 2, only if a real transferable lesson"],"quote":"optional <=30 word verbatim-style cleaned quote or empty","dup_flag":"if content is essentially a repeat of an adjacent date, note the repeated topic","leaks":["verbatim identity/promo strings spotted"]}}
`levels`: only values explicitly stated (numbers in crore for fii/dii). `events`: 0-4 items, only concrete verifiable claims (index moves with dates/levels, policy changes, corporate events, macro data, wars, fraud cases). No generic market states.

WRITE all JSON lines to the file {out} (one per transcript, in order). Then return a 5-line digest: counts, most notable events, data quality.

TRANSCRIPTS ({n}):
{files}
"""

SPECIAL_PROMPT = """You are an analyst extracting structured content from a SPECIAL-EPISODE transcript of an Indian stock-market trading educator, for an anonymized book with these 31 chapters: 1 why traders lose; 2 anatomy of failure; 3 discipline/process; 4 FII/DII flows; 5 VIX regimes; 6 option chain; 7 microstructure (gaps/expiry/index construction); 8 why derivatives exist; 9 calls and puts; 10 greeks; 11 implied volatility; 12 margins/collateral; 13 short straddles/strangles; 14 spreads & ratio spreads; 15 calendar spreads; 16 butterflies/condors; 17 portfolio hedges; 18 firefighting/adjustments; 19 event playbook; 20 budgets/elections; 21 wars/black swans; 22-25 chronicle 2018-26; 26 retail scams; 27 regulation (SEBI/rules); 28 taxation; 29 investing vs trading; 30 real assets (real estate/gold/bonds); 31 crypto.

Rules: NEVER output the speaker's real name or identity strings (note them in `leaks` only). Apply transcription corrections: {asr}. Only what the transcript says. Genericize personal trades/P&L as content (the numbers may teach), but if a passage is self-promotion/self-defense (business, penalty, family, luxury, travel), list it under exclude_passages.

Read each transcript IN FULL. For EACH, emit exactly ONE line of JSON (no fences):
{{"id":"...","date":"...","type":"special","title_clean":"cleaned title","summary":"<=60 words","chapter_targets":["chapter numbers, primary first"],"themes":["2-6 short theme tags"],"lessons":["transferable lessons, <=30 words each, max 5"],"strategies":[{{"name":"...","construction":"legs/strikes/quantities","numbers":"premiums/margins/breakevens/returns as stated","best_regime":"when to use","adjustments":"how managed/rescued","risks":"max loss / failure mode"}}],"event_claims":[{{"claim":"factual assertion with numbers/dates","verify":true/false}}],"quotes":["<=30 words cleaned, max 3, only distinctive"],"enhance":["complex topics needing worked examples/tables"],"exclude_passages":["self-promo/identity passages to drop"],"leaks":["verbatim identity/promo strings"],"quality":1-5}}
If no strategies exist, use []. Event claims: concrete verifiable assertions only.

WRITE all JSON lines to {out} (one per transcript, in order). Then return a 5-line digest.

TRANSCRIPTS ({n}):
{files}
"""

def make_batches():
    daily = [r for r in rows if r["series"] == "daily"]
    weekly = [r for r in rows if r["series"] == "weekly"]
    special = [r for r in rows if r["series"] == "special"]
    batches = []
    def chunk(lst, n, kind):
        for i in range(0, len(lst), n):
            c = lst[i:i + n]
            batches.append({"id": f"{kind}_{len(batches):03d}", "kind": kind, "items": c})
    chunk(daily, 25, "daily")
    chunk(weekly, 20, "weekly")
    chunk(special, 10, "special")
    return batches

def filelines(items):
    out = []
    for r in items:
        out.append(f"- id {r['id']} | date {r.get('date')} | {r['subtype']} | \"{r['title'][:70]}\" | path: {ROOT}/book/corpus/{r['id']}.txt")
    return "\n".join(out)

batches = make_batches()
os.makedirs(f"{AN}/manifests", exist_ok=True)
os.makedirs(f"{AN}/outputs", exist_ok=True)

# RESUME MODE: only emit tasks for batches that are missing or partially written
import json as _json
resume_entries = []
repair_map = []
for b in batches:
    f = f"{AN}/batch_{b['id']}.jsonl"
    have = set()
    if os.path.exists(f):
        for l in open(f):
            try:
                have.add(_json.loads(l)['id'])
            except Exception:
                pass
    missing_items = [r for r in b['items'] if r['id'] not in have]
    if len(missing_items) == len(b['items']):
        out = f
        resume_entries.append((b['id'], b, b['items'], out, False))
    elif missing_items:
        out = f"{AN}/batch_{b['id']}_fix.jsonl"
        resume_entries.append((b['id'] + '_fix', b, missing_items, out, True))
        repair_map.append({'batch': b['id'], 'missing': [r['id'] for r in missing_items]})

if repair_map:
    _json.dump(repair_map, open(f"{AN}/manifests/repair_map.json", "w"), indent=1)
print(f"resume: {len(resume_entries)} tasks needed ({len(repair_map)} partial-repairs)")

waves = [resume_entries[i:i + 60] for i in range(0, len(resume_entries), 60)]

json.dump(batches, open(f"{AN}/manifests/batch_index.json", "w"), indent=0)
print("batches:", len(batches), "waves:", [len(w) for w in waves])

for wi, wave in enumerate(waves):
    entries = []
    for key, b, items, out, is_fix in wave:
        # weekly uses the same light schema; the type field distinguishes it
        tpl = DAILY_PROMPT if b["kind"] in ("daily", "weekly") else SPECIAL_PROMPT
        task = tpl.replace("{asr}", ASR).replace("{out}", out).replace("{n}", str(len(items))).replace("{files}", filelines(items))
        entries.append({"key": key, "agent": "worker", "task": task,
                        "output": f"{AN}/outputs/{key}_report.md"})
    js = "const tasks = " + json.dumps(entries, ensure_ascii=False) + ";\nconst results = await runs.all(tasks);\nreturn results.map((r,i)=>[tasks[i].key, String(r).slice(0,140)]);\n"
    open(f"{JS}/phase2_resume_wave{wi}.js", "w").write(js)
    print(f"wave {wi}: {len(entries)} children, js size {len(js)//1024}KB")
