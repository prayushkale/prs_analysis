# Batch special_126 Report — Regulation/Scams/Investing Specials (Feb–Mar 2021)

## Digest (5 lines)
1. **10/10 transcripts analyzed** (0264, 0271, 0278, 0282, 0283, 0284, 0285, 0287, 0288, 0291) — one JSON line each written to `book/analysis/batch_special_126.jsonl`; all records schema-valid.
2. **Primary chapter targets:** 26 (retail scams: 0264, 0271, 0278), 27 (regulation: 0285 peak margin), 30 (bonds/gold: 0282, 0283, 0284, 0287), 3/1 (mind: 0288, 0291), 11 (IV: 0288, 0291), 17 (hedging: 0288).
3. **Standout content:** five-method broker-fraud anatomy; TN stamp-duty overcollection scandal; opposite-account P&L fraud + trainer-vetting heuristics; peak-margin → structurally-higher-VIX causal chain; bond price/yield mechanics with live Bharat Bond numbers; gold's three-input Indian price function; IV-crush explainer.
4. **Verification queue:** 20 concrete claims flagged (Tamil Nadu stamp duty ₹50→₹600/cr + court stay; Bharat Bond 2030 @₹1,108 vs 2031 @~₹995; BofA $3,000 gold call vs <$1,700 actual; Budget 2021 gold duty 12.5%→10%; 2013 taper Nifty −20% 6,200→5,100; 2003-07 Sensex 3,000→21,000; Sun Pharma 100→1,100 2008-14; peak-margin ~15% vs 5% global; SBI lot 3,000; CDSL ₹5 pledge fee).
5. **Scrub list for writers:** own workshop price/capital gating, Google-form sub-broker pitch, Jaguar/Vahan story, family accounts, Shimla trip, ₹85L donation self-reference, 2 friend-anecdote framings; name variants "P. R. Sunder/PR Sunder/Sundar".

## Notes for compiler
- 0285 contains a complete **strategy card** (weekly far-OTM short puts under elevated IV) with numbers — feed Part IV.
- 0271's integrated-margin double-blocking math (₹1.5 crore on 100 lots) is a ready-made worked example for ch 12.
- 0283+0284 form a coherent macro mini-course (rates→bonds→equities→taper) — sequence them in ch 30 with 0282 as the primer.
- 0287's "gold = international × USDINR × duty" decomposition is the cleanest gold chapter scaffold found so far.
- 0288/0291 supply Part I maxims: "process over product", "certainty in an uncertain market", conviction-at-tops observation.
- One unverifiable claim (regulator told an MTM poster to stop) kept with verify:false — present as his account or drop.
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts read in full; 10 schema-valid JSON records written to book/analysis/batch_special_126.jsonl; 5-line digest report at book/analysis/outputs/special_126_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_126.jsonl",
    "book/analysis/outputs/special_126_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 (json.dumps write of 10 records)",
      "result": "passed",
      "summary": "10 valid JSONL records written, one per transcript in order"
    }
  ],
  "validationOutput": [
    "10 records; ids 0264,0271,0278,0282,0283,0284,0285,0287,0288,0291; 20 event_claims; 3 strategy cards; leaks and exclude_passages populated"
  ],
  "residualRisks": [
    "One claim (regulator advising MTM poster to stop) is unverifiable - flagged verify:false for compiler discretion",
    "Two event_claims marked verify:false are directional (RBI policy frequency, Zerodha scale) and may be dropped"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_special_126.jsonl (10 analysis records) and special_126_report.md digest",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Anonymization handled at analysis level: identity strings isolated in leaks[], self-promo passages listed in exclude_passages[] for the writer agents"
}
```
