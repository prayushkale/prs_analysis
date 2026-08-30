# Batch daily_081 report (25 transcripts, ids 2836–2866, 2025-10-07 → 2025-10-28)

## Digest (5 lines)
1. **Counts:** 25/25 transcripts read in full and converted to JSONL at `book/analysis/batch_daily_081.jsonl` (25 valid JSON lines, schema-compliant, source order preserved; 12 pre-market, 13 post-market; zero extraction gaps).
2. **Most notable events:** Nifty's four-day ~900-point breakout attempt from 25,000 to 25,900 and the first 2025 intraday cross of 26,000 (failed close, twice); Trump's 100% China tariff (Oct 10) and Nasdaq's ~4% drop with a 48-hour U-turn; Trump sanctions on Russian oil (crude +5%) with India reportedly phasing out Russian crude — RIL/OMCs sold; Infosys ₹1,800 buyback without promoter participation (+5%); FDI-in-PSU-banks 20%→49% last-hour spike; Emirates NBD–RBL Bank stake deal; Nikkei's first close above 50,000; ~26 lakh traders exiting per media reports; ~35% USD-adjusted Indian underperformance vs S&P (rupee 82→88); Axis Bank Q2 miss (~-26% profit); GST collections +₹17,000 crore post-cut (Sept data).
3. **Data quality:** High. ASR errors corrected silently per dictionary (gif/GIFT, "shot/shorter" conflations, name variants Pierre/Pias/Piers/PR Tundar/P.E.R./Kunder/Kumbhar/Sunder/Kundar). One speaker misstatement flagged for verification: 2020 negative crude quoted as "-$15" (actual WTI settle -$37.63, 20 Apr 2020). S&P 5,700→6,900 claimed as "~25%" — actually ~21%; flagged.
4. **Method observations worth the book:** futures-premium/basis tracking as a short-covering gauge (70→100→130 then 130→70 collapse, quantified as a −60 pt long-futures trap); VIX-rising-with-price as a short-squeeze tell; support mapping by option tenor (weekly 25,500 / monthly 25,200 / quarterly 24,500); "first test of a round number fails" rule demonstrated twice at 26,000; biased strangle for low-conviction views; rupee-appreciation↔FII-flow feedback loop; tenor-based margin (+5% beyond 9 months) for far-expiry planning; first-test-failure vs GST-news six-week price lag (buy the delay, not the headline).
5. **Leaks found (all noted in records):** recurring Bengaluru workshop promos + "contact our office/description" CTAs, Dubai residence hints, Chennai travel mention, Diwali/Muhurat framing, personal portfolio/position disclosures (Nifty BeES/Bank BeES, short Nifty 800 lower, Dec 24,000P/27,000C, US-market short), friend anecdotes (100 kg silver, MCX 8,000, 25,000 put), YouTube-channel-blocking remark, "sponsored by Delta.exchange" in every file, and ~10 distinct ASR name variants. All are excluded from content fields and isolated in `leaks`.

## Coverage note
Batch covers the full Oct 2025 window: the tariff-shock whipsaw week (Oct 13–17), the results-driven breakout week (Oct 17–23: TCS/Infosys/Axis/HDFC/ICICI/RIL + Muhurat), and the 26,000 denial + expiry week (Oct 23–28). Pre/post pairs are consistent; minor day-to-day repetition flagged via `dup_flag` on 2848 and 2866.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts (2836-2866) read in full and converted to exactly 25 schema-compliant JSON lines written in source order to book/analysis/batch_daily_081.jsonl; output report written to book/analysis/outputs/daily_081_report.md; scope not widened (no edits to other batches, metadata, or book files)."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_081.jsonl",
    "book/analysis/outputs/daily_081_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 jsonl write + json.loads validation loop",
      "result": "passed",
      "summary": "25 records written; all 25 lines parse as valid JSON; id sequence matches expected manifest order"
    }
  ],
  "validationOutput": [
    "written and validated: 25 records",
    "order correct: True",
    "schema fields present on every record: id, date, type, summary, levels, events, lessons, quote, dup_flag, leaks"
  ],
  "residualRisks": [
    "Speaker numeric claims needing web verification are flagged verify:true in records (e.g., -$15 crude quote is actually -$37.63; S&P 5,700->6,900 is ~21% not ~25%; Axis profit -26%; Tata Capital/LG subscription figures; 26 lakh trader exodus; Nikkei 50,000; FDI 20%->49%)",
    "Two ASR-garbled passages (2844 US selloff magnitude, 2853 GIFT gap) were summarized conservatively rather than quoted"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch analysis JSONL (25 records) and batch report; no other files touched",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch covers Oct 2025 breakout-and-denial window; leak strings isolated in `leaks` fields for the book's banned-terms QA; dup_flag set on 2848 and 2866 for compiler dedup."
}
```
