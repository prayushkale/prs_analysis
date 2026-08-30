# Batch daily_011 Analysis Report

## Digest
1. **Count:** 25/25 transcripts analyzed (ids 0580–0610, 16–17 Sep → 4 Oct 2021; daily pre/post series). Output: `book/analysis/batch_daily_011.jsonl` (25 valid JSONL lines, schema-checked).
2. **Most notable events:** Telecom relief package + bad bank (NARCL, ₹30,600 cr guarantee) breakout; Bank Nifty ATH crossing Feb high (~37,700); Evergrande default scare → HK 52-week low, share suspension (4 Oct); Sept-2021 FOMC "if the economy is good" taper language; India VIX +25% in 3 sessions crossing 17; US 10-yr yield >1.5%; Dow ±500–970 intraday days; quadruple witching volatility; self-reported ~₹10.1 crore half-year F&O P&L (unaudited, self-claimed).
3. **Recurring content:** FII-selling-heavyweights vs DII-buying-PSUs imbalance; sector rotation (IT→real estate→autos); sell-the-news (HDFC 2x advance tax); gambler's fallacy; VIX regimes (<15 bull / >30 danger); "market is God" option-selling philosophy.
4. **Data quality:** Good; systematic ASR errors applied (taxbeddy→TaxBuddy, 5pisar→5paisa, Quattac→Kotak, Wix→VIX, "15,600"→17,600). One suspect date: **0603** (titled 29-Sep but content matches 4-Oct Evergrande suspension; flagged in JSONL). One garbled figure: 0607 US CPI "3.5%" likely 5.3% (flagged).
5. **Leaks logged:** all 25 carry verbatim leak entries — name variants (P. R. Sundar/Sunder), sponsors (TaxBuddy, 5paisa, Delta Exchange absent here), workshop/fan-meet promos (0592, 0606, 0608), family account (0608 "my son's company"), broker name "Manson consultancy", Tamil-language identity (0608), self-named "PR Sundar indicator".

## Validation
- JSONL parse check passed: 25 lines, all required schema keys present, 25 unique ids matching the batch manifest.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts (0580,0581,0582,0583,0586,0587,0588,0590,0591,0592,0593,0594,0595,0596,0599,0600,0601,0602,0603,0604,0605,0606,0607,0608,0610) read in full; one schema-compliant JSON line each written to book/analysis/batch_daily_011.jsonl; no scope widened beyond the batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_011.jsonl",
    "book/analysis/outputs/daily_011_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c \"json.loads each line of batch_daily_011.jsonl; assert required keys\"",
      "result": "passed",
      "summary": "25/25 lines parse; all required schema fields present; 25 unique ids match batch assignment"
    }
  ],
  "validationOutput": [
    "valid JSONL lines: 25 | unique ids: 25"
  ],
  "residualRisks": [
    "id 0603 title date (29-Sep-2021) conflicts with content (Evergrande suspension = 4-Oct-2021); flagged in JSONL for Phase 3 verification",
    "0607 US CPI figure garbled in source ('3.5%'); flagged with likely value 5.3%",
    "0592 in-person-workshop promo and 0608 self-referential P&L passages retained only inside leak/exclude notes for later scrubbing"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured per-transcript analysis JSONL (25 entries) for daily batch 011 plus this report; no other files touched.",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Speaker self-references and sponsor names appear ONLY in leak fields, never in summaries/lessons/quotes; 'PR Sundar indicator' anecdote genericized in quote text."
}
```
