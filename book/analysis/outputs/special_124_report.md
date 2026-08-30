# Batch special_124 Report

## Digest (5 lines)
- 10/10 transcripts analyzed and written to `book/analysis/batch_special_124.jsonl` (ids 0208–0228, Dec 2020–Jan 2021: US Georgia Senate event risk, Mission Options E07–E09, Sun TV stock study, market-cycle parables, gold framework, Nifty 50K thesis).
- Extraction highlights: 32 transferable lessons, 29 verifiable event claims (Georgia runoff Jan-5-2021, 2003–07 EPS×PE bull decomposition, gold duty history 1%→10%→12.5%, gold spikes $1,910/$2,070, Nifty lot size 75, Andhra Valley/Tata Power flat-decade pattern), 4 strategy entries (long call/put worked examples, covered-call method, ITM/ATM/OTM selection framework).
- Identity-risk finding: **0216 (₹7.5 crore P&L showcase) is the batch's exclusion candidate** — family member names, company name, client IDs, brokers, Singapore hedge-fund licensing; salvageable only for the 25%-vs-42% corporate-vs-personal tax point and the self-competition message. Flagged in exclude_passages/leaks.
- ASR corrections applied silently: "Zeebu/Zebu"→Zerodha, "NSC"→NSE, "obstra.definh.com"→opstra.definedge.com, "NPS"→NPA (0217 context), "bunny/penny market"→sideways market, "Tapper Tendrum"→Taper Tantrum, "Raja Sabha"→Rajya Sabha, Maran/Karunanidhi name garbles.
- Quality: five 5s, four 4s, one 2 (0216). Chapter coverage skew: 9 (calls/puts), 29 (investing), 3 (mind), 30 (gold), 19/20 (events).

## Notes for compiler
- 0216's corporate-vs-personal tax claim needs verification before use in ch. 28.
- 0210 is political-name-dense (Maran family, DMK) — content is company-factual but per approved policy keep it minimal/neutral in ch. 29.
- 0213/0217 personal biographies (teacher past, Singapore years, father's anecdote) → genericize per voice guide.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts (0208, 0209, 0210, 0213, 0215, 0216, 0217, 0219, 0223, 0228) read in full and emitted as one schema-compliant JSON line each, in order, to book/analysis/batch_special_124.jsonl; anonymization rules applied (identities recorded in leaks only); ASR corrections applied; 5-line digest returned."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_124.jsonl",
    "book/analysis/outputs/special_124_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json-validation of batch_special_124.jsonl",
      "result": "passed",
      "summary": "10/10 lines parse as JSON; ids in order; all required keys present; 32 lessons, 29 event claims, 4 strategies."
    }
  ],
  "validationOutput": [
    "records: 10; ids: 0208,0209,0210,0213,0215,0216,0217,0219,0223,0228; all have required keys: True"
  ],
  "residualRisks": [
    "0216 contains heavy identity content; compiler must honor its exclude_passages list.",
    "0210 political-family content requires neutral trimming per book policy.",
    "Two broker names in 0216 ('YRV Securities', 'JP Capital') are uncertain ASR readings; flagged but unconfirmed."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch analysis JSONL (10 records) and batch report for special_124.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "0216 recommended for near-total exclusion (self-referential P&L showcase); its only book-worthy elements are the corporate-vs-personal tax comparison (needs verification) and the 'compete with yourself' quote."
}
```
