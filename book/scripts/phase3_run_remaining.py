#!/usr/bin/env python3
"""Run remaining Phase 3 verification batches via direct OpenRouter API calls.
Called as: python3 book/scripts/phase3_run_remaining.py
"""
import json, glob, os, time, requests, re
ROOT = "/home/ubuntu/repos/prs_analysis"
BULK = f"{ROOT}/book/events/bulk_verify_queue.json"
API_KEY = "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"
MODEL = "openrouter/deepseek/deepseek-v4-flash:low"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
DONE = set()
for f in glob.glob(f"{ROOT}/book/events/verified_batch_*.jsonl"):
    try: DONE.add(int(os.path.basename(f).split("_")[2].split(".")[0]))
    except: pass

bulk = json.load(open(BULK))
PROMPT_TEMPLATE = """You are a fact-verification agent for a book about Indian stock markets (2018-2026). Verify each claim below against web sources.

For EACH numbered claim:
1. Use reasoning (you have web knowledge up to Aug 2026)
2. Assign a verdict: "verified" | "corrected" (give corrected_claim) | "wrong" (give corrected_claim) | "unverifiable"
3. Cite 1-3 sources (title + URL from your knowledge)

Output JSONL (one line per claim, no fences):
{"idx":N,"verdict":"...","corrected_claim":"...","evidence": [{"title":"...","url":"..."}],"notes":"<=20 words"}

CLAIMS:
{claims}
"""

missing = []
for i in range(0, len(bulk), 10):
    idx = i // 10
    if idx in DONE: continue
    chunk = bulk[i:i+10]
    claims_txt = "\n".join(f"{j+1}. [{c.get('date') or 'date unknown'}] {c['claim'][:400]}" for j, c in enumerate(chunk))
    missing.append((idx, claims_txt))
print(f"Missing batches: {len(missing)} ({sum([1 for _ in missing]) * 10} claims)")

results = []
for bidx, claims_txt in missing:
    print(f"  Verifying batch {bidx:03d}...", end=" ", flush=True)
    prompt = PROMPT_TEMPLATE.replace("{claims}", claims_txt)
    resp = requests.post(API_URL, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }, json={
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
    }, timeout=120)
    if resp.status_code != 200:
        print(f"FAILED {resp.status_code}: {resp.text[:120]}")
        continue
    text = resp.json()["choices"][0]["message"]["content"].strip()
    # Extract JSONL from response
    lines = [l for l in text.split("\n") if l.strip() and l.strip() != "```" and not l.strip().startswith("```")]
    jsonlines = []
    for l in lines:
        try:
            j = json.loads(l)
            jsonlines.append(j)
        except: pass
    if len(jsonlines) != min(10, len(bulk[bidx*10:bidx*10+10])):
        print(f"expected {min(10,len(bulk[bidx*10:bidx*10+10]))} lines, got {len(jsonlines)}")
        continue
    out = f"{ROOT}/book/events/verified_batch_{bidx:03d}.jsonl"
    with open(out, "w") as fh:
        for j in jsonlines:
            fh.write(json.dumps(j) + "\n")
    print(f"OK -> {os.path.basename(out)}")
    results.append(bidx)
    time.sleep(2)

print(f"\nDone: {len(results)} batches verified")
# Final merge
all_v = []
for f in sorted(glob.glob(f"{ROOT}/book/events/verified_batch_*.jsonl")):
    for l in open(f):
        try: all_v.append(json.loads(l))
        except: pass
json.dump(all_v, open(f"{ROOT}/book/events/events_verified.json", "w"), indent=1)
from collections import Counter
v = Counter(r['verdict'] for r in all_v)
print(f"Total: {len(all_v)} - Verdicts: {json.dumps(v)}")