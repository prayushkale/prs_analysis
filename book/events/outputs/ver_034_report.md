# Verification Report — batch 034

**Task:** Fact-verification of 10 market claims (2018–2026) against web sources for the "Dhanraj" book.
**Method:** Google News RSS search (publisher headlines with dates), Bing web search, direct article fetches. No `web_search` tool in this fork — used curl-based search instead (network verified working).
**Result:** 10/10 claims adjudicated: **4 verified, 6 corrected, 0 wrong, 0 unverifiable**.

| # | Claim (short) | Verdict | Key correction |
|---|---|---|---|
| 1 | Iran fired drones/missiles at Jordan + Gulf states, 10-Jun-2026 | ✅ verified | Event confirmed (AP, ISW, Reuters, 10-Jun-2026); exact 12:45 PM IST time unconfirmed |
| 2 | Trump 10% tariffs on EU nations, 25% threat, Jan-2026 | ⚠️ corrected | 19-Jan-2026 US-EU tariff row (Greenland) confirmed, Nifty <25,600, Sensex −324; "10% already raised on certain EU nations" unverified as same-day action; 25% matches May-2026 EU auto tariffs |
| 3 | DeepSeek triggered chip/AI selloff ("~3-4 months before Feb-2026") | ⚠️ corrected | DeepSeek selloff was **27–28 Jan 2025** (Nvidia −$589–600B, record mcap loss), not late-2025; separate DeepSeek chip selloff 7-Jul-2026 post-dates transcript |
| 4 | NDA wins 2024 election (3rd term); June series Nifty +1500 / Bank Nifty +4000 | ✅ verified | Nifty +~1,480 closes (22,530→24,010) = "~1,500" within rounding; highest post-election monthly gain; 24,000 reached 28-Jun-2024 |
| 5 | US regional/mid-sized bank collapse, early 2023, contagion | ✅ verified | SVB + Signature failed 10–12 Mar 2023, First Republic May 2023; 20–25%+ single-session regional drops consistent with reporting |
| 6 | SC power tariff order, week of Oct-29-2018; power stocks +5–15% | ⚠️ corrected | Rally confirmed (Tata Power, CESC, Adani Power up to ~16%, Business Standard) but date is **12-Oct-2018**, ~2 weeks early |
| 7 | Adani ASM + margin hike 25%→50%, Feb-2023 | ⚠️ corrected | ASM for Adani Ent./Ports/Ambuja confirmed (2–6 Feb 2023); Adani Ports on F&O ban list 3-Feb-2023; exact 25%→50% margin figures unverified → use hedged phrasing |
| 8 | Gold import duty +9%, night of 12-May-2026 | ✅ verified | Duty rose **6%→15% (+9 pp)** 12–13 May 2026 (forex/rupee motive); "fuel prices" aside = likely ASR garble |
| 9 | BoB ₹3,400 cr loss "worst in history", stock +25% next day | ⚠️ corrected | Loss was **₹3,102 cr**, announced **25-May-2018**; "worst in history" hyperbole; +25% next-day move unconfirmed |
| 10 | Feb-2025: 8 red candles; Sep-Oct 2025: 9 red candles (worse) | ⚠️ corrected | Feb-2025 = 8 sessions (worst in 29 yrs, ~₹94L cr wiped); Sep-2025 = **8 sessions** (broken 1-Oct-2025), NOT 9 — equal, not worse |

## Verification details

**Claim 1 (verified)** — AP News, 10-Jun-2026: "US launches new strikes on Iran, which fires back at Gulf states and Jordan." ISW "Iran Update Special Report, June 10, 2026." Reuters same day: "US, Iran exchange attacks as Trump threatens further escalation." Jordan intercepting "7 missiles, 6 drones from Iran" (Anadolu/Al-Monitor, 24-Jul-2026) confirms the missiles/drones modality. The specific intraday timestamp from the transcript (12:45 PM IST) is not independently confirmable.

**Claim 2 (corrected)** — TOI, 19-Jan-2026: "Nifty50 ends below 25,600; BSE Sensex down over 300 points as Trump tariff fears spook markets." Second TOI piece: "Indian markets retreat on US-EU trade war over Greenland issue: Sensex falls 324 points." Thus the Jan-2026 date and the tariff-fear market impact are confirmed, with the row tied to the Greenland/EU dispute. The claim's "10% already raised on certain European nations" could not be confirmed as an implemented 19-Jan-2026 measure (a 10% global levy existed in 2026 per Budget Lab; the 25% figure corresponds to the May-2026 EU auto tariff round). The speaker's recollection is directionally right but the specific tariff details are unreliable.

**Claim 3 (corrected)** — The DeepSeek selloff is a real and major event but dated **27–28 Jan 2025** (NBC: Nvidia −$600B; Reuters: "DeepSeek sparks AI stock selloff; Nvidia posts record market-cap loss"; Bloomberg: −$589B). The speaker's "3-4 months before Feb 2026" is a memory error; the event was ~13 months earlier. A separate DeepSeek-related chip selloff (18 Jan... 7 Jul 2026, NDTV Profit) post-dates the transcript and should not be conflated.

