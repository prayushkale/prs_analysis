# Batch special_158 Report — 10 special-episode transcripts (Feb–Mar 2024)

## Summary
All 10 transcripts read in full; 10 JSON records written to `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_158.jsonl` (one line per transcript, schema-compliant).

## Coverage
| id | date | topic | chapters | quality |
|---|---|---|---|---|
| 2095 | 2024-02-03 | Intraday strategy breakdown in high vol; stop-loss jumps; calendar inversion | 13,7,5,3 | 4 |
| 2117 | 2024-02-18 | Covered straddle on HDFC Bank/Bajaj Finance; averaging rules | 13,29,3 | 4 |
| 2128 | 2024-02-24 | Worst time to buy; election risk-reward; midcap froth | 29,20,1 | 4 |
| 2139 | 2024-03-02 | Election playbook 2004/2009/2014; vote-counting day rule; SEBI-AMFI froth | 19,20,29 | 5 |
| 2149 | 2024-03-08 | Reverse mortgage explainer | 30,29 | 3 |
| 2150 | 2024-03-09 | Mission Options 2 preview; long/short jargon | 9 | 2 |
| 2151 | 2024-03-09 | Long call: breakeven, NVIDIA example, EMH | 9,11,19,20 | 5 |
| 2163 | 2024-03-16 | Long put: insurance, black swan, momentum tips | 9,17,21 | 5 |
| 2164 | 2024-03-16 | Gold & real estate vs interest-rate channel | 30,29 | 4 |
| 2176 | 2024-03-23 | 2024 outlook: YTD catch-up thesis, 24,000 target, SIP froth | 24,20,29 | 4 |

## Key verification items (event_claims, verify=true)
- 2004 −30% / 2009 +20% (two upper circuits) / 2014 & 2019 +1-2% election reactions
- SEBI→AMFI mid/small-cap froth circular (28 Feb 2024); MF stress tests; SME manipulation probe
- YTD Mar-2024: Japan +22%, Vietnam +12.8%, US +10%, India +1%
- SIP flows ~₹41k cr small-cap / ~₹22k cr mid-cap, large-cap net outflow; midcap +67% vs EPS +66%
- DIIs bought ~₹14,000 cr HDFC Bank (Feb 2024); HDFC −4-5% post Jan-2024 results; Infosys lot 400
- Gold history: fixed until ~1971; 1980 4–5× spike; ₹850→₹4,000/gm 2008–13; US CPI 9% (2022)
- Bank Nifty ±1,000-point intraday moves Feb 2024; Meta +20%/Amazon +7-8% earnings reactions

## Anonymization notes
- Leaks catalogued per record: name variants (P. R. Sundar / Sunder / Pia), SEBI-ban disclosures (2139, 2176 — exclude), school-teacher career (2149, 2150), age ("I am 60", 2149), Dubai property/office (2095, 2164), 4kg gold purchase (2164), family (son trades 2117, wife 2164), workshop/mentorship promos (2117, 2151, 2176), "Mission Options" course branding (2150, 2151, 2163 — rename in book), Tamil proverb (2176).
- Personal trades genericized as illustrative (US NVIDIA call, 4kg gold) per policy.

## Data quality notes
- 2149/2150 are low-density for the book (3 and 2 quality): 2149 contributes only the reverse-mortgage explainer; 2150 is a series preview (analogy only).
- 2095 has garbled numeric passages (backtest ₹ figures "8-30,000", "80 percent written" = return) — numbers recorded as-stated with caveats.
- 2151 "NVIDIA $680→$760" conflates stock price with expectations; flagged for verification against actual NVDA Feb-2024 earnings move.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; 10 schema-compliant JSON records written to book/analysis/batch_special_158.jsonl; digest report written to book/analysis/outputs/special_158_report.md; no scope beyond the assigned batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_158.jsonl",
    "book/analysis/outputs/special_158_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read 10 transcript files via read tool (corpus/2095..2176)",
      "result": "passed",
      "summary": "All 10 files read completely, no read errors"
    }
  ],
  "validationOutput": [
    "10/10 transcripts covered; each JSON line has id/date/type/summary/chapter_targets/themes/lessons/strategies/event_claims/quotes/enhance/exclude_passages/leaks/quality",
    "39 event_claims captured (30 flagged verify=true); 6 strategies (1 full + framework entries); 21 leak strings catalogued for the banned-terms list"
  ],
  "residualRisks": [
    "2095 backtest figures garbled by transcription; recorded as-stated and flagged",
    "2151 NVIDIA price/volume conflation noted; needs verification against actual Feb-2024 NVDA data"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch JSONL (10 records, 23KB) and batch report for special_158",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch is part of Phase 2 wave (specials). 2139 and 2176 contain SEBI-ban self-references which are hard exclusions for the book; their market content (election playbook, outlook) remains usable after scrubbing."
}
```