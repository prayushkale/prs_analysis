# How I Built a 518-Page Trading Book From 3,288 Trading Videos

> A field report on turning eight years of daily market commentary — several million spoken words — into a verified, print-ready book, using a pipeline of extraction, analysis, fact-checking, and typography.

---

## The problem

A practising Indian derivatives trader posted market commentary almost every trading day between late 2018 and mid-2026: a pre-market brief before the bell, a post-market review after the close, a weekly Sunday outlook — and, in between, a complete options course, hundreds of strategy breakdowns, and walkthroughs of every budget, election, war, and regulatory shock that touched Indian markets.

That is **3,288 transcripts** and **several million spoken words** of genuine trading education — but scattered across eight years of daily noise. Repeated. Revised. Occasionally contradicted as markets changed.

This is the story of how I took that raw material and produced **a 518-page, 6"×9", print-ready PDF book** — with 31 chapters across 8 parts, 5 appendices, and a database of 900 fact-checked market events.

The whole build ran in **8 phases**, numbered `phase0` through `phase7`, and every artifact is committed in the repo. Here's the engineering behind each one.

---

## Phase 0 — Corpus extraction: 3,288 files → clean text

**Script: `phase0_extract.py`, `phase0b_strip_headers.py`**

The source material lived as `PRS Data.zip` — a 160 MB archive of **2,366 `.docx` files and 922 `.txt` files**, one per video transcript, named inconsistently (promos, reruns, bad dates, duplicate numbers).

Phase 0 had to:

- **Parse `.docx` directly** — `zipfile` + WordprocessingML XML parsing, no heavyweight library (and no LibreOffice required).
- **Fix mojibake** — the transcripts were full of mangled UTF-8: `Γé╣` → `₹`, `ΓÇö` → `-`, `ΓÇÖ` → `'`, emoji garbage stripped, `├ù` → `x`. A hand-built character map normalized everything.
- **Parse metadata** from filenames — ID, date, series type (daily / weekend / special), doc type — into **`book/meta/metadata.jsonl`**.
- **Detect duplicates and "wrong" files** — promos and non-trading content got flagged with an `excluded_firstpass` reason (e.g. `promo`).
- **Strip boilerplate headers** from each transcript so analysis wasn't polluted by opening credits.

Output: **`book/corpus/0001.txt` … `3288.txt`**, plus a clean metadata index. 100% of transcripts ended up dated.

---

## Phase 1 — The editorial bible: agreeing *what the book is* before writing it

**Script: `phase1_readers.js`**

Before generating a word, I locked the creative direction into an **editorial bible** (`book/editorial/`):

- **`chapter_map.md`** — the full blueprint: single volume, **6"×9", ~150k words ≈ 500 pages**, 8 parts, 31 chapters, with a word budget and *source attribution per chapter* (which transcript IDs feed which chapter).
- **`banned_terms.md`** — the anonymization and style blacklist.
- **8 "reader reports"** (`reader_R1.md`…`R8.md`) — structured review passes giving feedback on the plan before committing to it.

The bible decided the book's *point of view*: **the market is the protagonist** — the durable lesson, not the daily headline.

---

## Phase 2 — Transcript analysis: 3,253 records with structured signal

**Scripts: `phase2_wave0.js`, `phase2_wave1.js`, `phase2_wave2.js`, `phase2_make_batches.py`, `phase2_resume_wave0/1.js`**

Each transcript was batched and run through a reader model to produce **structured analysis records** in `book/analysis/batch_daily_*.jsonl`.

Each record carries:
- `id`, `date`, `type`
- `summary` — a condensed description of the episode
- `levels` — market levels / tick data mentioned
- `events` — discrete market events referenced
- `lessons` — the durable trading lessons
- `quote` — a cleaned, anonymized verbatim quote
- `dup_flag` — duplicate detection
- `leaks` — anonymization leaks (names, values) to scrub

The work was spread across **170 batch files** in resumable waves — a notebook-style long task chopped into checkpoints I could re-run after interruptions. Result: **3,253 / 3,253 records analyzed**.

---

## Phase 3 — Event verification: 900 claims fact-checked against the public record

**Scripts: `phase3_cluster.py`, `phase3_make_verifiers.py`, `phase3_verifiers_0/1.js`, `phase3_prep_queue.py`, `phase3_wiki_verify.py`, `phase3_complete_missing.py`, `phase3_run_remaining.py`, `phase3_rest_verify.py`**

The philosophy of the book was **"verification over memory."** So every market event named in the commentary — crashes, elections, the Adani–Hindenburg episode, the Jane Street order, FII exoduses — was pushed through a fact-checking queue.

- **`phase3_cluster.py`** clustered similar claims and deduplicated them.
- **Verifier agents** (multiple wave scripts) checked each claim against web sources: search + fetch, collecting URLs as evidence.
- **`phase3_wiki_verify.py`** cross-checked against structured/knowledge sources.
- Every claim got a verdict.

The final **`book/events/events_verified.json`** holds **900 events**:

| Verdict | Count |
|---|---|
| ✅ verified | 415 |
| 🔧 corrected | 292 |
| ❓ unverifiable | 188 |
| ❌ wrong | 5 |

Each entry has an `idx`, a `verdict`, a **`corrected_claim`** (the accurate narrative, with corrections noted where the source commentary misremembered a number), and `evidence` — a list of `{title, url}` source citations. Load-bearing facts in the book anchor to these citations.

---

## Phase 4 — Chapter briefs: the execution plan for each of 31 chapters

**Scripts: `phase4_candidates.py`, `phase4_prep_briefs.py`, `phase4_compiler.py`, `phase4_briefs.py`**

