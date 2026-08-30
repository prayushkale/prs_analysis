# Chapter 9: Calls and Puts
Part: III Options from First Principles

## Source count
- Transcripts directly mapped: 62
- Unique IDs: 62

## Top themes
- extraordinary dividend adjustment
- American vs European options
- stock lending and borrowing
- dividend capture arbitrage
- liquidity and trading bans
- margin architecture reform
- time decay proportionality
- profit booking psychology
- exchange product pipeline
- option strike adjustment

## Key lessons
- [2767] Span margin equals maximum risk plus exposure margin; an option buyer pays only premium (max risk known) while a seller pays ~50,000 for a 10,000-rupee max-risk position - exposure margin is a policy choice, not a risk measure.
- [2767] India offers Nifty options to 5 years but stock options only 3 months with poor liquidity; long-dated stock options and futures would let investors earn premium on holdings, as US covered-call practice shows.
- [2767] If the goal is moving traders from short-dated frenzy to long-dated calm, penalize intraday daily (not just expiry days) and reward long tenure by removing the 9-month extra margin and exposure margin.
- [0111] Time decay is proportional to remaining time: a one-week option loses ~20% of its value on day one, but ~100% on expiry day - expiry-day selling harvests decay that weekly sellers spread across days.
- [0111] India charges full span+exposure margin on covered calls against demat shares (no cash-F&O link); holding a long future instead cuts the short call's span to zero - only exposure margin applies.
- [0108] When a dividend exceeds 5% of market value, exchanges adjust option strikes (and premiums) on ex-date - the broker did not change anything; check corporate actions before trading stock options.
- [0111] Bond yields falling means older bonds trade at a premium (Bharat Bond 1 near 1080-1090 vs 1000 face); pledging older listed bonds can beat waiting for new issues to clear collateral approval.
- [0136] When FII ownership hits the sectoral cap, arbitrage breaks: the ADR can hold a 10% premium indefinitely because FIIs cannot buy more in India - so the premium is information, not free money.
- [0106] There is no safe strategy and no permanently fundamentally strong company - Reliance Communications/Infrastructure/Capital were once blue chips; understand risk and reward per strategy.
- [1131] A warrant is functionally a long-dated call: pay premium now, exercise at a fixed price until expiry, maximum loss capped at premium - but with issuer/liquidity risk and thin markets.

## Strategies (if applicable)
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "Cash Secured Put", "construction": "Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery", "numbers": "Bajaj Finance 1800PE sold at Rs.100 (2 lots, Rs.50,000 collected); Nifty Apr 7500PE ~Rs.57; Dec-2020 6000PE ~Rs.200; ~Rs.19 lakh premium collected; claimed Rs.45 lakh FY21 P&L in 3 weeks", "best_regime": "Sideways-to-up markets, or when you want a lower entry price in a quality stock", "adjustments": "Square off the put and buy shares in the open market instead of physical delivery; exit any time before expiry", "risks": "Profit capped at premium; stock can fall far below strike; requires full cash backing of the strike"}
- {"name": "OTM credit-sale adjustment on a losing ratio", "construction": "Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65", "numbers": "Pre-adjustment loss ~Rs 3,000; post-adjustment profit ~Rs 2,000 per lot", "best_regime": "After a results miss confirms the directional view is dead", "adjustments": "Collected credit exceeds the defined max loss; no further action needed unless stock reverses hard", "risks": "New short call adds upside risk; acceptable because view is now neutral-bearish"}
- {"name": "Synthetic futures (long/short)", "construction": "Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs", "numbers": "Demo: June futures -222 vs synthetic -219 on a 222-point fall; cost base 7.5 lakh (futures) vs ~30,000 (synthetic) per lot at Nifty 10,000, lot 75", "best_regime": "Any directional view where collateral efficiency matters; far-month exposure", "adjustments": "Exit both legs together; unbalanced exit leaves a naked leg with higher margin", "risks": "Stock synthetics fail on deep-ITM liquidity; index only"}
- {"name": "Collateral-funded option selling (HNI pattern)", "construction": "Pledge debt mutual funds/bank FDs as collateral; sell options against the margin; keep interest as primary return", "numbers": "Stated pattern: 6-7% interest on debt funds while trading on pledged limit", "best_regime": "Wealthy, income-focused sellers who accept trading as a bonus stream", "adjustments": "Not applicable - structural allocation", "risks": "Trading losses eat the collateral cushion; interest is not guaranteed against credit events"}

## Enhancement candidates
- Three-strike scenario table (expiry at -500/flat/+400) with payoffs and probabilities
- worked example of strike adjustment arithmetic after a special dividend
- Contract-spec table for the three index families
- Box: why positional stop-losses differ structurally in India vs US markets
- Payoff diagram for long put with insurance analogy table (deductible = intrinsic value gap)

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0003
0024
0025
0036
0052
0064
0068
0073
0089
0094
0100
0106
0108
0110
0111
0117
0121
0124
0132
0136
0145
0168
0188
0192
0195
0197
0198
0209
0219
0228
