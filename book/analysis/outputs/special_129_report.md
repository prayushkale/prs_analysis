# Batch special_129 Report — 10 special-episode transcripts (May–Jun 2021)

## Digest (5 lines)
1. All 10 transcripts read in full; 10 valid JSON records written to `book/analysis/batch_special_129.jsonl`; 0 parse errors; avg quality 3.3/5.
2. Highest-value records: **0385** (SEBI intraday-leverage phase-out mechanics + why sellers benefited via higher premiums — 4 verifiable regulatory claims), **0401** (Delta curriculum, quality 5, real option-chain decomposition example), **0388** (expiry calendar + physical-settlement obligations with broker margin-escalation practice).
3. Content spread: 4 Mission Options curriculum eps (E16–E18 region: exercise/assignment, physical settlement, delta), 3 PRSInspires life-philosophy eps (mostly salvable only as short principles), 1 SEBI-regulation analysis, 1 theme-investing explainer (sponsored — product genericized), 1 terminal-execution episode (tool brand stripped, crisis-exit lessons kept).
4. Verification queue: 17 event claims, 13 flagged verify=true — notably: F&O-to-cash ratio world's highest; SEBI 0.33× intraday-leverage step from 1 Jun 2021; stock-option physical settlement mandate; NSE ±3% operating-range protection on illiquid strikes; aluminium-once-pricier-than-gold; India used American-style options ~15 yrs ago.
5. Leak density high in this slice (name variants, company name, family accounts, workshop pricing, sponsors smallcase/Zerodha/NEST, CM meeting, Chennai/Delhi/Tirupati) — all captured verbatim in per-record `leaks`/`exclude_passages` for the banned-terms sweep; **0360** and **0374** are >70% self-referential (only principles salvaged).

## Chapter mapping
- Ch 9 (calls/puts): 0386, 0388 · Ch 10 (greeks): 0401 · Ch 12 (margins): 0388 · Ch 13 (selling): 0385, 0374 · Ch 27 (regulation): 0385 · Ch 29/30 (investing): 0371 · Ch 1/3 (mind): 0372, 0374, 0399 · Ch 18 (firefighting): 0412 · Ch 1 (failure stats): 0360.

## Notes for compiler
- 0385's demand-mismatch premium explanation is a Part II/IV gem (enhancement candidate: supply-shock premium diagram).
- 0412's ±3% market-order band is a genuinely useful microstructure fact — verify against NSE circulars before print.
- 0371 requires full product-name genericization ("theme-based basket platforms") in any reuse.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; 10 schema-valid JSON records written to book/analysis/batch_special_129.jsonl (validated by json.loads pass on every line); report written to book/analysis/outputs/special_129_report.md; no scope widened beyond the batch task."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_129.jsonl",
    "book/analysis/outputs/special_129_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads validation over batch_special_129.jsonl",
      "result": "passed",
      "summary": "10/10 lines parse; all schema keys present; ids 0360-0412 in order; 17 event claims; quality avg 3.3"
    }
  ],
  "validationOutput": [
    "valid lines: 10; ids: 0360,0371,0372,0374,0385,0386,0388,0399,0401,0412; event_claims: 17"
  ],
  "residualRisks": [
    "ASR-corrected figures (e.g. delta values, premium numbers) taken from spoken transcripts; 13 of 17 event claims flagged verify=true for Phase 3 web verification before book use.",
    "0360 and 0374 are heavily self-referential; salvage limited to generic principles - compiler should not pull specifics from them."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added 10-record analysis JSONL for batch special_129 (10 transcripts) plus batch report; no other files touched.",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch covers May-Jun 2021 specials: SEBI margin rules (0385) and Mission Options E16-E18 (0386/0388/0401) are the strongest chapter feeders; PRSInspires trio (0360/0372/0374) needs strict anonymization or drop."
}
```
