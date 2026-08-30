# Verification Report — ver_028

Batch: 10 claims (India markets 2018–2026)
Method: Google News RSS search helper + Yahoo Finance chart API for hard index figures; Bing RSS unusable (spam-polluted) — Google News used exclusively.

## Verdicts

| idx | Verdict | Summary |
|-----|---------|---------|
| 1 | **verified** | Evergrande crisis 2021: HQ-sale talks (Bloomberg/Reuters), HK bear market (Bloomberg), tech crackdown — all confirmed |
| 2 | **corrected** | 2011/2013/2015 corrections were NOT uniform 15–20%: actual drawdowns −26.7% (2011), −11.9% (2013), −25.1% (2015–16); "bottomed and reversed" correct |
| 3 | **verified** | Fed 50bp hike on 4 May 2022 confirmed (CNBC, Investopedia); matching-expectations short-covering read consistent |
| 4 | **unverifiable** | Specific NSE pre-market rate glitch on 20-Sep-2023 could not be corroborated from available sources |
| 5 | **corrected** | 26-Feb-2021 crash: Nifty −568 pts close (−3.8%), Bank Nifty −1,745 close (−4.8%, ~−1,890 to intraday low); "700 pts Nifty" overstated, "2000 pts BankNifty ~5%" close |
| 6 | **verified** | Oct-2018 ICICI results reaction corroborated: Nifty near lows on Fri 26-Oct, +220-pt gap-and-hold rally Mon 29-Oct; +5% ADR figure not independently confirmed |
| 7 | **verified** | Peak 26,277 (27-Sep-2024) → low 23,263 (21-Nov-2024) ≈ −3,014 pts; relief rally to 24,768 (13-Dec) then sold down; 23,300 broken (22,124 close 28-Feb-2025) |
| 8 | **verified** | 2025 GST rationalisation confirmed (rate reductions incl. 28%→18%, 12%→5% categories), effective later in Nov 2025 |
| 9 | **verified** | Bihar 2025: NDA win confirmed (Business Standard, India Today, ET); market break-out failure is speaker's reading, consistent with muted action |
| 10 | **corrected** | NDX two-day falls: Sep-2023 hawkish hold −497 pts (−3.3%); Dec-2022 hawkish dot plot −~500 pts (−4.2%); ~600 pts modestly overstated; claim date ambiguous |

## Data quality notes
- Index figures verified from Yahoo Finance daily OHLC (NSEI, NSEBANK, NDX).
- Where news sources were unavailable via the RSS helper for niche claims (4, 6 sub-detail), market data corroboration was used instead.
- Bing RSS consistently returned unrelated spam — excluded from evidence.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified all 10 claims in batch ver_028; wrote JSONL results with verdicts/evidence to book/events/verified_batch_028.jsonl and this report to the authoritative output path. No scope widening beyond the assigned verification task."
    }
  ],
  "changedFiles": [
    "book/events/verified_batch_028.jsonl",
    "book/events/outputs/ver_028_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 search_helper.py \"<query>\" for each claim",
      "result": "passed",
      "summary": "Google News RSS searches for all claims; corroborating headlines found for claims 1,3,8,9"
    },
    {
      "command": "Yahoo Finance ^NSEI / ^NSEBANK / ^NDX chart API fetches (bash python)",
      "result": "passed",
      "summary": "Hard index data for claims 2,5,6,7,10; minimal/clean JSON"
    }
  ],
  "validationOutput": [
    "10/10 claims assigned verdicts (6 verified, 3 corrected, 1 unverifiable)",
    "Every corrected claim includes accurate replacement figures with data provenance",
    "JSONL: 10 valid JSON lines, one per claim",
    "Unverifiable claim (4) marked without guessing, per instructions"
  ],
  "residualRisks": [
    "Claim 6 ADR +5% figure unconfirmed by a direct source; market-reaction corroboration used",
    "Claim 1 A50 ~-25% magnitude not separately pinned to a source",
    "Claim 10 exact target date ambiguous in source claim (2022-12-18 vs 2023-09-20); both scenarios evaluated",
    "Bing RSS unreliable in this environment; evidence limited to Google News + market data"
  ],
  "noStagedFiles": true,
  "diffSummary": "New files only: verified_batch_028.jsonl (10 claim verdicts) + outputs/ver_028_report.md (this report)",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "For the book: claims 2, 5, 10 should use the corrected figures when cited. Claim 4 should be presented as unverifiable/hearsay or dropped. All Finance-Yahoo URLs embed the exact period windows used; other sources cited by outlet + headline since search RSS links are google-news redirect URLs."
}
```