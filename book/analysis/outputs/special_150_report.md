# Batch special_150 Report — 10 transcripts (Mar–Apr 2023 specials)

## Digest
1. **Records written:** 10/10 JSON lines → `book/analysis/batch_special_150.jsonl` (validated JSON, one line per transcript, in order).
2. **Notable content:** 4 substantial explainers — broker-fund-safety/ASBA reform (1539), yield-curve inversion & recession (1547), Fed dilemma/SVB–Credit Suisse (1560), IT-sector structural decline (1573). High verification value: ~20 concrete event claims (SVB −60% day, Credit Suisse −25% record low, Nifty 16,800→18,900→16,900 round trip, IT index −22.38% vs Nifty −1.38%, debt-fund tax change Apr 1 2023).
3. **Duplicates flagged:** 1554≈1547, 1569=1560 (verbatim), 1580=1573 (verbatim) — compiler should drop dupes; 4 short stubs (1545, 1554, 1582, 1585) are partial transcripts of promo/fragment videos.
4. **Leaks noted for QA:** name variants ("PR Sunder", "P. R. Sundar"), course promo (1545), Delta Exchange sponsor mention (1585), personal-holdings/self-attribution passages (1539, 1582) — all captured in per-record `leaks`/`exclude_passages`.
5. **Chapter mapping:** strongest feeds to 26/27 (scams/regulation), 21/22 (black swans/chronicle), 29 (investing), 13/18 (straddle fragment), 28 (taxation), 14/31 (crypto ratio fragment).

## Data quality
- 1539, 1547, 1560, 1573: quality 4–5, full-text, dense facts.
- 1545, 1582, 1585: quality 1–2 stubs; content preserved where extractable, marked fragmentary.
- Duplicates quality 1 with cross-references to canonical ids.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts read in full; 10 valid JSON records written in order to book/analysis/batch_special_150.jsonl matching the requested schema (id/date/type/summary/chapter_targets/themes/lessons/strategies/event_claims/quotes/enhance/exclude_passages/leaks/quality); dup flags set for 1554/1569/1580; identity strings recorded in leaks only, never as output content."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_150.jsonl",
    "book/analysis/outputs/special_150_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "wc -c corpus/{1545,1547,1554,1560,1569,1573,1580,1582,1585}.txt",
      "result": "passed",
      "summary": "Identified 4 stub files (<1KB) and 2 exact-size duplicate pairs before deep reading"
    },
    {
      "command": "read tool on 10 transcript files",
      "result": "passed",
      "summary": "All 10 transcripts read completely (2,366-word main transcripts + stubs)"
    }
  ],
  "validationOutput": [
    "10/10 records cover the 10 assigned ids in order (1539,1545,1547,1554,1560,1569,1573,1580,1582,1585)",
    "All lines are single-line parseable JSON objects",
    "3 verbatim/near-verbatim duplicates flagged for compiler dedup (1554->1547, 1569->1560, 1580->1573)",
    "No real-name strings outside leak logs"
  ],
  "residualRisks": [
    "Stub transcripts (1545/1554/1582/1585) are partial captures - their full strategy/tax content exists in other fuller transcripts; compiler should not treat these as the canonical source",
    "Event claims marked verify:true (~20) need web verification before print, especially exact % moves and dates"
  ],
  "noStagedFiles": true,
  "diffSummary": "Created structured analysis JSONL for batch special_150 (10 records, 16.4KB) plus markdown digest report",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch contains an unusually high share of duplicates/fragments (3 verbatim dupes, 4 stubs) - typical of the Mar-2023 promo-heavy period; canonical content is in 1539/1547/1560/1573 which are dense and well-mapped to chapters 21, 22, 26, 27, 29."
}
```
