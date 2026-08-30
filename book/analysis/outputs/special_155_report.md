# Batch special_155 Report — 10 special-episode transcripts (ids 1820–1887, Aug–Sep 2023)

## Digest (5 lines)
- 10/10 transcripts analyzed; 10 valid JSON lines written to `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_155.jsonl` (21.5KB, no fences, one object per line).
- Strongest content: 1824 (real-estate yield math + fraud typology → ch 30/26), 1877 (hedging cost-benefit + margin-resizing insight → ch 17), 1887 (AIF Cat-III 2x-leverage + tax-asymmetry case → ch 27/28), 1842 (election surprise rule for LEAPS → ch 19/20), 1830/1854 (bearish combo + double-ratio executions → ch 13–16).
- Verification queue: 22 event claims flagged (PFC/REC multi-baggers, DDT→investor-level tax change, 2004 −30% / 2009 +20% circuit day, Evergrande filing + HK bear market, SpaceX crypto write-down, Burry 13F, MLD terms, AIF rules, F&O 400× cash volume).
- Exclusions: **1866 excluded entirely** (pure political speculation, no market lesson — per approved policy). SEBI-ban self-references found in 1830/1877 and a Mauritius hedge-fund plan in 1887 logged as exclude_passages; team-member names (Srikant, Sharath, Abhishek, son Ashwin) captured in leak log.
- Data quality: 1820–1854, 1877, 1887 = 4/5 (numbers-dense, concrete); 1829, 1881 = 3/5; 1866 = 2/5 (excluded).

## Notes
- 1830 confirms the SEBI trading-ban period (started May 2023) — all 2023+ "trades" are paper trades; writers must label them as illustrative.
- 1887 contains a complete, high-value Part VII/VIII case study (why India lacks hedge funds) with three structural reasons and a COVID long-short example.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts (1820-1887) read in full; exactly one JSON line per transcript written to book/analysis/batch_special_155.jsonl following the mandated schema; anonymization rules applied (real name never in output fields, leaks logged); political video 1866 excluded per policy; digest returned."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_155.jsonl",
    "book/analysis/outputs/special_155_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read 10 corpus transcript files (1820, 1824, 1829, 1830, 1842, 1854, 1866, 1877, 1881, 1887)",
      "result": "passed",
      "summary": "All 10 transcripts read in full"
    },
    {
      "command": "write book/analysis/batch_special_155.jsonl",
      "result": "passed",
      "summary": "10 JSONL records, 21.5KB"
    },
    {
      "command": "python3 -c json-per-line validation of batch_special_155.jsonl",
      "result": "not-run",
      "summary": "per-child sandbox has no execution tool; JSON hand-validated line by line"
    }
  ],
  "validationOutput": [
    "10/10 lines present, one JSON object per line, schema fields populated (id, date, type, title_clean, summary, chapter_targets, themes, lessons, strategies, event_claims, quotes, enhance, exclude_passages, leaks, quality)"
  ],
  "residualRisks": [
    "Speaker-asserted numbers (PFC/REC returns, 2004/2009 election moves, AIF rule details) flagged verify:true and await Phase-3 web verification",
    "1866 political video excluded entirely; if any election-mechanics context is wanted in ch 20 it must come from other transcripts"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch analysis JSONL for special_155 (10 records) and this report",
  "reviewFindings": ["no blockers"],
  "manualNotes": "ASR corrections applied throughout (global queues->cues, FIAs->FIIs, GIF Nifty->GIFT Nifty, Sabi->SEBI). 1830/1877 contain SEBI-ban period confirmation: all speaker trades after May 2023 are paper trades - book must label them illustrative."
}
```
