# Verification Report — vermillion (batch_088)

**File written:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_088.jsonl` (10 lines, schema-validated)

**Method:** Google News RSS querying (curl) for each claim; cross-checked with Reuters, Moneycontrol, BusinessLine, TradingView, Groww, Livemint, Fortune India, Business Standard, Samco, Guardian/BBC/Reuters (Foxconn), and U.S. EIA. Where the claim concerned unpublished intraday option-premium prints or exact stock-level ticks, verdict = `unverifiable` (no public data exists; no guesses made).

## Verdict summary

| idx | Claim (short) | Verdict |
|-----|---------------|---------|
| 1 | Bank Nifty 57k call ~100→10-12 (28 May 2025) | unverifiable |
| 2 | Bank Nifty −650/+650 intraday recovery, HDFC +30, ICICI +20 (29 May 2025) | unverifiable |
| 3 | Bank Nifty 48k→56k in April 2025, consolidation | **corrected** |
| 4 | Bank Nifty >500 pts intraday, 45,700 call 10→300 (14 Sep 2023) | unverifiable |
| 5 | Crude >$120 (mid-2022) → ~$76-77 (Dec 2022); rupee 81-83 | verified |
| 6 | India CPI Nov 2022 = 5.88% vs ~6.4% exp., first in 2-6% band | verified |
| 7 | Axis & Adani fresh ATHs (Dec 2022); ICICI 950→910 | verified (ICICI tick unconfirmed) |
| 8 | China civil unrest at Foxconn iPhone plants (Nov 2022) | verified |
| 9 | Nifty +200 on 10 Mar 2026 with 25,500 call 67→46 | unverifiable |
| 10 | Banking 61,500→53-55k; auto −10-15% wiping GST gains (Mar 2026) | verified |

## Key corrections / notes for the book

1. **Claim 3 (should be corrected in text):** Bank Nifty's first cross of **56,000 was 3 June 2025** (ahead of the RBI MPC), NOT April 2025. The April 2025 tariff-recovery rally took Bank Nifty from ~48-49k lows back toward the low-to-mid 50s. Any manuscript text must say "crossed 56,000 in early June 2025."
2. **Claim 9 caution:** On 10 Mar 2026 the tape was *split* — Nifty snapped a 2-day losing streak (oil plunge, BusinessLine) while Bank Nifty fell >2% (TradingView). If the book cites this date, it must present both facts; the option-premium figure is unconfirmed and Nifty ~24,000 makes a 25,500 call far OTM (premium 67 seems inconsistent).
3. **Claim 7:** Axis Bank record high confirmed ~8 Dec 2022 (₹12,000 cr bond-raise plan, Fortune India); Adani Enterprises at record highs Dec 2022 (pre-Hindenburg, ₹4T mcap regained). The ICICI 950→910 detail is plausible but not independently confirmed — soften if printed.
4. **Claim 5 & 6 & 8 & 10:** all verified at the stated level of rounding; safe to print as-is.

## Commands run
- `curl` Google News RSS: `news.google.com/rss/search?q=...` for each claim (multiple queries per claim, max ~2-3).
- Python schema validation of the output JSONL (10/10 valid).

## Residual risks
- Google News RSS returns redirect-encoded URLs; evidence URLs are the RSS search endpoints (titles + outlet names are the reliable part).
- Intraday option-premium and exact stock-tick claims (idx 1, 2, 4, 9) are inherently unpublished — recorded as `unverifiable` rather than guessed.
- For 2026 claims (idx 9, 10) this verification reflects public reporting available in this environment; chronology is internally consistent across five independent outlets.