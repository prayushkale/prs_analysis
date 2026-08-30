# Chapter 8: Why Derivatives Exist
Part: III Options from First Principles

## Source count
- Transcripts directly mapped: 21
- Unique IDs: 21

## Top themes
- covered interest arbitrage
- probability and premium
- market structure facts
- futures vs cash market
- transaction-cost math
- collateral efficiency
- call-option-mechanics
- hedging with forwards
- what is a derivative
- hedging origin story

## Key lessons
- [0072] Resting limit orders far from spot can get filled by flash spikes; square off immediately - such dislocations vanish in seconds and cannot be systematically captured.
- [1074] Leverage needs (long via margin funding, short via SLB) already exist without stock futures - and SLB would pay lenders (mutual funds, hence retail) extra yield.
- [1238] Futures are settled daily via mark-to-market: the day's loser pays the exchange immediately and the winner receives - losses can be called in cash daily.
- [0297] Same directional view, three instruments: cash ties up full capital, futures one-third margin, options only premium with loss capped at premium paid.
- [0071] Futures gains are business income (expenses deductible); cash equity gets 10% LTCG / 15% STCG - pick the instrument with the tax profile you prefer.
- [0297] Instead of long futures, buy an in-the-money call; instead of short futures, buy an in-the-money put - similar payoff, strictly capped downside.
- [1187] Arbitrage: simultaneous buy/sell of the same asset across two markets at different prices; the gap is the profit with no directional risk.
- [1074] Index derivatives are structurally hard to manipulate; stock derivatives enable bear-raids, collateral-value attacks and expiry-day games.
- [0071] For large capital, long futures funded by pledged debt instruments beats cash buying: interest income exceeds the cost-of-carry premium.
- [0297] Stocks can crash 40-70% in a day (DHFL, Infibeam); option buyers' loss stays at premium while cash/futures holders take the full hit.

## Strategies (if applicable)
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Synthetic futures (long/short)", "construction": "Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs", "numbers": "Demo: June futures -222 vs synthetic -219 on a 222-point fall; cost base 7.5 lakh (futures) vs ~30,000 (synthetic) per lot at Nifty 10,000, lot 75", "best_regime": "Any directional view where collateral efficiency matters; far-month exposure", "adjustments": "Exit both legs together; unbalanced exit leaves a naked leg with higher margin", "risks": "Stock synthetics fail on deep-ITM liquidity; index only"}
- {"name": "Covered interest carry trade (1995 example)", "construction": "Borrow SGD at 3%, place INR NRNR deposit at 20%, hedge FX with a 3-year forward costing ~2%/yr", "numbers": "gross spread 17%; net ~15% riskless; 10 lakh -> ~17.5 lakh over 3 years", "best_regime": "large interest-rate differentials with hedged currency risk", "adjustments": "roll forward hedge; watch repatriation rules", "risks": "counterparty/country risk; hedge cost creep"}
- {"name": "ITM call instead of long futures", "construction": "Buy deep ITM call (e.g. SBI 200CE at Rs46 with spot 245, lot 3000) instead of 1 lot futures", "numbers": "Premium ~Rs1.38L vs futures margin ~Rs2.5L vs cash Rs7.35L; at 260: ~Rs45,000 gain all three; charges cash 1,684 / futures 174 / options 329", "best_regime": "Strong directional view with defined horizon; want futures-like exposure with capped risk", "adjustments": "Exit anytime before expiry; premium tracks underlying", "risks": "Max loss = premium paid; decay works against you if the move is delayed past expiry"}

## Enhancement candidates
- five-derivative-types table (forwards/futures/options/swaps/swaptions)
- Dojima Rice Exchange history sidebar
- Rollover calendar workflow
- cash vs futures feature-by-feature comparison table
- Tulip mania fact box (historians dispute extreme prices)

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0071
0072
0089
0182
0183
0185
0188
0189
0192
0209
0297
0426
0860
0910
1074
1187
1198
1212
1213
1232
1238
