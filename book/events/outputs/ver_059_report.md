# Verification Report — ver_059

**Output file:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_059.jsonl` (10/10 claims, valid JSONL, one per claim)

**Method:** Web verification via Google News RSS (publisher titles + publication dates as evidence) and targeted queries per claim (2–4 queries each). Primary sources preferred: CNBC, Reuters, Livemint, Business Standard, TOI, Groww. Specificity note: several claims assert precise intraday/percentage figures (e.g., a 400-point Nasdaq-100 swing, ₹6,200 crore daily FII sell, Wipro ADR −8.5%, Infosys ADR +3%) that could not be confirmed from accessible sources → verdict **unverifiable**, with directional context where available.

## Verdict summary

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | Nasdaq 100 swung >400 pts on quadruple-witching day 15-Sep-2023 | **unverifiable** |
| 2 | S&P moved >3% on CPI days ~6 months through 2022; benign CPI sparked >5% rally | **corrected** |
| 3 | Crypto fell ~10% (20-Sep-2021) on US stablecoin regulation reports | **corrected** |
| 4 | HDFC Bank Q4 (17-Apr-2021) slightly below expectations; TCS −5% then recovery | **verified** |
| 5 | Kotak/RBL/IDFC First/IDBI/Central Bank strong Q4FY23 over 30-Apr-2023 weekend | **corrected** |
| 6 | Kotak 31-May-2023 spike = MSCI forced buying | **unverifiable** |
| 7 | FIIs sold ~₹6,200 cr on 24-Feb-2025 | **unverifiable** |
| 8 | Nifty rallied ~300 pts on 5-Mar-2025 after ten down sessions | **corrected** |
| 9 | Wipro ADR −8.5%; Infosys ADR +3% (Jan-2022 results) | **unverifiable** |
| 10 | LIC IPO papers; size estimated ₹75,000–80,000 cr (~$10B) | **corrected** |

## Corrections applied (for the book compiler)

- **#2** → Verified core: S&P 500 +5.5% on 10-Nov-2022 (best day since 2020) after cooler CPI; 13-Sep-2022 −4.3% after hot CPI. The ">3% for six months" generalization fails (most other 2022 CPI days were smaller moves). Use: "CPI days drove sharp S&P 500 moves in late 2022 (−4.3% on 13 Sep; +5.5% on 10 Nov 2022)."
- **#3** → Crypto −10% on 20-Sep-2021 confirmed; attribution corrected to **Evergrande default fears / global risk-off** (US stablecoin regulation secondary at most).
- **#5** → Weekend + company list confirmed (Sat 29-Apr-2023 was the results day); soften "all strong" to per-bank framing.
- **#8** → Nifty +**254.65 pts** (Sensex +740.30) on 5-Mar-2025 per Groww closing report; the "ten consecutive down sessions" prior streak not confirmed.
- **#10** → LIC DRHP filed mid-Feb-2022 confirmed (India's biggest IPO); contemporaneous size estimates clustered ₹60,000–70,000 cr (≈$8–10B; some floated up to ~₹75,000 cr) — not a firm ₹75–80,000 cr; actual offer ~₹21,008 cr at ₹902–949 band, opened 4-May-2022.

## Residual risks
- Search-engine/bot restrictions limited access to primary page bodies; evidence URLs are Google News RSS canonical links (title + date + publisher provenance) rather than publisher page URLs.
- Granular intraday/percentage claims (#1, #6, #7, #9) remain unverifiable — recommend hedging or dropping the specific numbers in the book rather than asserting them.
- The environment's news index skews to 2026 content, making strict historical (2021–2025) article discovery harder; corroboration is strongest where the feed returned articles with exact matching publication dates.