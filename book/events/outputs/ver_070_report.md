# Verification Report — Batch 070

**Agent:** worker (delegated) · **Method:** Yahoo Finance historical closes (^NSEI, ^SPX, INR=X, PFC.NS, RELIANCE.NS, BHARTIARTL.NS, RANEHOLDIN.NS, ^INDIAVIX) + Bing News RSS (news search) + Business Standard article fetch. NSE/stooq block direct scraping; Yahoo + news RSS were the usable sources.

**Verdict summary:** verified 2 · corrected 6 · unverifiable 2 (of 10)

| # | Claim (short) | Date | Verdict | Key finding |
|---|---|---|---|---|
| 1 | Nifty 21.7K low → 26.4K high; fibs 24,600/24,100 | 2026-03-04 | corrected | Actual low 22,059/22,161 (7 Apr 2025); fibs ≈24,740/24,230. 24,600 zone was broken 4 Mar 2026 (close 24,480). |
| 2 | India VIX −13% post-budget; long-dated CE collapse | 2025-02-01 | verified | VIX 16.25→14.35 (3 Feb) = −11.7%; −15.8% by 7 Feb. Premium ticks unverifiable but direction plausible. |
| 3 | 25,000 PE (1d) at ₹26 vs usual 5–6 | 2024-09-19 | unverifiable | Context consistent (spot 25,377, ~378 OTM, VIX 13.37 pre-FOMC) but exact premium not publicly confirmable. |
| 4 | Jio stopped ₹200/250; RIL +160 pts; Airtel +20 | 2025-08-19 | corrected | Jio plan news verified (reported 209/249; base ~299). RIL +₹38.40 (+2.78%) ≈ 70–80 index pts, not 160. Airtel +17.4 ✓. |
| 5 | Rane 10–11% yield 2014–15; 2–3x in 3 yrs | 2022-06-21 | corrected | Rane Holdings ~2.2x (mid-2014→2017), ~6.8x by 2018. Yield figure unconfirmed. |
| 6 | PFC +4–5% on 3 Jan 2023 to ₹157 | 2023-01-03 | corrected | PFC actually +4.2% to ₹124.80 that day; ₹131 hit Mar-2023, ₹157 only Jun-2023. ≥10% PFC/REC yields plausible. |
| 7 | Puts 25,350/25,400 ₹8–10 → ₹200–250 | 2026-01-20 | verified | Breakdown verified (Nifty −353 pts to 25,232; news "Below 25,200"). Premium swing plausible; ticks unverifiable. |
| 8 | FII+DII flows vs Nifty +40/−80 (21–22 Jun 2023) | 2023-06-22 | unverifiable | Nifty moves match exactly (+40.15, −85.6). Daily FII/DII flows not retrievable; not guessed. |
| 9 | GST 1.72 → 1.89 lakh cr (Sep 2025) | 2025-10-07 | corrected | Sep-2025 GST = ₹1.89 lakh cr (+9.1%, released 1 Oct 2025) ✓; rate cuts effective 22 Sep ✓; "1.72" baseline unsubstantiated. |
| 10 | Nifty flat vs S&P +21–25%; rupee 82→88; 35% underperformance | 2025-10-28 | corrected | S&P +20.1% (5,738→6,891) ✓; rupee ~83.7→88.4 (+5.6%), not "82→88"; USD underperformance ≈27%, not 35%. |

**Method notes**
- NSE (nsearchives) returns HTTP 000 (blocks non-browser agents); Stooq requires JS proof-of-work + auth cookie that still returns "Access denied"; Bing web search returns generic index pages; **Bing News RSS + Yahoo chart API were the workhorses**.
- All corrected_claim fields contain only facts confirmed by the cited sources; nothing was guessed.
- Multi-part claims carry a single verdict at claim level; components are separated in notes/corrected_claim.

**Residual risks**
- Two "unverifiable" verdicts (claims 3, 8) reflect absence of public records, not contradiction.
- Claim 1's "~21,7xx" low may relate to a futures/GIFT reference the speaker used; the spot-index low is used in the correction.
- Option-premium precision claims (2, 7) verified at the market-move level only.