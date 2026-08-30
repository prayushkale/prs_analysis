# Batch daily_018 Report — 25 transcripts (25 Jan – 11 Feb 2022, post-market/pre-market reports)

## Counts
- Transcripts read in full: 25/25 (0804–0843, gap-free per batch list)
- JSONL written: `book/analysis/batch_daily_018.jsonl` — 25 valid lines, schema-checked, 25 unique ids
- Composition: 11 post_market, 13 pre_market, 0 weekly; all dated 2022-01-25 → 2022-02-11

## Period narrative (what this batch covers)
Union Budget 2022 window and the January–February 2022 FII-selling crisis: Nifty 16,836→17,800→17,100 whipsaw; record January FII cash selling (claimed 41,000+ cr, ~$6B); budget-day rally + fade; Meta's record ~$250B one-day market-cap loss (2–3 Feb); BoE back-to-back hike (3 Feb); RBI's dovish surprise (10 Feb) triggering a 2,000-pt Bank Nifty two-day rally; US CPI 7.5% (10 Feb, highest since 1982) and the 11 Feb overreaction day with a rare ~20-pt Nifty futures discount marking the bottom; first FII net-buy day since 11 Jan (+109 cr on 11 Feb). Adani Wilmar IPO/listing and Adani-over-Ambani richest-Asian news; LIC IPO filing news (₹75–80K cr) as the looming liquidity overhang; fake-Telegram-channel scam warning (7 Feb).

## Notable verifiable event claims (→ Phase 3 verification queue, highest value first)
1. US CPI Jan-2022 = 7.5%, highest since 1982; core +0.6% m/m (0838/0841/0843)
2. Meta −27% on 3 Feb 2022, largest ever one-day market-cap loss (claimed ~$250B; actual ~$232B — correction candidate)
3. RBI 10 Feb 2022: rates unchanged, accommodative stance, dovish tone → Bank Nifty +650 from low (0840); speaker's "20bp reverse-repo hike" expectation vs actual SDF +40bp — verify exact mechanics
4. BoE 3 Feb 2022: second consecutive hike, first back-to-back since 2004 (0821/0822)
5. US Q4-2021 GDP +6.9% (0808); Alphabet 20:1 split + after-hours +7% (0814); Amazon −8%→+15%, Snap −23%→+60% (0820/0822)
6. FII flow claims: 7,100 cr (25 Jan), 13,000 cr two days, 3,624 cr (31 Jan), 21–183 cr (1 Feb, data revision noted), streak "every session since 12 Jan", first buy 109 cr (11 Feb), Jan total "41,346 cr", FY22 "~1.75 lakh cr" — several figures likely need correction vs NSDL data (Jan 2022 FPI equity net ≈ 33–34K cr; SIP claim "20,000 cr/month" vs actual ~12,300 cr)
7. Lata Mangeshkar's passing (6 Feb) → Mumbai money/currency market closure + RBI policy timing claim (0829) — verify
8. Adani Wilmar IPO subscription (QIB ~6x final, retail 4x, HNI 56x, shareholders 33x) and listing/circuit behavior ("20% upper circuit" claimed — verify band); Adani becomes Asia's richest (8 Feb) (0833)
9. Bank of England + ECB meetings (3 Feb); Tata Sons extends N. Chandrasekaran 5 years (11 Feb) (0843)
10. 2018-Feb analog: Dow −10% in one day incl. after-hours; 2019 corporate-tax cut 30%→22% "Nirmala candle" precedent (0807/0832)

## Data quality
- ASR quality moderate; systematic corrections applied (Quattac→Kotak, pipecet/5pisar→5paisa, taxbeddy→TaxBuddy, Hrithik→heavyweight watchlist phrase, Latha Makeshkar→Lata Mangeshkar, weeks→VIX, Potag/Quatac→Kotak, "CSUN"→(?), "NICA"→Nykaa flagged uncertain)
- Numbers-dense era; index levels internally consistent across pre/post pairs (cross-checked 0806↔0807, 0817↔0819, 0820↔0821, 0834↔0840↔0843)
- `levels` convention used: fii_cr/dii_cr positive = net sell (₹ cr), negative = net buy
- dup_flags: 0817↔0819 (same FII/DI data revision), 0838↔0841 (CPI preview overlap), light Meta/CPI repetition across 0820–0822

## Recurring transferable lessons (for Part II/V/VI mapping)
- Event days = positioning days ("who blinks first"); true reaction comes the next session (result-day rule)
- Good news is bad news in a tightening cycle; news has no intrinsic value, interpretation does
- Basket selling at the European 1:30pm open; late-session (professionals') selling as institutional signal
- VIX regimes: US VIX >30 danger, <25 comfort; falling VIX on red days = limited downside; futures-at-discount extremes mark bottoms
- FII selling absorbable while DIIs buy; both selling = fragility (31 Jan–7 Feb proof case)
- DII support floor ≈ monthly SIP/20 trading days (speaker's framework; figure needs correction)
- Option-seller's alignment: price direction + IV crush + time decay

## Leak log (all scrubbed from outputs; only flagged in `leaks`)
- Name variants: "P. R. Sunder", "PR Sunder", "P R Sunder", "Mr. Sundar", self-reference "no matter what Mr. Sundar says"
- Sponsors: 5paisa (pipecet/pi pisar/5pisar), Delta Exchange, TaxBuddy (taxbyd/taxbeddy), Finbingo (twin bingo/free in bingo/spinbingo/windbingo)
- Personal: live P&L claims (84 lakh/1.25–1.3 cr day; 2 cr in 2 sessions), capital disclosure (20–25 cr), "three-four accounts", Adani Wilmar allotment (65 shares x2 accounts), Hero MotoCorp 3,000 shares, ITC/Adani positions, Benz GLS quip, "time to go for party", son "Ashwin" + "richest person in Chennai", "Tamil guy" pride remark, "my father was a playboy" joke, workshop ₹5,000–60,000 mentions, "not SEBI registered", fake-Telegram warning (self-referential but scam-relevant → genericize for Part VII), "open letter to FM" video promos, Twitter/live-video refs, job-offer joke, Kalanidhi Maran anecdote (public figure — trim to fact)

## Residual risks
- FII flow figures may diverge from NSDL final data (revision lag acknowledged in-source for 1–2 Feb); verification pass must reconcile
- "20% upper circuit" for Adani Wilmar and "SBI Mutual Fund IPO" claims unverified
- Two transcripts (0817/0819) cover the same session from different evenings — compiler must not double-count budget-day content
