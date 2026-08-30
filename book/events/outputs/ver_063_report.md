# Verification Report — batch 063 (10 claims)

**Method:** Web verification via Google News RSS (The Hindu, Al Jazeera, Reuters, CNBC, Moneycontrol, Business Standard, Livemint, Firstpost, India Briefing, Indian Express, Fortune, ABC/Guardian/AP/NBC), using the repo's existing `search.py` helper (Google News engine). Each claim given 2–3 targeted queries max.

## Result Summary

| idx | Verdict | Key correction |
|-----|---------|----------------|
| 1 | verified | Iran–Israel missile conflict (Mar 2026) confirmed: The Hindu "Iran sends missiles into Israel" (24 Mar 2026); Fortune/CNBC document the war and Trump's balking/postponement talk. |
| 2 | corrected | Quake (Noto, 1 Jan 2024) + tsunami warnings + Haneda JAL/coastguard collision (2 Jan 2024) all real; timing detail fixed — quake was New Year's Day, Japanese markets reopened 4 Jan 2024, not the "first trading day". |
| 3 | verified | Biden withdrew from the 2024 race on 21 Jul 2024 (Reuters/NBC/AP/Al Jazeera). Claim's internal 2024-04-22 date tag was a metadata error. |
| 4 | corrected | India–Mauritius DTAA protocol (8 Mar 2024) verified; treaty-text publication in Apr 2024 triggered FPI sell-offs (Indian Express). Exact "22,800 → 21,800 futures" levels not independently confirmed; ~1,000-pt correction window is consistent with early-2024 Nifty peak-to-trough. |
| 5 | verified | Feb 1, 2026 Budget crash (Sensex −1,550 pts, Nifty < 24,850) + Feb 3, 2026 trade-deal rally (+2.5%, Reuters/Hindu) both confirmed. |
| 6 | verified | 2021 budget day +4.7% (biggest gain); 2020 the prior >2% fall; Feb-2026 fall worst since 2020 but ~1.9% (<2%) — claim "only 2020 & 2021 >2% in last 10 years" holds. |
| 7 | verified | Fed 25 bp cut on 10 Dec 2025 confirmed (third cut of 2025); "slower pace ahead" supports hawkish-guidance risk. |
| 8 | corrected | April-2024 FPI selling on Mauritius treaty + Iran-Israel verified; single-session ~₹8,000 cr figure unconfirmed (April-total >₹5,200 cr confirmed; treat ₹8,000 cr as approximate). |
| 9 | verified | Five-state (MP/Raj/CG/Telangana/Mizoram) elections: final-phase polling ended 30 Nov 2023, exit polls 30 Nov evening, counting 3 Dec 2023 — as claimed. |
| 10 | verified | 9 Jul 2025 deadline passed without India deal; US tariffs resumed 1 Aug 2025 (India Briefing; CNBC roundup). |

**Tally: 7 verified, 3 corrected, 0 wrong, 0 unverifiable.**

## Notes for the book compiler
- Claims 4 and 8 share the same root event (Mauritius DTAA amendment, Mar–Apr 2024) — cite the Indian Express explainer for both.
- Claim 1's "Trump postponed a planned attack by 5 days" detail is reported but not independently confirmed; if printed, frame as "per reports at the time".
- Claim 6 should be printed with the 2021 +4.7% / 2020 fall figures as the supporting data.

## Output file
Results written to `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_063.jsonl` (10 lines, valid JSONL, schema-compliant).