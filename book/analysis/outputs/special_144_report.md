# Batch special_144 Report (10 transcripts, ids 1220–1242, Sep 2022)

## Digest
1. **Coverage**: 10/10 transcripts analyzed; 10 JSON lines written to `book/analysis/batch_special_144.jsonl`; all parse as valid single-line JSON.
2. **Content mix**: 1 full stock-analysis episode (1220 Tata Investment Corp), 2 full geopolitics/outlook episodes (1225 Nord Stream gas war, 1239 retail-flows outlook), 5 micro-lessons (1221 premium interest, 1226 delta, 1232 derivative types, 1238 MTM, 1222/1242 parables), 1 philosophy clip (1229).
3. **Verification queue**: 19 concrete event claims flagged (GDP 13.5%, Nord Stream shutdown details, Germany 55%→9.5% energy dependence, demat/SIP records, EM-fund 94%/12.7%→18%, China 14-year zero return, India-UK 5th-largest economy, London pub energy bill, Tata-group stock moves).
4. **Chapter targets**: mostly ch29 (investing), ch21/23 (wars/chronicle), ch4 (FII flows), ch8–12 (derivatives basics), ch1/3 (mind).
5. **Leaks**: name variants in 1220/1225/1239 ("P. R. Sundar/Sunder"), Sun TV appearance (1220), Tamil-cinema cultural framing (1222) — all logged in `leaks`/`exclude_passages` for scrubbing.

## Data-quality notes
- 1232: title says "4 TYPES" but transcript enumerates 5 (forwards, futures, options, swaps, swaptions) — recorded as-is.
- 1239: metadata date 2022-09-10 but transcript states recorded 3 Sep 2022 — noted in summary.
- 1221/1226/1229/1232/1238 are short clips (quality 2–3); 1220/1225/1239 are substantive (quality 4).

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts (1220-1242) read in full and converted to exactly 10 JSONL records at book/analysis/batch_special_144.jsonl with the mandated schema (id, date, type, title_clean, summary, chapter_targets, themes, lessons, strategies, event_claims, quotes, enhance, exclude_passages, leaks, quality); batch report written to book/analysis/outputs/special_144_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_144.jsonl",
    "book/analysis/outputs/special_144_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read book/corpus/{1220,1221,1222,1225,1226,1229,1232,1238,1239,1242}.txt",
      "result": "passed",
      "summary": "10/10 transcripts read in full"
    },
    {
      "command": "write book/analysis/batch_special_144.jsonl",
      "result": "passed",
      "summary": "10 JSONL records, one per transcript, in order"
    }
  ],
  "validationOutput": [
    "10 JSON lines, schema-complete; ASR corrections applied (Sunder->persona-neutral, SGX Nifty kept pre-2023); 19 verify-flagged event claims extracted; identity strings confined to leaks fields"
  ],
  "residualRisks": [
    "1229/1242 are near-content-free parables (quality 1-2) - compiler may drop them",
    "Event claims (e.g., 70,000->420,000 pound pub bill) are speaker-asserted and pending Phase-3 web verification"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_special_144.jsonl (10 records) and special_144_report.md digest",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "1232 title/transcript mismatch (4 vs 5 derivative types) recorded faithfully; 1239 recorded-3-Sep vs uploaded-10-Sep discrepancy noted for chronology"
}
```
