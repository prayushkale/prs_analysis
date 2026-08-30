# Batch daily_092 Report (transcripts 3172–3198, 22 Jun – 13 Jul 2026)

**Digest (5 lines):**
1. 25/25 transcripts read and converted; 25/25 valid JSON records written to `book/analysis/batch_daily_092.jsonl`; 79 concrete event claims extracted (58 flagged verify=true).
2. Period covers the July-2026 monthly expiry cycle: violent 23,800–24,300 consolidation box, five-day breakout rally (+600), Trump "no more ceasefire" headline crash (-500+), and recovery off 24,000/23,800 supports.
3. Most notable event claims: Trump declaring the US–Iran ceasefire over (Sensex -1,000 in 30 min); Iran attacking tankers + declaring the Strait of Hormuz closed with a US 48-hour ultimatum; death of Ayatollah Khamenei referenced by Iran's president; Reliance Jio IPO announcement; Infosys breaking 1,000 / TCS 2,000 (-50%+); South Korea's 8% lower circuit (7th time in 2026); prop-desk FD leverage ban + STT-hike bid-ask widening; first 2026 session with FII+DII each buying >₹2,000 crore.
4. Data quality: high. Speaker numbers internally consistent across sessions (box edges, straddle premiums, VIX levels cross-check); one probable transcription garble flagged ("23,330" for a 24,450-straddle downside; "2.75 crore → 75 lakhs" MTM recovery reading kept approximate); ASR map applied throughout (Uranus→Iran, streets of Armas→Strait of Hormuz, ICSA→ICICI, Quotac/Kotag→Kotak, weeks→VIX, food-sea-rebalancing→MSCI, ASMR→ASML).
5. Leak surface: recurring name variants ("Pierre/Pia Sundar"), Delta Exchange sponsors, workshop promos with office contacts, personal P&L disclosures (6-cr Apr–Jun; Dec 23,000-put book), family (wife/gold), Tamil Nadu location + police-commissioner legal matter (3175/3177), political resignation joke (3180/3181), FM-resignation rumor (3184) — all logged in `leaks` for the banned-terms scrub; political-joke and rumor passages should be dropped at writing time.

**Duplication notes:** post-markets largely restate their same-day pre-markets (dup_flag set on 10 pairs); the compiler should dedupe toward the post-market + the 3182 weekly-outlook (richest single source in this batch).

**Verification priorities for Phase 3 (highest-salience claims):** Trump ceasefire announcement (2026-07-08); Khamenei death reference (2026-07-13); Hormuz closure + tanker attacks; Infosys <1,000 / TCS <2,000; Jio IPO announcement; Korea lower-circuit count; India H1-2026 Nifty -10%; STT-hike spread widening; RBI FCNR/G-sec measures.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 transcripts in batch daily_092 read in full; 25 valid JSONL records (schema-complete, ASR-corrected, leak-logged) written to book/analysis/batch_daily_092.jsonl; validation script confirmed 25/25 parse with required keys and correct id order; report written to the authoritative output path."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_092.jsonl",
    "book/analysis/outputs/daily_092_report.md"
  ],
  "testsAddedOrUpdated": [
    "inline python validation of JSONL schema, parse rate, and id order (run in-session, not persisted as a test file)"
  ],
  "commandsRun": [
    {
      "command": "python3 -c (JSONL validation: parse each line, assert required keys, compare id sequence to batch manifest)",
      "result": "passed",
      "summary": "25/25 lines valid, ids match expected order, 79 event claims extracted"
    }
  ],
  "validationOutput": [
    "lines: 25 valid: 25 errors: []",
    "ids match order: True",
    "total event claims: 79"
  ],
  "residualRisks": [
    "Two probable ASR/number garbles retained with approximations flagged (23,330 downside band; Mar-31 MTM -2.75cr recovery wording) — verify before quoting",
    "2026-dated geopolitical/corporate claims (Trump ceasefire, Khamenei death, Hormuz closure, Jio IPO) need Phase-3 web verification; unverifiable ones must be dropped or hedged in the book"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured analysis for 25 transcripts (2026-06-22..2026-07-13) as batch_daily_092.jsonl plus batch report",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Post-market reports largely restate same-day pre-markets (dup_flags set on 10 pairs); compiler should prefer post-market versions plus transcript 3182 (richest outlook). Leak log is dense in this batch: personal P&L, family, Tamil Nadu location, political jokes/rumors — all captured for the anonymization pass."
}
```
