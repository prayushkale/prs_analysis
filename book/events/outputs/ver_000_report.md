# Batch 000 — Fact-Verification Report (10 claims)

**Model note:** Verification performed via web search (Google News RSS, Bing RSS, publisher sites). All 10 claims processed; results written to `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_000.jsonl`.

## Summary of verdicts

| idx | Claim topic | Verdict | Key correction / note |
|-----|-------------|---------|----------------------|
| 1 | June 4, 2024 election-day Nifty crash | **corrected** | Intraday fall ~8.5% (low ~21,281), close ~-6%; "crash ~10% then recovers to 26,000" wrong — 26,000 was reached only in late Sep 2024 (record highs 32× in 2024). Naidu/Nitish support confirmed same night. |
| 2 | HDFC Bank Q3 FY24 results → Bank Nifty gap ~1,500 pts | **verified** | Q3 results Jan 16, 2024; HDFC Bank -8.5% (worst since COVID; ₹1 lakh crore MCap lost); Nifty worst day since June 2022. |
| 3 | April 8, 2026 ceasefire news → Nifty 24,000 | **unverifiable** | No reputable source found for a specific Apr 8, 2026 ceasefire / 24,000 surge; similar US-Iran ceasefire rallies seen Mar–Jun 2026. |
| 4 | GST 2025 slab cuts (28→18, 12→5), eff. Sept 22, 2025 | **corrected** | Confirmed reform effective 22 Sep 2025 (5%/18% main slabs + new 40% luxury rate via GST Council; signal at Aug-15 speech). |
| 5 | 2019: FPI-tax U-turn + corporate tax cut 30→22% | **corrected** | Two separate events: Aug 2, 2019 surcharge rollback (FPIs) and Sep 20, 2019 (Friday) corporate tax cut 30→22% (25.17% eff.); Bank Nifty +8% biggest single-day gain. |
| 6 | Aug 5, 2024 Nikkei >10% crash (yen carry unwind) | **verified** | Nikkei -12.4%, worst since 1987 Black Monday; weak US jobs data Aug 2 triggered global risk-off. |
| 7 | Adani-Hindenburg: NSE ASM / trading ban | **corrected** | Adani firms placed under ASM (price-band surveillance, tradeable — not a ban; Adani Ports on F&O ban list Feb 3, 2023). FPO closed fully subscribed despite sub-price trading; stock then fell ~30%+. |
| 8 | Feb 2020 budget-day COVID crash | **corrected** | Budget Feb 1, 2020 (Saturday); first session after (Feb 3, 2020) Sensex -988 pts, Nifty below 11,700 (~-2.2%) on COVID fears. |
| 9 | 2024 FM reappointment + 2019 FM-appointment-market anecdote | **verified** | Sitharaman reappointed FM June 2024 (Modi 3.0); 2019 appointment (May 31/June 1, 2019) anecdote corroborated. |
| 10 | Trump 25% tariffs Mexico/Canada effective Mar 4, 2025 | **verified** | Timeline: Feb 1 announcement → pause → confirmed Feb 27 → effective Mar 4, 2025; US markets fell sharply. |

## Distribution
- Verified: 4 (idx 2, 6, 9, 10)
- Corrected: 5 (idx 1, 4, 5, 7, 8)
- Unverifiable: 1 (idx 3)

## Notes for the book pipeline
- Claim 3 (2026 ceasefire) should be re-checked against primary sources at compile time, or treated as speaker recollection (hedged) rather than verified fact.
- Claims 1, 5, 8 are classic "speaker compresses two events / rounds numbers" cases — book should use the corrected_claim text.
- All evidence titles/URLs included per claim in the JSONL.