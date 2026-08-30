#!/usr/bin/env python3
"""Generate Phase 3 verification agent waves."""
import json, os

ROOT = "/home/ubuntu/repos/prs_analysis"
batches = json.load(open(f"{ROOT}/book/events/verification_batches.json"))

def make_task(b):
    items = b["items"]
    lines = []
    for i, item in enumerate(items):
        lines.append(f'{i+1}. {item["claim"][:220]} (date: {item.get("date","unknown")}, seen {item["times_seen"]}x)')
    claims_text = "\n".join(lines)
    return f"""You are a fact-checker for a market history book about the Indian stock market 2018-2026. For EACH claim below, use web_search to verify it against reliable sources (NSE/BSE data, SEBI circulars, RBI/Fed announcements, major financial news). Output EXACTLY one JSON object per line (no markdown fences, no extra text) with schema:
{{"id":"{b["id"]}","claim":"<truncated claim text>","verdict":"verified|corrected|unverifiable","corrected_fact":"<corrected fact if verdict=corrected, else same as claim>","sources":["<url>"],"confidence":"high|medium|low"}}

Rules:
- Search for each claim individually; use 1-3 web searches per claim.
- "verified" = claim matches public record; "corrected" = materially wrong (wrong date/level/direction) - provide corrected_fact with the right data; "unverifiable" = cannot be confirmed or too vague.
- Include source URLs for verified/corrected items.
- Be strict with numbers and dates.

CLAIMS TO VERIFY:
{claims_text}

Write all JSON lines to the file exactly as specified, one per claim, in order. You do NOT need to write a report file; just return the same JSON lines in your final message."""

def build(tasks, fname):
    js = "const tasks = " + json.dumps(tasks, ensure_ascii=False) + ";\nconst results = await runs.all(tasks);\nreturn results.map((r,i)=>[tasks[i].key, String(r).slice(0,150)]);\n"
    with open(f"{ROOT}/book/scripts/{fname}", "w") as f:
        f.write(js)
    print(f"wrote {fname}: {len(tasks)} agents")

os.makedirs(f"{ROOT}/book/events/outputs", exist_ok=True)

all_tasks = []
for b in batches:
    all_tasks.append({
        "key": b["id"],
        "agent": "worker",
        "model": "openrouter/z-ai/glm-5.3-flash:low",
        "task": make_task(b),
        "output": f"{ROOT}/book/events/outputs/{b['id']}_report.md",
    })

# waves of <= 60
w0, rest = all_tasks[:60], all_tasks[60:]
build(w0, "phase3_verifiers_0.js")
if rest:
    build(rest, "phase3_verifiers_1.js")
print("total agents:", len(all_tasks))