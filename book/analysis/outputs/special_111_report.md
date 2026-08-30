# Batch special_111 Report — 10 transcripts analyzed

## Deliverable
- JSONL written: `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_111.jsonl` (10 records, schema-complete, validated)
- All 10 transcripts read in full from `book/corpus/` (0002, 0003, 0024, 0025, 0026, 0027, 0028, 0030, 0031, 0034)

## Digest (5 lines)
1. **10/10 transcripts analyzed**: 21 verifiable event claims (DHFL −60%, Yes Bank −30%, Indiabulls HF −25% in Sept-2018; India VIX 60.05 & upper-circuit +10% day in April-2020; FII 85% short at 12,000; Sun Pharma 100→1,100 2008–14; Bajaj Finance 2400→4900), 6 strategy/framework entries, 10 quality scores (avg 4.2).
2. **Chapter spread**: Part I (1,3), Part II (5,6), Part III (9,11,12), Part IV (13,14,18), Part V (21) — strongest contributions to ch-9 (buy-vs-sell primers 0003/0024/0025), ch-5 VIX (0027/0028/0030 form a complete VIX trilogy with worked math), ch-12 collateral (0026).
3. **Highlights**: cricket-analogy options primer (0024); the falling-VIX "right direction, still losing" proof with weekly/monthly/far-month put data (0028); strangle forced-roll margin mechanics (0030); news-quadrant + lead-indicator doctrine (0031); strike/expiry ladder diversification with honest position-level losses (0034).
4. **Anonymization**: 14 leak strings logged (name variants in 7 files; 0034 is leak-dense: broker name, son's company, workshop fees, back-office walkthrough — all mapped to exclude_passages; 0026 franchisee-business line flagged).
5. **Verification priorities**: Sept-2018 NBFC panic claims and April-2020 VIX/circuit claims are concrete and dated — high-priority for the bulk queue; SGX no-options claim (0025) is the most checkable unusual assertion.

## Notes
- ASR corrections applied per dictionary (Wix→VIX, Quattac→Kotak, shorter up→shot up, S bank→Yes Bank flagged for verification).
- 0002's "IL&FS India bull housing finance" normalized to Indiabulls Housing Finance with a verify flag (speaker conflation of IL&FS and Indiabulls).
- 0030 contains a mid-video assistant interruption artifact — recorded in exclude_passages.
- One record (0034) carries personal P&L figures, kept as illustrative content per approved policy, with identity linkage stripped.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; 10 schema-complete JSON records written to book/analysis/batch_special_111.jsonl; report written to book/analysis/outputs/special_111_report.md; no scope beyond the assigned batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_111.jsonl",
    "book/analysis/outputs/special_111_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.load validation of batch_special_111.jsonl",
      "result": "passed",
      "summary": "10 records parsed; all 15 required fields present in every record; 21 event_claims, 6 strategies"
    }
  ],
  "validationOutput": [
    "records: 10; ids: 0002,0003,0024,0025,0026,0027,0028,0030,0031,0034; missing fields: none"
  ],
  "residualRisks": [
    "Speaker conflated IL&FS and Indiabulls Housing Finance in 0002 - normalized with verify flag; compiler should keep the verify flag.",
    "0034 personal P&L figures retained as illustrative content per policy; identity strings stripped from content but present in leaks field for QA."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one batch JSONL (10 analysis records) and one batch report; no other files touched.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch special_111 of the Phase 2 resume run; JSONL order matches the assigned transcript order."
}
```