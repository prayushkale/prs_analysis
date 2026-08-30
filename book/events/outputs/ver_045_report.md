# Verification Report — batch ver_045

Verdict summary for 10 claims (results in `book/events/verified_batch_045.jsonl`):

| idx | Verdict | Key correction / note |
|-----|---------|----------------------|
| 1 | unverifiable | Mar-2023: FII record-short index futures + Adani Ambuja $450m stake sale plausible (deleveraging documented via GQG block deals) but exact figures unconfirmable this run |
| 2 | corrected | 2026 war was **US–Iran (with Israel)**, not Indo-Pak; ceasefire/pause announced by Trump on **Apr 8, 2026** (verified); Nifty ~23,000–24,800 zone consistent, exact 24,000 close/range unconfirmed |
| 3 | corrected | 14.7% / 20.5M jobs figures are from the **May 8, 2020** BLS report (April data); Apr 3, 2020 release showed -701k jobs / 4.4%; Dow did not fall on May 8 |
| 4 | corrected | Khomeini **b. 17 May 1900 (alt. 1902), d. 3 Jun 1989** — ~77–79 in 1979, deceased; 'now 86' false |
| 5 | corrected | Kargil War May–Jul 1999 verified; market rose >30% after war (per Wikipedia); specific wartime ~5–6% fall unconfirmed |
| 6 | corrected | 2008: Nifty fell **~60–64% peak-to-trough** (Sensex -63%), NOT ~30%; ~30% better matches 2004 |
| 7 | corrected | Second wave (Apr–May 2021) low ~14,100–14,200; **7,000–8,000 was the Mar 2020 first-wave crash** (close 7,610.25 on 23 Mar 2020) |
| 8 | unverifiable | Jun 14, 2021 FPI-accounts-freeze episode (Albula/Cresta/APMS) real but no citable URL retrievable; ₹1.5 lakh crore figure unconfirmed |
| 9 | corrected | Farm-law repeal announced **19 Nov 2021** (bill passed 29 Nov 2021) verified; 'Nifty fell 500+ on 22 Nov' unconfirmed |
| 10 | verified | Powell's hawkish **Jackson Hole speech Aug 26, 2022** ('some pain ahead', rates high 'for some time') → sharp US equity selloff |

## Notes for the compiler
- Claims 1 and 8 are the weakest: if either appears in the book, further source retrieval is recommended before quoting numbers.
- C2's corrected framing matters for the 2026 chronicle chapter: the tranches conflate an "Indo-Pak war" reading with what was in fact the US–Iran (Strait of Hormuz) war of Feb–Apr 2026, with Pakistan acting as peace broker (proposed "Islamabad Accord").
- C3/C6/C7 are classic speaker-confusion corrections (release dates, crash magnitudes, COVID wave attribution) — use the corrected claims in the text.

## Method
- Engines available this run: Bing (mostly returned index pages for news queries), Wikipedia API/extracts (worked well), Wayback Machine CDX + archived pages (worked, later went temporarily offline), Stooq/BLS (bot-blocked). No native web_search tool in this subagent's toolset; all verification done via curl/python HTTP retrieval.
- Only claims with retrieved primary/secondary sources were marked verified; unconfirmed numbers were not guessed.