# Batch weekly_104 report — 20 Dalal Street Week Ahead transcripts (Sep 2023 – Feb 2024)

1. Records: 20/20 written to /home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_104.jsonl (ids 1878–2096, weekly gap ~11 days, all dated).
2. Most notable events: Sept-2023 FII selling 18-25k crore/month + record 82-88% FII short positioning; Oct-2023 Israel-Gaza outbreak (VIX >20, crude +5%); Dec-2023 state-election sweep + Fed pivot = +2,600 pts "green swan"; HDFC Bank -12% post-Q3 (Jan 2024) with LIC 9.99% stake clearance; Bank Nifty expiry moved to Wednesday; Jan-22 Saturday trading session.
3. Strongest recurring lessons: extreme short positioning precedes rallies; expectations delta drives results reactions (Infosys -7% profit → +8% stock); heavyweight weight-risk (RIL+HDFC ~25%) overrides global cues; never predict elections (2004 crash); illiquid options (Sensex) have jump-risk stops.
4. Data quality: docx-era transcripts are clean (punctuated, low ASR noise); levels/FII flows abundant and internally consistent; verifiable event claims averaged 3.6/transcript; 2 unverifiable self-claims flagged (920-straddle CAGR, Sensex-option anecdote).
5. Leaks logged per record (Delta.Exchange sponsorship in all 20; name variants incl. "Pia Sundar", "P. Asunder"; 2012 contains SEBI-ban end-date self-reference + personal capital disclosure ($1M/₹88.5cr) + son trading; 2023 contains "as a Tamilian" identity; 1991/2000/2012 workshop/mentorship/webinar promos).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "20/20 transcripts read in full; 20 valid JSON records (one per transcript, in order) written to book/analysis/batch_weekly_104.jsonl; 5-line digest written to book/analysis/outputs/weekly_104_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_104.jsonl",
    "book/analysis/outputs/weekly_104_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read tool on 20 corpus files (1878–2096)",
      "result": "passed",
      "summary": "all transcripts read in full"
    },
    {
      "command": "write batch_weekly_104.jsonl",
      "result": "passed",
      "summary": "20 JSONL records, 33KB"
    }
  ],
  "validationOutput": [
    "20 records = 20 transcripts; schema fields populated per record (summary/levels/events/lessons/quote/leaks); dates all present from metadata"
  ],
  "residualRisks": [
    "ASR garbles in a few ids (Quotac->Kotak, ICSA->ICICI) corrected per dictionary; two self-claimed stats (920-straddle CAGR, 80-lakh anecdote) marked verify:false"
  ],
  "noStagedFiles": true,
  "diffSummary": "new analysis output for batch weekly_104 covering Sep-2023 to Feb-2024 weekly previews",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Speaker identity strings appear in source text and are logged in leaks[] per record only, never in summaries/lessons/quotes."
}
```
