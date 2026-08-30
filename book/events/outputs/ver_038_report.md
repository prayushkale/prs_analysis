# Verification Report — batch_038 (10 claims)

## Method
- Market-move claims were checked against official daily OHLC data (Yahoo Finance API — Dow ^DJI, Nasdaq 100 ^NDX, Nifty 50 ^NSEI, Nifty Bank ^NSEBANK, Nifty Midcap 50 ^NSEMDCP50, USD/INR INR=X).
- Policy/macro claims (US-China tariffs, US CPI) were checked against Reuters, CNBC, PBS, Al Jazeera, NPR and the China–United States trade war Wikipedia article.
- For daily FII/DII flow figures and niche intraday microstructure claims, archival news searching was attempted via Google News RSS, Bing and Brave; the reachable search index is heavily weighted to 2025–2026 content, so several 2021/2024 daily items could not be independently sourced.

## Verdict summary
| # | Claim (short) | Verdict |
|---|---|---|
| 1 | Dow -250 Thu, +450 record close Fri (8-9 Jul 2021) | **verified** |
| 2 | Dec 2021: Nifty -900 over two sessions; Bank Nifty -2,600 | **verified** |
| 3 | May 12 2025 US-China tariff cut to 30% / 90 days | **verified** |
| 4 | Jun 2021 rupee record ~74.25; Nifty breaks 15,500; Bank Nifty -900 then +250 | **corrected** |
| 5 | US CPI 8.6% vs 8.3%, 40-yr high; Dow -650 then -880 | **verified** |
| 6 | Aug 2022: Dow ~-1,000 (~3%); NDX ~-900 from ~13,750 | **corrected** (end level ~32,900 not ~34,000) |
| 7 | Post-Jackson Hole: Dow ~-1,300; NDX ~-800 to 12,400 | **verified** |
| 8 | 26-Feb-2024 Midcap flash fall ~1-1.5%; stops fail | **corrected** (level ~14,000, not 945; stop-loss detail unverified) |
| 9 | Expiry-to-expiry May27→Jun10 2021: Nifty +500; Bank Nifty -50 | **corrected** (Nifty +400 close-to-close; Bank Nifty +36, flat) |
| 10 | Dec 17 2021: FII -2,000 cr, DII +1,500 cr | **unverifiable** (market move confirmed; daily flows unsourced) |

## Key data points (from official daily data)
1. Dow: 8-Jul-2021 close 34,421.93 (-259.86); 9-Jul-2021 close 34,870.16 (+448.23, record close).
2. 20-Dec-2021: Nifty low 16,410.2; Bank Nifty low 34,018.4. Two-session Nifty drop ~-890 to -970; Bank Nifty ~-2,680 to -2,770.
3. May 12, 2025 Geneva deal: US tariffs on China cut to 30% (from up to 145%) for 90 days; China's retaliatory tariffs cut to 10%. (Wikipedia: "The US agreed to cut tariffs on Chinese goods to 30%, while China reciprocated with tariff reductions...")
4. 17-Jun-2021 USD/INR intraday high 74.52, close 74.25; 18-Jun-2021 Nifty high 15,761.5 / low 15,450.9 (-310, broke 15,500); Bank Nifty high 34,787.4 / low 33,908.95 (-878) / close 34,558 (+649 from low, not ~250).
5. 10-Jun-2022: US May CPI 8.6% vs 8.3% expected, highest since 1981. Dow -638.11 (9-Jun) and -880.00 (10-Jun); two-day -1,518 (-4.6%).
6. 23-Aug-2022: Dow closed 32,909.6 (-1,089 vs 18-Aug close 33,999); NDX closed 12,881.8, intraday low 12,852.7 (from ~13,720 high on 16-Aug = ~-6.4%).
7. 29-Aug-2022: Dow 32,099.0 (Aug-25 close 33,291.8 → -1,193; high-to-low -1,333); NDX low 12,440.4 (Aug-25 close 13,143.6 → -703).
8. 26-Feb-2024: Nifty Midcap 50 high 14,083.8 / low 13,856.5 (high-to-low -1.61%), close 13,977.9 (-0.60%) — a flash dip with partial same-day recovery. "945" level in the source is a transcription artifact.
9. 27-May-2021 Nifty close 15,337.85 → 10-Jun-2021 close 15,737.75 (+400); 11-Jun-2021 close 15,799.35 (+461). Bank Nifty 27-May 35,095.05 → 10-Jun 35,131.20 (+36).
10. 17-Dec-2021: Nifty -263 to 16,985.2; Bank Nifty -930 to 35,618.6. Daily FII/DII provisional figures could not be independently confirmed.

