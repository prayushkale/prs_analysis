# Chapter 10: The Greeks, Demystified
Part: III Options from First Principles

## Source count
- Transcripts directly mapped: 12
- Unique IDs: 12

## Top themes
- theta and vega dominance
- option selling tail risk
- institutional programs
- probability-of-profit
- delta misconceptions
- option-selling-edge
- implied volatility
- strangle with bias
- payoff equivalence
- quadruple witching

## Key lessons
- [0810] Gamma effect: in the final week a 10-30 rupee option can multiply 5-10x on a violent move - buyers must exit on momentum; sellers holding to expiry can still be destroyed.
- [1226] Delta = option-price change per one-unit underlying change; ITM options have high delta (bigger absolute profits), far OTM options have low delta (small absolute moves).
- [0110] Delta equivalence is not payoff equivalence: two ATM calls match a future's delta but accumulate time decay; the synthetic future matches the payoff itself.
- [0401] Option prices never move by delta alone - gamma, theta, vega and rho bend real-world moves (ATM call gained 45 on a 114-point rally, not the expected ~57).
- [0401] Cheap far-OTM options carry tiny deltas - their absolute upside even in a big rally is small; low price is not low risk per rupee of expectation.
- [0110] On any single day the two calls may lose less than the future - the difference appears over weeks of churn, when decay compounds.
- [0810] Large holders exit cash positions via staged sell-cash/buy-futures pairs on expiry day so the fall is hedged by the futures gain.
- [0778] Ratio spreads monetize a bounded directional view - long the move, short the overshoot, credit-funded wings for limited risk.
- [0810] Aggressive operators stack cheap puts and call sales before forcing expiry-day moves - premium windfalls fund the slippage.
- [0124] Selling a put profits in 4 of 5 scenarios (~80%); buying a call profits in 1 of 5 (~20%) - the structural seller's edge.

## Strategies (if applicable)
- {"name": "Synthetic long future", "construction": "Buy ATM call + sell ATM put (same strike/expiry)", "numbers": "Worked day (8 Jul 2020): Nifty 10766 to 10682 (-82); 10800 CE fell 36, PE rose 44, synthetic loss ~80 vs future 82-84", "best_regime": "Directional long exposure with lower capital than futures; premium received on the put offsets", "adjustments": "Roll at new ATM as trend extends", "risks": "Early assignment is absent in India (European index options); margin on the short put leg"}
- {"name": "Put-selling vs call-buying scenario framework", "construction": "ATM put sold at premium P vs ATM call bought at premium C (Nifty 10,750; 30-Jul-2020 expiry)", "numbers": "Put sold at 212; call bought at 160; put seller loses only below 10,538; call buyer profits only above 10,910", "best_regime": "Teaching framework for choosing selling over buying under a mild directional view", "adjustments": "n/a (conceptual)", "risks": "Tail risk: seller's loss is open-ended beyond breakeven"}
- {"name": "Gamma awareness for expiry-week selling", "construction": "Short ATM options held into expiry vs square-off rule", "numbers": "ATM premium 50 \u2192 ~110 (more than doubled) on a 100-point sudden move; normal delta move would be 50\u219260", "best_regime": "Never for sellers in the final days unless hedged", "adjustments": "Close/roll before expiry week; keep far-OTM hedges as real hedges, not margin dummies", "risks": "Whipsaw doubles short-premium exposure in hours"}
- {"name": "Theta-aware expiry choice", "construction": "Buyers: options with \u22651 month left; sellers: write near expiries while managing gamma", "numbers": "\u20b9100 option loses ~\u20b92/day at 50 days, ~\u20b950/day at 2 days (all else equal)", "best_regime": "Seller: final expiry weeks; buyer: far-dated directional plays", "adjustments": "Buyers roll to next month rather than hold through final-week decay", "risks": "Near-expiry gamma can overwhelm theta for both sides on news shocks"}
- {"name": "TCS earnings call-ratio with financed wings", "construction": "Buy 2 lots 3800 call @~150.5; sell 3 lots 4000 call @~59.5; buy 1 lot each of two OTM calls (~19 and ~12 premium) to equalize; sell 2 lots 3700 put @31.85, buy 2 lots 3500 put @7.45", "numbers": "Breakevens 3,678 and 4,122; max profit ~36,000 (near 4,000 close); max loss ~53,000; margin ~1.5 lakh; ~4-5% return target in 2.5 weeks; IV-drop profit of 65,000 MTM already banked on the earlier identical position", "best_regime": "Mildly bullish into an event with inflated IV; expect support near a round level (3,700)", "adjustments": "Speaker notes further adjustments possible with extra capital (method kept proprietary in source)", "risks": "Gap beyond upper breakeven; assignment risk beyond 4,000 on 3:1 short ratio; liquidity in deep-ITM legs"}

## Enhancement candidates
- Worked IV-rank calculation table (low 10, high 50, current 25 = 40%)
- Worked decomposition: observed option move vs delta-predicted move (residual = other greeks)
- Greek decomposition chart for the three structures
- Payoff diagram walkthrough of the 1:3 ratio with financed wings
- five-scenario payoff table (both sides) with exact breakevens

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0110
0124
0401
0427
0441
0455
0778
0810
1172
1201
1226
1830
