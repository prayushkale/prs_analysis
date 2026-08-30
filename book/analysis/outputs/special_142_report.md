# Batch special_142 Report — ids 1176–1195 (10 special episodes, 15–23 Aug 2022)

## Deliverable
- **JSONL written:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_142.jsonl` — 10 records, one per transcript, in order, all valid JSON with the full required schema.
- Validation: 10/10 parse; required fields present in all; 8 event claims queued for verification; 1 full strategy recipe captured; no real-name leakage outside the `leaks` field.

## Batch digest
1. **1176 STT or Punishment** (tax) — STT born 2004 in lieu of LTCG; LTCG's return = double taxation. → ch 28/27.
2. **1178 Loans are not sin** (philosophy) — leverage as opportunity-cost tool; personal P&L genericized. → ch 3/29.
3. **1180 Birth of NSE** (trivia) — 1992 founded / 1993 licensed / 1994 operational. → ch 7 + glossary.
4. **1183 Quadruple witching** (terminology) — 4×/yr all four contract classes expire together. → ch 7/19.
5. **1185 Charity vs business** (parable) — never mix the two mental accounts. → ch 1/3.
6. **1186 SGB arbitrage** (★ flagship of this batch, quality 5) — SGB at ~10% discount + 2.5% interest, pledged as collateral (cash component), short MCX gold futures removes price risk, contango rolls ≈31% on margin; scalable to 100g Gold Mini; optional short-put overlay. Full strategy record with numbers. → ch 17/30/12; heavy enhancement queue (payoff table, haircut/limit math, roll arithmetic).
7. **1187 Arbitrage defined** — one-line glossary entry.
8. **1189 99% traders fail** (★ core Part I material, quality 5) — the canonical failure journey: cash → leveraged futures → TA workshop → 9-lot gap blowup → 2-lot overcorrection (ROCE vs portfolio return) → thesis: success = margin management. Plus workshop profit-screenshot scam mechanics. → ch 1/2/12/26.
9. **1192 Blue chip** (etymology) — casino chip origin. → glossary/ch 29.
10. **1195 Market is not complex** — simplicity doctrine; jargon as marketing weapon. → ch 3/13.

## Notable for downstream phases
- **Strategy Library**: the SGB + short-futures hedged carry (1186) is a complete, novel recipe with stated numbers — candidate for ch 17 worked example.
- **Part I anchor**: 1189's failure arc is the best single narrative for chapters 1–2 found so far in this batch.
- **Verification queue (8)**: 2004 STT/LTCG swap; LTCG reintroduction; NSE 1992/93/94 dates; quadruple witching definition; SGB 2019-S6 price ~₹4,800/g vs ₹5,300 physical (Aug 2022); MCX gold Oct-22 ~5,311 + Dec contango ~273–300; SGB 2.5% interest; Reliance ₹1,000→₹5,000→~₹2,560 post-bonus path.
- **Leaks logged** (in-field only): name variants ("PR Sunder", "Pia Sundar"), workshop promos (1189, 1195), personal holdings/P&L (1178, 1186 first-person SGB disclosure) — all flagged in `exclude_passages`/`leaks` for the anonymization pass.
- **Enhancement candidates**: position-sizing table (1189), SGB payoff/haircut tables (1186), STT/LTCG timeline (1176).

acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 transcripts (1176, 1178, 1180, 1183, 1185, 1186, 1187, 1189, 1192, 1195) read in full and exactly one schema-compliant JSON record each written in order to book/analysis/batch_special_142.jsonl; ASR corrections applied in interpretation; identity strings confined to leaks field; output report at the authoritative path book/analysis/outputs/special_142_report.md. No scope widened."
    },
    {
      "id": "criterion-2",
      "status": "satisfied",
      "evidence": "Validation command run: 10/10 records parse as JSON, all 15 required fields present in every record, 8 event_claims and 1 strategy captured, regex scan confirms no banned name patterns outside the leaks field. File size: batch_special_142.jsonl = 11,738 bytes."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_142.jsonl",
    "book/analysis/outputs/special_142_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c (validate JSONL: parse all lines, check required fields, count event_claims/strategies, regex banned-name scan)",
      "result": "passed",
      "summary": "10/10 valid JSON records, all required fields present, no name leakage outside leaks field"
    }
  ],
  "validationOutput": [
    "records: 10 | all valid JSON: True",
    "ids: ['1176','1178','1180','1183','1185','1186','1187','1189','1192','1195']",
    "fields ok: True | event_claims total: 8 | strategies: 1",
    "no name leakage outside leaks field: True"
  ],
  "residualRisks": [
    "8 event claims (STT 2004 history, NSE dates, SGB/MCX gold prices Aug-2022, Reliance price path) are unverified until the Phase 3 web-verification pass runs",
    "1186 SGB arithmetic (~31% ROI on margin) is as stated by the speaker; payoff math should be re-derived during chapter enhancement before print"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_special_142.jsonl (10 structured analysis records) and special_142_report.md (batch digest + downstream notes + acceptance report)",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch contains two quality-5 items: 1186 (SGB hedged-carry strategy recipe) and 1189 (canonical trader-failure narrative) - recommended anchors for chapters 17 and 1-2 respectively."
}
```