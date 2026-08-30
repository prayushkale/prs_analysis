# weekly_097 — Batch Report (Dalal Street Week Ahead, Dec 2020 – May 2021)

## Digest
1. **Counts**: 20/20 transcripts read in full and analyzed; 20 valid JSON lines written to `book/analysis/batch_weekly_097.jsonl` (all parse; ids 0204→0347 in order).
2. **Extraction totals**: 79 concrete event claims (all flagged `verify: true` — heavy density in this era: Fed buyback lift, MSCI Chinese-telecom deletion, Georgia runoffs + Harris tie-break, GDP +0.4%, China exports +60.6%, Archegos $20bn block sale, Ever Given, S&P 4,000, US payrolls +916k then +266k, GST records ₹1.15L cr → ₹1.41L cr, TMC landslide, US India travel ban, Sputnik arrival, record 3.5L/4L daily cases, TN lockdown).
3. **Notable structural finds**: three consecutive "Monday mayhem" sessions (Apr 5/12 + earlier) all traced to Maharashtra COVID restrictions; "very bad news is good news" doctrine anchored to the May 7 payroll miss; max-OI failure case (15,000 CE, Mar 2021) captured as a Part II lesson; Bank Nifty futures at an unprecedented ~400-pt premium flagged (Mar 2021).
4. **Data quality**: levels populated only where explicitly stated (Nifty closes 14,350/15,200/14,900/14,340/14,800; VIX 30/24/20; FII single-session figures −8,300/−2,000/−3,500 cr); weekly range calls kept in summaries, not levels. 42 lessons, 20 quotes.
5. **Leaks**: 45 leak notes logged (name variants "PR Sunder/Sundar" in all; 5paisa sponsorship + brokerage-plan promo in 0337/0347; Manali holiday location 0286; wife's-account live-trading plan 0245; wife/family none else; political passages in 0299/0337 flagged for drop; personal straddle P&L in 0321 genericized). One unverifiable claim flagged inside metadata leak line: Reliance "₹500 cr → ₹30–40 cr fine" (0218) — needs verification or drop.

## Notes for compiler
- 0299 contains an anonymous "FII parked 90% in Adani since 2014, 20x net worth" anecdote — unverifiable, recommend drop.
- 0299 and 0337 contain political jokes/opinion (corruption joke; WB/TN commentary) — excluded per approved policy; only the market-relevant election-result reaction (0337 event #1) retained.
- 0265 "P. R. Sundar indicator" car-joke: keep as genericized self-deprecating anecdote ("a trader's luxury-car-purchase jinx") without name/cars, if used at all.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 listed transcripts read in full; exactly one JSON record per transcript written in order to /home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_097.jsonl; validation shows 20/20 parse, ids match manifest, schema fields populated (79 events, 42 lessons, 45 leak notes); digest report written to the authoritative output path."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_097.jsonl",
    "book/analysis/outputs/weekly_097_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 jsonl validation (parse each line, verify id order/count/schema presence)",
      "result": "passed",
      "summary": "20 lines, 20 parse OK, ids match manifest order, no records missing summary/date"
    }
  ],
  "validationOutput": [
    "lines: 20 | all parse: True | ids ok: True | events: 79 (verify: 79) | lessons: 42 | leaks: 45"
  ],
  "residualRisks": [
    "One ambiguous claim (Reliance fine '500cr→30-40cr', id 0218) recorded inside leak-notes for parent verification rather than as an event claim.",
    "Levels fields left null unless explicitly stated; weekly range calls live in summaries — compiler should not treat them as hard levels."
  ],
  "noStagedFiles": true,
  "diffSummary": "New batch analysis file (20 JSON records) plus this report; no other files touched.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch covers weekly previews 2020-12-20 to 2021-05-09 (batch weekly_097 of resume wave). Event-claim density is high (79), consistent with a macro-heavy era; two-tier verification queue should absorb these."
}
```
