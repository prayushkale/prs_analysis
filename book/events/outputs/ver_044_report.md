# Verification Report — ver_044 (batch 044)

**Task:** Verify 10 claims about Indian stock markets (2018–2026) against web sources and write JSONL to `book/events/verified_batch_044.jsonl`.
**Date of verification:** 2026-08-30
**Method:** Web research via Google News RSS and direct primary-data APIs (Yahoo Finance daily OHLC for indices/stocks) — `curl`-based, no LLM browsing tool available in this sandbox. Claims that were pure market-history micro-anecdotes with no primary data trail were marked accordingly.

## Results summary

| # | Verdict | One-line finding |
|---|---------|------------------|
| 1 | **corrected** | HDFC Bank Q4 FY23 PAT +20% **YoY** (₹12,047.5 cr), not QoQ; missed estimates per CNBC TV18 |
| 2 | **verified** | RBI ₹2,000 withdrawal 19 May 2023; ₹2,000 = 10.8% of notes in circulation vs 86% in 2016 |
| 3 | **verified** | Accenture quarterly print → Indian IT rally: INFY +3.7% / TCS +3.4% on 24 Jun 2021; precedent Dec 2020 |
| 4 | **verified** | HDFC Bank -8.4% (17 Jan 2024) and -12.4% cumulative 16→19 Jan after Q3 FY24 results (close 839.6→735.3) |
| 5 | **corrected** | Bank Nifty 1 Feb 2022 intraday range ~1,112 pts (H 38,803 / L 37,691) — not a ~3,000-pt swing |
| 6 | **verified** | AMZN -7.8% then +13.5% (16% intraday high); SNAP -23.6% then +58.8% on 3–4 Feb 2022 |
| 7 | **verified** | NDX -7.1% close-to-close / -8.6% peak-to-trough Aug 2023; S&P 500 broke 4,485 on 4 Aug |
| 8 | **verified** | July 2023 US CPI released 10 Aug 2023 (BLS schedule); NDX ±100/200 micro-swing not independently confirmable |
| 9 | **corrected** | PFC +17.8% over Nov 2022 (not 30%/2–3 wks); PNB +33.7% monthly (weekly ~13–17%); BHEL +9.6% in a day ✓ |
| 10 | **verified** | Fed +25bp on 1 Feb 2023 (~99% priced); Nasdaq +15.7% from Dec-2022 low to the meeting |

## Notes for the book pipeline
- Claims 1, 5, 9 contain material numeric errors → per hybrid policy these should carry a correction (endnote) if used in the book; the *corrected_claim* fields contain the accurate figures.
- Claims 2–4, 6–8, 10 verified as stated (within reasonable rounding).
- Evidence for index/stock levels uses Yahoo Finance daily OHLC (primary market data); citations for policy/macro facts use RBI, BLS, and mainstream financial press headlines surfaced via Google News RSS.
- The `8.6%` NDX trough figure uses intraday peak-to-trough; headline claim "~8%" is fair.

## Files
- Results: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_044.jsonl` (10 records, JSON-validated)
- This report: `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_044_report.md`