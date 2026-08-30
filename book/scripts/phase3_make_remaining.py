#!/usr/bin/env python3
"""Phase 3 resume helper: regenerate verification workflow for any missing batches.
Run:  python3 book/scripts/phase3_make_remaining.py   -> emits book/scripts/phase3_resume.js
Then: subagent workflowScriptPath=book/scripts/phase3_resume.js (async:false, timeout 3600000)
"""
import json, glob, os
ROOT = "/home/ubuntu/repos/prs_analysis"
bulk = json.load(open(f"{ROOT}/book/events/bulk_verify_queue.json"))
done = set()
for f in glob.glob(f"{ROOT}/book/events/verified_batch_*.jsonl"):
    done.add(int(os.path.basename(f).split("_")[2].split(".")[0]))

PROMPT = open(f"{ROOT}/book/scripts/phase3_prompt.txt").read() if os.path.exists(f"{ROOT}/book/scripts/phase3_prompt.txt") else None
# prompt template is embedded in phase3_make script; reconstruct from git history or redefine:
PROMPT = """You are a fact-verification agent for a book about Indian stock markets (2018-2026). Verify each claim below against web sources.

For EACH numbered claim:
1. Use web search (2-3 targeted queries max per claim) - prefer NSE/niftyindices, SEBI/PIB, Reuters, Economic Times, Moneycontrol, Business Standard.
2. Assign a verdict:
   - "verified" - the claim is accurate as stated (numbers/dates within reasonable rounding)
   - "corrected" - substantially right but with wrong details; give corrected_claim with accurate numbers/dates
   - "wrong" - materially false; give corrected_claim with the true fact
   - "unverifiable" - could not confirm from reputable sources; do NOT guess
3. Cite 1-3 sources each (title + URL).

IMPORTANT: Write results as JSONL (one line per claim, no markdown fences) to the exact file: {out}
Schema: {{"idx":N,"verdict":"verified|corrected|wrong|unverifiable","corrected_claim":"only if corrected/wrong","evidence":[{{"title":"...","url":"..."}}],"notes":"<=20 words"}}

Work efficiently: if a claim is clearly generic, 'unverifiable' after one query is acceptable.

CLAIMS:
{claims}
"""

entries = []
per = 10
for i in range(0, len(bulk), per):
    if (i // per) in done:
        continue
    chunk = bulk[i:i + per]
    claims_txt = "\n".join(f"{j+1}. [{c.get('date') or 'date unknown'}] {c['claim'][:400]}" for j, c in enumerate(chunk))
    task = PROMPT.replace("{out}", f"{ROOT}/book/events/verified_batch_{i//per:03d}.jsonl").replace("{claims}", claims_txt)
    entries.append({"key": f"ver_{i//per:03d}", "agent": "worker", "model": "openrouter/deepseek/deepseek-v4-flash:low",
                    "task": task, "output": f"{ROOT}/book/events/outputs/ver_{i//per:03d}_report.md"})

print("missing verification batches:", len(entries))
if entries:
    # waves of 25 to stay under in-flight budget
    W = 25
    n = 0
    for wi in range(0, len(entries), W):
        wave = entries[wi:wi+W]
        js = "const tasks = " + json.dumps(wave, ensure_ascii=False) + ";\nconst results = await runs.all(tasks);\nreturn results.map((r,i)=>[tasks[i].key, String(r).slice(0,120)]);\n"
        open(f"{ROOT}/book/scripts/phase3_resume_w{n}.js", "w").write(js)
        print(f"  -> book/scripts/phase3_resume_w{n}.js ({len(wave)} children)")
        n += 1