- **`phase4_candidates.py`** mapped analysis records and verified events to the right chapter.
- **`phase4_compiler.py`** called an LLM API (OpenRouter, `deepseek/deepseek-v4-flash` at the time) to turn each chapter's candidate material + verified facts into a **structured brief**.
- The result: **224 brief files** in `book/chapters/briefs/` (multiple brief drafts per chapter across the 31 chapters), plus a candidate index in `book/chapters/candidates/`.

Each brief specified what the chapter should cover, which sources to draw from, and which verified events to cite. This is what kept 31 chapters written by (possibly) different writer runs coherent — a shared plan from a single compiler.

---

## Phase 5 — Writing: assembling 31 chapters from briefs

**Scripts: `phase5_make_writers.py`, `phase5_writer.py`, `phase5_write_part.py`, `phase5_manuscript.py`, `phase5_assemble.py`, plus writer wave JS scripts**

Writing was itself a pipeline:

- **`phase5_manuscript.py`** produced the full manuscript text from the briefs.
- **`phase5_assemble.py`** combined parts into a single manuscript.
- Part-by-part writer runs (with retry and test scripts like `phase5_part6_retry.js`, `phase5_writers_w0/w1.js`) filled in chapters.

The output grew through three checkpoints, visible in the git history:

1. **`28c286d`** — book *foundation*: first manuscript + PDF + verification DB.
2. **`3a3ad77`** — **86-page** 6×9 PDF manuscript (all 31 chapters, 8 parts).
3. **`6511b8a`** — **518-page** final edition, with appendices and events DB.

Final manuscript word counts:
- `manuscript.md` — **51,298 words**
- `manuscript_full.md` — **118,041 words** (the expanded, print edition)

---

## Phase 6 — Anonymization & QA: zero banned terms

**Script: `phase6_review.js`**

A dedicated review pass swept the manuscript against the editorial bible:

- **Anonymization** — strip leaks of personal names and values (`leaks` flagged earlier in Phase 2 are re-checked here).
- **Style enforcement** — the `banned_terms.md` blacklist is enforced.

Result: **zero banned terms** in the final manuscript. This is the editorial bar that turns copyrighted *voice* into a defensible work of *synthesis*.

---

## Phase 7 — PDF build: Markdown → Typst → print-ready 518 pages

**Scripts: `phase7_convert.py`, `phase7_typst.py`, `phase7_typst_build.py`; binary: `book/bin/typst`**

The last mile was typesetting. I didn't use word processors — I used **Typst**, a modern markup/typesetting system (compile-time, unlike LaTeX).

- **`phase7_convert.py`** hardened the Markdown: escaped `[]#$@<>~'"` characters, converted `**bold**`/`*italic*` to Typst `#strong[]`/`#emph[]`, and stripped runtime artifacts (the Contents block, the runtime appendices listing).
- **`phase7_typst.py` / `phase7_typst_build.py`** generated the `.typ` template — **6"×9" paper**, 0.8" margins, 10pt body, `1.1.1` heading numbering, `Noto Sans`/`DejaVu Sans` text — and compiled with the bundled Typst binary.
- Output: **`book/final/book.pdf`** — **4.7 MB, 518 pages, print-ready**.

The book's structure (from `frontmatter.md`):

- **Front matter** — title page, disclaimer, preface, TOC
- **Part I** The Trader's Mind (3 ch)
- **Part II** How This Market Works (4 ch: FII/DII flows, VIX, option chain, microstructure)
- **Part III** Options from First Principles (5 ch)
- **Part IV** The Strategy Library (6 ch)
- **Part V** Trading the Events (3 ch)
- **Part VI** A Market Chronicle 2018–2026 (4 ch — built on the verified events DB)
- **Part VII** Predators & Protectors (3 ch)
- **Part VIII** Wealth Beyond the Screen (3 ch)
- **Appendices A–E** — glossary, strategy quick reference, verified timeline, sources & verification log, correction log

---

## The numbers, end to end

| Input | 3,288 transcripts | 2,366 `.docx` + 922 `.txt` |
|---|---|---|
| Analysis | **3,253 / 3,253** records | across **170** batch files |
| Verification | **900** events fact-checked | 415 verified · 292 corrected · 188 unverifiable · 5 wrong |
| Writing | **31 chapters / 8 parts / 5 appendices** | 118,041 words (full edition) |
| QA | **0** banned terms | anonymization + style pass |
| Output | **518-page 6"×9" PDF** | 4.7 MB, Typst-compiled |

## Lessons worth keeping

1. **Verification is a feature, not a tax.** The fact-checking database (`events_verified.json`) is what separates a *distillation of commentary* from a *book with a source log*. Every historical claim can point at citations.
2. **An editorial bible beats a good outline.** Locking voice rules, banned terms, source→chapter mapping, and word budgets *before* writing is what keeps dozens of written chapters coherent.
3. **Resumable waves > giant monolithic jobs.** Nearly every phase (`phase2_wave0/1/2`, `phase3_wave0/1/2`, `phase5_writers_w0/1`) was chunked into checkpoints. Long, flaky agent tasks are tamed by making them re-startable.
4. **Modern typesetting tools win.** Typst turned a Markdown manuscript into a genuinely print-ready 6×9 book in seconds — no LaTeX ceremony, no Word.
5. **Let the recency of numbers be honest.** 188 events were *unverifiable*, and 5 were simply *wrong* in the original commentary. The book records all five corrections in an appendix. A thesis nobody can check isn't worth printing.

---

*All pipeline scripts, intermediate JSONL, the verification database, and the final PDF are committed and recoverable — the full build is reproducible from the repo.*