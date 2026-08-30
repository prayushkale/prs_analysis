# Batch weekly_096 Report — 20 transcripts analyzed

## Digest
- **Records written:** 20/20 → `/home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_096.jsonl` (27KB, valid JSONL, one record per transcript in order)
- **Coverage:** Weekly previews 0133–0196 (Aug 9 – Dec 13, 2020), incl. the two-part Sep 6 weekly (0151/0152)
- **Most notable events captured:** AGR Supreme Court saga & Vodafone Idea ₹25,000cr loss + F&O ban (Aug 2020); Reliance–Future Retail $3.38B deal (Aug 29); Apple –16% two-day unwind (~$300B, Sep 3–4); FTSE-rebalance Kotak/HDFC Bank selling (Sep 18); Trump COVID hospitalization (Oct 2); 1,150-point no-news October rally; BSNL/MTNL directive hitting telecoms (Oct 12); US election week playbook (Nov 1); RCEP signing (Nov 15); record November FII inflow >₹60,000cr; RBI's HDFC Bank digital bar (Dec 2); IIP turning positive; PSU-bank +7% index day
- **Data quality:** docx-era text is clean (proper punctuation); ASR garbles handled via dictionary (Lull Street, Quattac→Kotak, weeks→VIX, MSA→MSCI, Indescent→IndusInd, Bipro→Wipro, IAP/IIP, Jashpal Bhatti joke kept as cultural color); dates cross-check with content; levels consistently stated
- **Recurring structure confirmed for Part II/V writing:** fixed weekly skeleton (review → events → data → OI read → range forecast → disclaimer), FII/DII flow framing, max-OI consensus logic, event pre-pricing ("markets don't react twice")
- **Leaks logged:** name variants in every intro; YouTube/member/follower/office references (0142, 0157, 0177, 0178, 0187); social-media self-refs (0176, 0180); personal positions noted as content (not leaks)

## Flagged for verification (high value)
AGR hearing dates & verdict (Sept 1, 2020); Vodafone Idea Q1 loss figure; Future Retail deal $3.38B; Apple $2T & Sep 3–4 −16%; US unemployment 8.4%; FTSE Sep 2020 rebalance; Trump Walter Reed Oct 2; ₹2-crore interest-on-interest affidavit; May 18, 2009 ~20% circuit; BSNL/MTNL directive Oct 12; US Q3 GDP +30%+ (actual +33.1%); GST >₹1 lakh crore Oct; Biden 270 EVs Nov 7; MSCI Nov rebalancing ₹18–23K cr; RCEP 15 nations Nov 15; Japan Q3 +5%; record Nov FII ₹60K cr; RBI–HDFC Bank action Dec 2; November global rally stats (Italy +26% etc.); IIP positive Dec; PSU bank index +7% day.

## Residual risks
- 0157's "Amazon investing 20 billion dollars in Reliance retail" is likely a transcription/figure garble (Amazon's 2019 Future Coupons deal was ~$1B); flagged verify=true, needs source check before any book use.
- Option-premium figures (straddle ₹2,000/₹3,000, 20% S&P straddle) are plausibly garbled; marked verify=false (hard to source), unsuitable for print without corroboration.
- "Poland president infected / Pence aides positive" kept as context events; verify if used.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 assigned transcripts read in full; 20 valid JSON records written to book/analysis/batch_weekly_096.jsonl matching the required schema; findings report written to the authoritative output path"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_096.jsonl",
    "book/analysis/outputs/weekly_096_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads per line of batch_weekly_096.jsonl",
      "result": "passed",
      "summary": "20/20 lines parse as valid JSON; ids in order 0133-0196"
    }
  ],
  "validationOutput": [
    "20 records, one per transcript, in order; schema fields present (id/date/type/summary/levels/events/lessons/quote/dup_flag/leaks)",
    "1 continuation duplicate flagged (0152->0151); 6 high-value events flagged verify=true per transcript on average"
  ],
  "residualRisks": [
    "Amazon '20 billion dollars' figure in 0157 likely garbled - verify before print",
    "Option premium figures (0170, 0177) marked verify=false - not print-safe without corroboration"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch JSONL (20 records) and per-batch findings report; no code changes",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Weekly transcripts of 2020 are unusually rich in dated, verifiable events - excellent chronicle material for Part VI."
}
```
