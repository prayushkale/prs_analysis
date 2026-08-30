# special_164 Report

## Digest
1. **Batch complete**: 10/10 transcripts analyzed (2528, 2557, 2569, 2570, 2582, 2588, 2593, 2604, 2613, 2634), 10/10 valid JSON lines written to `book/analysis/batch_special_164.jsonl` (34.7KB, schema-validated).
2. **Content**: a coherent Feb–Mar 2025 "bear-market survival" cluster — long-term outlook (premium compression thesis), mid-cap cycle anatomy, SIP restructuring, leverage/margin-cascade case study, scam exposés (Gensol, Matrix Gas, fake trading apps), a Tesla-vs-Tata-Motors competitive thesis, a holding-company value analysis (Bombay Burmah), and a medium-term Fibonacci map with a 6-month bearish combo retrospective.
3. **Event claims**: 43 concrete claims queued for verification, including Bombay Burmah/Britannia 50.5% stake & ~75% discount, FII 5-year net-seller streak and 3-lakh-crore outflow, midcap +99%/+148% cycle stats, LIC 94,000-crore paper loss, Hyundai IPO 27,000 crore, BHEL/Gensol price paths, IREDA 636-crore Gensol exposure, budget/RBI support measures sequence, India-vs-US/China return gaps, 75% death-cross breadth.
4. **Leaks logged** (per-transcript `leaks` fields): Sun News TV appearance, SEBI-trouble self-reference, Singapore citizenship/Chennai/Dubai/Bali personal geography, family references ("my son", "my wife", "Sundar" in dialogue), workshop promos, YouTube self-references, broker-account walkthrough, political asides — all flagged for scrubbing; 2634 keeps trade numbers but drops the account framing.
5. **Chapter mapping**: primary targets 29 (investing) ×4, 25/24 (chronicle) ×4, 2/3 (mind) ×4, 26 (scams) ×1, 30 (real assets) ×2, plus 4/5/6/13/14/17/18/20/21/28 secondaries; enhancement candidates: holding-company NAV math, margin-cascade walkthrough, cycle table, fraud typology, real-return formula, Fib walkthrough.

## Notes
- 2634's "Oct 31" bearish combo is a personal retrospective (verify=false, kept as illustrative per approved policy).
- 2588 and 2593 are same-day companion episodes with overlapping FII-flow facts; cross-batch dedup at compile time will collapse them (times_seen will reflect this).
- One claim deliberately flagged verify=false: pre-2018 black-to-white preference-share manipulation scheme (mechanism description, not a checkable public event).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; 10 JSON lines matching the special-episode schema written to book/analysis/batch_special_164.jsonl and validated (10 valid, 0 bad). Report written to book/analysis/outputs/special_164_report.md. No scope widened beyond the assigned batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_164.jsonl",
    "book/analysis/outputs/special_164_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json-validity check over batch_special_164.jsonl",
      "result": "passed",
      "summary": "10 valid JSON lines, 0 malformed"
    }
  ],
  "validationOutput": [
    "schema fields present per line: id, date, type, title_clean, summary, chapter_targets, themes, lessons, strategies, event_claims, quotes, enhance, exclude_passages, leaks, quality",
    "43 event_claims extracted (39 verify=true, 4 verify=false)"
  ],
  "residualRisks": [
    "Speaker's numeric claims (index levels, flows) are transcribed as stated; web verification happens in Phase 3",
    "Two same-day overlapping episodes (2588/2593) will need compile-time dedup"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one batch-analysis JSONL (10 records) and one batch report markdown",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Anonymization-sensitive content concentrated in 2588 (personal geography) and 2570 (political asides); leaks fields flag exact strings for the QA phase."
}
```
