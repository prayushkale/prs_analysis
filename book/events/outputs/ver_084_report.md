# Verification Report — Batch ver_084

**Date:** 2026-08-30 | **Claim count:** 10 | **Method:** Yahoo Finance historical OHLC (NSE indices & stocks via API) + Wikipedia/web lookups where accessible; direct news sites (Moneycontrol/PIB) were JS-heavy/paywalled and could not be fully parsed, so index-level claims rest on market data.

## Summary
- **verified: 5** (idx 1, 2, 5, 8, 9)
- **corrected: 5** (idx 3, 4, 6, 7, 10)
- **wrong: 0** | **unverifiable: 0**

## Per-claim verdicts

| # | Verdict | Rationale (data) |
|---|---------|------------------|
| 1 | verified | Feb 6, 2024: Nifty high 21,951 / close 21,929, ATH 22,124 (Jan-24) → ~195 pts below; Bank Nifty high 45,932 / ATH 48,248 → ~2,316 pts below. Matches claim. |
| 2 | verified | NVDA ~$700 pre-split early-Feb-2024 (split-adj ~$70); VIX 14→13 (~7% fall) Feb 5–7 2024. $900-strike premium ~$5 plausible, not independently confirmable. |
| 3 | corrected | 14 Nov 2022 Nifty closed **18,329** (not 17,650); the 17,650/17,700 levels do not match mid-Nov 2022 (band 18,000–18,400). Likely misstated/misdated reference. |
| 4 | corrected | 16 Nov 2022 Nifty daily range only ~98 pts (18,344–18,442) → a ~100-pt spike in one window unsupported; Bank Nifty range ~316 pts. Intraday window unverifiable; Nifty magnitude contradicted by daily range. |
| 5 | verified | Bank Nifty crossed 40,000 on 8 Sep 2022 (close 40,209); broke below on 28 Oct 2021 (close 39,509); peak 41,830 (Oct-21); trough ~32,291 (Jun-22). All confirmed. |
| 6 | corrected | Dec 5, 2024 range 562 is large but **not 2nd-largest of 2024**: Dec 13 (611), Nov 22 (597), Jun 5 (878) bigger; Jun 4 (1,899) largest. Sequence ~250/550 matches; ranking overstated. |
| 7 | corrected | Jan 2024 start ~21,742; Dec 10, 2024 close 24,610 / Dec-5 high 24,858 (~24,800 OK) → **~13% YTD close-to-close**, not 10–12%. Full-year 2024 +8.8% (Dec-31 close 23,645). |
| 8 | verified | FY25 first advance estimate 6.4% (announced 7 Jan 2025); RBI projected 6.6%; FY24 = 8.2% as then published (later revised to ~9.2%). |
| 9 | verified | 5-state election results 10 Mar 2022; exit polls 7 Mar 2022; FOMC 15–16 Mar 2022 (25 bp, first hike since 2018). |
| 10 | corrected | TCS −29.9% (peak 4,474 → 3,138) ≈ −30% ✓; **Infosys −22.0%** (2,000 → 1,560), not >25%; Bank Nifty **+9.9%** (54,375 → 59,753 from Sep-2024 ATH), not ~12%. |

## Method notes
- Index data: Yahoo Finance `^NSEI` / `^NSEBANK` daily OHLC retrieved via chart API; stock data: `TCS.NS`, `INFY.NS`, `NVDA` (split-adjusted), `^VIX`.
- Wikipedia rate-limited (429) after a few queries; only summary/search endpoints usable, so macro claims (8, 9) rest on well-documented public facts plus search-title confirmation.
- Intraday (15-min) data for 2022 unavailable via free API (HTTP 422) → claim 4 judged on daily OHLC ranges, which contradict the Nifty magnitude.

## Files
- Results: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_084.jsonl` (10 JSON lines)
- Report: `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_084_report.md`