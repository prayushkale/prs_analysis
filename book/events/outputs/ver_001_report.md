# Verification Report — batch ver_001

**Task:** Verify 10 market-history claims from the "Dhanraj" book corpus against web sources.
**Method:** Throttled Wikipedia MediaWiki/REST API queries (search + article extracts), ~35 requests, rate-limit aware (429 handled with backoff + cache).
**Primary source preference:** NSE/niftyindices/SEBI/PIB/Reuters/ET/Moneycontrol were not directly reachable from this sandbox; Wikipedia provided the reachable, citable baseline. Judgments below also use standard, well-documented market history.

## Verdict summary

| # | Claim (short) | Verdict | Key correction |
|---|---|---|---|
| 1 | War Feb 28 → ceasefire Apr 8 (2026) | **verified** | Confirmed as the 2026 Iran war (US-Israel vs Iran); US-Iran ceasefire agreed 8 Apr 2026. |
| 2 | Japan crash / yen-carry unwind Aug 2024 | **verified** | Nikkei -12.4% on 5 Aug 2024 (worst since 1987). |
| 3 | India-Pak ceasefire May 12 2025, Nifty +1,000 | **corrected** | Ceasefire effective **10 May 2025**; 12 May = first trading day reaction. |
| 4 | 2009 election: spike then close red | **wrong** | 18 May 2009 was a record +17% rally (closed sharply up, not red). |
| 5 | Credit Suisse halts Adani collateral (Jan-Feb 2023) | **verified** | Confirmed late Jan 2023; rout deepened through Feb. |
| 6 | 2009 election gap-up ~20%, circuit halt | **corrected** | Actual +17.3% Nifty / +17% Sensex; circuit halt correct. |
| 7 | Russian strikes near Poland during Biden visit (Mar 2022) | **verified** | Biden in Warsaw 25-26 Mar 2022; strikes hit western Ukraine ~24-26 Mar. |
| 8 | 'Sitharaman candle' budget-day crash | **unverifiable** | Ambiguous budget; common usage = 20 Sep 2019 bullish tax-cut candle. |
| 9 | RBI prop-funding rule Feb 2026, brokers -8-10% | **unverifiable** | No source found; 8-10% single-day market fall needs news-DB check. |
| 10 | Jan 2011 FII selling + ~20% 2011 decline | **verified** | 2011 actual decline ~24% (Nifty & Sensex); early-Jan selling consistent. |

**Counts:** verified 5 · corrected 2 · wrong 1 · unverifiable 2

## Notes for the compiler
- Claims 1, 2, 3, 5, 6, 7, 10 are safe to use with the corrections/precisions above.
- Claim 4 must NOT be used as stated (historical reversal); use the corrected record if the writer wants the 2009 lesson.
- Claims 8 and 9 should be re-checked against a news archive (Moneycontrol/ET/Reuters) before inclusion; unverifiable = drop or hedge.

**Output written to:** /home/ubuntu/repos/prs_analysis/book/events/verified_batch_001.jsonl (10 lines, schema-conformant).