**Claim 4 (verified)** — Livemint 9-Jul-2024: "Nifty 50 logs highest monthly gain post-Lok Sabha election result"; Livemint 29-Jun-2024: Nifty's 1,000-point surge to 24,000 in record 17 sessions. Third Modi/NDA term confirmed (Jun 2024). Closing-basis Nifty move ≈ +1,480 points — "more than 1500" is within roundoff of a speaker citing the series swing; Bank Nifty ≈ +3,900–4,000 similar. Fine for the book with "~1,500" phrasing.

**Claim 5 (verified)** — Reuters 13-Mar-2023 confirms SVB failure/backstop; CNBC 13-Mar-2023 covers SVB + Signature; CFI documents First Republic (May 2023). Regional bank contagion with 20–25%+ single-day plunges (e.g., mid-cap regionals) is consistent with contemporaneous reporting (KRE index, PacWest/Western Alliance moves). Verified.

**Claim 6 (corrected)** — Business Standard, 12-Oct-2018: "Power stocks rally; Tata Power, CESC, Adani Power gain up to 16%." The rally magnitude matches the claim (5–15%); the date does not (12-Oct vs "week of Oct 29"). The SC-order attribution was the standard reporting frame of that rally (SC tariff-clearance), but since the retrieved headline alone doesn't prove it, the book should say "on Supreme Court tariff-related clarity reported in mid-October 2018."

**Claim 7 (corrected)** — Livemint/Indian Express 2-Feb-2023 + NDTV Profit 6-Feb-2023 confirm ASM on Adani Enterprises, Adani Ports, Ambuja Cement. Moneycontrol 3-Feb-2023 confirms Adani Ports on the F&O ban list. The precise "Adani Enterprises margin 25%→50%" figures with the ~doubling are widely reported for the Feb-2023 episode but could not be pinned to a single retrieved source; recommend "margin requirements were sharply raised (approximately doubled)" in the book.

**Claim 8 (verified)** — Indian Express/Rediff/Moneycontrol, 13-May-2026: gold & silver import duty hiked to **15%** (from 6% → +9 percentage points), announced the night of 12-May-2026, "in bid to secure forex" amid a declining rupee. Exactly +9% as the transcript claims. The transcript's "and potentially fuel prices" is a probable transcription garble (no fuel linkage in any source; concern was smuggling/imports).

**Claim 9 (corrected)** — Moneycontrol & TOI, 25-May-2018: "Bank of Baroda Q4 net loss at Rs 3,102 crore on jump in bad loan provisions." So: ₹3,102 cr (not ₹3,400 cr), May-2018 (not late 2018/early 2019). "Worst possible report in Indian corporate history" is rhetorical hyperbole. The next-day +25% share jump is a well-known pattern class (bank stocks rallying on kitchen-sink quarters — cf. Quartz "India's biggest banks are piling on the losses, and investors are loving it") but the specific +25% BoB move is not confirmed by retrieved sources; hedge it.

**Claim 10 (corrected)** — Reuters 28-Feb-2025: "Indian stocks' worst run in 29 years, wiping $1 trillion in wealth" (8 sessions ending 28-Feb-2025; India Today: ₹94 lakh crore/$1T gone). TOI & Outlook Money 30-Sep-2025: Nifty "8th straight session" in the red; ET 1-Oct-2025: "Nifty breaks 8-day losing streak." Therefore the Sep-2025 streak was 8 sessions, **not 9**. Both episodes were 8 sessions — the book's comparison line must be corrected to "equal to the February 2025 tariff-period streak, not worse."

## Sources used (all via Google News RSS / publisher, dates in headers)
- AP News, ISW, Reuters, NPR, BusinessLine (Iran/Gulf/Jordan, June 2026)
- The Times of India, The Budget Lab, Kuehne+Nagel, ABN AMRO, Al Jazeera, Fortune (US-EU tariffs 2026)
- NBC News, Reuters, Bloomberg, NDTV (DeepSeek/Nvidia 2025 & 2026)
- Livemint, Reuters (Nifty 2024 record rally)
- Reuters, CNBC, CFI (US bank failures 2023)
- Business Standard (power rally 12-Oct-2018)
- Livemint, Indian Express, Reuters, NDTV Profit, Moneycontrol (Adani ASM/ban list Feb-2023)
- Indian Express, Rediff MoneyWiz, Moneycontrol, World Gold Council, Reuters (gold duty May-2026)
- Moneycontrol, The Times of India, Quartz (BoB Q4 FY18)
- Reuters, India Today, ET, TOI, Outlook Money (losing streaks Feb-2025 / Sep-2025)

## Caveats
- No `web_search` tool in this fork; used Google News RSS via curl (publisher+date+URL) plus Bing. High-confidence on macro/headline events; some micro-details (exact intraday timestamps, one-day share reactions, precise margin percentages) could not be independently sourced and are flagged.
- Several Google News links are redirect wrappers (they resolve to the publisher article).
- All 10 claims written to `book/events/verified_batch_034.jsonl` in the required schema.