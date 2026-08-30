# Batch daily_089 — Analysis Report (ids 3081–3111, 2026-03-27 → 2026-05-11)

## Deliverable
- **JSONL written (overwritten):** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_089.jsonl`
- 25 lines, one JSON per transcript, in manifest order. Schema-complete: id, date, type, summary, levels, events, lessons, quote, dup_flag, leaks. **100 event claims** (verify-flagged), 25 lessons, 11 distinctive quotes, leak logs on every line.

## Content digest
This batch is a continuous war-crisis narrative (fictionalized 2026 US–Iran conflict over the Strait of Hormuz) told through daily pre/post reports:

1. **Escalation (Mar 27 – Apr 6):** Trump deadline flip-flops; US breaks swing low; Iran attacks UAE/Kuwait; US fighter jet shot down (pilots rescued); crude $95→$126. India VIX ~27 vs inverted India>US VIX relationship. FII selling at records (₹1.2L cr March, ~₹8L cr since Jan 2024, ₹35,000 cr from HDFC Bank alone in 3 months).
2. **Ceasefire phase (Apr 8–22):** 15-day ceasefire (Iran confirms); 1,800-pt/4-day rally; technically-long signal at 24,000; Islamabad talks fail; US ship shoots Iranian cargo vessel; IRGC-vs-politicians split; expiry-day extreme premiums (₹8-9 for 4%-away strikes).
3. **Results season + tax shock (Apr 23–30):** HCL -10%; Infosys beats yet ADR falls (IT -25% from ATH vs Nifty -10%); Axis drags banks; ECL provisioning news (Apr 2027) sinks Bank Nifty ~1,000 pts; rare FII+DII double-sell day; STT +150% wrecks futures liquidity (10-20 pt spreads, synthetic-future migration, multi-year-low future premium).
4. **Coiling resolution (May 4–11):** month of ±200-pt daily reversals netting to zero (24,025 Apr 8 → 24,033 May 5); five-week 23,600–24,600 coil; 12:30pm 150-pt/10-min spikes; SBI ex-dividend discount mistaken for selling; PM's fuel-conservation advice; 3-4% breakout/breakdown imminent, breakout favored.

## Standout transferable lessons captured
- "Markets cannot take the uncertainty" (recurring thesis of the whole crisis).
- Futures premium as truth serum (low premium = genuine buying; premium spike into good news = short covering).
- VIX behavior reads: VIX-down-on-bad-news = priced in; VIX-up-on-green-close = binary event pricing.
- War-of-attrition physics: Iran's storage vs Asia's fuel reserves set the clock.
- Ex-dividend discounts masquerading as bearish futures pressure.
- STT-driven liquidity migration (spread widening, synthetic futures) as measurable tax damage.

## Data quality notes
- Heavy ASR garbling in this batch: "streets of farmers/Armas/our mass"→Strait of Hormuz; "FAA/FIA"→FIIs; "weeks/Bix"→VIX; "since sex"→Sensex; "RIGIC/regic"→rejig; "IC7/ICSA"→ICICI; "corruption added"→call OI added; "700%"→7% (Accenture). Corrections applied in interpretation; errors not echoed.
- One structural JSON bug (stray `"dup_flag":""` inside `lessons` arrays on 3 lines) was produced during writing and fixed; final file validates 25/25.
- **Self-audit found and fixed:** three May records were mislabeled against the manifest (3103/3104/3105 content shifted by one; actual 3103 content had been dropped). All relabeled, missing 3103 record reconstructed from the read transcript, dates aligned to manifest (3101 → 2026-04-30).

## Identity/promo leak log (highest-value items)
- Workshops: "workshop in Bengaluru by the end of this month... early bird offer of 60,000 rupees... contact our office... details in the description" (3104/3105, 3106, 3107).
- Location/travel trail: "went to my village for my temple festival" + "came to Chennai early morning 3 a.m." (3081); "traveling to US... settle down in Canada for about one and a half month" (3082); "at Great Canyon" (3086); "settled down in Canada Toronto" (3089); "near Vancouver" (3106/3107-era); Las Vegas/Grand Canyon (3087-3088).
- "Tamil channel" political-video plan (3105); sponsor garbles of Delta Exchange on every file; recurring "hope you enjoyed listening/watching" outros.
- Personal positions/P&L references (3086 firefighting losses; 3090/3099/3100 own option books) — kept as genericizable content per book policy, flagged in leaks.

## Verification priority (events likely for the book)
Highest-salience claims from this batch for Phase 3: FII cumulative selling ~₹8 lakh crore since Jan 2024; ₹1.2L-cr March 2026 monthly record; STT +150% effective April 1, 2026; RBI $100M bank forex-exposure cap and its backfire; ECL provisioning norms effective April 2027; SEBI Bank Nifty weightage rejig (75% of FII financial selling = HDFC+ICICI); Infosys out of top-10 market cap; Samsung $1T market cap; India VIX>US VIX inversion.
