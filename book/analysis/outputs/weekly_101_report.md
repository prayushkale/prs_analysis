# Batch weekly_101 Report — 20 Dalal Street Week Ahead transcripts (Jul–Nov 2022)

## Digest
- **Records:** 20/20 transcripts processed → `book/analysis/batch_weekly_101.jsonl` (20 clean JSON lines, validated).
- **Extraction:** 80 verifiable event claims, 40 transferable lessons, 1 quote per transcript, identity/promo leaks logged in all 20 records.
- **Most notable events (flagged for web verification):** US CPI 9.1% historic print (Jun-22) yet markets rose (surprise lesson); Jackson Hole 9-minute speech / $78B rich-list loss; Nasdaq +9.4% two-day rally after Nov-22 CPI (biggest in 15 years); NSE ruling that HDFC merger keeps Nifty weightage (HDFC +6%); India windfall-tax cut (13,300→10,500/tonne); iron-ore export duty cut to zero; Nord Stream 1 halt; Xi house-arrest rumour (marked verify:false — unconfirmed); Nasdaq 13,700→12,000 post-Jackson-Hole; Rakesh Jhunjhunwala's death at 62.
- **Recurring structural content:** OI-based range construction (max-OI strikes, straddle-premium breakeven math), FII futures positioning % (83%→55% shorts; 65% long in Nov), VIX regime reads (India VIX <15 = bull zone, >20 = stress), stock-of-the-week series with entry/stop/target mechanics (HDFC Bank, JSW Steel, IndiGo, Muthoot, Eicher short, Bharat Forge, OFSS, Reliance AGM spread, SAIL), seasonality doctrine (October bullish, Diwali ATH cluster, September volatile), decoupling thesis (Asia vs Europe/US), surprise-vs-expected reaction doctrine.
- **Data quality:** Good.docx-era transcripts are cleanly transcribed; consistent ASR garbles corrected per dictionary (taxbeddy→TaxBuddy, weeks→VIX, Quattac→Kotak, Toji→Doji, CB→SEBI, ICSA→ICICI, Motocop→Motocorp, Potag→RBL/"Portag"→uncertain-flagged). One claim (21,000 Dec-23 CE 455→400) marked verify:false as internal-trade anecdote; one Bank of Baroda loss-then-rally anecdote marked verify:false (date uncertain).
- **Leak patterns (for scrub list):** sponsor mentions in every episode (Delta.Exchange, TaxBuddy), name variants ("P. R. Sundar", "P R Sunder", "P. S. Sundar"), Singapore/Dubai/Bali travel hints, workshop/conference promos + "link in the description", "Hope you enjoyed watching" outros, personal P&L anecdotes (₹1 crore Adani trades, S-Class, Rolls-Royce joke), Twitter/social-media self-references, "not a SEBI-registered analyst" disclaimers.

## Notable dates covered
1107 (10 Jul) → 1119 (17 Jul) → 1132 (24 Jul) → 1146 (31 Jul) → 1158 (7 Aug) → 1173 (14 Aug) → 1188 (21 Aug) → 1205 (28 Aug) → 1223 (4 Sep) → 1241 (11 Sep) → 1253 (18 Sep) → 1270 (25 Sep) → 1284 (2 Oct) → 1295 (9 Oct) → 1306 (16 Oct) → 1317 (23 Oct) → 1325 (30 Oct) → 1336 (6 Nov) → 1345 (13 Nov) → 1356 (20 Nov) — a continuous weekly record of the 2022 H2 bear-market bottom (15,200 low → ATH attempt at 18,600).

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 assigned transcripts read in full; 20 validated JSON records written to book/analysis/batch_weekly_101.jsonl with the required schema (id, date, type, summary, levels, events, lessons, quote, dup_flag, leaks); report written to the authoritative output path book/analysis/outputs/weekly_101_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_101.jsonl",
    "book/analysis/outputs/weekly_101_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c (validate JSONL: parse every line, check 20 records, required ids present, schema fields present)",
      "result": "passed",
      "summary": "20 records, 0 bad lines, all required ids present, 80 events / 40 lessons extracted"
    }
  ],
  "validationOutput": [
    "records: 20, bad lines: 0",
    "all required ids present: True",
    "total events: 80, total lessons: 40, leaks noted in 20/20 records"
  ],
  "residualRisks": [
    "Event claims carry speaker-asserted numbers pending Phase 3 web verification; two anecdotes marked verify:false (undated Bank of Baroda rally, personal IV-crush trade)",
    "A few ASR-garbled stock names remain uncertain (e.g. 'Potag bank', 'katha steel', 'edamtha') and were not forced into corrections"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured per-transcript analysis (JSONL, 20 records) and a batch report (md) for weekly transcripts 1107-1356",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch covers a continuous weekly record of the 2022 H2 bear-market bottom and recovery; stock-of-the-week mechanics and OI/straddle-breakeven arithmetic are recurring chapter material."
}
```
