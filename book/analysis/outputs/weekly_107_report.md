# batch_weekly_107 — Findings Report

## Digest (5 lines)
1. 20/20 Dalal Street Week Ahead transcripts (Feb 10 – Jul 4, 2025) read in full; 20 valid JSONL records written to `book/analysis/batch_weekly_107.jsonl`; 57 verifiable event claims captured, 39 flagged verify=true, 18 opinion/estimate items flagged verify=false.
2. Most notable event arc of the batch: tariff-crash double bottom at 21,750 (Apr 7) → Pahalgam attack & 2% India dip (Apr 25–May 9) → ceasefire +1,000-pt day (May 12) → Moody's US downgrade (May 16) → three-week 24,500–25,200 coil → Israel-Iran war rounds (Jun 13, Jun 21 B-2 strike; crude +10%) → breakout June 26 (+3% week) → SEBI–Jane Street ruling (Jul 4).
3. Data quality: good; speaker's index levels/flows are internally consistent across weeks (23,869 swing high, 21,750 low, 24,920 post-ceasefire close, 56,000 Bank Nifty ceiling, 26,277 ATH all recur), making cross-verification straightforward. Premium quotes (22,500PE @10–20, 26,000CE >100, PCR 1.2) are his on-screen reads — flagged verify=false.
4. Identity/promo leaks logged in every record (name ASR variants Pia/Pierre/P.E.R./T.S. Bunder; Delta Exchange sponsor in all 20; leaks unique to this batch: ₹25L+GST HNI mentorship with 2-month Chennai residency (2687), Bangalore/Mumbai workshops (2605/2653), Singapore–Malaysia travel (2709), Mercedes S-Class purchase anecdote (2594)).
5. Lessons bank: 30+ transferable rules captured — shock-vs-news decay doctrine, S/R flip mapping, double-bottom put sales at support, VIX<15 regime filter, index-rejig mechanical flows, "chameleons" regime-switching, buy-dip vs sell-rally regime test, weekend telltales (crypto/Sunday markets), positioning-over-results on result days.

## Notable recurring threads for the compiler
- The 24,500–25,200 consolidation coil and its June 26 breakout is the clearest teaching sequence of H1-2025 (appears in 2699, 2709, 2715, 2724, 2735, 2749).
- Bank Nifty index-rule rebalancing (2709) cross-references special episode 2873 — merge into one book treatment.
- Jane Street arc begins here (2749) and continues in special episodes — chronicle-ready.
- Political-opinion passages (Trump tirades in 2637, "untrustworthy" remarks) kept out of lessons/quotes per policy; market facts preserved.

## Output files
- `book/analysis/batch_weekly_107.jsonl` — 20 records (authoritative structured output)
- `book/analysis/outputs/weekly_107_report.md` — this report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 listed transcripts read in full and exactly 20 schema-compliant JSON lines written to book/analysis/batch_weekly_107.jsonl; findings digest written to book/analysis/outputs/weekly_107_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_107.jsonl",
    "book/analysis/outputs/weekly_107_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 jsonl write + per-line json.loads validation loop",
      "result": "passed",
      "summary": "20/20 lines parse; each has id, type=weekly, list-typed events"
    }
  ],
  "validationOutput": [
    "wrote 20 records to /home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_107.jsonl",
    "all 20 transcripts read via read tool before extraction"
  ],
  "residualRisks": [
    "Some index levels/premiums are speaker's spoken figures (flagged verify=false where on-screen reads); Phase 3 verification should confirm 21,750 low, 23,869 swing high, 24,920 May-12 close, 56,000 Bank Nifty, 26,277 ATH, June 26 breakout close, and Moody's May 16 downgrade timing"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one batch analysis JSONL (20 weekly-report records, Feb-Jul 2025) and its findings report",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Result 2687 contains the densest leak in this batch (HNI mentorship pricing + Chennai/Dubai residency) - already flagged for Phase 6 scrub list; 2637/2675 contain political-opinion rants excluded from lessons and quotes per approved policy."
}
```
