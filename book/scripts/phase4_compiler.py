#!/usr/bin/env python3
"""Phase 4 compiler: Generate chapter briefs from analysis data + verified facts.
Reads candidate lists per chapter, calls OpenRouter API to produce structured briefs.

Usage: python3 book/scripts/phase4_compiler.py [--sample N]
"""
import json, glob, os, requests, sys, time
ROOT = "/home/ubuntu/repos/prs_analysis"

PARTS = [
    (1, "The Trader's Mind", [1,2,3]),
    (2, "How This Market Works", [4,5,6,7]),
    (3, "Options from First Principles", [8,9,10,11,12]),
    (4, "The Strategy Library", [13,14,15,16,17,18]),
    (5, "Trading the Events", [19,20,21]),
    (6, "A Market Chronicle 2018–2026", [22,23,24,25]),
    (7, "Predators & Protectors", [26,27,28]),
    (8, "Wealth Beyond the Screen", [29,30,31]),
]

API_KEY = "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"
MODEL = "deepseek/deepseek-v4-flash"

# Load chapter candidate data
candidates = {}
for f in glob.glob(f"{ROOT}/book/chapters/candidates/*.json"):
    d = json.load(open(f))
    candidates[d["chapter"]] = d

# Load verified events
verified = json.load(open(f"{ROOT}/book/events/events_verified.json"))

# Load some analysis samples per chapter for context
SAMPLE = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].lstrip("-+").isdigit() else 5

PROMPT = """You are a chief editor compiling a book about Indian stock markets. Given below: a book PART description, its constituent CHAPTERS, a sample of source transcript IDs mapped to these chapters, and a sample of web-verified market events.

Write a COMPILER BRIEF for this part (not the full chapter content). Include for EACH chapter:
1. **Purpose** (1-2 lines): what this chapter must teach
2. **Key sources**: transcript IDs to use, with guidance on what each contributes
3. **Verified facts** to anchor the chapter on (from the events list)
4. **Enhancement tasks**: which complex topics need worked examples/tables
5. **Complexity estimate**: easy / medium / hard (for word budget)
6. **Length target**: suggested words (within the overall part budget)

Format: Markdown. Keep concise - the writers will flesh out.

PART: "{part_name}" (Chapters {chapters})
ANALYSIS SOURCE SAMPLE (transcript IDs mapped to this part):
{source_sample}

VERIFIED EVENTS SAMPLE (relevant to this part):
{events_sample}
"""

def call_api(prompt):
    resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers={
        "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"
    }, json={
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 4096
    }, timeout=120)
    return resp.json()["choices"][0]["message"]["content"].strip()

for pnum, pname, chs in PARTS:
    print(f"\nPart {pnum}: {pname} ({len(chs)} chapters)...")
    # Gather source IDs for this part
    src_ids = set()
    for cn in chs:
        if cn in candidates:
            for cid in candidates[cn].get("candidates", []):
                src_ids.add(cid)
    if not src_ids:
        print(f"  No candidates for part {pnum}, skipping")
        continue

    # Sample the source IDs
    src_sample = list(src_ids)[:SAMPLE*5]
    # Find relevant verified events
    part_keywords = []
    for cn in chs:
        text = candidates[cn] if isinstance(candidates[cn], str) else json.dumps(candidates[cn])
        # keyword heuristic
    # simpler: take top events and filter later
    events_sample = [e for e in verified if e["verdict"] != "unverifiable"][:10]

    prompt = PROMPT.replace("{part_name}", pname)\
                   .replace("{chapters}", json.dumps(chs))\
                   .replace("{source_sample}", json.dumps(src_sample, indent=1)[:2000])\
                   .replace("{events_sample}", json.dumps(events_sample, indent=1)[:2000])

    try:
        content = call_api(prompt)
        out = f"{ROOT}/book/chapters/briefs/part_{pnum:02d}_{pname.lower().replace(' ','_')[:30]}.md"
        os.makedirs(f"{ROOT}/book/chapters/briefs", exist_ok=True)
        with open(out, "w") as f: f.write(content)
        print(f"  -> {len(content)} chars -> {os.path.basename(out)}")
    except Exception as e:
        print(f"  FAILED: {e}")
    time.sleep(1)  # rate limit

print("\nPhase 4 compiler complete.")