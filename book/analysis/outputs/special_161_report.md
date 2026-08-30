# Batch special_161 Report — Regulation, Taxation & Outlook specials (10 transcripts, Jun–Sep 2024)

## Digest (5 lines)
1. All 10 transcripts read in full; 10 valid JSON records written to `book/analysis/batch_special_161.jsonl` (24.9KB), schema-complete with 41 verifiable event claims, 6 strategies, 22 transferable lessons.
2. Backbone of Part VII (Predators & Protectors): SEBI committee proposals analyzed (2321a, 2344a, 2365a), the FY24 loss study dissected (93%/6%/1%, ₹1.8L cr negative-sum, cost waterfall), Budget-2024 triple tax shock (2366b), GST-vs-income-tax argument (2332a).
3. Strong Part I / Part XXIX material: business-qualities framework for trading, media-narrative critique, market mood cycle (pessimism→euphoria), RSI>80 correction evidence (2354a).
4. **2349b (Reservation) flagged for FULL EXCLUSION** — pure political/social opinion with heavy identity disclosure (caste self-ID, named influencer friend, Singapore teacher past); zero market content.
5. 41 event claims queued for verification (election-day −9.3%, Fed 50bp Sep-2024, STT/CGT hikes, NSE collateral cut, ₹29-crore deepfake scam, VLS Finance/Suzlon ruin cases); one speaker claim flagged as likely inverted (STT futures/options hike percentages in 2366b).

## Highlights for the compiler
- **Best quotes**: "Somebody's loss is not somebody's gain — it is the loss minus one lakh crore" (2365a); "Any government agency will send you a notice — it will never call you on the phone" (2329b); "Don't catch the running bus" (2354a/2358a); "Whether you make a profit or a loss, you still pay the STT" (2366b).
- **Enhancement candidates**: business-vs-speculative income table; cost waterfall of ₹1.8 lakh crore; 20-year RSI>80 correction table; GST threshold country comparison; mood-cycle framework table.
- **Identity leaks logged**: name variants (P. R. Sundar/Pierre/Pia/P. A.), co-host names (Sharif/Sharat), son's company account, broker-friend ₹1/lot arrangement, workshop pricing (₹50,000+GST), workshop.prsundar.com, Singapore teacher/citizenship hints, Chennai/village references, caste self-identification — all captured in `leaks`/`exclude_passages` per record for the QA sweep.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts (2321a, 2324b, 2329b, 2332a, 2344a, 2349b, 2354a, 2358a, 2365a, 2366b) read in full; exactly one schema-compliant JSON line each written in order to book/analysis/batch_special_161.jsonl; report written to book/analysis/outputs/special_161_report.md; scope limited to the assigned batch (no other batches touched)."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_161.jsonl",
    "book/analysis/outputs/special_161_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c \"json.load each line of batch_special_161.jsonl\"",
      "result": "passed",
      "summary": "10/10 lines parse as valid JSON with required fields (id, summary, chapter_targets, lessons, event_claims, leaks, quality)"
    }
  ],
  "validationOutput": [
    "10 valid JSONL records; ids in expected order: 2321a, 2324b, 2329b, 2332a, 2344a, 2349b, 2354a, 2358a, 2365a, 2366b",
    "41 event claims flagged for verification; 2349b marked exclude_entirely (political/social content per editorial policy)"
  ],
  "residualRisks": [
    "Speaker's STT hike percentages in 2366b appear inverted vs official Budget-2024 figures — recorded with verify=true for correction in Phase 3",
    "Some anecdotes (dosa price, ₹500cr put loss, friend's ₹3L scam) are unverifiable and marked verify=false"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one new batch JSONL (10 structured analysis records) and one batch report; no existing files modified",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "2349b is fully excluded content per the approved editorial policy (exclude political/social opinion); retained as a schema-complete record with empty market fields so batch lineage stays complete."
}
```
