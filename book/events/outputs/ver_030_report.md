# Verification Report — Batch ver_030

**Output file written:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_030.jsonl` (10 JSONL records, schema-compliant)
**Run by:** delegated fact-verification agent (worker), tools: curl/wget via bash + embedded knowledge; search engines via Bing News/Bing Web endpoints.
**Date of run:** ~2026-08-30

## Verdict summary

| # | Verdict | Headline finding |
|---|---------|------------------|
| 1 | **corrected** | RBI currency-derivatives circular was **5 Jan 2024** (not April), implementation deferred to **3 May 2024**; hedging-only substance correct |
| 2 | **verified** | Oct-2021 monthly expiry selloff confirmed: Bank Nifty 40,874→39,509 close (~1,580 intraday high-low); Nifty 18,211→17,857 (~354 pts) |
| 3 | **corrected** | India ~8x vs Shanghai roughly-flat 2008-2023 is right, but Shanghai DID reach ~5,178 (Jun 2015), so "never reached 4,000" is wrong |
| 4 | **verified** | RBI surprise 40 bps off-cycle repo hike + 50 bps CRR, 4 May 2022 — correct |
| 5 | **wrong** | Nifty spot on 1-Jan-2024 stayed below 22,000 (high 21,834); 22,000 milestone hit mid-Jan-2024; 200-pt futures premium unsupported |
| 6 | **verified** | Fed hiked 11 times (Mar-2022→Jul-2023), Dec-2023 pivot signal correct; Nifty rally ~2,400–2,500 pts (less than the stated ~3,000) |
| 7 | **corrected** | BTC $30K→$36.6K Oct-Nov 2023 price path is right, but driven by ETF *anticipation* (incl. 16-Oct-2023 false approval report); real approval 10-Jan-2024 |
| 8 | **corrected** | Five-state results were **11 Dec 2018** (not 21 Nov); Balakot **26 Feb 2019** confirmed; FII sell/buy narrative consistent |
| 9 | **corrected** | Feb-2026: gold fell ~5% (not $400/6%), silver ~10%, cause = strong dollar/Fed jitters; China suspended silver/oil *funds* + Lunar New Year closures, no "excess speculation" halt |
| 10 | **verified** | Brent 12-day losing streak ending 13-Nov-2018, ~7.5% single-day fall, >25% from $86.77 peak — corroborated |

## Notes for the book pipeline
- Claims 1, 3, 5, 7, 8, 9 carry material corrections and should use the `corrected_claim` text (or footnoted corrections) per the hybrid policy.
- Claim 5 is the most significant discrepancy: the speaker's memory of 1-Jan-2024 (futures >22,000 with >200pt premium) is contradicted by primary NSE/Yahoo spot data; the 22,000 milestone was crossed in mid-Jan-2024.
- Claim 2: Bank Nifty ~1,500-pt fall is well supported; Nifty's own fall (~354 pts) exceeded the stated "200-300".
- Evidence URLs: Reuters links are homepage/archive-level where the article ID was not resolvable via curl; Yahoo Finance OHLC URLs are query endpoints that return the actual historical data used.