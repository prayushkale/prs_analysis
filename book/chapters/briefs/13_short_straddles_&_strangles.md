# Chapter 13: Short Straddles & Strangles
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 79
- Unique IDs: 79

## Top themes
- diversification across strikes and expiries
- technical vs fundamental analysis
- crude oil OMC inverse relation
- position movement with market
- limited-risk credit structure
- implied volatility comparison
- VIX collapse as profit driver
- bearish combo retrospective
- case study with daily data
- futures vs options overlay

## Key lessons
- [2788] The HNI entry method: park the purchase money in debt funds, sell a put at your target (3,000PE at 27 rupees); if assigned, you buy at your price having earned interest plus premium; if not, the premium is income.
- [2788] TCS: 75% promoter-held cash cow funding the group via dividends; PE compressed from ~40 to ~21-22 as the stock fell ~30-35% from 4,500 toward 3,000 - below 3,000 it becomes a buy-the-dips value candidate.
- [0115] A short straddle is a living position: when the market trends, shift the straddle to the new ATM instead of nursing the old strike - movement with the market is the edge backtests cannot capture.
- [2788] When 92% of FIIs are net short index futures and sentiment is universally bearish, good news becomes rocket fuel - the May 2025 ceasefire produced a ~4% single-day rally from maximum pessimism.
- [0115] Ratio spreads with a defended support (9500) win in both directions: the long put lost 1.84 lakh as the market rallied, but repeated short-put rounds returned ~4.24 lakh plus weekly overlay.
- [0080] Margin relief can seduce into over-sizing: four lots at 300-point risk recreates 1,200 points of exposure. Options trading is risk and position management, not strike selection.
- [2788] Buy businesses, not tickers: avoid structurally volatile stories (the Tata Motors 100-to-1,000-to-100 rollercoaster) and prefer cash-cow compounders at compressed valuations.
- [2219] Hedge-fund playbook (as alleged): quietly accumulate cheap puts and sell calls, then slam the underlying with simultaneous heavyweight sell orders, covering instantly lower.
- [0355] Option buyer has no MTM; all daily settlement is between seller and exchange (exchange obligation, collateral-eligible) unlike futures' counterparty obligations (cash).
- [2723] Call calendar = short near-dated call + long far-dated same-strike call: low margin (~50K vs ~1.7L for a naked straddle), limited but real loss if the trend extends.

## Strategies (if applicable)
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "VIX-based expected-move strangle placement", "construction": "Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%", "numbers": "VIX 60 -> monthly band ~17.3%; spot 8,000 -> sell puts below ~6,500, calls above ~9,500; May 8,000 straddle ~1,600 (~20% for 37 trading days)", "best_regime": "Elevated VIX (crisis); recompute daily as VIX moves", "adjustments": "None stated - guideline framing, refresh band as VIX changes", "risks": "Band is statistical, not a wall; theta/other factors shift premiums; violent moves can exceed the band"}
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Cash Secured Put", "construction": "Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery", "numbers": "Bajaj Finance 1800PE sold at Rs.100 (2 lots, Rs.50,000 collected); Nifty Apr 7500PE ~Rs.57; Dec-2020 6000PE ~Rs.200; ~Rs.19 lakh premium collected; claimed Rs.45 lakh FY21 P&L in 3 weeks", "best_regime": "Sideways-to-up markets, or when you want a lower entry price in a quality stock", "adjustments": "Square off the put and buy shares in the open market instead of physical delivery; exit any time before expiry", "risks": "Profit capped at premium; stock can fall far below strike; requires full cash backing of the strike"}

## Enhancement candidates
- expectation-psychology sidebar for Part I
- Stop-loss-and-cost-revision straddle workflow
- Liquidity-premium explanation: why far legs gap
- Table: VIX regime (11-15 low) vs strategy pairing rules
- Bitcoin consolidation-to-breakout pattern

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0003
0025
0027
0030
0034
0036
0037
0040
0042
0048
0054
0063
0073
0077
0080
0103
0104
0105
0109
0114
0115
0127
0129
0131
0146
0156
0165
0168
0169
0326
