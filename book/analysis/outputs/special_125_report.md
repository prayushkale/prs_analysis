# Batch special_125 Report — 10 transcripts analyzed (ids 0229–0257, Jan–Feb 2021)

## Output
- Structured analysis: `book/analysis/batch_special_125.jsonl` — 10 records, all valid JSON, all 15 required keys present.

## Digest
1. **Coverage**: 10/10 transcripts read in full and converted to one JSON record each: 0229 (crude oil history), 0230 (Q&A), 0237 (budget outlook), 0239 (India-China border), 0240 (Mission Options E10), 0243 (GameStop), 0244 (budget strategies), 0246 (budget live trading), 0250 (GameStop-in-India), 0257 (Bharat Bond/HNI pledging).
2. **Strategy content**: 7 complete strategy recipes captured (put/call back spreads, put/call ratio spreads, butterfly conversion, live budget-day ratio structure, collateral-first capital structure) with legs, breakevens, max P/L and margins as stated.
3. **Verification queue**: 29 concrete event claims flagged (crude $10→$150, fracking self-sufficiency, GameStop 15x/+130%, Melvin -$5B, VIX +63%, budget-day historical ≤2% rule, 400-point max gap across 7 crises, GST record ₹1.2L crore, Sikkim clash timing, Reliance +40%, haircuts, Jet Airways 120% margin, Gitanjali cascade…).
4. **Anonymization**: leaks logged per record — name variants (P R Sunder/Pia Sundar), business email, Twitter/blog handles, Iron Collar course, advisory/mentorship pricing, Zerodha, family/son references, Tamil-identity and political asides; political jokes and promo passages listed under exclude_passages per policy.
5. **Chapter mapping**: primarily feeds ch 7 (microstructure), 9/11 (options/IV), 14/16 (spreads/butterflies), 19/20 (event playbook/budget), 21 (black swans), 22 (chronicle 2021), 26/27 (scams/regulation), 28 (taxation), 29/30 (investing/real assets), 12 (margins/collateral); 8 enhancement candidates noted (payoff decomposition, squeeze mechanics, budget move tables, haircut tables).

## Notable extraction quality
- 0244 and 0246 are the richest strategy sources in this range: full back-spread/ratio-spread doctrine with numbers, plus a live trade log with 81% PoP math.
- 0239 is a textbook "price moves before headlines" case study (Sikkim clash) — high chronicle value.
- 0250 gives the definitive India-vs-US shorting framework (SLB friction, circuits, dynamic margins, MWPL bans).
- ASR corrections applied per dictionary (e.g., "GIF nifty"→GIFT/SGX by era, "Sabi"→SEBI, "Wix"→VIX, "Kotech"→Kotak, "Xerodha"→Zerodha, "Janet Allen"→Janet Yellen noted in leaks).
- Claims flagged `verify:false` as rhetorical/illustrative (SBI option-chain numbers in E10; Apple results date uncertainty).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; batch_special_125.jsonl written with 10 valid JSON records (schema-validated: 15 required keys each); report written to the mandated output path special_125_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_125.jsonl",
    "book/analysis/outputs/special_125_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads validation loop over batch_special_125.jsonl",
      "result": "passed",
      "summary": "10 records parsed, all required keys present"
    }
  ],
  "validationOutput": [
    "valid JSONL: 10 records"
  ],
  "residualRisks": [
    "Illustrative option-chain numbers (0240) and one earnings-date claim (0239) flagged verify:false - excluded from verification queue by design",
    "ASR-garbled proper nouns (e.g., 'Janet Allen', 'Susslan') corrected with best-guess mappings noted in leaks for QA cross-check"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added 10-record structured analysis JSONL and per-batch report for special_125 (transcript ids 0229-0257)",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch contains the Jan-2021 budget strategy block (0244/0246) - high-value source for chapters 14/16/19; political asides in 0239/0243/0246 listed under exclude_passages per approved policy."
}
```
