#!/usr/bin/env python3
"""Assemble manuscript.md from front matter + 31 chapters + generated appendices."""
import json, glob, re

ROOT = "/home/ubuntu/repos/prs_analysis"
PARTS = [
    ("PART I — THE TRADER'S MIND", ["01","02","03"]),
    ("PART II — HOW THIS MARKET WORKS", ["04","05","06","07"]),
    ("PART III — OPTIONS FROM FIRST PRINCIPLES", ["08","09","10","11","12"]),
    ("PART IV — THE STRATEGY LIBRARY", ["13","14","15","16","17","18"]),
    ("PART V — TRADING THE EVENTS", ["19","20","21"]),
    ("PART VI — A MARKET CHRONICLE, 2018–2026", ["22","23","24","25"]),
    ("PART VII — PREDATORS & PROTECTORS", ["26","27","28"]),
    ("PART VIII — WEALTH BEYOND THE SCREEN", ["29","30","31"]),
]

front = open(f"{ROOT}/book/final/frontmatter.md").read()
out = [front, "\n\n"]

# TOC
out.append("## Contents\n\n")
for ptitle, chs in PARTS:
    out.append(f"**{ptitle}**\n\n")
    for n in chs:
        text = open(f"{ROOT}/book/chapters/parts/ch{n}.md").read()
        m = re.match(r"#\s+Chapter \d+:\s*(.+)", text)
        title = m.group(1).strip() if m else f"Chapter {int(n)}"
        out.append(f"- Chapter {int(n)}: {title}\n")
    out.append("\n")

# Appendices placeholders (content added by build scripts)
out.append("**Appendices**\n\n- A: Glossary\n- B: Strategy Quick Reference\n- C: Verified Market Timeline 2018–2026\n- D: Sources and Verification Notes\n- E: Correction Log\n\n")

for ptitle, chs in PARTS:
    out.append(f"\n\n# {ptitle}\n\n")
    for n in chs:
        text = open(f"{ROOT}/book/chapters/parts/ch{n}.md").read().strip()
        # normalize H1 chapter headings to H2 for print hierarchy
        text = re.sub(r"^# ", "## ", text, count=1, flags=re.M)
        out.append(text + "\n\n")

manuscript = "".join(out)
open(f"{ROOT}/book/final/manuscript.md", "w").write(manuscript)
words = len(manuscript.split())
print(f"manuscript.md assembled: {words:,} words (front+chapters)")

# ---- Appendix C: verified timeline ----
recs = [json.loads(l) for l in open(f"{ROOT}/book/events/events_verified_enriched.jsonl")]
tl = []
for r in recs:
    if r["verdict"] in ("verified", "corrected") and r.get("date"):
        claim = r.get("corrected_claim") or r.get("claim","")
        tl.append((r["date"], claim.strip()))
tl.sort()
with open(f"{ROOT}/book/final/appendix_c_timeline.md", "w") as fh:
    fh.write("## Appendix C: Verified Market Timeline, 2018–2026\n\n")
    fh.write("Events below were asserted in the source commentary and verified against public records (verdicts 'verified' or 'corrected'; corrected facts shown).\n\n")
    cur = None
    for d, c in tl:
        y = d[:4]
        if y != cur:
            fh.write(f"\n### {y}\n\n")
            cur = y
        c = re.sub(r"\s+", " ", c)[:320]
        fh.write(f"- **{d}** — {c}\n")
print("appendix C entries:", len(tl))

# ---- Appendix E: correction log ----
corr = [r for r in recs if r["verdict"] in ("corrected", "wrong") and r.get("corrected_claim")]
with open(f"{ROOT}/book/final/appendix_e_corrections.md", "w") as fh:
    fh.write("## Appendix E: Correction Log\n\n")
    fh.write("Where the original commentary materially misstated a fact, the verified correction is recorded here.\n\n")
    for r in corr[:200]:
        fh.write(f"- **Original:** {r.get('claim','')[:200]}\n  **Corrected:** {r['corrected_claim'][:250]}\n  **Verdict:** {r['verdict']}\n\n")
print("appendix E entries:", len(corr))

# ---- Appendix D: sources ----
urls = {}
for r in recs:
    for e in r.get("evidence", []) or []:
        u = e.get("url")
        if u and u.startswith("http"):
            urls[u] = e.get("title", "")
with open(f"{ROOT}/book/final/appendix_d_sources.md", "w") as fh:
    fh.write("## Appendix D: Sources and Verification Notes\n\n")
    fh.write(f"Verification performed against {len(urls)} distinct public sources, including exchange/regulator publications and financial press archives.\n\n")
    for u, t in sorted(urls.items()):
        fh.write(f"- {t} — {u}\n")
print("appendix D sources:", len(urls))
