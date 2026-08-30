# Batch special_157 Report — 10 special episodes analyzed (Dec 2023 – Jan 2024)

## Files written
- **Primary output:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_157.jsonl` — 10 JSON lines, one per transcript, in order (1978, 1990, 1999, 2011, 2022, 2032, 2038, 2043, 2055, 2065). Each line: summary, chapter_targets, themes, lessons, strategies, event_claims (verify flags), quotes, enhance candidates, exclude_passages, leaks, quality.

## Digest
1. **1978 (Why Technical Analysts Lose)** — Capital context and position sizing dominate TA outcomes; treadmill + 9-lot-vs-2-lot paradox; never borrow to trade. Quality 4. → ch 1,2,3,29.
2. **1990 (Conference Call-Ratio Review)** — 15-month call ratio (16kCE long, 2×20kCE, 3×13kPE financing) → ~3,300 pts; >9-month margin rule; VIX-30 exit rule. Quality 4. → ch 14,12,18.
3. **1999 (TA Conversion Story)** — Hourly→daily parameter change made trend-following work; "different cars, same destination"; method diversification. Quality 4. → ch 1,2,3.
4. **2011 (Value vs Momentum)** — Best-in-batch: crisis calendar 2008–2022, contra picks (ITC/PFC/REC/BSE), dividend-yield floor, −10/−20/−30% ladder. Quality 5. → ch 29,30.
5. **2022 (Positive Black Swan)** — Taleb explained then flipped: 2009 +20% two-circuit day and 2019 tax-cut candle as upside tail risks; two-sided risk for traders. Quality 4. → ch 21,18,5.
6. **2032 (2023 Rewind)** — Bad-year→good-year rule; 2023 anatomy: March bottom ~16,800 → Dec blast ~+2,500 pts. Quality 4. → ch 24,19.
7. **2038 (Dubai Meet Promo)** — Pure announcement, zero market content; flagged ENTIRE transcript for exclusion. Quality 1.
8. **2043 (Right Time to Buy?)** — Asset-cycle tables (Chennai flat, Reliance, gold), valuation premium, rollover-cost math (~9%/yr), builder-fraud parable. Quality 4. → ch 29,30,24.
9. **2055 (Nifty 24K Logic)** — Four-anchor target derivation (VIX-implied move, FD risk premium, PPF spread, rollover hurdle); election-reaction table 2004–2019. Quality 4. → ch 24,20,5.
10. **2065 (Term-Structure Put Calendar)** — India VIX is 1-month so June election IV invisible; reversed deep-ITM put calendar, +25% ROI in 10 sessions, defined risk. Quality 5. → ch 11,15,5.

## Verification highlights (event_claims with verify=true)
Election-day reactions (2009 +20%, 2004 crash), 2019 corporate-tax cut, Dec-2023 +2,500-point series, >9-month SEBI margin surcharge, Nifty PE ~30–35 claim (likely overstated — flag), 2004 "−30%" claim (needs correction check), North Korea Jan-5-2024 shelling ("missiles" misnomer), Feb-2024 vote-on-account.

## Anonymization notes
Leaks logged for all 10 (name variants "PR Sunder"/"Pia Sundar"; workshop/conference promos; SEBI-ban and penalty self-references — 2038 excluded entirely, 2032/2055 partial exclusions; US-market-residency hints in 2065). Personal P&L genericized per policy.

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts read in full; 10-line JSONL written to book/analysis/batch_special_157.jsonl (25,012 bytes) matching the required schema; report written to book/analysis/outputs/special_157_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_157.jsonl",
    "book/analysis/outputs/special_157_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read tool on 10 corpus files (1978, 1990, 1999, 2011, 2022, 2032, 2038, 2043, 2055, 2065).txt",
      "result": "passed",
      "summary": "All 10 transcripts read completely"
    }
  ],
  "validationOutput": [
    "10/10 transcripts analyzed; JSONL lines follow the special-episode schema; ASR corrections applied (Sphan→Swan, Najib→Nassim Nicholas Taleb, NSC→NSE, ICSF→ICICI, India weeks→India VIX, struggles→strangles, Tapper→Taper)",
    "One transcript (2038) flagged for full exclusion as promo-only"
  ],
  "residualRisks": [
    "Speaker's numeric claims (Nifty PE 30-35, 2004 -30% crash, 2004 'India shining' framing) are flagged verify=true and may need correction at writing time",
    "2038 event_claims empty by design (promo content); compiler should skip it"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured analysis for 10 special-episode transcripts (batch_special_157) plus a batch report",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Strategy data in 1990 and 2065 is unusually rich (constructions with full numbers) - priority inputs for chapters 14 and 15. 2011 is the strongest source for the crisis-calendar and staggered-entry ladder (chapter 29)."
}
```