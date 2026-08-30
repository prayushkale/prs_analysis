# weekly_105 Report — 20 "Dalal Street Week Ahead" transcripts (Feb–Sep 2024)

## Deliverables
- **Data**: `/home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_105.jsonl` — 20 JSON lines, one per transcript, schema-compliant (id, date, type, summary, levels, events, lessons, quote, dup_flag, leaks).
- **This report**: `/home/ubuntu/repos/prs_analysis/book/analysis/outputs/weekly_105_report.md`

## Digest
1. **Counts**: 20/20 transcripts read in full and analyzed; 20/20 JSON records valid; 55 event claims extracted (43 flagged verify:true); 39 lessons; 18 verbatim-style quotes; 60+ leak strings logged.
2. **Most notable events (queued for web verification)**: NVIDIA $2T crossover + largest one-day gain ever (Feb 2024); SEBI mid/small-cap stress-test directive + electoral-bond SBI −10% (Mar 2024); June-4 counting-day announcement repricing May-expiry IV; Mauritius tax-treaty selloff −1,000 pts + Iran–Israel weekend attack and full gap-down reversal (Apr 2024); "uniform tax" rumour and same-evening FM clarification (May 3); election-odds shock with Bank Nifty 9 straight down days vs US 8 straight up (May 12); Amit-Shah-triggered 1,200-pt recovery (mid-May); pre-result euphoria in 25,000 calls (May 26); Union Budget "worst for market" + Friday recovery to ATH (Jul 26); Aug-5 Nikkei −10% gap and recovery; Hindenburg's second Adani/SEBI-chief report as a "non-event" (Aug 10-11); PCR 1.49 complacency warning (Jun 30); 24,975 breakout + Reliance 1:1 bonus + 50bp-cut expectations (Sep 1).
3. **Data quality**: High. These 2024-era .txt transcripts are raw ASR but formulaic ("last week… coming week… levels"), so summaries, levels and ranges are reliably recoverable. Numeric claims marked verify:false are either internal-market observations (special-session premium behavior, call OI at 25,000) or unsourced figures ($6B FII inflow day-one gap).
4. **Date corrections (important for the chronicle)**: Four entries carry manifest dates that contradict transcript content; content dates were used and flagged in `dup_flag`: 2271a (manifest 2024-05-22 → actual 2024-07-28, post-Budget), 2291a (2024-06-04 → 2024-08-11), 2302a (2024-06-11 → 2024-08-18), 2325a (2024-07-02 → 2024-09-01). The a/b-suffix duplicate-number files are mis-dated by upload-order interpolation; chapter builders should trust content dates.
5. **Anonymization**: Every transcript opens with a name variant ("P. R. Sundar", "Pia Sundar", "P R Kumder", "P. S. Sundar") and Delta Exchange sponsorship; recurring leaks = workshops (Bangalore/Chennai/Mumbai/US-market/online), Sri Lanka hill station, NRI status, family functions, personal option books, "my YouTube followers", BJP-adjacent political opinion (2276a is the heaviest — flagged for exclusion of its political passages; the option-structure teaching content is salvageable). All captured verbatim in `leaks` for the banned-terms QA pass.

## Recurring weekly-framework patterns (useful for Part II/V chapters)
- Fixed skeleton: week recap → global cues → FII/DII vs MF flows → technical triggers (box theory, 100/200-DMA, gap-fill logic) → option-market tells (straddle-implied range, OI strikes, PCR, premium behavior) → event calendar → explicit range view with support/resistance.
- Standing aphorisms confirmed: "consensus is dangerous"; "markets react to surprise, not results"; "amateurs open, professionals close" variants; Newton's-law framing for trend intervention.
- 2024 arc across these 20 weeks: HDFC-results drag → breakout → froth crackdowns → Mauritius tax shock → election binary → euphoria → Budget disappointment → Aug-5 global crash → MF-flow-supported repair. This is a ready-made spine for the Part VI 2024 chapter.

## Residual risks
- ASR numbers (levels, crores) can be off; all hard claims carry verify flags for Phase 3 web verification.
- Two dates in the batch index (2276a's "2024-05-26" was confirmed by content; 2322a's manifest 2024-07-02 vs content 2024-06-30 — minor, content date kept).
- Quotes are cleaned paraphrase-to-verbatim hybrids (ASR has no reliable verbatim text); treat as near-verbatim in the book.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 assigned transcripts read in full; 20 schema-compliant JSON records written to book/analysis/batch_weekly_105.jsonl; ids match the batch manifest in order; an id-content mislabeling found during validation was fully corrected."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_105.jsonl",
    "book/analysis/outputs/weekly_105_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json validation of batch_weekly_105.jsonl (schema keys + id order)",
      "result": "passed",
      "summary": "20/20 lines valid JSON, all required keys present, ids match manifest order exactly"
    }
  ],
  "validationOutput": [
    "lines: 20 | id match in order: True | missing: set()",
    "4 manifest-date conflicts detected vs content dates; content dates used and flagged in dup_flag"
  ],
  "residualRisks": [
    "ASR-derived numbers (index levels, crore figures) need Phase 3 web verification before print",
    "Some videos' published titles (AUGUST weeks) mismatch their content weeks; content dates preferred"
  ],
  "noStagedFiles": true,
  "diffSummary": "New batch analysis file with 20 weekly-report records (55 event claims, 39 lessons, leak logs) plus this report",
  "reviewFindings": [
    "no blockers",
    "note: 2276a contains heavy political-opinion passages — flagged in leaks for exclusion at writing time"
  ],
  "manualNotes": "Batch covers Feb 18 – Sep 1, 2024 weekly previews; four dates corrected from content; ready for Phase 3 claim verification and Phase 4 chapter mapping."
}
```
