# Verification Report — ver_015 (batch 015)

Verified 10 claims about Indian stock-market events (2018–2026) using market price data (Yahoo Finance historical candles for ^NSEI, ^NDX, ^GSPC, ^IXIC, ^DJI, BTC-USD, ETH-USD, RELIANCE.NS), Wikipedia (2018 Union Budget, TCS, 2025 India–Pakistan war), plus Bloomberg/FT/Reuters references captured via Wikipedia citations.

Results written to: `book/events/verified_batch_015.jsonl` (one JSON per claim).

## Verdict summary

| # | Verdict | Key finding |
|---|---------|-------------|
| 1 | **corrected** | Trump tariff crash Apr 2025: Nifty low ~21,744 (7 Apr) correct; starting level was ~23,300 (Apr 2025), not 26,300 (Sep-2024 peak). NDX low ~16,542 from ~22,223 peak, not "25,000". |
| 2 | **corrected** | Crypto crash 21 Jan 2022: BTC -10.4% correct; ETH -14.8%, not "nearly 10%". |
| 3 | verified | Export duty on petrol/diesel/ATF (30 Jun 2022) → RIL -7.2% close / -8.2% intraday on 1 Jul 2022. "~8%" accurate. |
| 4 | **corrected** | May-2022 CPI 8.6% (10 Jun 2022) vs 8.3% expected (claim said 8.4%); S&P -8.7%, Nasdaq -9.4% over following week — "nearly 10%" roughly right over a week, overstated for strictly four days. |
| 5 | verified | Powell Jackson Hole 26 Aug 2022: Dow -3.03% (-1,008 pts), "some pain" speech ~7:35 PM IST. |
| 6 | verified | TCS Q2 FY22 results 8 Oct 2021 (post-market); Accenture read-across standard. |
| 7 | verified | India–Pakistan ceasefire mid-May 2025; Nifty closed exactly 24,925 on 12 May 2025. |
| 8 | **corrected** | Surgical strikes real but on 29 Sep 2016 (not 2017/2018): Nifty -2.6% intraday, -1.8% close. |
| 9 | **corrected** | Gujarat results 18 Dec 2017: Nifty -2.5% intraday then recovered (+0.5% close); "~500 pts / 5%" overstated. |
| 10 | verified | LTCG 10% (>₹1L, no indexation) reintroduced in 1 Feb 2018 Budget; market corrected afterward. |

### Corrections that matter for the book
- Claim 1 (Nifty 26,300→21,700; NDX 25,000→16,000) — the speaker merged the Sep-2024 all-time high with the Apr-2025 crash start. Books/editors should use: Nifty fell from ~23,300 (early Apr 2025) to intraday low 21,744 (7 Apr 2025), i.e. ~-17% from the 26,277 Sep-2024 peak; NDX fell from ~22,223 (Feb 2025) to ~16,542 (7 Apr 2025), -25.6%.
- Claim 9 (Gujarat "500-point crash") — actual intraday fall ~190–260 points (2–2.5%), then V-recovery to close green.

## Evidence sources (primary)
- Yahoo Finance chart REST API: ^NSEI, ^NDX, ^GSPC, ^IXIC, ^DJI, BTC-USD, ETH-USD, RELIANCE.NS (historical daily candles for the relevant windows).
- Wikipedia: 2018 Union Budget of India; Tata Consultancy Services; 2025 India–Pakistan war (with Reuters/FT citations).

## Residual risks
- Some claims rely on the speaker's recollection of intraday timing (e.g., "within seconds" falls) that market data cannot fully confirm; verdicts reflect the verifiable close/intraday-range facts.
- Claim 6's "Accenture results lifted Indian IT expectations" is a market-narrative read-across, confirmed as standard coverage but not a single-citable price event.

## Files written
- `book/events/verified_batch_015.jsonl` (10 lines, one JSON per claim)
- This report at `book/events/outputs/ver_015_report.md`

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified exactly the 10 assigned claims (ver_015); wrote results as one JSON line per claim to book/events/verified_batch_015.jsonl and this report to the authoritative output path book/events/outputs/ver_015_report.md. No scope expansion: no extra claims added, no source files modified."
    },
    {
      "id": "criterion-2",
      "status": "satisfied",
      "evidence": "Evidence for every verdict: 6 verdicts backed by Yahoo Finance historical daily-candle data (NSEI Apr-2025 low 21,744; NDX low 16,542; BTC/ETH 21-Jan-2022 closes; RELIANCE 1-Jul-2022 -7.2%; DJI 26-Aug-2022 -3.03%; NSEI 12-May-2025 close 24,925; NSEI 29-Sep-2016; NSEI 18-Dec-2017; SPX/IXIC Jun-2022), plus Wikipedia/Bloomberg/FT/Reuters citations for LTCG-2018, TCS-Q2FY22 date, and the 2025 ceasefire. Commands run documented below; nothing staged in git."
    }
  ],
  "changedFiles": [
    "book/events/verified_batch_015.jsonl",
    "book/events/outputs/ver_015_report.md"
  ],
  "testsAddedOrUpdated": [
    "Validated JSONL by re-parsing the written file (json.loads per line succeeded for all 10 records)"
  ],
  "commandsRun": [
    {
      "command": "curl Yahoo Finance chart API for ^NSEI, ^NDX, ^GSPC, ^IXIC, ^DJI, BTC-USD, ETH-USD, RELIANCE.NS",
      "result": "passed",
      "summary": "Retrieved historical daily candles for all verification windows; used to confirm levels/dates/percent moves."
    },
    {
      "command": "curl Wikipedia pages (2018 Union Budget of India, TCS, 2025 India-Pakistan war) + DuckDuckGo HTML search for LTCG 2018",
      "result": "passed",
      "summary": "Confirmed LTCG reintroduction after 14-year absence (1 Feb 2018 Budget), TCS Q2 FY22 date 8 Oct 2021, ceasefire ~11-12 May 2025."
    },
    {
      "command": "python3 write/validate JSONL",
      "result": "passed",
      "summary": "Wrote 10 JSON records; file re-parsed line-by-line with json.loads successfully."
    }
  ],
  "validationOutput": [
    "10/10 claims verified with verdicts: verified=6, corrected=4 (claims 1, 2, 4, 8, 9 -> actually corrected=5: 1,2,4,8,9; verified=5: 3,5,6,7,10)",
    "All result JSON records validated as parseable JSONL"
  ],
  "residualRisks": [
    "Intraday timing details in speaker recollections (e.g. 'within seconds') not independently confirmable; verdicts anchored to verifiable OHLC data.",
    "Claim 6 read-across (Accenture -> Indian IT) is narrative confirmation, not single-price-event verification."
  ],
  "noStagedFiles": true,
  "diffSummary": "Created two new files: verified_batch_015.jsonl (10 claim-verification records with verdicts/evidence) and outputs/ver_015_report.md (this report). No existing files modified.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Correct verdict tallies: 5 verified (idx 3,5,6,7,10) and 5 corrected (idx 1,2,4,8,9). The two corrections with the highest book-impact are idx 1 (Nifty '26,300' start level wrong - actual Apr-2025 level ~23,300; 26,277 was the Sep-2024 ATH) and idx 9 (Gujarat 5% crash overstated - actual ~2.5% intraday)."
}
```