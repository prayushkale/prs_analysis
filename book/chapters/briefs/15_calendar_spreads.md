# Chapter 15: Calendar Spreads
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 13
- Unique IDs: 13

## Top themes
- technical vs fundamental analysis
- implied volatility term structure
- limited-risk credit structure
- index heavyweight catch-up
- stock lending & borrowing
- defined-risk structures
- post-move consolidation
- mean reversion failure
- non-directional combos
- portfolio construction

## Key lessons
- [3001] ITM put calendar: sell near-month put (collect premium), buy far-month put (protection) - best for budget when you expect near-term consolidation but want long-term protection
- [2723] Call calendar = short near-dated call + long far-dated same-strike call: low margin (~50K vs ~1.7L for a naked straddle), limited but real loss if the trend extends.
- [2994] If people think market won't make a big move, they sell straddle. If premium is very high, market is expecting a big move - don't sell straddle, do a calendar
- [1322] Mean reversion breaks on corporate actions: REC's fall from 140 to 105 was a 1:3 bonus adjustment, not a correction - the retracement trade expired worthless.
- [2734] Calendars are net-debit structures; finance the debit by selling an adjacent strangle only if you also accept the larger margin that comes with it.
- [1749] A deep-ITM put calendar converts a bullish view into low-margin, capped-risk exposure; roll-over cost (~₹3,500-4,000/month) is the real max risk.
- [2734] Know your margin with and without the financing legs: 2 lakh with the strangle vs 70K without changes both risk sizing and return percentages.
- [0662] A crash portfolio: ~60% index ETFs, ~10% gold (crisis hedge — gold rose in 2008 and 2020), ~30% debt/REITs you can liquidate to buy the dip.
- [2723] After a very large single-direction move, markets statistically consolidate or drift slightly opposite - that is the calendar's home regime.
- [1322] Pattern-matching past crashes fails when the policy regime differs: 2008/2020 recoveries needed 0% rates + QE; 2022 had rising rates + QT.

## Strategies (if applicable)
- {"name": "Bank Nifty rollover analysis", "construction": "Long (or short) futures rolled monthly", "numbers": "~100 pts typical next-month premium; ~1,200 pts (~5-6%) cost per year for longs; shorts collect it", "best_regime": "Long-term shorts benefit from rollover premium; long-term longs should buy cash instead", "adjustments": "Hedging is cheaper on futures than on cash positions", "risks": "Premium varies 40-200 pts monthly; longs underperform cash by the premium"}
- {"name": "ITM put calendar (low-VIX regime)", "construction": "sell current-month ITM put (16,000PE July), buy same strike far-month put (16,000PE December) as the hedge", "numbers": "July PE 350->150 (+200); Dec PE 580->490 (-90); net ~+110 = ~5,000 rupees/lot; margin ~50,000; ~10% in 3 weeks; back-office: sold 1,250 qty +1.1 lakh, bought 750 qty -54k, net +55k", "best_regime": "India VIX at multi-year lows, quiet drift up or sideways", "adjustments": "exit early if VIX regime turns; keep partial hedge ratio honest (he ran 1,250 short vs 750 long)", "risks": "sharp VIX spike hits the short leg; partial hedging leaves crash exposure; far-month liquidity is thin"}
- {"name": "Long-dated combo: call ratio + cash-secured put (Dec-2022 expiry)", "construction": "Sell ~500 qty 15,000PE; buy 250 qty 18,000CE; sell 500 qty 20,000CE (i.e., 1 call ratio + 1 cash-secured put)", "numbers": "Entered ~Nov 2021 with Nifty ~18,000; premiums ~350/1600/800; breakevens ~14,500 and ~22,700; margin ~\u20b91.5 lakh; target return 20-25% on margin", "best_regime": "Neutral-to-bullish one-year view with wide safety band", "adjustments": "Beyond 20,000-22,000, roll the short calls upward in stages to recapture upside ('we teach that in workshops')", "risks": "Loss below ~14,500 (accepts assignment \u2014 wants to buy there); upside capped above 22,000 unless adjusted"}
- {"name": "Post-crash call ratio (Dec-2021)", "construction": "Buy 17,700CE, sell 2x 18,300CE after Nifty's ~900-point fall", "numbers": "Entered at equal premium (600 vs 300x2) \u2192 near-zero downside loss (~\u20b92,000 on current marks); profit if Nifty recovers up to ~18,800", "best_regime": "After a sharp fall when recovery odds are good", "adjustments": "If market rips beyond 18,800, roll or square the shorts", "risks": "Upside beyond upper strike; small absolute downside already built in"}
- {"name": "ETH long call ratio + short puts", "construction": "Buy 3000CE; sell 5000CE x3; sell 2000PE x2", "numbers": "Margin $1,200; +$420 (~35%) in under 3 months (~10%/month)", "best_regime": "Range-bound high-IV crypto", "adjustments": "None - held", "risks": "Upside caps at 5000; downside naked put x2"}

## Enhancement candidates
- Worked margin-vs-gap table: lot size 75, fall of 500/1200/1500 points vs collected margin
- Worked example of weekly roll cash flows
- Table: VIX regime (11-15 low) vs strategy pairing rules
- Risk-size ladder: naked vs winged versions of the same view
- Payoff table: calendar at expiry vs 1 week out for ±0/±1/±2% moves; margin comparison vs naked straddle

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0155
0481
0662
0967
1322
1749
1809
1854
2065
2723
2734
2994
3001
