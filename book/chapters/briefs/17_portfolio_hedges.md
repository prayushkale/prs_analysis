# Chapter 17: Portfolio Hedges
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 52
- Unique IDs: 52

## Top themes
- crude oil OMC inverse relation
- multi-strategy capital pools
- margin unfairness to hedgers
- futures vs options overlay
- margin architecture reform
- defined-risk construction
- stock lending & borrowing
- bank heavyweight weakness
- adjustments vs stop-loss
- SIP + pledging + hedging

## Key lessons
- [2767] Span margin equals maximum risk plus exposure margin; an option buyer pays only premium (max risk known) while a seller pays ~50,000 for a 10,000-rupee max-risk position - exposure margin is a policy choice, not a risk measure.
- [2767] India offers Nifty options to 5 years but stock options only 3 months with poor liquidity; long-dated stock options and futures would let investors earn premium on holdings, as US covered-call practice shows.
- [2780] Because the protected position cannot lose, you can ladder new collars every further 5% of market fall using debt-fund tranches (20% at -10%, then each -5%) - courage without conviction-destroying drawdowns.
- [2780] A collar funded by equal premiums (buy 25,000PE, sell 28,000CE on Dec-2026) gives zero downside and ~3,400 points of capped upside (~13-14% over ~17 months) - slightly better than FD with full protection.
- [2767] If the goal is moving traders from short-dated frenzy to long-dated calm, penalize intraday daily (not just expiry days) and reward long tenure by removing the 9-month extra margin and exposure margin.
- [2748] Retail collateral rules cap net short exposure (500-crore rule), yet one foreign entity held ~45,000 crore of options - limits must apply at ultimate-beneficiary-owner level, not per entity.
- [2780] India charges span + exposure + extra >9-month margin even on hedged ETF positions, where the US charges nothing for covered calls - friction that keeps zero-risk capital out of the market.
- [0132] Removing the protective long leg on expiry day converts your short into a naked position - margin and risk jump; close positions yourself rather than letting settlement decide.
- [2253] Betting-market polls must be read cautiously: money-weighted (one whale can skew), tiny sample vs actual electors, and thresholds may not match the majority mark (300 vs 272).
- [0132] Capital gates: avoid stock options without ~1 crore (adjustment margins), avoid option selling below ~10 lakh; stick to large-cap liquidity to stay clear of ban-list freezes.

## Strategies (if applicable)
- {"name": "Infosys earnings iron fly with financed wings", "construction": "Sell 650CE + 650PE (5 lots); buy 720CE + 580PE; sell 2x 750CE (10 lots) and 2x 550PE to finance the wings", "numbers": "650CE @31, 650PE @27.50, 720CE @7.35, 580PE @8.40, 750CE @4, 550PE @4.46; max profit ~Rs.3.58 lakh (~15%) if Infosys closes at 650; protection 710 up / 590 down", "best_regime": "Results eve with elevated implied volatility", "adjustments": "Exit after results or keep far wings with a stop-loss; watch volatility crush", "risks": "Beyond 750/550 the financing legs turn the risk unlimited again; overnight gap risk"}
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Futures + rolling short straddle on a long-term holding", "construction": "Long monthly future; sell ATM calls; convert to straddles; roll puts lower as market falls (1460->1440); add 1520C", "numbers": "entry 1422, May-2020 series; +159,186 total vs ~35-40k unhedged; margin <=5 lakh vs 15 lakh cash", "best_regime": "long-term bullish holding with two-way volatility", "adjustments": "square and re-strike puts on reversals; roll future at ~1 point cost in bearish tape", "risks": "gap risk on naked legs; assignment/roll slippage"}
- {"name": "Hedged short put", "construction": "Sell near put + buy a further-OTM put same expiry", "numbers": "Speaker example: sold 9400-put style positions; hedge put cuts margin drastically and caps loss", "best_regime": "Any short-put view; mandatory insurance", "adjustments": "Not advised live; know risk-reward before entry", "risks": "Unhedged version: margin cascade and uncapped gap risk"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}

## Enhancement candidates
- Timeline table: the Jane Street episode (order, volumes impact, ban, settlement)
- Box: converting 1:1, 1:2 odds into implied probabilities with the parlay formula
- Margin friction comparison: India ETF+collar vs US covered call
- Bitcoin call ratio spread payoff table with breakevens
- Trade-by-trade adjustment ladder diagram for the Reliance position

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0040
0061
0071
0078
0088
0091
0098
0104
0129
0132
0140
0143
0148
0155
0156
0165
0169
0230
0288
0320
0426
0538
0662
0709
0772
0799
0825
0879
0890
1186