## Notes for the book (hybrid correction policy)
- Claims 4, 6, 8, 9 carry corrected_claim text with exact figures — use those in the text and/or add a chapter endnote citing the Yahoo/Wikipedia/CNBC/PBS sources above.
- Claim 10: keep the market move with exact closes; the FII/DII daily numbers should be dropped or explicitly hedged as the presenter's recollection.
- Claim 8's stop-loss non-execution detail is the presenter's account; present as "traders reported" rather than as a verified market-structure fact.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified all 10 claims in batch_038 using official daily market data (Yahoo Finance quotes for ^DJI, ^NDX, ^NSEI, ^NSEBANK, ^NSEMDCP50, INR=X) and policy sources (Reuters, CNBC, PBS, Al Jazeera, Wikipedia trade-war article). Produced verdicts (5 verified, 4 corrected, 1 unverifiable), corrected_claim text for all corrected/wrong items, and 1-2 sources per claim. Scope confined to the assigned batch; no other files touched."
    }
  ],
  "changedFiles": [
    "book/events/verified_batch_038.jsonl",
    "book/events/outputs/ver_038_report.md"
  ],
  "testsAddedOrUpdated": [
    "JSONL validity/automatic check: 10/10 rows parse as JSON, idx sequential 1-10, verdicts within schema enum, no evidence missing (ran inline via python)"
  ],
  "commandsRun": [
    {
      "command": "timeout curl searches (Google News RSS, Bing HTML/video, Brave, lite/duckduckgo) + Yahoo Finance chart API fetches via python3 urllib",
      "result": "passed",
      "summary": "Yahoo daily OHLC retrieved for all six symbols; Google News RSS returned policy sources for claims 3 & 5; Bing/Brave/DDG largely blocked or 2025-2026-biased, limiting archival verification of claims 4/8/10 daily details"
    },
    {
      "command": "python3 JSONL validation (parse each line, assert idx/verdict schema, evidence presence)",
      "result": "passed",
      "summary": "10/10 rows valid; verdicts: 5 verified, 4 corrected, 1 unverifiable"
    }
  ],
  "validationOutput": [
    "verified_batch_038.jsonl: 10 rows, all schema-valid, idx 1..10, evidence present on every row",
    "No 'wrong' verdicts issued; 4 corrections supplied with exact alternate figures; 1 unverifiable with confirmed market context"
  ],
  "residualRisks": [
    "Daily FII/DII provisional figures for exactly 17-Dec-2021 could not be sourced (claim 10 marked unverifiable)",
    "Stop-loss non-execution detail on 26-Feb-2024 (claim 8) is the presenter's account, not independently confirmable",
    "'Record low' framing for the June-2021 rupee (claim 4) is media-dependent; corrected_claim uses precise intraday/close levels",
    "Repo does not provide a native web-search tool; evidence obtained via curl/urllib against public endpoints"
  ],
  "noStagedFiles": true,
  "diffSummary": "Wrote 10 lines of JSONL evidence (one per claim) to book/events/verified_batch_038.jsonl and this report to book/events/outputs/ver_038_report.md; no source changes.",
  "reviewFindings": [
    "no blockers",
    "URL typo fixed in two evidence entries (Bank Nifty symbol ^NSEBANK, Midcap symbol ^NSEMDCP50)"
  ],
  "manualNotes": "The delegation's output-path override (ver_038_report.md) was honored; the task-specified JSONL was also written at book/events/verified_batch_038.jsonl. Search index is 2025-2026-weighted, so older daily financial figures were verified against Yahoo official daily market data rather than news archives."
}
```