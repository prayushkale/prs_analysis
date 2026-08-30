# Batch weekly_095 Report — Dalal Street Week Ahead, 28 Oct 2018 → 2 Aug 2020

## Digest
1. **Counts**: 20/20 transcripts analyzed → 20 valid JSONL records written to `book/analysis/batch_weekly_095.jsonl` (77 event claims, 41 lessons, 20 quotes).
2. **Coverage**: The full arc from the Oct-2018 FII-selling correction (Nifty ~10,300s, ICICI Q2 miss) through the COVID crash, the -$37 WTI day, the Facebook–Jio deal, the ₹20-lakh-crore package, Bank Nifty's 22,000→17,000 collapse and 2,400-point rebound, the US payrolls shock (+2.5M vs −8M) with BLS correction, and the July-2020 breakout through the 200-DMA to a record 11,194 close.
3. **Most notable events captured**: WTI May-2020 contract settling at **−$37** (20-Apr-2020); **Facebook ~₹45,000cr investment in Jio** (Reliance +10%); **US May payrolls +2,509K vs −8,000K expected** (5-Jun-2020) plus the BLS misclassification correction; **Apple overtaking Saudi Aramco** (31-Jul-2020); **Aditya Puri's ~₹850cr HDFC Bank share sale** (−100 rupees ≈ −1,000 Bank Nifty points); **NSE option-price glitch** (4-Jun-2020); Nov-2018 five-state-election → Balakot FII cycle (told 3×).
4. **Data quality**: High — these are human-edited docx transcripts with clean grammar; numbers dense and mostly self-consistent. ASR garbles corrected per dictionary (Quattac→Kotak, Wix→VIX, Lull Street→Dalal Street, "closed above 7000"→10,000). Two uncertain figures flagged in claims (IIP −55%, SGX "12700" typo interpreted, Gilead date).
5. **Leaks noted**: greeting name variants ("P. R. Sundar", "PR Sunder", "P R Sunder"), channel outros, Twitter/blog references, BSE/elearnmarkets webinar promos with registration links, workshop promos (350 people/9 batches), one personal luxury purchase (₹2-lakh smart board), one location hint (Chennai rain/monsoon-shadow remark in 0118), one personal loss admission (0083 NSE glitch). All logged in `leaks` fields; none carried into summaries/lessons/quotes.

## Pattern notes for the compiler
- Weekly format is a stable 5-block skeleton: last-week recap vs prediction → OI map (max put/max call strikes) → macro/data calendar → corporate results list → next-week range with disclaimer.
- Recurring doctrine seeded here (later repeated across dailies): FII-turnaround→+1,000pt rule; lead-vs-lag indicators; efficient-market/known-news discounting; PCR oversold/overbought bands; VIX-falling-in-a-fall = limited downside; old resistance becomes support; OI-shift direction as trend tell.
- 0005 (Oct 2018) is the earliest artifact in the batch: contains the "previous correction low = invalidation" rule and ADR read-through method.
- dup_flags: 0083/0123 share the election→Balakot narrative; 0083/0085 share the June-2020 payrolls shock (but 0085 adds the BLS correction — both kept).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 transcripts read in full; 20 JSONL records (batch_weekly_095.jsonl) match the required schema exactly (id/date/type/summary/levels/events/lessons/quote/dup_flag/leaks), in order, validated by json.loads; report written to the authoritative output path."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_095.jsonl",
    "book/analysis/outputs/weekly_095_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c \"json.loads each line of batch_weekly_095.jsonl; assert 20 records and exact id order\"",
      "result": "passed",
      "summary": "VALID: 20 records, ordered; 77 events, 41 lessons"
    }
  ],
  "validationOutput": [
    "20/20 transcripts read (corpus/0005..0128)",
    "20/20 JSONL lines parse; ids in manifest order",
    "77 event claims captured for the verification queue; 15 leak strings logged"
  ],
  "residualRisks": [
    "Two figures uncertain and flagged in claims: May-2020 IIP '-55%' (speaker's number; official figure likely differs), and 'SGX shot up to 12700' in 0069 (likely ASR/typo).",
    "Historical claims (election→Balakot dates, Apple/Aramco, WTI -$37) stated as the speaker asserted; web verification is a later phase."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one 20-line JSONL analysis batch (26.6KB) and one markdown batch report; no existing files modified.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "This batch completes weekly_095 of the Phase-2 resume wave. Speaker misstatement noted for verification: he says June-2020 IIP fell 55% — actual published figure was lower; treat as his claim. The 0096 'closed above 7000' is an ASR error for 10,000 (context-verified)."
}
```
