# Batch special_146 Report (10 transcripts, ids 1276–1322, Sep–Oct 2022)

## Output
- JSONL written to `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_146.jsonl` — 10 lines, one per transcript, validated JSON.

## Digest
1. **Coverage**: 10/10 transcripts analyzed — 4 short clips (1276, 1279, 1282, 1285), 6 full episodes (1283, 1294, 1305, 1316, 1318, 1322).
2. **Chapter spread**: ch12 margins/collateral (1276, 1279), ch29–30 investing & real estate (1282, 1283, 1285), ch28 taxation (1294 — the HNI Dubai/FPI tax-avoidance explainer), ch31 crypto (1305 BTC financed combo + prior ETH straddle update), ch26 scams (1316 fund-manager cost illusion, 1318 opposite-account P&L scam), ch23/02 outlook (1322 Nifty-35k debunk with Fed-regime logic).
3. **Most valuable finds**: 1316's full cost-stack math (10L capital consumed annually by brokerage/STT/slippage) and 1318's opposite-account scam mechanics are flagship Part-26 material; 1322 is a standout "techno-fundamentalist" essay; 1294 documents both HNI tax routes in rare detail.
4. **Verification queue**: ~18 concrete event claims flagged (Nifty 15,200 June-2022 low, 2008/2020 recovery magnitudes, REC 1:3 bonus, US 7.22% mortgages Oct-2022, golden-visa/LRS/FPI rules, BoA $3,000 gold call, crypto inflows from Ukraine/Russia/Pakistan).
5. **Leaks noted**: name variants (1283, 1294, 1305, 1318, 1322); 1294 is leak-dense (Singapore base, OCI, Dubai trips, office solicitation); 1305 sponsor/CTA heavy; 1322 Chennai apartment + conference promos; 1318 Mercedes joke + "MTM trend started by me". All logged per-record in `leaks`/`exclude_passages`.

## Data quality
- These docx-era transcripts are clean (punctuated, no heavy ASR garble). Known corrections applied: NSC→NSE (1276), name variants normalized in lessons/quotes.
- One factual swap flagged for the correction log: 1285 cites 2 lakh as principal exemption and 1.5 lakh as interest (actual: 80C principal 1.5L, 24(b) interest 2L).

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "batch_special_146.jsonl written with exactly 10 valid JSON lines (one per assigned transcript, in order), following the mandated schema including chapter_targets, strategies, event_claims, leaks and exclude_passages"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_146.jsonl",
    "book/analysis/outputs/special_146_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads per line of batch_special_146.jsonl",
      "result": "passed",
      "summary": "10/10 lines parse as valid JSON"
    }
  ],
  "validationOutput": [
    "10 records; ids 1276,1279,1282,1283,1285,1294,1305,1316,1318,1322; 18 verify-flagged event claims; 3 strategies captured; leak lists populated for 5 records"
  ],
  "residualRisks": [
    "speaker's numeric claims (recovery percentages, cost figures) taken as stated; verification deferred to Phase 3 event queue",
    "1285 tax-concession figures appear swapped vs statute; flagged in enhance notes"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch analysis JSONL (10 records) and batch report for special_146",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Docx-era transcripts in this range are notably clean; 1276/1279/1282/1285 are one-to-three-paragraph clips with quality rated 2."
}
```
