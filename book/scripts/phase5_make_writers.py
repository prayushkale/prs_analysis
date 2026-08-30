#!/usr/bin/env python3
"""Phase 5 generator: create chapter-writer workflowScript JS files.
Run: python3 book/scripts/phase5_make_writers.py
Then: subagent workflowScriptPath=book/scripts/phase5_wave0.js (wave 1, etc.)
Waves of 8 part-writers (recommended for cost) or 31 chapter-writers.
"""
import json, os, re

ROOT = "/home/ubuntu/repos/prs_analysis"
BRIEFS = f"{ROOT}/book/chapters/briefs"
OUT_DIR = f"{ROOT}/book/chapters"

# 8 parts merging adjacent chapters (cost-saving approach)
parts = {
    "part1-mind": {"chapters": "01-why-traders-lose|02-anatomy-of-failure|03-discipline-process",
                   "title": "Part I: The Trader's Mind"},
    "part2-mechanics": {"chapters": "04-fii-dii-flows|05-vix-regimes|06-option-chain|07-microstructure",
                         "title": "Part II: How This Market Works"},
    "part3-options": {"chapters": "08-why-derivatives|09-calls-and-puts|10-greeks|11-implied-volatility|12-margins",
                      "title": "Part III: Options from First Principles"},
    "part4-strategies": {"chapters": "13-short-straddles|14-spreads-ratios|15-calendars|16-butterflies|17-hedges|18-firefighting",
                         "title": "Part IV: The Strategy Library"},
    "part5-events": {"chapters": "19-event-playbook|20-budgets-elections|21-wars-black-swans",
                     "title": "Part V: Trading the Events"},
    "part6-chronicle": {"chapters": "22-chronicle-2018-2020|23-chronicle-2021-2022|24-chronicle-2023-2024|25-chronicle-2025-2026",
                        "title": "Part VI: A Market Chronicle 2018–2026"},
    "part7-regulation": {"chapters": "26-retail-scams|27-regulation|28-taxation",
                         "title": "Part VII: Predators & Protectors"},
    "part8-wealth": {"chapters": "29-investing-vs-trading|30-real-assets|31-crypto",
                     "title": "Part VIII: Wealth Beyond the Screen"},
}

def slug(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    return re.sub(r"\s+", "-", s.strip()).strip("-")

writer_prompt = """You are a chapter writer for "Dhanraj" — a print book about Indian stock markets compiled from 3,253 transcripts (2018–2026). Write {title} in polished English. Third-person teaching voice; first-person only for personal anecdotes attributed to Dhanraj.

VOICE RULES: Clear, direct English. Dated levels are illustrative, not evergreen. No political opinion. No reference to banned terms (identified in briefs below).

ANONYMIZATION: NEVER use: Sundar/Sunder/PRS/Pia/Pierre/any real name, Delta Exchange/TaxBuddy/5paisa/Finbingo/NEST, Chennai/Dubai/Singapore, workshop/conference/charity, son/wife/family/channel/brand. Replace personal P&L with genericized examples.

INPUTS (read each brief fully - use read tool):
{inputs}

OUTPUT: Write to book/chapters/{outname}.md
Target {word_target} words. Structure: hook (dated market moment) -> first-principles exposition -> worked example (where applicable) -> real-market case study from brief's source IDs -> Key Takeaways box (3-6 bullets).

Enhance complex topics with worked numerical examples and payoff tables where briefs flag them.
"""

entries = []
for key, info in parts.items():
    chs = info["chapters"]
    briefs = []
    for c in chs.split("|"):
        bf = os.path.join(BRIEFS, f"{c}.md")
        if os.path.exists(bf):
            briefs.append(bf)
    inputs = "\n".join(f"- {b}" for b in briefs)
    task = writer_prompt.replace("{title}", info["title"]).replace("{inputs}", inputs).replace("{outname}", key).replace("{word_target}", "5000" if len(briefs) <= 3 else "7000")
    entries.append({"key": key, "agent": "worker", "model": "openrouter/deepseek/deepseek-v4-flash:low",
                    "task": task, "output": os.path.join(OUT_DIR, f"{key}_writer_report.md")})

# 8 writers → one wave
js = "const tasks = " + json.dumps(entries, ensure_ascii=False) + ";\nconst results = await runs.all(tasks);\nreturn results.map((r,i)=>[tasks[i].key, String(r).slice(0,120)]);\n"
open(f"{ROOT}/book/scripts/part_writers.js", "w").write(js)
print(f"part_writers.js: {len(entries)} children (deepseek-v4-flash:low)")
print("Ready: subagent workflowScriptPath=book/scripts/part_writers.js")