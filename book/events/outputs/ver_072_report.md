# Verification Report — Batch 072

**Run by:** delegated worker subagent (fact-verification)
**Output:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_072.jsonl`
**Claims verified:** 10 | **Verdicts:** 7 verified · 2 corrected · 1 unverifiable

## Methodology
- Index/stock level claims (2, 3, 6, 7, 9, 10) verified against **Yahoo Finance v8 chart API** daily OHLC for the exact date windows (NSEI, NSEBANK, DJI, IXIC, HDFCBANK.NS, RELIANCE.NS).
- Macro/policy claims (1, 4, 8) verified via **Google News RSS** (CNBC, Reuters, Indian Express, Business Standard, Livemint, Times of India).
- Where a claim includes an intraday/attribution micro-detail not present in public sources (e.g., GIFT Nifty −150 pts in 15 min, index point-contributions from individual stocks), the hard, verifiable core was checked and the micro-detail flagged in `notes`.

## Per-claim results

1. **verified** — March 2024 US CPI 3.5% YoY (prior 3.2%) on 10-Apr-2024; 10-yr Treasury yield jumped above 4.5% after release (CNBC). Bond-price dip direction confirmed; GIFT Nifty micro-move noted as consistent but not independently sourced.
2. **verified** — 26-May-2022 Dow +1.61% (32,120.28→32,637.19), Nasdaq +2.68% (11,434.74→11,740.65); US Q1-2022 GDP 2nd estimate −1.5% annualized that day (advance −1.4%, ~−1.3% expected).
3. **verified** — 2-Jun-2022 US session Dow intraday swing ~740 pts (low 32,509 → high 33,248, close +1.33%); Nasdaq +2.69%. Microsoft growth-guidance concern + cloud-name strength directionally consistent; precise "cloud +10–12%" not independently confirmed (noted).
4. **verified** — India Q1 FY22 GDP +20.1% YoY released 31-Aug-2021 (expectations ~19.8–20%; SBI Ecowrap ~8.5–9% FY22 view). Indian Express/IBTimes confirm.
5. **unverifiable** — Bank Nifty 37,100 PE strike was plausibly ATM/OTM (index high 37,140 that day), and a "free-trade" stop-loss-cascade incident circa Sep-2021 has been reported historically, but the specific one-second ₹360→₹1,921.80 spike, 252,000 qty, and ~₹38cr figure could not be confirmed from accessible public sources. Recommend direct NSE circular check if this incident is included in the book.
6. **verified** — HDFC Bank 52-week low 726.65 (claim ~725); Jan-2026 high >1,000 (period high 1,020.5); 29-May-2026 low 737.75 ("touched 735" within rounding). Point-contribution attribution (~90 Nifty / ~500 Bank Nifty pts) noted as unverifiable intraday estimates.
7. **corrected** — Reliance bands: the post-Oct-2020 1:1 bonus 2,200–2,800 band (2021–2023, unadjusted) is broadly right, but "800–1,000 for ~10 years" overstates the pre-2020 band (Yahoo adjusted 2013–2017 range 175–435; x2 for bonus ≈ 350–870 unadjusted). Verify against NSE unadjusted history before quoting.
8. **verified** — Tata Capital IPO band ₹310–326 (claim ~300–320) set week of 29/30-Sep-2025; unlisted market far higher ("up to 70% value erosion" supports ~₹1,000+ unlisted); ~20 new IPOs that week confirmed (Business Standard IPO calendar). ₹345 rights-issue price not directly confirmed (noted).
9. **verified** — Nifty 17,101.95 (28-Jan-2022 close) → 17,780.0 (2-Feb-2022 close) ≈ +680 ("~700" rally after budget); Meta −25% intraday 3-Feb-2022; Nifty fell to 17,560.2 that day and 17,213.6 by 7-Feb (−~300 from peak). Accurate.
10. **corrected** — Two-session fall was ~500 (−261 on 23-Oct, −160 on 25-Oct 2023 from prior closes), not "600 at 300 each". The ~800 decline matches peak-to-trough 19-Oct high 19,681.8 → 26-Oct low 18,837.85 (−844) over 4–5 sessions; "nearing 19,000" accurate (19,122 close 25-Oct; 18,857 close 26-Oct).

## Residual risks
- Several claims carry intraday tick-level or attribution details that cannot be independently sourced (claims 1, 3, 5, 6). These are flagged in `notes`; the book should avoid presenting them as independently verified facts.
- Claim 5 (NSE "free trade" incident) needs an NSE circular / contemporaneous exchange announcement to be verified — flagged for direct-source check.
- Claim 7 should be re-stated using NSE unadjusted price history.