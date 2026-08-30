# Verification Report — Batch 054

**Task:** Verify 10 market/policy claims against web sources for a book on Indian stock markets (2018–2026).
**Timestamp:** 2026-08-30 (UTC)
**Methods:** Google News RSS (hl=en-IN, IN region) headline retrieval with publication dates; Yahoo Finance daily OHLC API for Nifty (^NSEI), Bank Nifty (^NSEBANK), Nifty Auto (^CNXAUTO) index history; Wikipedia API; local corpus cross-check (book/corpus/, book/analysis/ JSONL) to ground dates of speaker-specific claims.

## Summary

| # | Claim | Verdict |
|---|-------|---------|
| 1 | 2023 state elections → ~15% rally | **corrected** |
| 2 | SVB collapse, Nifty broke 17,000 (Mar 2023) | **verified** |
| 3 | Iran drones Saudi/UAE + Pakistan relay (May 2026) | **verified** |
| 4 | SEBI F&O measures ~Oct 1, 2024 | **verified** |
| 5 | SEBI cut options volume ~50% (Oct 2024→Jan 2025) | **corrected** |
| 6 | 50% cash component + 2% ELM expiry-day (Nov 2024) | **corrected** |
| 7 | Oct 2024 correction 26,300→21,750, below 22,000 | **corrected** |
| 8 | Israel war Apr 2024, ~1,000–1,100 pt total fall | **verified** |
| 9 | GST cut cars → Oct 2025 auto rally 10–12%, Nifty 26K | **corrected** |
| 10 | Budget Feb 1, 2025: ₹12 lakh nil tax, ₹60k rebate, CG excluded | **verified** |

**Verdict distribution:** 5 verified, 5 corrected, 0 wrong, 0 unverifiable.

## Per-claim details

### 1. 2023 state-election rally — corrected
- Confirmed: 5 states voted Nov 7–30, 2023; results Dec 3, 2023; BJP swept Rajasthan, MP, Chhattisgarh (Reuters Dec 3, 2023; DW Dec 3, 2023).
- Nifty data (Yahoo Finance): closed 20,133 on Nov 30; +1.9% on Dec 4 (first session after results); window high 22,298 on Feb 23, 2024 → **+10.8%** from Nov 30, not ~15%. (≈18% only if measured from the Oct-26, 2023 low.)
- Correction: rally was ~10–12% from pre-results close to the Feb-2024 high.

### 2. Silicon Valley Bank / March 2023 — verified
- SVB failed Mar 10, 2023 (third-largest US bank failure at the time); Signature Bank followed; contagion narrative "contained" by US authorities but spread globally.
- Nifty data: intraday lows 16,828–16,987 between Mar 14 and Mar 20; **closed below 17,000 on Mar 15 (16,972), Mar 16 (16,986), Mar 20 (16,988)**.
- Bank Nifty fell ~6.4% (41,257 close Mar 9 → 38,613 low Mar 16). Claim text truncated at "~80" (likely ~800+); actual fall was larger (~2,600 pts).
- Verdict: verified; note the truncation and that the Bank Nifty fall was larger than implied.

### 3. Iran drones & Pakistan peace relay (May 2026) — verified
- Reuters (May 17, 2026): "UAE and Saudi Arabia report drone incidents as Iran war deadlock drags on."
- DW / Asharq Al-Awsat / Al Jazeera (May 18, 2026): Iran sent a (revised) peace proposal to the US **via mediator Pakistan**.
- Reported drone counts ("six, three each") not independently confirmed; the events themselves are verified.

### 4. SEBI F&O measures (Oct 1, 2024) — verified
- Reuters (Oct 1, 2024): "India tightens rules for booming equity derivatives market."
- ET (Oct 1, 2024): "Sebi announces 6-step framework…"; TOI (Oct 2); ICICI Direct (Oct 8); Indian Express (Nov 19) confirms the Nov 20, 2024 implementation date for the bulk of measures (weekly-expiry rationalization, lot sizes, margin/monitoring rules).

