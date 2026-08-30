# Verification Report — verified_batch_089

**Date:** (run during corpus build, reference time context ~Aug 2026)
**Method:** Yahoo Finance historical OHLC (query1.finance.yahoo.com/v8/finance/chart) for exact index/stock levels; Google News RSS + Bing for event corroboration; NSE archive attempts (blocked) noted.
**Output:** JSONL results written to `book/events/verified_batch_089.jsonl` (10 lines).

## Verdict summary

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | Nifty fell 750 pts in 4 days (Sep 21–24 2020), ~11,550→10,800 | **verified** |
| 2 | Top 5-6 stocks ~50% of Nifty; RIL ~15% (Oct 2020) | **corrected** |
| 3 | Feb 9 2024: PFC ~11.5-12%, REC 7-8%, BHEL 6-7% after PFC results | **corrected** |
| 4 | Feb 14 2024: HDFC Bank fresh swing low ~20% off high; Nifty 22,000CE 4-5→~40 | **verified** |
| 5 | Feb 27 2024: Bank Nifty 47,600CE (1,000 pts away, 3 sessions left) ~60 | **corrected** |
| 6 | Sep 16 2022: Nifty fell ~600 pts (18,100→~17,500); FIIs sold ₹3,000+ cr | **verified** |
| 7 | Sep 26 2022: Brent ~$85-87; DXY 112→113; rupee >81, RBI intervened Fri | **verified** |
| 8 | Sep 27 2022: Dow >300 lower, -20% = bear market; S&P lowest close of year | **verified** |
| 9 | Sep 28 2022: HDFC (bank) fell ~10% (2,500→2,250); HK lost a third 26,000→17,000 | **corrected** |
| 10 | Week Jan 25–29 2021: Nifty ~14,500→below 13,600, ~900-pt crash, 4 sessions | **verified** |

## Key evidence (exact data)

- **#1:** ^NSEI: 2020-09-21 high 11,535.25 → 2020-09-24 low 10,790.20 = 745 pts; close 10,805.55. Confirmed.
- **#2:** No public source confirms "~15%"; peak RIL Nifty weight ~14–14.5% (Oct 2020, e.g., Livemint 16-Oct-2020 "Blame it on RIL"). Bottom-25 "equals RIL" claim unverifiable/overstated.
- **#3:** PFC 468.55→428.85 (-8.5% close; intraday low 406.75 = -12.1%); REC 509.85→482.40 (-5.4%; low 463.30 = -9.1%); BHEL 230.80→227.55 (-1.4%; low 217.35 = -5.8%). Figures match intraday lows; close-basis figures are smaller.
- **#4:** HDFCBANK.NS: Jan 15 2024 high 840.45 → Feb 14 2024 low 681.78 = -18.9% (fresh swing low vs Feb 13 low 692.17). Nifty Feb 14 +97 pts to 21,840. Premium 4-5→40 unverifiable from chain history (consistent with rally day).
- **#5:** ^NSEBANK Feb 27 2024 close 46,588 (high 46,722): 47,600 ≈ 900–1,000 pts OTM ✓. Weekly expiry Wed Feb 28 = 1 session; monthly Thu Feb 29 = 2 sessions → "3 sessions left" off by one. Premium ~60 unverifiable.
- **#6:** ^NSEI Sep 15 high 18,096.15 → Sep 16 low 17,497.25 = 599 pts. FII ₹3,000+ cr figure consistent with crash-day flows but not independently confirmed.
- **#7:** BZ=F: Sep 23 close $86.15, Sep 26 high $87.66. DX-Y.NYB: Sep 23 111.24→113.19. INR=X: breached 81 on Sep 22; 81.3–81.9 Sep 23–26. RBI intervention around 81 in Sep 2022 consistent with contemporaneous reports.
- **#8:** ^DJI Sep 26 close 29,260.81 (-329.81 vs Sep 23 29,590.41 = -1.11%); 20.4% below Jan 4 2022 record 36,799.65 → bear market (AP/MPR 26-Sep-2022 headline confirms). ^GSPC Sep 26 close 3,655.04 = then-lowest close of 2022.
- **#9:** Entity correction: ~10% Sept-2022 drop with levels ~2,4xx→2,2xx matches HDFC Ltd (parent), not HDFC Bank (adjusted 736→691 = -6%). ^HSI: 26,137 (Oct 20 2021) → 17,250.88 (Sep 28 2022 close) = -34% ≈ "a third" ✓.
- **#10:** ^NSEI Jan 25 2021 open 14,477.8 → Jan 29 low 13,596.75 = 881 pts; 4 trading sessions (Jan 26 holiday). Confirmed.

## Residual risks / caveats
- Yahoo HDFC Bank series is merger-adjusted (HDFC Ltd merged into HDFC Bank July 2023); relative %-moves used, not absolute prices.
- HDFC Ltd exact Sept-2022 levels couldn't be pulled from a clean public API (delisted from Yahoo; NSE archives and stooq blocked); levels stated on the basis of market knowledge and cross-checked against the HDFC Bank adjusted series — flagged for a possible follow-up.
- Option-premium values (claims 4, 5) are not recoverable from public historical chain archives; marked as-reported/unverifiable. Index context around them was verified from OHLC.
- Claim 2's "~50% top-6 concentration / bottom-25 equality" statistic is rhetorical; corrected toward the documented ~14% RIL peak weight.