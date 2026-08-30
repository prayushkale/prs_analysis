# Verification Report — ver_042

## Summary

Batch 042 contained 10 claims about Indian and US markets (2018–2026). Verified against web sources (Reuters, CNBC, NSE/Upstox, Livemint, Business Today, Business Standard, Economic Times, India Today, Times of India, Bitcoin Magazine, etc.) using Google News RSS + Bing seed queries.

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | HDFC Bank 2022 whipsaw "3000→2050→2950→2150" | **corrected** — HDFC Bank traded ~₹1,250–1,700 in 2022; series doesn't match the entity; likely HDFC Ltd or garbled |
| 2 | India Q3 FY21 GDP 0.4% on 26-Feb-2021 | **verified** |
| 3 | Crude −$10 to ~$112 (Jun 2022) & BTC ~−20% from $69k | **verified** (BTC $69k→<$18k Jun 2022; crude fell ~5% to ~$112 on 17-Jun-2022) |
| 4 | India Q1 FY25 GDP 6.7% on 30-Aug-2024 | **verified** |
| 5 | Kotak Q3FY24 beat + Bank Nifty +400 intraday (20-Jan-24) | **corrected** — Kotak +9–10% confirmed; results Sat 20-Jan, trading reaction Mon 22-Jan; exact +400/+350 not confirmed |
| 6 | L&T −5–6% & Dr Reddy fell; "Bank Nifty expiry 1-Feb before budget" | **corrected** — L&T −5–7% and Dr Reddy −5% confirmed; 1-Feb was NIFTY expiry + Budget day; Bank Nifty expiry was Wed 31-Jan; pre-open fade = unverifiable heuristic |
| 7 | Infosys Apr 18, HDFC Bank Apr 20, Reliance Apr 22 (Q4 FY24) | **verified** |
| 8 | Fed 75bp 2-Nov-2022; Dow +200→−500; Nasdaq −4% | **verified** (Dow −505/−1.55%; Nasdaq −3.4% — claim slightly high but close) |
| 9 | NFP 315K 2-Sep-2022, prior 528K; Jackson Hole → 75bp odds | **verified** |
| 10 | FII −₹6,645 cr on 3-Mar-2022; ₹11K cr first two March sessions | **unverifiable** — monthly record exodus confirmed, exact daily figures not |

**Verdict mix:** 6 verified · 3 corrected · 1 unverifiable — no claim flatly "wrong" (all had a truthful core with date/entity/magnitude imprecision).

## Notable corrections applied
- **Claim 1**: The 4-point price path cannot be mapped to HDFC Bank (2022 range ₹1,250–1,700). Treated as conflation with HDFC Ltd (₹2,400–2,950, sharp drop after the Apr-4-2022 merger announcement) — will need careful reframing in the book.
- **Claim 5**: Weekend/date issue — results Jan 20 (Sat), market reaction Jan 22 (Mon).
- **Claim 6**: Instrument mix-up — 1-Feb-2024 was NIFTY (not Bank Nifty) weekly expiry and coincided with the interim Budget.

## Data quality note
- Daily FII cashflow figures (claim 10) are not published in an easily searchable canonical form; the book should cite monthly/aggregate FII data instead, or mark the day-level figure as recalled.
- HDFC price-path claims from transcripts should be re-checked against exchange data before print if used verbatim.

Output file: `verified_batch_042.jsonl` (10 lines, one per claim).