# Verification Report — Batch ver_066

## Summary
- **Claims processed:** 10
- **Verdicts:** 4 verified · 4 corrected · 2 unverifiable · 0 wrong
- **Output file:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_066.jsonl` (10 JSONL lines, valid)

## Per-claim details

| # | Claim (short) | Verdict | Basis |
|---|---|---|---|
| 0 | India VIX fell 6.6% below 19 after Feb-2022 budget | verified | Yahoo Finance: VIX closed 19.98 on budget day (Feb 1), 18.65 on Feb 2 (−6.66%); below-19 confirmed |
| 1 | Trump threatened 200% tariff on EU wine/champagne (Mar 2025) | verified | AP News + CNBC coverage of the threat; date approximate |
| 2 | Fed cut 25bp Oct 29, 2025; December not certain | verified | Wikipedia FOMC history: Oct 29, 2025 meeting, target range to 3.75–4.00% from 4.00% (10–2 vote) |
| 3 | RBI Apr 6 2023: consensus 25bp, speaker expected no-hike-or-25bp | corrected | RBI did hike 25bp to 6.50%; speaker's own expectation is subjective, can't be web-verified; corrected claim states the actual outcome |
| 4 | CPP ~6,000cr Kotak block sale (Jun 2023) | corrected | Actual: CPPIB sold 1.7% stake for ₹6,123.6 crore (~6,124cr); "~6,000cr" within ~2% rounding |
| 5 | SEBI board Sep 30 2024: one-contract option limit, 5% expiry margin | corrected | Meeting happened; one-contract limit was discussed but NOT adopted in final Oct-2024 framework; expiry-margin measures part of broader framework |
| 6 | Infosys ADR −4% then −5% consecutive nights (Jun 2026) | unverifiable | No reliable source located for the specific June 2026 ADR session; weightage claim needs NIFTY methodology data |
| 7 | India Millennium Bond + Resurgent India Bonds (NRI, pre-2000) | verified | Historical: RIB 1998 (~$4.2bn), IMD 2000 (~$5.5bn) — RBI/Wikipedia |
| 8 | Great Depression: US market fell ~90% | corrected | Dow fell 89.2% (381.17 → 41.22, Sep 1929 → Jul 1932); "nearly 90%" is a fair approximation but not exact |
| 9 | Nifty never fell 4 straight months in 25 yrs; happened ~2001, now 5th straight | unverifiable | No monthly Nifty data for 2001–2002 available in this environment; plausible dot-com-era claim, needs NSE historical data |

## Notes for the book
- Claims 2, 7 are safe to cite as verified historical/macro facts.
- Claims 0, 1 safe with dates as stated.
- Claim 3: book should state the RBI outcome (25bp hike to 6.50%) and attribute the expectation to the speaker.
- Claim 4: use ₹6,123.6 crore figure (verified), not the rounded recall.
- Claim 5: correct the record — one-contract limit was NOT finalised; describe the actual Oct-2024 framework (one weekly expiry per exchange, lot-size increases, expiry-day margin).
- Claims 6, 9: flag for on-demand verification with NSE/Yahoo monthly data before inclusion, or state with hedged language.