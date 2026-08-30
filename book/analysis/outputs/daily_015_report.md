# Batch daily_015 — Analysis Report (25 transcripts, Dec 3–21, 2021)

## Deliverable
- `book/analysis/batch_daily_015.jsonl` — 25 JSON lines, schema-complete, order verified against the task manifest.
- Coverage: 92 concrete event claims extracted (76 flagged verify=true), 100 identity/promo leak flags, 24 transferable lessons, 12 cleaned quotes.

## Batch content
Pre/post market report pairs spanning the December 2021 FII-selling crisis: Omicron whipsaw (early Dec), the 17,100/17,000 breaks (Dec 6–7), the V-shaped 600-pt recovery (Dec 8), the pre-Fed/CPI jitter week (Dec 13–16), the quadruple-witching breakdown (Dec 17), and the capitulation crash (Dec 20–21: Nifty 17,310→16,400; Bank Nifty 36,700→34,100) with the first stabilization attempt (Dec 21).

## Key recurring threads (for compiler)
1. **FII program selling as the market's single driver** — 16–20 consecutive sessions, ~₹1.37 lakh cr since Apr 1; speaker's "five reasons" parody; FPI-taxation thesis; rupee 76.23 as repatriation evidence; PM-VC/PE meeting ignored.
2. **Retail/DII absorption regime change** — demat +1.87 cr FY22-to-Oct, MF +1.91 cr accounts/10 months; Nov SIP-equity inflows ₹11,600 cr; "three rowdies" retail-alignment parable; IPO subscription flip (retail 4–5x, QIB zero: RateGain, Shriram Properties).
3. **Microstructure teachables** — max-OI strike flips (17000PE→17000CE); ATM put build-up as a range forecast (16800 box); gap-up-as-liquidity for sellers; 2:35pm basket orders; last-half-hour DII defense; VIX −7.5% on violent closes; premium collapse post-Fed; 17,500 straddle as month-range pricing.
4. **Capitulation anatomy** — blue chips −6–8% in two sessions, first >10% Nifty / >20% Bank Nifty breaks outside COVID/Lehman; 2004 as the last −30% year; "markets stabilize only after capitulation"; valuation floors (Tata Steel 4 P/E).
5. **Event playbook data points** — US CPI 6.8% (40-yr high) absorbed with Dow +200 ("factored in"); Fed taper doubling to $30bn; BoE hike; ECB taper; quadruple witching; Omicron headline cycle (WHO doubling warning, Netherlands lockdown, UK first death "with Omicron").
6. **Strategy footnotes** — 17500 short straddle @600 (Dec 3); ladder selling 17500→17100 calls into the fall; zero-cost Reliance collar (Jan 2400CE / 2500CE+2600CE / Dec 2700CE); cash-secured puts in private banks/Hero MotoCorp/PSU high-yielders; "sell calls into every 100-pt spike" survival rule.

## Anonymization queue (verbatim leaks passed to QA)
- Sponsors: taxbeddy.com, finbingo.com, 5paisa/5pcet/pipeisa variants, Delta Exchange — every file.
- Name variants: "P. R. Sunder", "PR Sunder", "P R Sunder", "P or Sundar".
- Luxury/self: Mercedes S-Class 8th-car announcement + car-jinx history (0726, 0740); "not a SEBI registered analyst" (0724); Adani-trolling P&L defense (0724); Ramakrishna Mission College anecdote (0725); friend "Jagan" (0740); Chennai builder story with city + CM-bribe detail (0724 — keep lesson, strip identifiers); Twitter/"my followers" framing throughout.
- Political passages to drop per policy: BJP-vs-Congress market-behavior comparison (0732).
- Tone fix: "markets are like women" analogy (0720) — replace.

## Data quality
- Transcripts are clean human-edited docx-era text (not raw ASR); occasional speaker self-corrections and one truncated line (0723 tail) — no data loss impact.
- Speaker's own numeric slips to treat cautiously: Oct (25k)/Nov (40k) MTD figures vs 0713's ~85k two-month claim; "14 sessions" vs 15 on Dec 15; corporate-tax cut quoted as "30→20%" (actual 30→22%). All such figures cross-checked against adjacent dates in the JSONL `verify` flags.
- Dated claims needing web verification (priority): Dec-2021 FII daily/MTM figures, US CPI 6.8% print (Dec 10), Fed taper $30bn (Dec 15), BoE hike (Dec 16), WHO Omicron doubling guidance, Netherlands lockdown, Evergrande default, Star Health 79% subscription, demat/MF account statistics, IIP 3.2%, Nov CPI 4.91%.

## Residual risks
- Two near-duplicate pairs (0716/0717; 0729/0731) carry overlapping stats — flagged in `dup_flag` for the compiler to dedupe.
- Speaker-estimated FII figures pending at recording time (0712 ">5000", 0738 "~3000+") are marked verify=false where not confirmed in-file.
