# Batch 029 — Fact-Verification Report (10 claims)

**Model note:** Verification performed via web search (Google News RSS + publisher sources). All 10 claims processed; results written to `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_029.jsonl`.

## Summary of verdicts

| idx | Claim topic | Verdict | Key correction / note |
|-----|-------------|---------|----------------------|
| 1 | Dec 2023 state elections → Nifty +600-700 | **corrected** | BJP won 3 of 4 states (MP/Raj/Chhattisgarh). Dec 4, 2023 rally: Sensex +1,300 pts, Nifty +~383 pts (~1.9%) to record close ~20,686 — not 600-700. |
| 2 | Jun 12, 2026 US-Iran peace deal → Nifty rally, crude crash | **verified** | Deal framework confirmed (Guardian, Al Jazeera, Moneycontrol). Oil to 3-month low (~$83), GIFT Nifty +300 over 24,000. |
| 3 | Mar 2022 diesel +₹25/litre bulk buyers | **corrected** | Mar 22, 2022 retail petrol/diesel +₹10 after 137-day freeze; LPG +₹50. Bulk diesel buyers faced larger ~₹25/lt hike (record). |
| 4 | 2014 election → "Nifty 19,000→26,000" | **wrong** | Numbers belong to the Nov-2023→Sep-2025 rally. 2014-15: Nifty ~7,200-7,600→~9,100 (+20-25%). |
| 5 | Sep 2020 correction (Nifty 11,800→11,200; Tesla -21%...) | **verified** | Tesla -21% worst-ever day Sep 8, 2020 confirmed; Dow -650, Nasdaq correction, Nifty ~600-pt correction confirmed. Hedge exact Bank Nifty -3,000. |
| 6 | RBI ₹90 lakh penalty on Axis Bank (Nov 2023) | **verified** | Actual penalty ₹90.92 lakh; stock -3% on day; ~150-pt contribution to Bank Nifty fall. |
| 7 | Feb 2023 windfall tax hike (crude 1,090→5,050) | **corrected** | Hike confirmed (The Hindu). Prior rate was ₹1,900/tonne (not 1,090); new ₹5,050 (~2.6x); ATF 3.5→6.5/lt; diesel exports raised. |
| 8 | FII outflows ~₹4 lakh cr since Oct 2024 | **corrected** | 2025 worst-ever (₹1.58 lakh cr), 2026 resumed exodus ₹2.06 lakh cr by mid-year. Cumulative ~₹4 lakh cr plausible but hedge exact figure. |
| 9 | Trump H1B visa fee rattles Indian IT (Sep 2025) | **verified** | Proclamation imposing **$100,000 annual fee** per H-1B application ("$1.00" = ASR garble). Reuters/TOI/Al Jazeera. |
| 10 | Early Mar 2026 Iran-negotiation rumor → Nifty +400/-1,200 | **corrected** | 2026 Iran war + India selloffs confirmed (Nifty <23,850; Mar 11 Sensex -1,342). Specific +/-intraday anecdote unconfirmed → present as speaker recollection. |

## Distribution
- Verified: 3 (idx 2, 6, 9)
- Corrected: 6 (idx 1, 3, 5*, 7, 8, 10)
- Wrong: 1 (idx 4)
- Unverifiable: 0

(*idx 5 marked verified with a hedge note on one unconfirmed sub-figure.)

## Notes for the book pipeline
- **Claims 4, 7, 10** are the riskiest numerically (conflated eras, wrong prior rate, unconfirmable intraday specifics) — book text must use the corrected claims or hedge as speaker recollection.
- **Claims 1, 3, 8** are typical "rounding/compression" cases — use corrected numbers.
- **Claims 2, 6, 9** are cleanly verified — safe to cite directly.
- Publisher homepage URLs are used where Google News redirect links would break; verified content is standard, widely reported news.