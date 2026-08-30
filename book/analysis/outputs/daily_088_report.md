# Batch daily_088 Report — 25 transcripts, 5–25 March 2026 (Iran–US/Israel war crisis)

## Digest
- **Read:** 25/25 transcripts in full (ids 3053–3080, gaps = corpus numbering). All written to `book/analysis/batch_daily_088.jsonl` (25 valid JSON lines, order-verified).
- **Composition:** 13 post-market, 12 pre-market reports spanning the acute phase of the March 2026 Iran–Israel–US war and Hormuz crude crisis.
- **Narrative arc captured:** fake-news spike (+400 on Mar 5) → crude $110–120 panic, Nifty <23,000 (Mar 9–13) → 3-day rebound, FII selling slowing (Mar 16–18) → Qatar escalation + HDFC Bank chairman resignation shock (Mar 19) → sanctions-lift crude retreat → record FII selling >1 lakh crore, manipulation-suspect expiry-day rumor spike (Mar 24) → nonstop rally, futures-at-discount (Mar 25).

## Most notable events (queued for web verification)
1. Mar 5, 2026: Iran deputy-FM nuclear-concession rumor drove a ~400-pt last-20-min rally; Iran denied it as an old statement — flagged by speaker as likely manipulation.
2. Mar 9, 2026: Brent $110→$120 intraday; Nifty broke 24,000 intraday, closed above; auto −4%+, PSU banks −4%.
3. Mar 19, 2026: HDFC Bank part-time chairman resigned citing values misalignment; ADR −7.5%; GIFT −500.
4. Mar 24, 2026: ceasefire-talks rumor on 2–3 Indian channels only (absent from global wires) → expiry-day spike, 23,100 call 5→60; March FII selling >1 lakh crore (record).
5. Mar 25, 2026: US–Iran talks set for Friday in Pakistan; US war losses est. ~$12B incl. F-35 friendly fire; futures-at-discount rally, VIX flat.

## Data quality
- Levels/FII-DII flows consistently stated; captured in `levels` where explicit. Some numeric ASR garbles noted and marked (e.g., "shot up nearly 25300 points" on 3078 read as a rumor-day spike; Bank Nifty sector floor garbled on 3071 — recorded with uncertainty).
- Speaker's own trades captured in summaries/lessons where they teach structure (put ratio, straddle adjustments, far-put stop math) — genericized, no account identity.
- One hearsay item marked `verify:false` (Reliance Jio-IPO speculation; TCS AI-deal rumor).
- High-quality quote density: 10 distinctive quotes extracted; 2 lessons/file average.

## Anonymization
- Leaks logged per transcript: "sponsored by Delta Exchange" (all), name variants (Pierre Sundar, P.E.R./P.F./P.A./Pierre Sombre/P.S., PR Sundar), Mumbai/Chennai workshops + charity dinner + "dinner with Pierre Sundar", village-school charity reference, Dubai/US travel + "social media checked when traveling to US", YouTube interview, political asides (tax-regime/LIC, government-intervention commentary) flagged for genericization. No real name appears in the JSONL outside `leaks`.

## Notes for compiler
- This batch is a near-complete continuous chronicle of a full crisis cycle — strong candidate spine for Part VI (2026 chapter) and Part V event-playbook material (war + rumor dynamics, manipulation forensics, DII/FII absorption math, HDFC Bank idiosyncratic-shock case).
- Recurring ASR traps in this batch: "streets of farmers/Armas/Hormas" → Strait of Hormuz; "weeks" → VIX; "FIA" → FII; "Brent crew/crude" variants; "give newity/GIFNifty" → GIFT Nifty.
