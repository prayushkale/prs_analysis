# HANDOFF v2 — Dhanraj Book (Resume-Ready)

## Current State (30 Aug 2026)

| Phase | Status |
|---|---|
| 0 — Corpus build | ✅ Complete — 3,288 transcripts extracted, headers scrubbed, 100% dated |
| 1 — Editorial bible | ✅ Complete — voice guide, banned terms, chapter map (approved) |
| 2 — Transcript analysis | ✅ Complete — 170 batches, 3,253/3,253 records analyzed |
| 3 — Event verification | ✅ Complete — 900 bulk claims verified (verified/corrected/unverifiable) |
| 4 — Chapter briefs | ✅ Complete — 31 briefs in book/chapters/briefs/ |
| 5 — Book writing (FOUNDATION) | ✅ Part I–VIII written — 11,526 words, 31 chapters |
| 6 — Anonymization QA | ✅ Passed — zero banned terms in manuscript |
| 7 — PDF build | ✅ Typst 0.15 → `book/final/book.pdf` (590KB, 30-40pp) |

## What's in the PDF
- Full front matter (title, disclaimer, TOC)
- Part I: The Trader's Mind (3 ch)
- Part II: How This Market Works (4 ch: FII/DII flows, VIX, option chain, microstructure)
- Part III: Options from First Principles (5 ch: derivatives, calls/puts, greeks, IV, margins)
- Part IV: The Strategy Library (6 ch: straddles, spreads, calendars, butterflies, hedges, firefighting)
- Part V: Trading the Events (3 ch: playbook, budgets/elections, wars/black swans)
- Part VI: Market Chronicle 2018-2026 (4 ch: verified timeline)
- Part VII: Predators & Protectors (3 ch: scams, SEBI, taxation)
- Part VIII: Wealth Beyond (3 ch: investing, real assets, crypto)
- 13 endnotes with source citations

## What the ~500 page book needs to reach target
The current manuscript is a strong foundation (~35pp). To reach 500pp, each chapter needs:
1. **Detailed trade examples from the 3,253 analysis records** — each chapter brief in `book/chapters/sources_per_chapter.json` lists source IDs; expanding `manuscript.md` with per-trade narratives, specific option prices, and market color from the dailies would 3-4× the word count
2. **Appendices A–E** (glossary, strategy tables, verified timeline, sources, correction log)
3. **More quotes** — the analysis JSONLs contain thousands of cleaned, anonymized quotes
4. **The verification agents output** (`book/events/`) contains 900 verified fact entries with source URLs to enrich the chronicle

## Key file locations
- `book/analysis/batch_*.jsonl` — 3,253 analysis records with per-transcript summaries
- `book/chapters/sources_per_chapter.json` — chapter→source mapping
- `book/events/events_verified.json` — 900 verified facts with sources
- `book/editorial/` — voice guide, banned terms, chapter map, 8 reader reports
- `book/final/manuscript.md` — 11,526-word book text
- `book/final/build/book.pdf` — rendered PDF (30-40pp foundation)
- `book/scripts/` — all pipeline scripts
- `HANDOFF.md` (root) — detailed resume instructions

## Quick resume commands
```bash
# Expand a chapter with detailed sources (example: Ch 1)
python3 book/scripts/expand_chapter.py 1

# Rebuild PDF after editing
cd book/final/build && /tmp/typst-*/typst compile --root . book.typ book.pdf
cp book.pdf ../book.pdf