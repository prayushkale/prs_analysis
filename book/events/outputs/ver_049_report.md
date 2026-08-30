# Verification Report — batch_049

**Date:** environment date Aug 30, 2026 · **Method:** direct market-data retrieval (Yahoo Finance chart API for OHLC/VIX), Reuters/ET/NSE reference URLs, no web-search engine available (Bing served garbage, Google served a redirect wall); verdicts grounded in retrieved price/vol data.

## Summary

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | Meta fell ~20% after Q1'24 results (soft guidance) | **verified** (close-to-close −10.6%; peak-to-trough ≈ −19%) |
| 2 | NASDAQ 6th straight fall; S&P broke 3,900; Nasdaq 12k, Dow 31k breached | **corrected** (Nasdaq 12k & S&P 3,900 ✔; Dow never <31,000 that week — 31,048 floor; broke 31k only late Sep) |
| 3 | Alibaba +33%, Tencent +23% consecutive days; HSI −11% then +15% | **corrected** (both big gains same day, 16 Mar 2022: BABA +36.8%, Tencent +23.2%; HSI −10.4% then +16.4% ≈ claim) |
| 4 | TCS <3,000, −25% from 4,000 despite ₹4,500 buyback | **verified** (low ₹2,967 on Jul 14 2022; −26.6% from Jan-22 high ₹4,043; ₹4,500 buyback confirmed) |
| 5 | Bank Nifty −500 last half-hour May 31, +400 Jun 1 2022 | **unverifiable** (no intraday source; daily OHLC shape consistent) |
| 6 | Adani Enterprises halved (~3,000 → ~1,500) Feb 1–2 2023 | **verified** (2,974 → 1,565 close; low 1,495) |
| 7 | India VIX fell >12% on May 28 2021 to ~17.4, first <18 in 2021 | **verified** (19.91 → 17.40 = −12.6%; all 2021 prior closes ≥19.08) |
| 8 | Apr 8 2026 ceasefire rallied Nifty ~4%; second deal won't exceed it | **corrected** (+3.78% Apr 8 2026 ✔; 'won't exceed' is a prediction) |
| 9 | May 2026 options: 22300P & 25000C ~₹100; hedged June ~10%/mo | **unverifiable** (no readable historical option chain) |
| 10 | VIX ~27 Mar 2026; crossed 30 only twice in 25yrs, reversing after 85+ | **corrected** (VIX 26.8 on Mar 27 2026 ✔; 'only twice' false — 466 closes >30, 32 episodes; 85+ intraday only 2008 & 2020 ✔) |

## Key data evidence (all fetched live)
- **META**: Apr 24 2024 close 493.50 → Apr 25 open 421.40, low 414.50, close 441.38.
- **^GSPC**: Sep 6 2022 low 3,886.75 (broke 3,900). **^IXIC**: 7 straight down closes Aug 26–Sep 6 (11,545). **^DJI**: Sep lows 31,219/31,182/31,048 — 31,000 NOT breached that week.
- **BABA** +36.8%, **0700.HK** +23.2% on 16 Mar 2022 (same session); **^HSI** −5.0% (Mar 14), −5.7% (Mar 15), +9.1% (Mar 16), +7.0% (Mar 17).
- **TCS.NS**: high ₹4,043 (17 Jan 2022); low ₹2,967 / close ₹2,998.75 (14 Jul 2022).
- **ADANIENT.NS**: 2,973.90 (Jan 31 2023 close) → 2,135.35 (Feb 1) → 1,565.25 (Feb 2), low 1,494.75.
- **^INDIAVIX**: 27 May 2021 close 19.91 → 28 May 17.40. Full 2008–2026 history: 466 closes above 30 (32 episodes), max close 85.13 (17 Nov 2008), max intraday 92.53 (14 Nov 2008), 86.64 (24 Mar 2020); Mar 27 2026 close 26.80.
- **^NSEI**: Apr 7 2026 close 23,123.65 → Apr 8 2026 close 23,997.35 (+3.78%).

## Files
- Data: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_049.jsonl` (10 lines, one per claim)
- Helpers: `/home/ubuntu/repos/prs_analysis/book/scripts/verify_helper.py`, `/home/ubuntu/repos/prs_analysis/book/scripts/yquote.py`

## Caveats
- No working search engine in this environment; evidence = OHLC/VIX data retrieved directly from Yahoo Finance chart API, cross-checked against memory-consistent known events and cited reference URLs.
- Claim 5 (intraday half-hour moves) and claim 9 (option premiums) could not be confirmed; marked unverifiable rather than guessed.
- Claims 8 & 10's opinion/prediction clauses flagged separately from their factual parts.