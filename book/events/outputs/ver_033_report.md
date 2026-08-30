# Verification Report — Batch 033

**Path:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_033.jsonl`
**Claims verified:** 10 of 10 (5 verified, 5 corrected, 0 wrong, 0 unverifiable)

## Summary
| idx | Verdict | Claim short | Key correction (if any) |
|-----|---------|-------------|--------------------------|
| 1 | verified | Coal India FPO (₹4,500 cr base + ₹9,000 cr greenshoe = ₹13,500 cr), Oct 2018 announcement | — (note: FPO later deferred; claim is about the announcement, accurate) |
| 2 | corrected | Black Monday "1986, >30%" | Actual: **19-Oct-1987, Dow −22.6%**; October-bullish framing itself retained |
| 3 | corrected | Kobe quake "1994"; loss ">$1.5B" | Quake **17-Jan-1995**; Leeson losses ~GBP 827m (≈$1.3–1.4B); Barings sold for £1 |
| 4 | verified | GST India 2017, slabs 0/5/12/18/28% + cess | — |
| 5 | verified | US plunge ~7% on 11-Jun-2020 (COVID resurgence + Fed caution) | — (Dow −6.74%, S&P −5.9%) |
| 6 | corrected | India–China Sikkim tension Jan-2021; precise market numbers | Face-off Jan-2021 verified; SGX/Nifty magnitudes unconfirmed; note Aug-2021 Naku La is the major clash |
| 7 | corrected | BP offload "20% Rosneft stake for $25bn" | Stake is **19.75%**; ~$14bn value; **$25bn is the charge/hit**; Russia's non-resident sale ban confirmed |
| 8 | corrected | CBR hike "9% → 20%" | Was **9.5% → 20%**, 28-Feb-2022 (emergency) |
| 9 | verified | Nifty >4% 3-session fall, Mar-2026, Iran-war + FII outflows >₹10,000 cr | Real-world 2026 coverage confirms (worst week in 15 months; Nifty −500 pts on 13-Mar) |
| 10 | verified | US PPI surprise 18-Mar-2026; S&P >2% high-to-low | Coverage confirms PPI jump + S&P slide with Brent ~$110 |

## Sources used
Reuters, CNBC, The Guardian, WSJ, Financial Times archive mentions, Britannica, Investopedia, Federal Reserve History, ET, TOI, NDTV Profit, Fortune India, India Today, thehitavada, Barchart, Seeking Alpha (via Google News RSS + Bing RSS).

## Notes for the book
- Corrections in rows 2, 3, 7, 8 are the kind of "material speaker slips" the hybrid correction policy flags → chapter endnote with corrected fact + source.
- Row 6's market-move specifics should be hedged in the chronicle ("recalled / approximate") since intraday SGX/Nifty figures for 25-Jan-2021 were not independently confirmable.
- Rows 9, 10 are 2026 events present in the transcript corpus; real-world coverage corroborates them — safe to present as verified events.

**Validation:** JSONL schema-checked (10/10 lines parse; verdict enum valid). No other files modified.