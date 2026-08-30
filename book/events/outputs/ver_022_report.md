# Verification Report — batch_022 (10 claims)

## Summary
- Claims verified: 4 | corrected: 6 | wrong: 0 | unverifiable: 0
- Output: `book/events/verified_batch_022.jsonl` (10 records, JSONL)
- Method: Google News RSS (targeted queries), Yahoo Finance chart API for exact OHLC, and reputable source headlines (Reuters, CNBC, Moneycontrol, Business Today, ETLegalWorld, The Indian Express, Livemint, Investopedia).

## Per-claim results

| idx | Verdict | Key finding |
|-----|---------|-------------|
| 1 | corrected | NVIDIA intraday ~-11% on 8-Mar-2024 (high 97.40 → low 86.51) and ~$2T market cap verified; the "+7% next session" actually came on 12-Mar (+7.2%), the immediate next session (11-Mar) closed -2% |
| 2 | corrected | Kotak ~+9% (1,783→1,946 real, 19↔27-May-2022) rather than exactly +10% (1,750→1,920); direction/timing right, magnitude ~1pt low |
| 3 | verified | HDFC Bank Q2 FY22 (16-Oct-2021): net profit ₹8,834 cr +17.7% YoY, deposits all-time high → "17-18%" matches |
| 4 | verified | July-2022 CPI expectations: headline ~8.7% vs prior 9.1%, core ~6.1% vs 5.9%; actual 8.5%/5.9% (softer) |
| 5 | verified | Nifty closed 24,718.60 on 13-Jun-2025 → 23,000 put exactly 1,700 pts OTM; 19-Jun weekly expiry = 4 sessions later; premium level plausible (not independently reported) |
| 6 | corrected | HDFC Bank fell ~7.4%/₹130 (3-Jul high ~1,757 → 12-Jul low ~1,627 real) ahead of 17-Jul-2023 Q1 results; claim's ₹120/8% slightly low |
| 7 | corrected | 20-Dec-2023: Nifty −506 pts (21,593→21,087), Bank Nifty −963 pts (48,166→47,203) from index data; ~500/~1,000 confirmed, mid/small ~5% plausible but exact % unconfirmed |
| 8 | corrected | Abrdn exited HDFC AMC 20-Jun-2023 for ₹4,079 cr (claim's 3,920–4,000 slightly low); SBI MF buyer confirmed (2.9%→6.9%); daily FII −1,942/DII +1,972 consistent, not confirmed separately |
| 9 | verified | Infosys Q4FY23 weak (13-Apr-2023), shares −9%/ADR ~−10%; TCS soft too |
| 10 | corrected | Dow 13 consecutive up-sessions ending 26–27-Jul-2023, longest since 1987 (record 14 in 1897); the "26-Jul" detail is accurate to within a session (streak reached 13 at 27-Jul close) |

## Data quality notes
- Yahoo Finance prices are split/bonus-adjusted (NVDA 1:10 Jun-2024, Kotak 1:5, HDFC Bank 2:1); percentage moves and real-price reconstructions noted per claim.
- Google News RSS returns wrapped redirect URLs; titles + publisher + date captured as evidence, with canonical source names cited.
- Where a specific tick price or daily FII/DII figure could not be independently confirmed, the claim was marked accordingly rather than guessed.

## Residual risks
- Claim 5's exact ₹5.56 premium and claim 8's exact daily FII/DII totals are terminal-data items not published in news; plausible and internally consistent but not independently confirmable.
- Claim 7's mid/small-cap ~5% intraday figure rests on that day's broad-selloff headlines, not an exact index print.