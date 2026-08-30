# Batch special_166 Report — 10 special episodes (Jul–Aug 2025)

## Digest
1. **10/10 transcripts analyzed** → 10 valid JSON lines written to `book/analysis/batch_special_166.jsonl` (35KB, all schema fields present).
2. **Content mix**: 3 strategy episodes (put ratio, zero-cost collar, cash-secured put), 4 regulation/Jane Street episodes, 2 GST/taxation episodes, 1 training-scams exposé, 1 India bear-case outlook.
3. **Verification queue**: 26 concrete event claims extracted (Jane Street ₹5,000cr order + 4 entities + 45,000cr options; Aug-27 tariff notification; US appeals-court tariff ruling; rupee >88; GDP 7.8%/CPI 1.5% mismatch; GST 2.0 slabs; Sep-2019 tax-cut 10% rally; FII 4-5 lakh crore outflows; 91% loss study; Bank Nifty 12→14 constituents).
4. **Strategy assets**: 3 complete strategy recipes with numbers (put ratio split strikes +2.73% on 2.22L margin; Dec-2026 zero-cost collar 25,000PE/28,000CE at 950/950; TCS 3,000PE cash-secured put at 27 with 11L debt-fund backing) — ready for Part IV worked examples.
5. **Anonymization**: 25+ leak strings logged (name variants ×10; heavy self-defense passages in 2802 flagged for exclusion — MCA/mentorship-fee/biography; political framing in 2796/2808 kept as policy facts with opinion passages excluded).

## Notes for compiler
- 2756/2748/2767 form a 3-part Jane Street arc → backbone for ch. 27 (regulator's dilemma) + ch. 7 (index concentration math).
- 2793+2796 = GST 2.0 pair → ch. 28 + ch. 20 (2019 shock-therapy parallel is the key narrative link).
- 2802's scam-typology + vetting checklist → ch. 26 core; exclude_passages list is extensive (self-defense content).
- 2808 supplies the Part VI 2025-era bear-case scaffolding (FD-catch-up math, tariff arithmetic).

## acceptance-report
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts (2740, 2748, 2756, 2767, 2780, 2788, 2793, 2796, 2802, 2808) read in full; exactly 10 schema-conformant JSON lines written to book/analysis/batch_special_166.jsonl; no scope beyond the assigned batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_166.jsonl",
    "book/analysis/outputs/special_166_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json validation loop over batch_special_166.jsonl",
      "result": "passed",
      "summary": "10/10 lines parse as JSON; required fields (type, summary, chapter_targets, leaks) present in all records"
    }
  ],
  "validationOutput": [
    "lines: 10 | ids: 2740,2748,2756,2767,2780,2788,2793,2796,2802,2808",
    "all valid JSON, schema fields present"
  ],
  "residualRisks": [
    "ASR-garbled influencer names in 2802 (e.g. 'Avadudh Sate', 'Abhishek Gair') need spelling verification before any named use; kept flagged in event_claims with verify:true",
    "A few numeric claims are speaker-only (FII 92% net-short share, export dependence 70%, Singapore GST threshold) and are marked verify:false pending Phase 3"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_special_166.jsonl (10 structured analysis records) and this report; no other files touched",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "2802 (Training SCAMS) is the most self-referential transcript in the batch; its exclude_passages list must be enforced in compilation. 2796/2808 contain party-political framing that was preserved only as market-policy facts per approved policy."
}
```
