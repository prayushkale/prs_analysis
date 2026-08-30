# special_136 Report — batch_special_136

10/10 transcripts analyzed (ids 0842–0864, Feb 2022 era). JSONL written to `book/analysis/batch_special_136.jsonl`.

## Digest
1. **Count**: 10 records, all valid JSON, in file order 0842→0864.
2. **Standout content**: 0844 (complete post-Budget-2022 crypto tax explainer: 30% flat / no set-off / 1% TDS / gifts) → chapters 28+31; 0845+0864 (Ukraine war pair: NATO/Crimea explainer + natural-gas-politics thesis, 2014-Crimea 3-4% precedent, crisis-every-2-years table) → chapters 21+19+25; 0863 (crypto options premium comparison BTC ~$6-7K vs BankNifty ~2,500 pts ATM; 24×7 gap-risk insight; portfolio margining launch) → chapter 31.
3. **Psychology/method mini-episodes**: 0848 (TA is part of the system, not the heart — horoscope analogy), 0854 (unlimited-risk dogma rebuttal), 0857 (greed asymmetry buyer vs seller), 0860 (arbitrageurs/speculators/hedgers) → chapters 3, 8, 9.
4. **Low-value**: 0842, 0851 (one-line charity/value episodes, quality 1 — mergeable as footnotes into chapter 3).
5. **Leaks flagged**: named associate (crypto-exchange CEO by name) in 0863 with heavy sponsor/T-shirt/family-trading content — excluded_passages captured; name variants "P. R. Sunder"/"Pia Sundar" in 0844/0845/0864; TaxBuddy promo in 0844; Tamil cultural markers in 0851; village-origin hint in 0864. 22 verification-flagged event claims (Nord Stream 2 $11B, Brent $26→$95, Crimea-2014 3-4% correction, 14,000 deaths since 2014, Feb-2022 troop buildup, crypto-tax effective dates).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts (0842-0864) read in full; 10 JSON records with required schema (id, date, type, title_clean, summary, chapter_targets, themes, lessons, strategies, event_claims, quotes, enhance, exclude_passages, leaks, quality) written in file order to book/analysis/batch_special_136.jsonl; identity strings confined to leaks/exclude_passages; ASR corrections applied."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_136.jsonl",
    "book/analysis/outputs/special_136_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read book/corpus/{0842,0844,0845,0848,0851,0854,0857,0860,0863,0864}.txt",
      "result": "passed",
      "summary": "10/10 transcripts read in full"
    }
  ],
  "validationOutput": [
    "10 JSON lines emitted, one per transcript, in order; schema fields present in all records"
  ],
  "residualRisks": [
    "0864's '200-DMA crossed around 10,800' figure looks ASR-garbled (expected ~16,000s for Feb 2022); claim recorded with verify flag",
    "0863 interview is sponsor-heavy; promo exclusion list may not be exhaustive for writing stage"
  ],
  "noStagedFiles": true,
  "diffSummary": "New batch analysis file with 10 records + authoritative report copy",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "0842/0851 are sub-100-word filler episodes (quality 1); compiler may footnote-merge them."
}
```
