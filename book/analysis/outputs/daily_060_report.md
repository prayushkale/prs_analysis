# Batch daily_060 Report — Pre/Post Market Reports, Apr 26 – May 15, 2024 (25 transcripts)

## Counts
- 25/25 transcripts read in full and analyzed (ids 2230, 2233–2241, 2243–2252, 2255–2260; two trading-holiday gaps: May 1, May 4-5 weekend, May 11-12 weekend).
- 61 event claims extracted (all with verify flags), 50 lessons, 77 identity/promo leak strings logged.
- JSONL written to `book/analysis/batch_daily_060.jsonl` — 25 records, schema-validated (id/date/type/summary/levels/events/lessons/quote/dup_flag/leaks).

## Most notable events captured (for the verification queue)
1. **Pre-election FII exodus**: FIIs sold >₹80,000cr Jan–Apr 2024; every May session was a selling session (~₹30,000cr in May to May 13); escalation days of ₹7,000cr (May 8, 9) unmatched by DIIs.
2. **Election-fear VIX regime**: India VIX 10→20+ over 13 consecutive up sessions; 52-week high on May 9 from a 52-week low 11 days prior; June-expiry straddles pricing a 6.5–7% move; Adani Enterprises June straddle ~20%.
3. **May 2024 round trip**: third consecutive 1,000-point Nifty fall-and-recovery (22,900→21,900→22,400); box theory 21,500/22,000–22,500/23,000; 50% retracement at ~22,300–22,400 held as resistance on May 15.
4. **Policy/rule shocks**: RBI draft project-finance guidelines (May 6) — PFC/REC/IRFC −8–12%, PSU bank index −3.5%; provision math (0.5%/2%/8–12% of net worth).
5. **"Amit Shah candles"**: Home Minister's May 13 TV remark marked the low; +450 points follow-through May 14; VIX first decline in 13 sessions May 14.
6. **Global contrast**: Dow 8 straight up days, Nasdaq record, UK FTSE ATH, DAX/CAC 52-week highs — while India fell on local election uncertainty ("FII-dependent, not data-dependent").
7. **Microstructure episodes**: Apr 30 Bank Nifty futures at ~100-point discount, 49,800CE ₹5→₹250→₹0 ("Jane Street kind of people" injections); HDFC Bank ex-dividend ₹19.55 with HNI dividend-tax arbitrage; Kotak JMD resignation drag; Bharat Forge −15%→+15% results whipsaw.
8. **Event-history claims**: 2009 result-day +20%, 2014 +1%, 2019 +0.5%, 2004 −25–30%; VIX >30 before 2014/2019 elections.

## Transferable lessons (feed Parts II, V, VI)
- Flow balance (FII sell vs DII buy) is the single best short-term regime gauge; unmatched FII selling produces free falls.
- India VIX mechanically embeds post-event expiry premiums — rising VIX pre-event is pricing, not panic.
- Binary-event playbook: nil positions into the event date, hedge portfolios with financed puts, trade only 1–2 day horizons, structure no-downside-risk strategies (butterflies).
- "Markets falling without a reason are the dangerous ones"; demand-supply needs no news; channels invent reasons.
- Expiry-day "injections" by large operators — book profits early, never fight machines.

## Data quality
- Raw-ASR .txt era (2024+): systematic errors consistent with the correction dictionary (GIFT/GIF Nifty, FIA→FII, Wix→VIX, Kotak variants, "Jane's Creek"→Jane Street, "IRDA"→IRFC, "Zippla"→Zomato context).
- Dates reliable (daily sequence); most numeric claims internally consistent across pre/post pairs (pre rehashes prior post — dup_flag set on ~9 pre-market records).
- P&L/position claims: none personal in this batch beyond generic friend anecdotes; no strategy P&L to verify.
- Leaks: Delta Exchange/Tradex sponsor lines in every transcript; outro boilerplate everywhere; one follower-count self-reference (2234); minor Tamil-proverb identity hints (2235, 2241); political figures appear only as market-reaction context (kept per policy as dated facts, opinion stripped).

## Verification priorities from this batch
High (specific, dated, book-relevant): FII ₹80k cr Jan–Apr 2024; VIX 10→20 (13 sessions) & 52-wk high May 9; RBI project-finance draft norms & PFC/REC/IRFC reaction; Amit Shah May 13 remark & market reaction; Apr 30 Bank Nifty futures discount episode; Apple $110bn buyback (+8% AH); GST ₹2 lakh crore record; 2004/2009/2014/2019 result-day moves; HDFC Bank ex-dividend & 50% retracement.
