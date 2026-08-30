# Chapter 27: The Regulator's Dilemma
Part: VII Predators & Protectors

## Source count
- Transcripts directly mapped: 59
- Unique IDs: 59

## Top themes
- system vs discretionary traders
- FII taxation treaty arbitrage
- margin unfairness to hedgers
- intraday leverage phase-out
- banker's guarantee loophole
- margin architecture reform
- inheritance tax mechanics
- business failure vs fraud
- option buyers vs sellers
- government policy shocks

## Key lessons
- [2767] Span margin equals maximum risk plus exposure margin; an option buyer pays only premium (max risk known) while a seller pays ~50,000 for a 10,000-rupee max-risk position - exposure margin is a policy choice, not a risk measure.
- [2767] India offers Nifty options to 5 years but stock options only 3 months with poor liquidity; long-dated stock options and futures would let investors earn premium on holdings, as US covered-call practice shows.
- [2756] Regulators release combined buyer-seller loss data; the honest question is what share of losers are option buyers versus sellers - pressure on sellers shrinks supply and raises premiums, hurting buyers more.
- [2767] If the goal is moving traders from short-dated frenzy to long-dated calm, penalize intraday daily (not just expiry days) and reward long tenure by removing the 9-month extra margin and exposure margin.
- [2205] When a promoted platform faces allegations, promoters should verify claims (speaker had his team check whether tradex offered RBI-prohibited forex products) and be ready to end the relationship.
- [0130] Settlement mechanics: T-day trade, T+1 funds/shares to broker/exchange, T+2 demat/money transfer; early pay-in avoids the shortfall but forfeits the auction-market rescue for short deliveries.
- [2748] Retail collateral rules cap net short exposure (500-crore rule), yet one foreign entity held ~45,000 crore of options - limits must apply at ultimate-beneficiary-owner level, not per entity.
- [2756] Bank Nifty with 12 stocks where four hold ~80% (HDFC Bank ~30%) can be moved by a 1,000-crore order in two names - index design itself enables manipulation; want 15+ stocks, max 10% each.
- [0585] Stop-loss-market orders are structurally dangerous near crowded strikes: when everyone's trigger fires at once, your fill lands wherever liquidity is - within the day's legal price band.
- [0080] Margin relief can seduce into over-sizing: four lots at 300-point risk recreates 1,200 points of exposure. Options trading is risk and position management, not strike selection.

## Strategies (if applicable)
- {"name": "Hedged short option (spread)", "construction": "Sell 10,000C / buy 10,200C (200pt); variants 300-400pt", "numbers": "~25,000-32,000 margin vs 80-90k naked; max risk = spread width", "best_regime": "any directional credit view", "adjustments": "roll wings as market trends", "risks": "max loss = width x lot; premium give-up"}
- {"name": "Short straddle with far wings", "construction": "Sell 9,500CE+9,500PE (July), buy 8,500PE+10,500CE (June weekly/next series)", "numbers": "margin ~45,000-55,000 after ~40-60k premium receivable; straddle premium >1,000 pts in July 2020", "best_regime": "high-IV months with distant wings affordable", "adjustments": "re-buy expired wings weekly", "risks": "gap through wings; weekly-wing rollover friction"}
- {"name": "ITM put calendar", "construction": "Sell 10,000PE current month, buy 10,000PE next month", "numbers": "margin <30,000", "best_regime": "neutral-to-mildly-bearish", "adjustments": "roll short leg at expiry", "risks": "fast rallies inflate long-leg decay loss"}
- {"name": "Weekly far-OTM short puts into expiry (illustrative)", "construction": "Sell ~1,000-point OTM index puts ~3 sessions before weekly expiry", "numbers": "14,000PE sold ~\u20b920 with Nifty ~15,000; even 12,150PE (3,000 points away) traded ~\u20b90.75-0.85", "best_regime": "elevated IV caused by margin-driven supply squeeze", "adjustments": "with intraday limits gone, pre-fund reversal legs; run fewer lots", "risks": "peak-margin penalty, gap-through-strike risk, one-day crashes exceed 1,000 points only in Lehman/COVID-class events"}
- {"name": "BTC short strangle (live demo)", "construction": "Sold BTC 68,000 call (~711 USDT, 100 contracts = 0.1 BTC, 25x leverage, margin ~273 USDT) and sold BTC 36,000 put (~255 USDT margin) for late-January expiry", "numbers": "Expecting BTC to stay between 36,000 and 68,000 dollars; combined margin ~528 USDT", "best_regime": "Range-bound high-IV crypto; one-month horizon", "adjustments": "Exchange-native take-profit and stop-loss settings due to 24-hour trading", "risks": "Full margin loss on a breach of either breakeven; exchange/counterparty risk; 0.05% fee drag"}

## Enhancement candidates
- Timeline table: the Jane Street episode (order, volumes impact, ban, settlement)
- 2x-leverage worked-example table; business-income vs capital-loss tax asymmetry case; AIF category comparison table
- Worked example: single-owner business vs partnership vs listed company - tax flow at each stage
- Full cost waterfall: where ₹1.8 lakh crore of losses went (STT, brokerage, exchange, GST, stamp duty) as a table
- three-outcome decision tree for policy cases and typical sector reaction to each

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0080
0125
0130
0134
0137
0150
0158
0250
0271
0285
0327
0385
0585
0657
0714
0747
0805
0873
0922
1074
1167
1176
1252
1335
1469
1506
1508
1539
1663
1665
