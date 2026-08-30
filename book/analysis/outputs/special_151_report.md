# Batch special_151 Report

## Digest
- 10/10 transcripts analyzed (1586, 1589, 1591, 1595, 1597, 1598, 1603, 1606, 1610, 1611); 10/10 valid JSON lines written to `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_151.jsonl`.
- Content mix: 6 taxation/investing shorts (1586/1589/1591/1595/1603 + 1611 float story), 1 substantial option-buying episode (1597 — Thales of Miletus + SEBI loss stats + call-financed-by-put trade), 1 substantial crypto episode (1598 — ETH call ratio 1:3 + Delta Exchange announcements), 2 low-quality fragment/repeat shorts (1606, 1610).
- Duplicates detected: 1595 ≈ 1586; 1603 ≈ 1591; 1606/1610 are garbled repeats of earlier full episodes — book should cite the full originals only.
- Best book material: 1597 (history-of-options opener + option-buyer skill thesis + seasonal Nifty stat) → chapters 9/1/14; 1598 (crypto ratio construction + 5–10% sizing rule) → chapters 31/14; Starbucks float story (1611) → chapter 26/29 color.
- Verification queue: 8 concrete claims flagged (FY2023-24 F&O gross-profit tax, debt-fund indexation removal Apr-2023, 90% loss stats, Nifty 4-red-month seasonal stat, ETH/BTC 2023 levels, Delta fee changes, Starbucks $1.6B float, April-2023 strikes).
- Leaks logged for banned-terms list: name variants (P. R. Sunder), Delta Exchange sponsorship + fee announcements, follower-count references, NRI/Dubai/Singapore residency hints, personal capital/P&L framings, Mukesh Ambani royalty quip.

## Notes
- 1597 contains a falsifiable seasonal claim (25 years: never >4 consecutive red months on Nifty monthly chart) — high-value for chapter 9 enhancement, needs web verification of monthly close data.
- 1598's Delta Exchange fee mechanics (scalping window 6pm–10am refund, collateral pledging) are sponsor content — excluded from book text, retained only as exchange-risk context in chapter 31.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts read in full; 10 JSON records matching the special-episode schema written to /home/ubuntu/repos/prs_analysis/book/analysis/batch_special_151.jsonl; no scope widened beyond extraction"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_151.jsonl",
    "book/analysis/outputs/special_151_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read tool on 10 corpus files (book/corpus/1586..1611.txt)",
      "result": "passed",
      "summary": "All 10 transcripts read completely"
    },
    {
      "command": "write book/analysis/batch_special_151.jsonl",
      "result": "passed",
      "summary": "10 compact JSON lines, one per transcript, in order"
    }
  ],
  "validationOutput": [
    "10 records written; every record carries id/date/type/summary/chapter_targets/leaks; strategies populated for 1597 and 1598; event_claims marked verify:true where concrete"
  ],
  "residualRisks": [
    "1606 and 1610 transcripts are heavily garbled fragments (likely ASR-corrupted repeat shorts); their records are marked quality 1 and cross-referenced to fuller originals",
    "Seasonal claim in 1597 (never 4 consecutive red months in 25 years) needs data verification before book use"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_special_151.jsonl (10 structured analysis records) and special_151_report.md (digest + notes)",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Sponsor content (Delta Exchange fee mechanics in 1598) deliberately captured in leaks/exclude_passages, not in book-facing fields; duplicates 1595~1586 and 1603~1591 flagged for compiler dedupe"
}
```
