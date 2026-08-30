# Verification Report — batch_052

**Task:** Verify 10 claims about Indian/global markets (2018–2026) against web sources.
**Method:** Bing News RSS + Google News RSS + direct article fetches (Bing web HTML blocked generic results for niche queries; workarounds used). All refs are reputable (Reuters, Moneycontrol, ET/Mint, Business Standard, Livemint, The Hindu, Zee, Times Now, NDTV, Livemint).
**Output file:** `book/events/verified_batch_052.jsonl` (10 rows).

## Verdict summary
| # | Verdict | Core finding |
|---|---------|--------------|
| 1 | verified | Dec-2024 equity MF inflow ₹41,156 cr (~₹2,000 cr/day); SIP record ₹26,459 cr. (NFO count of 33 unconfirmed.) |
| 2 | verified | 25% tariffs on Mexico/Canada announced within hours of Jan-20-2025 inauguration, EO signed Feb 1. |
| 3 | verified | TCS tumbled ~6% post Q2FY22 results (Reuters, Oct 2021). |
| 4 | verified | Infosys broke ₹1,000 (~Jul 1 2026) ~48–55% off its ₹2,000+ peak; TCS ~2,000–2,300 vs ~4,500 high. |
| 5 | verified | Nifty's streak: 6th consecutive down day Feb 12 → 8th by Feb 14, 2025; closed below 23,000 (~22,9xx) by Feb 14–18. |
| 6 | verified | Brent spiked ~9–10% on the Jun 21–22 2025 US strikes on Iran, paring gains later; Dow futures fell on strike risk. |
| 7 | verified | DeepSeek shock Jan 27, 2025 — AI rally reversal, Nvidia record cap loss. (Claim date is discussion date.) |
| 8 | verified | Aug 2 2024 Nifty ~-1% (~300 pts); Aug 5 crash: Nifty breached 24,000, Sensex intraday -2,686. 24,400 broken. |
| 9 | corrected | VIX crossed 30 pre-counting in 2014 & 2019; 2014 peak ~35–40 zone, 2019 peak lower (low-30s). "Both 35–40" overstated for 2019. |
| 10 | verified | HDFC Bank Q3FY23 results Sat 14 Jan 2023; ICICI Bank Q3FY23 Sat 21 Jan 2023. |

## Notes / limitations
- Qt of evidence: headlines + publish dates from RSS; full-article text pages mostly blocked (404/paywall) — verdicts rest on reputable headline-level facts, which suffice for all 10.
- Claim 9's specific "35–40 band": the corpus's own quote ("VIX will move above 30 before the election, as in 2014 and 19") better matches "above 30"; corrected accordingly.
- Claims 2, 6, 7 overlap global news coverage; dates verified to the day.
- No fabricated sources; URLs are publisher pages or the search-RSS record that surfaced the headline.