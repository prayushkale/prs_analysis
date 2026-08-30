# Verification Batch 037 — Report

**Task:** Fact-verification of 10 claims on Indian & global market events (2018–2026) using web sources.

## Methodology
- 25+ targeted web queries via Google News RSS + direct fetches (Wikipedia, CNBC, Business Standard, Reuters).
- Verdicts: `verified` / `corrected` / `wrong` / `unverifiable`, with 1-3 evidence sources per claim.
- No guessing: claims that could not be tied to reporting were marked accordingly; none were left `unverifiable` because all 10 mapped to documented coverage once ASR/date garbles were resolved.

## Results summary

| # | Claim subject | Verdict | Key correction |
|---|---|---|---|
| 1 | Iran-US conflict, Hormuz closure, crude $95→$107 (Apr 2026) | verified | — (Brent hit ≥$107 per multiple outlets) |
| 2 | FII FY21-22 outflow >₹2.5L cr, worst in history | corrected | True as of Apr-2022; FY26 later set a bigger record (SEBI annual report) |
| 3 | Nikkei crosses 40,000 first time in 40 yrs (Mar 2024) | verified | Actually the FIRST time ever; prior record ~38,957 (Dec 1989) |
| 4 | HDFC twins MSCI rejig → Bank Nifty ~1,000pt fall (May 2023) | verified | Date = 12 May 2023; twins sank 6%, biggest 1-day fall in 3 yrs |
| 5 | India MSCI EM weight 20% → 12% | verified | Peaked ~20% (2024) → below 14% → ~12% (2025-26) |
| 6 | SNB de-pegs CHF Jan 2015, ~40% surge, brokers bankrupt | verified | ~30-41% intraday at extremes; Alpari UK bankruptcy confirmed |
| 7 | 2025 tariff crash → recovery; Nifty ~8-9% for year | corrected | Actual CY2025 gain ~10% (10.0-10.5%) |
| 8 | Russia-Ukraine Feb 2022: Nifty gap -500, BankNifty -1,200 | verified | Matches Sensex -2,700 intraday, biggest crash in 2 years |
| 9 | Feb 2026: HDFC Bank broke 900; Reliance broke 1,400 | verified | Consistent with 2026 coverage; RIL ~12% off record ~1,612 |
| 10 | S&P swung ~6% around Sep-11-2024 CPI | corrected | No ~6% swing; S&P closed up ~1% near records |

## Notable patterns
- ASR corruption in source claims: "MSA Regic" → MSCI rejig; "streets of Armas" → Strait of Hormuz.
- Transcript date tags are *video dates*, not always the *event date* (e.g., SNB 2015 retrospect, HDFC-May-2023 retrospect) — the book should present event dates, not video dates.
- Speaker's recollections trend accurate on direction and magnitude; percentage precision (8-9% vs 10%) drifts — book should print verified numbers.

## Files written
- `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_037.jsonl` (10 records, one per claim)
- This report: `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_037_report.md`