### 5. Options volume decline ~50% — corrected
- Direction verified: ET (Aug 2026) "Options volumes crash over 50% in FY26 after Sebi's strict rules"; NDTV Profit (Mar 4, 2025) "F&O Trade Slows Down From December High"; ET (Mar 5, 2025) "Sebi's F&O cleanup takes 20% retail option traders away."
- The specific figures (₹4 lakh cr/month in Oct 2024 → <₹2 lakh cr by Jan 2025) could not be confirmed from the sources retrieved; the ~50% order of magnitude within the Oct-2024–early-2025 window is plausible and directionally supported.
- Correction: keep the ~50% direction; avoid unverified month-level crore figures.

### 6. 50% cash component + 2% ELM — corrected (mis-dated bundle)
- Verified: additional **2% extreme-loss margin on expiry-day index-option positions** effective **Nov 20, 2024** as part of the Oct-1-2024 SEBI framework (speaker's own transcript id 2448 dated 2024-11-21 matches this; Livemint, Nov 21, 2024 "Sebi margin rule on option sellers more bite than bark").
- The **50% cash-margin component** is a separate, earlier measure: the speaker's own "SEBI'S 50/50 Rule" video (corpus id 1665) is dated **2023-05-13**. It is not part of the Nov-2024 framework.
- Correction: present the two measures separately with their correct dates.

### 7. Oct 2024 correction — corrected (conflates two legs)
- ATH 26,277 (Sep 27, 2024). Leg 1 (Oct–Nov 2024): low 23,263 (Nov 21, 2024). Leg 2 (Feb–Mar 2025): low **21,965 on Mar 4, 2025** — the only reading below 22,000 in the window; never 21,750.
- Correction: two-leg structure, peak-to-through ~16%; not a single Oct-2024 fall to 21,750.

### 8. Israel war / April 2024 — verified
- Nifty: Apr 10 high 22,776 → Apr 19 low 21,778 ≈ **998 points (~4.4%)**. Iran's first direct attack on Israel (Apr 13–14, 2024) drove the selloff; India–Mauritius tax-treaty tightening (amending protocol, Apr 2024) coincided (Lexology, May 28, 2024).
- Claimed "1,000–1,100 point total decline" matches the data.

### 9. GST 2.0 & Oct 2025 — corrected
- Verified: GST Council (Sept 3–4, 2025) rationalized car rates; price cuts effective Oct 1, 2025; record Oct PV sales **5.57 lakh units**, 2W retail **+52%** (FADA via ET Auto, Nov 7, 2025). Nifty Oct 2025 range 24,606→26,104 (≈1,500 pts); 26,000 crossed Oct 21–29, 2025.
- Not supported: "auto index +10–12%" — Nifty Auto rose ~4.2% intra-month (Oct 9 low → Oct 23 high); ~17–19% only from the Aug-1 low to Sep/Oct highs.
- Correction: keep the verified market facts; fix the auto-index % (≈4% intra-Oct; ~17–19% off the early-Aug low).

### 10. Budget Feb 1, 2025 — verified
- BS and India Today (both Feb 1, 2025): new-regime income up to ₹12 lakh became tax-free (FY2025-26) via a **₹60,000 rebate** under section 87A.
- Capital gains (short-term u/s 111A, long-term u/s 112A) are special-rate income and are **not** eligible for the 87A rebate — confirmed by later coverage (Upstox, Jan 2026; "exclusion from 87A rebate hurt… MF investors").
- Claim substance accurate.

## Tools/data used
- Google News RSS: `https://news.google.com/rss/search?q=...&hl=en-IN&gl=IN&ceid=IN:en` (headlines, publishers, pubDates).
- Yahoo Finance chart API: `query1.finance.yahoo.com/v8/finance/chart/^NSEI|^NSEBANK|^CNXAUTO` (daily OHLC).
- Wikipedia API (SVB collapse page exists/timestamps).
- Local corpus + analysis JSONL cross-checks (ids 1665, 2448; events/claims extraction).

## Caveats
- Google News RSS links are Google redirect URLs (stable; publisher pages may require JS).
- Some publishers behind paywalls; headline + date used as corroboration.
- For claim 5 exact monthly crore figures remain unverified; recommended to use "roughly half, reported >50% by FY26" phrasing in the book.
- For claim 3, exact drone counts unverified; recommended phrasing "drone incidents reported" rather than asserting counts.