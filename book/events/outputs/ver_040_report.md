# Verification Report — batch_040

**Date:** 2026-08-30 · **Method:** Yahoo Finance chart API (primary source for index/stock/yield/VIX levels — authoritative daily OHLC), Wikipedia extracts, NSE circular via Zerodha bulletin, and search-engine corroboration (Bing/Naver). Where the exact claim conflicted with primary market data, the claim was **corrected** to the accurate figures.

## Summary

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | Two delta-variant sell-offs mid-June & 19 Jul 2021; Dow fell sharply | **verified** |
| 2 | Credit Suisse/UBS US$3.2bn rescue, 19 Mar 2023; shares "7% higher" post-deal | **corrected** |
| 3 | Fitch downgrade Aug-2023; Nifty -700 pts from 20,000 in a day | **corrected** |
| 4 | 2024 election day Nifty -9.3% then +10% | **corrected** |
| 5 | HDFC -7-8% since Jan-2026 news; ICICI fell post-Q3; ~40% Bank Nifty weight | **verified** |
| 6 | Bajaj Housing Finance IPO listed ~16 Sep 2024 at ~₹140-150 (~100%) | **verified** |
| 7 | Nifty lot 75→65, Bank Nifty 35→30 from 1 Jan 2026 | **verified** |
| 8 | US 10Y hit ~2.41% around 23-Mar-2022, multi-year high | **verified** |
| 9 | India Q2 FY24 GDP 30 Nov 2023; exit polls 30 Nov; 5-state results 3 Dec 2023 | **verified** |
| 10 | 19 Aug 2025: Nifty futures first >25,000 since breakdown; VIX -4.5% | **verified** |

## Key corrections

- **#2** — Deal amount verified (CHF 3bn ≈ US$3.2bn, 19 Mar 2023, all-stock at CHF 0.76/share ≈ 59% discount). But after the deal, CS shares **fell ~50-60%** on 20 Mar 2023 (to ~CHF 0.82), they did **not** trade 7% higher.
- **#3** — Fitch action verified (AAA→AA+, 1 Aug 2023, first since 2011). But Nifty was at **19,733** (not 20,000; first crossed 20,000 only in Sept 2023) and fell **~207 pts (-1.05%)** on 2 Aug to 19,526 and **~145 more** on 3 Aug to 19,381 (low 19,296); **~350 pts over two sessions**, not 700 in one day. Dow fell 3 sessions (2–4 Aug), not four.
- **#4** — Election facts verified (BJP 240 seats < 272; TDP/JDU kingmakers). But the Nifty fall was **-8.5% intraday (low 21,281.45 vs 3-Jun close 23,262.85) and -5.9% close (21,884.50)** — not -9.3%. Recovery of ~+10% from the intraday low within ~a week is accurate (low 21,281 → 7 Jun close 23,290).

## Notes on verified items

- **#1** DJI data: 18 Jun 2021 close 33,290 (-~533 pts); 19 Jul 2021 close 33,962 (-725 pts, -2.09%) — two sell-offs, consistent.
- **#5** HDFC: 2-Jan-2026 close 1,001.60 → 18-Feb-2026 close 924.70 = **-7.7%** (low 903.90 on 13 Feb = -9.8%). ICICI fell ~-7.8% from mid-Jan peak after Q3, then recovered. Weight ~40% combined is plausible post-caps; ~2,000-pt drag on ~59k Bank Nifty is arithmetically consistent.
- **#6** Listed 16 Sep 2024 at open ₹150 (+114% over ₹70 issue); GMP had predicted ~114% (~₹140-150); closed ₹165 day one. Claim's "expected ~100% / ₹140-150" matches.
- **#7** NSE/NSE-circular via Zerodha: effective **30 Dec 2025 EOD**; first revised weekly expiry 6 Jan 2026, first monthly 27 Jan 2026. "Effective Jan 2026 series" is correct in substance.
- **#8** 10Y crossed 2.40% ~24-25 Mar 2022 (peak 2.50% on 25 Mar); "highest in 2-3 years" accurate (first time above 2.4% since 2019).
- **#10** 19 Aug 2025 intraday high 25,012.65; futures (spot+premium ~25-50) closing >25,000 consistent; first spot close >25,000 was 20 Aug (25,050.55). India VIX 18→19 Aug: 12.34 → 11.79 = **-4.5%**, matching. First time above 25k since the early-2025 breakdown — correct.

## Sources (primary)

- Yahoo Finance chart API — `^NSEI`, `^NSEBANK`, `^DJI`, `^TNX`, `^INDIAVIX`, `HDFCBANK.NS`, `ICICIBANK.NS`, `BAJAJHFL.NS` daily OHLC
- Wikipedia — "Acquisition of Credit Suisse by UBS" (deal terms, AT1 wipeout, date)
- Zerodha MarketIntel bulletin 429705 — NSE lot-size revision effective 30 Dec 2025
- TimesNow / Moneycontrol / Business Standard — Bajaj Housing listing, Fitch reaction