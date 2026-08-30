# Batch daily_091 Report — 25 transcripts (3142–3170), 3–19 June 2026

## Digest
- **Count**: 25/25 transcripts read in full; 25 valid JSON lines written to `book/analysis/batch_daily_091.jsonl`.
- **Period**: 3–19 June 2026 — 11 trading days (pre+post pairs; 3164 and 3160 not present in this batch range; 3148–3149 and 3164 belong to other batches).
- **Extraction totals**: 102 event claims (mostly `verify:true`), 53 transferable lessons, 99 leak strings logged.

## Most notable events in this batch (for verification queue)
1. **US–Iran deal arc dominates the fortnight**: helicopter strike near Hormuz (Jun 9-10) → deal in "final stages" (Jun 12) → Iranian-media confirmation mid-session Jun 12 (+300 short-covering rally) → signed Jun 17-18; Hormuz 60-day toll dispute unresolved; deal signing slated for Friday in Switzerland.
2. **AI-stock global correction**: Broadcom -12% (Jun 5); Nasdaq -6% Friday then +4% Monday then below Friday's low; claimed largest point fall in Nasdaq-100 history (~1,600 intraday, Jun 10); Samsung -6%/SK Hynix -8%; Korea+Taiwan market caps overtook India's; Nasdaq +32% in two months before the unwind.
3. **Policy arc**: US tariff on India +12.5% (Jun 3); G-Sec interest tax removed for FIIs (announced with Jun 5 RBI status-quo policy); FM promises further reforms (Jun 15-16); LTCG-cut rumours via unverified Twitter/broker channels caused violent swings; STT/spread critique (bid-ask 10-15 pts vs 0.5-1 earlier).
4. **India specifics**: Q4 GDP 7.8% vs 7.2% expected; Reliance -20%+ bear market, 50-week low, 10 of 12 sessions down; HDFC Bank -25% from January high; Adani overtook Ambani as Asia's richest; SIP stoppage ratio >100%; FIIs net sellers 11 consecutive months (March worst ~1.22 lakh crore), turned net buyers Jun 15-16 (~200 crore) before re-selling (-750 crore Jun 17).
5. **Corporate**: TCS near 10% lower circuit (Jun 3); Wipro -8%; Accenture -17/18% on weak guidance with Infosys ADR -9.6% (Jun 19); Tata Motors -8% on JLR ADR; HDFC Bank ex-dividend ₹13 over-adjusted; Reliance AGM filed Jio IPO DRHP; FTSE rebalancing whipsawed Bank Nifty ±200 in 20 minutes.
6. **Levels/technicals that carried the fortnight**: 23,300 broken five times before first close below 23,400 (Jun 5); double bottom 23,070; 23,000 max-OI put; recovery ladder 24,000 → 24,300 (50% Fib) → 24,800; VIX from >16 to <15; ATR compressed to ~110 points (tightest since Feb budget-STT shock).

## Data quality
- **ASR density**: high but systematic; the provided correction dictionary handled most (gif nifty→GIFT Nifty, RBA→RBI, FAA→FIIs, MSA rejic→MSCI rebalancing, bang nifty→Bank Nifty, shorter up→shot up, weeks→VIX). New garbles noted: "Edelter.exchange/Edelta.dex/Intel.exchange/Delta Data Exchange" (sponsor variants), "reddish and blue"→Radisson Blu, "HK high necks/SK Heinix"→SK Hynix, "foodsie/footsie"→FTSE, "Bihukar crew"→(garbled; context: governments can't tell everything openly), "ICSA/ICICI" consistent with dictionary, "Red Box India Global" (Twitter handle, uncertain spelling).
- **Numbers**: mostly plausible and internally consistent; a few speaker hyperboles flagged rather than silently trusted (e.g., NASDAQ "never fallen 1,500-1,600 points in history" — flagged verify; "gold fell more than 100%" is clearly a slip for ~1%+; "relays indices down around 200%" is a slip for -20%+; "76,000 put options" is a Sensex strike, fine).
- **Duplications**: pre-markets systematically recap prior-day post-markets (flagged via dup_flag on 3142, 3144, 3146, 3151, 3157, 3165, 3169 etc.); Adani-Ambani item appears in 3150+3151; G-Sec tax arc spans 3145→3147.
- **Leak hygiene**: 99 strings logged — speaker name variants (Pierre/Pia/P.F./P.S./PIR/PR Sundar), sponsor variants (Delta.Exchange and garbles), workshop CTAs (Chennai Jul 11-12, Radisson Blu Nungambakkam), personal trades (23,000→22,500 put shift, Sensex 76,000 puts, Reliance 1200PE, SGB/MCX hedge), wife/car/travel anecdotes, Twitter/"posted strategies" references. None of these entered summaries/lessons/quotes.

## Notes for compiler
- This fortnight is a dense primary source for **Part V (event playbook: two-session news repricing rule)**, **Part VI (2026 chronicle: Iran-deal rally + FII turn)**, **Part II (margin mechanics 3168; spread/liquidity critique 3155/3163)**, and **Part IV (calendar-spread margin worked example, 24,300 put calendar)**.
- Speaker's 2013 parallel (rupee crisis → multi-year stability) and "Nifty at 30K" series promise → flag for the medium-term outlook chapter.
- Distinctive recurring aphorisms captured: "amateurs open the market…", boy-who-cried-wolf (tiger) story, "first 30 minutes write off".
