# HANDOFF — "Dhanraj" Book Project
_Updated: 30 Aug 2026 · Status: paused at user request (token budget) · Resume-ready_

## Project goal
Turn 3,288 transcripts (2018–2026, "PRS Data/") into ONE anonymized, web-verified, print-ready book PDF (6"×9", ~500 pages) by "Dhanraj". No trace of the original channel/person/associates. Parallel subagent analysis (done); single compiler (pending).

## Locked decisions (user-approved)
1. Single volume ~500 pages · 2. Voice: distillation + first-person anecdotes · 3. P&L figures kept as genericized illustrative anecdotes + disclaimer · 4. Hybrid corrections (silent trivial fixes; endnote+source for material discrepancies) · 5. Political opinion excluded; market-relevant policy kept · 6. Typst for PDF build · 7. Subagents on LOW thinking (`deepseek-v4-flash:low`), main agent high thinking.

## Current state
| Phase | Status |
|---|---|
| 0 Corpus build | ✅ DONE — 3,288/3,288 extracted to `book/corpus/NNNN.txt`, headers/identity stripped, 100% dated, `book/meta/metadata.jsonl` |
| 1 Editorial bible | ✅ DONE — `book/editorial/`: voice_guide.md, banned_terms.md, chapter_map.md (user-approved), reader_R1–R8.md, sample_manifest.json |
| 2 Transcript analysis | ✅ DONE — 170/170 batches, **3,253/3,253 transcripts** analyzed → `book/analysis/batch_*.jsonl` (schema per phase2_make_batches.py) |
| 3 Event verification | 🔶 78% — 70/90 batches done (700 claims: 368 verified, 254 corrected, 73 unverifiable, 5 wrong) → `book/events/verified_batch_*.jsonl`. **20 batches (200 claims) remain** |
| 4 Chapter briefs | ⬜ Not started |
| 5 Chapter writing | ⬜ Not started |
| 6 Anonymization + QA | ⬜ Not started |
| 7 Typst build | ⬜ Not started |

## Key files
- Scripts: `book/scripts/` (phase0_extract.py, phase0b_strip_headers.py, phase2_make_batches.py, phase3_prep_queue.py, phase3_cluster.py, phase3_make_remaining.py)
- Queues: `book/events/bulk_verify_queue.json` (900 claims), `ondemand_pool.json` (8,544), `queue_clusters.json`
- Chapter plan: `book/editorial/chapter_map.md` — 8 parts / 31 chapters + appendices, with per-chapter source mapping in reader reports

## RESUME — run in this order
1. **Finish Phase 3** (~20 small children, cheap):
   - `python3 book/scripts/phase3_make_remaining.py` → regenerates `book/scripts/phase3_resume_w*.js` from disk state
   - Run each `phase3_resume_w*.js` via `subagent {workflowScriptPath, async:false, timeoutMs:3600000}`
   - Model: `openrouter/deepseek/deepseek-v4-flash:low` (glm-5.3-flash excluded account-wide until 31 Aug ~06:29 UTC — use deepseek or any registry model; **never glm-5.3-flash:high with 30+ concurrent children**: in-flight credit budget trips at ~30)
   - Merge: concatenate all `verified_batch_*.jsonl` → `book/events/events_verified.jsonl`
2. **Phase 4 — Chapter briefs (1 compiler agent, high context)**:
   - Give ONE `worker` (or run as main agent) the inputs: chapter_map.md, voice_guide.md, banned_terms.md, metadata.jsonl, and a per-chapter scan of `book/analysis/*.jsonl` (select records by chapter_targets/themes). Output: `book/chapters/briefs/NN-slug.md` with transcript-id source lists, dedupe instructions, enhancement tasks.
   - Tip: build a compact per-chapter candidate list first with a small python script (grep chapter_targets across analysis JSONLs) so the compiler prompt stays small.
3. **Phase 5 — Writing (parallel, LOW thinking)**: one writer per part (8 writers) or per chapter (31) from briefs + referenced analysis JSONs + verified facts; complex-topic enhancement agents where briefs flag them; single compiler merge pass → `book/final/manuscript.md`.
4. **Phase 6 — QA**: scripted banned-term scan (python, terms from banned_terms.md incl. ASR variants: "Sundar|Sunder|PRS|prsundar|Delta|TaxBuddy|5paisa|Finbingo|Chennai|Dubai|Singapore|son|wife|workshop|channel|subscribe|thumbnail|description") = must be 0 hits; then 1 reviewer per part (low thinking), fixes applied.
5. **Phase 7 — PDF**: install typst (single binary or `pip install typst`); 6"×9" template with TOC, chapter endnotes (from corrected verdicts), appendices A–E per chapter_map; build `book/final/book.pdf`; validate TOC/pages/fonts; final scan of extracted PDF text.

## Cost-control lessons learned (IMPORTANT)
- 64 concurrent glm-5.3-flash:high children ≈ consumed the key's in-flight budget twice. **Cap waves at ≤25-30 children on :low models.**
- Low thinking was ~5× faster and materially cheaper with no quality loss for extraction/verification tasks.
- On-demand verification pool (`ondemand_pool.json`, 8,544 items) exists precisely so NO further bulk verification is needed — writers cite only bulk-verified facts or mark `[VERIFY]` for spot checks.
- The biggest remaining cost is Phase 5. Recommend: 8 part-writers instead of 31 chapter-writers, deepseek :low, chapters ≤5K words per pass, and skip separate enhancement agents (fold enhancement instructions into writer prompts).
- If the key trips again: failures are checkpointed; just rerun `phase3_make_remaining.py`-style disk-state regeneration — nothing is ever lost. (If a model gets excluded, wait out the exclusion TTL or switch registry model.)

## Interruption forensics
- Wave-2 verification abort killed children ver_060–089 mid-flight; 12 of 20 missing files are from that wave; disk-state regen already accounts for everything (missing = 003,006,009,010,018,024,035,041,043,048,061,062,066,067,073,076,082,083,086,087).
- Nothing in Phases 0–2 needs re-running.

## Working conventions
- All state on disk, git-committed (`book/` tree). Rollback = `git checkout` last good commit; rerun only failed units.
- Author persona: "Dhanraj"; banned-terms list is the single source of truth for anonymization; 2923/1383/2926 + 34 first-pass exclusions are dropped videos.
