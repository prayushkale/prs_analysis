# Chapter 14: Spreads & Ratio Spreads
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 54
- Unique IDs: 54

## Top themes
- extraordinary dividend adjustment
- position movement with market
- bearish combo retrospective
- cash-settlement-vs-delivery
- political stability premium
- dividend capture arbitrage
- portfolio-level evaluation
- defined-risk construction
- option buyers vs sellers
- option strike adjustment

## Key lessons
- [0244] Even across seven major crises (Lehman, Greece, taper tantrum, China devaluation, demonetization+Trump, Brexit, Feb-2018 US flash crash), Nifty never gapped more than 400 points except Lehman and COVID; Bank Nifty max 1,200.
- [0115] A short straddle is a living position: when the market trends, shift the straddle to the new ATM instead of nursing the old strike - movement with the market is the edge backtests cannot capture.
- [0108] When a dividend exceeds 5% of market value, exchanges adjust option strikes (and premiums) on ex-date - the broker did not change anything; check corporate actions before trading stock options.
- [0115] Ratio spreads with a defended support (9500) win in both directions: the long put lost 1.84 lakh as the market rallied, but repeated short-put rounds returned ~4.24 lakh plus weekly overlay.
- [2737] Call ratio fits a mild bullish view with a defined resistance: long one ATM call, short two far-OTM calls - profit concentrated below resistance, loss capped above it by design asymmetry.
- [2737] No mechanical system survives all regimes: the 9:20 short-straddle bot era ended when daily 300-point ranges blew through bot stops - discretion with a view adapts.
- [0108] Market leadership can flip intraday (HDFC Bank morning, Reliance afternoon) - concentration of two names driving >50% of an index rally is a fragility signal.
- [0139] Spread math dominates: when Nifty rose ~1,100 points while Bank Nifty rose ~300, the long-Nifty/short-BankNifty pair collected the differential on both legs.
- [0115] Late entrants should not chase a running trade: the risk-reward at entry is gone; wait for the next series and start fresh (genericized member guidance).
- [0139] Pair trading isolates relative strength: you profit from the spread between two instruments, not from market direction - gaps and crashes largely cancel.

## Strategies (if applicable)
- {"name": "Falling-VIX combo (call ratio + put ratio)", "construction": "Bought 8,200CE, sold 3x 9,000CE; bought 8,000PE, sold 7,400PE + 7,300PE (as stated)", "numbers": "Sold ~3x quantity on the far leg both sides", "best_regime": "Falling VIX with a directional view; benefits from vega collapse on the short legs", "adjustments": "Not stated", "risks": "Upside loss above 9,000 on the 3:1 call ratio; downside acceleration through 7,300 on the put ratio"}
- {"name": "ICICI Bank call ratio (1x2) for earnings", "construction": "Buy 1 lot 350CE at ~2,440; sell 2 lots 380CE at ~1,190", "numbers": "near-zero net cost (~40-50 paise paid); max loss downside ~825; max profit zone 350-380; unlimited risk above 410; margin ~1.5 lakh net (2.53 lakh naked 380CE)", "best_regime": "mildly bullish stock pinned below known resistance into results", "adjustments": "not shown in this episode; speaker flags adjustment need if it gaps above 410", "risks": "gap above the sold strike doubles exposure; earnings gaps both ways"}
- {"name": "Call ratio spread (financed directional)", "construction": "Long 1x 9400CE; short 2x 9800CE; short 1x 10000CE (300/600/300 qty), plus weekly far-OTM call sales to offset net debit", "numbers": "9400CE ~219; 9800CE ~80; 10000CE ~45; net ~-4300 before weekly sales (~+2800 after); max profit ~1,15,000 at 9800 expiry; loss begins ~10,080", "best_regime": "Mildly bullish, expect stay below written strikes", "adjustments": "Promised follow-up through expiry; weekly-call sales used to neutralize debit", "risks": "Unlimited above 10,080 (net short top strike); upside capped at 9800 zone"}
- {"name": "OTM credit-sale adjustment on a losing ratio", "construction": "Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65", "numbers": "Pre-adjustment loss ~Rs 3,000; post-adjustment profit ~Rs 2,000 per lot", "best_regime": "After a results miss confirms the directional view is dead", "adjustments": "Collected credit exceeds the defined max loss; no further action needed unless stock reverses hard", "risks": "New short call adds upside risk; acceptable because view is now neutral-bearish"}
- {"name": "Limited-risk call ratio spread (1:3:2)", "construction": "Buy 1x 10,500 CE (Aug), sell 3x 11,000 CE (Aug), buy 2x 11,500 CE (Aug)", "numbers": "Net credit ~Rs 1,900; margin ~Rs 65,000 (Rs 63,000 effective); max profit ~Rs 37,000 at Nifty 11,000; upper breakeven 11,253; max loss ~Rs 37,000 above 11,500", "best_regime": "After a sharp rally, into strong resistance (200-DMA + 50% retracement of 12,400->7,500)", "adjustments": "Exit all legs together; partial exit leaves naked short calls", "risks": "Sustained breakout above 11,500 hits max loss; requires two-month view"}

## Enhancement candidates
- Payoff chart walkthrough: ratio sizing math for surplus short quantity
- Stop-loss-and-cost-revision straddle workflow
- full crypto ratio-spread worked example with payoff table
- Margin math: hedged vs naked leg span comparison
- Risk-size ladder: naked vs winged versions of the same view

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0028
0060
0063
0064
0098
0108
0109
0114
0115
0120
0126
0139
0148
0165
0228
0244
0246
0662
0778
0799
0815
0825
0879
0921
0958
0966
0967
1001
1142
1154
