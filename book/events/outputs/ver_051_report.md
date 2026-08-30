# Verification Report — Batch 051

## Results summary (10 claims)

| idx | Verdict | Claim (short) |
|-----|---------|---------------|
| 1 | verified | Crude ~$98–99 with $100 psychological line for India (Mar 12, 2026) — Brent closed at $100 amid Iran/Hormuz tanker-strike crisis |
| 2 | corrected | India fell 12–14% from Jan-2026 high 26,400; US <5% — India side confirmed (12% from peak, high 26,373); S&P/Dow <5% but Nasdaq entered correction |
| 3 | verified | Bank Nifty futures swung ~40,250→41,750 (Sep 14, 2022) with Nifty >18,000 — spot range 40,289–41,627, Nifty closed 18,004; global crash was Sep-13 US CPI |
| 4 | verified | TCS swing low ~3,000, −25% from 4,000, buyback @ ₹4,500 — low 2,926, ~−25% from 52-wk high; ₹4,500 buyback documented (Oct 2022) |
| 5 | corrected | Dow 7th consecutive session fall — actual streak was 6 sessions (Sep 20–27), −1,885 pts (~6%), S&P broke June intraday low (confirmed) |
| 6 | corrected | FIIs bought 12 straight sessions >₹18,000 cr — April-2023 FPI buying confirmed but exact streak/amount and "Dow 9-of-10" unverified; Dow fell 4 straight May 1–4 |
| 7 | corrected | Reliance 2,600→2,350 (~10%), HDFC ~10%, 25% combined Nifty weight — Reliance ~−11% mid-2023 peak to Oct low; HDFC ~−8%; combined weight ~21–22% not 25% |
| 8 | corrected | Strong ICICI/Kotak/RBL Q2 FY24 results weekend Oct 14–15 — results strong (ICICI +14.5%, Kotak +24%, RBL +46%) but reported weekend was Oct 21–22, 2023 |
| 9 | verified | Nifty first CLOSE below 22,800 on Feb 21, 2025 (22,795.9); GIFT Nifty −200 Friday night unverified sub-element |
| 10 | verified | Feb 10, 2022 CPI (Thu) consensus ~7.2–7.3%, actual 7.5%; VIX ~20 on Feb 9 after >30 in late Jan |

## Method
- Primary sources: Google News RSS (TOI, Reuters, CNBC, Livemint, MarketWatch, HT, Business Today, Fortune India, ET, Upstox), plus
  **Yahoo Finance daily OHLC** (`yf.py`) for index/price claims (Nifty, Bank Nifty, Dow, S&P 500, VIX, TCS, Reliance, HDFC Bank, ICICI/Kotak/RBL).
- Verdict policy: `verified` = claim matches reputable sources within reasonable rounding; `corrected` = direction right but dates/numbers/weights off; unverifiable sub-elements flagged in notes, never guessed.
- Note on Reliance/HDFC Bank Yahoo prices: values are bonus-adjusted (2024 1:1 bonus); real traded prices are ~2× the displayed values — adjusted in corrected_claim.

## Confidence per verdict
- Verified (1, 3, 4, 9, 10): backed by both numeric price data and news headlines.
- Corrected (2, 5, 6, 7, 8): core direction confirmed; specific numbers/dates corrected with evidence.
- No claims marked wrong or unverifiable wholesale; 2 sub-elements flagged unverified (GIFT Nifty −200; FII 12-session/₹18,000 cr exact figures).