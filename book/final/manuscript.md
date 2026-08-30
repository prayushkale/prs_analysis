# The Indian Market Trader's Handbook

*By Dhanraj*

## Disclaimer
The strategies, examples, and market observations in this book are compiled from educational trading content and are presented for informational purposes only. All P&L figures cited are illustrative and based on recollection; they are not audited track records. This book does not constitute investment advice. Past performance does not guarantee future results. Readers should consult a SEBI-registered advisor before making trading decisions.

## Preface
This book is compiled from thousands of hours of market commentary spanning 2018 through 2026. The author, Dhanraj, has distilled the most transferable lessons, strategies, and market observations from this body of work into a structured reference. Market events have been verified against publicly available sources where possible. Complex topics have been expanded with worked examples and explanatory tables. The goal is not to predict markets but to provide a framework for understanding them.

---

# Part I: The Trader's Mind

# Chapter 1: Why Most Traders Lose

Every year, millions of Indians step into the stock market hoping to build wealth through trading. The statistics, however, tell a sobering story.

## Themes
- diversification across strikes and expiries
- IPO strategy for small capital
- position movement with market
- technical analysis skepticism
- technical analysis conversion
- efficient market hypothesis

## Strategies
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Multi-strike, multi-expiry put selling (April 2020)", "construction": "Sold put options spread across various strike prices and expiry periods rather than one strike", "numbers": "7500PE sold around Rs.75 during a morning dip; SGX Nifty ~9200 vs ~9000 close", "best_regime": "Ultra-bearish consensus with the negative surprise already announced", "adjustments": "Exited or rolled by expiry; profit disclosed in a later review video", "risks": "Losses if the market breaks below the sold strikes; premium is the cap on profit"}
- {"name": "Monthly short option + weekly protective hedge", "construction": "Sell far-month option; buy near-week option slightly OTM below breakeven; re-buy weekly", "numbers": "9,000PE July sold (>100 premium), 8,900PE weekly bought; margin ~50,000 vs >1,00,000 unhedged", "best_regime": "credit selling with black-swan protection", "adjustments": "roll weekly wing; broker far-strike restrictions are the friction", "risks": "weekly wing expires worthless after rallies; rollover cost creep"}
- {"name": "Collateral-funded option selling (HNI pattern)", "construction": "Pledge debt mutual funds/bank FDs as collateral; sell options against the margin; keep interest as primary return", "numbers": "Stated pattern: 6-7% interest on debt funds while trading on pledged limit", "best_regime": "Wealthy, income-focused sellers who accept trading as a bonus stream", "adjustments": "Not applicable - structural allocation", "risks": "Trading losses eat the collateral cushion; interest is not guaranteed against credit events"}

*Sources: 30 transcripts*
---

# Chapter 2: Anatomy of a Trader's Failure

The path from novice to consistently profitable trader is rarely travelled. Most traders follow a predictable arc of enthusiasm, overconfidence, loss, and burnout.

## Themes
- technical vs fundamental analysis
- IPO strategy for small capital
- technical analysis conversion
- primary vs secondary market
- diversification of methods
- technical analysis limits

## Strategies
- {"name": "IndusInd earnings-day iron-fly style combo", "construction": "Sell 400CE + sell 400PE, buy 500CE + buy 300PE (current month)", "numbers": "profit down 77% vs expected 95% fall; stock closed ~15-17% higher", "best_regime": "earnings day when heavy short positioning built up", "adjustments": "speaker's own adjustments not disclosed; states adjustments depend on additional capital", "risks": "big gap moves on expiry; adjustments need reserve capital"}
- {"name": "Infosys bearish iron-condor-style spread + firefighting ladder", "construction": "Initial: 800PE long / 770PE short; 830CE short / 900CE long. Firefight: sold 780PE, 830PE, 900PE (later doubled), 850PE, 1000CE", "numbers": "Potential loss ~Rs 1.6-1.7L; final +Rs 21,826; extra margin ~Rs 15L; Infosys 780->830->915 (+20% in 2 days)", "best_regime": "Adverse post-results spike in a stock you can sell puts on", "adjustments": "Ladder put sales at rising supports; double quantity only as levels hold; cap with far-OTM calls", "risks": "Continued vertical moves; margin exhaustion; doubling short puts is aggressive"}
- {"name": "Hedged monthly book through expiry stress", "construction": "Directional futures/option legs + offsetting call hedges + occasional ratio spreads", "numbers": "Sep: BN -5.5L, hedges +1.5L, ratio +1.18L, ITC hedging +2.23L, Nifty +1.4L, SBI +38K, Sensex -2L \u2192 ~+10L on ~\u20b91 cr capital", "best_regime": "Volatile series where directional legs bleed", "adjustments": "Hedge in the next series when current-series data ends; move hedges to liquid proxies", "risks": "Illiquidity in new instruments (Sensex options) causes slippage and forced proxy hedging"}
- {"name": "Short-stock rescue ladder (firefighting)", "construction": "Short future + sold call went wrong; rescue = sold puts at 4,500/4,700/4,800/4,900/5,000/5,200 (4,500 qty total) + long Jan future + sold 5,500 call", "numbers": "Stock +250 (4,900->5,150); drawdown 3.5-4 lakh; ~1 crore extra margin; ~10 lakh margin per 1,000 qty; result +1.49 lakh", "best_regime": "When a short directional view is hit by a gap/momentum move you believe is temporary", "adjustments": "Ladder put sales into the spike, convert to hedged combo, keep averaging only with reserve capital", "risks": "Requires massive reserve margin; if the rally continues, losses compound - works only with deep pockets and fast execution"}
- {"name": "IPO cost-recovery hold", "construction": "Apply to quality IPOs with idle funds parked in 6-6.5% savings accounts; on allotment sell partial quantity to recover application cost; hold remainder free", "numbers": "Example: L&T issue ~1987-88, partly convertible debentures Rs50 doubled to ~Rs100 next day; held value estimated Rs50-60L today", "best_regime": "Small capital, no F&O skill yet; strong primary-market pipelines", "adjustments": "Review holdings annually; keep proceeds cycling into fresh quality IPOs", "risks": "Opportunity cost if markets run; allotment not guaranteed (refund is safe)"}

*Sources: 30 transcripts*
---

# Chapter 3: Discipline, Process, and Surviving First

Before strategy or analysis comes the foundation: discipline. This chapter is about building a framework that allows you to survive long enough to improve.

## Themes
- diversification across strikes and expiries
- time correction vs price correction
- positional trading infrastructure
- system vs discretionary traders
- corporate vs personal taxation
- IPO strategy for small capital

## Strategies
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Multi-strike, multi-expiry put selling (April 2020)", "construction": "Sold put options spread across various strike prices and expiry periods rather than one strike", "numbers": "7500PE sold around Rs.75 during a morning dip; SGX Nifty ~9200 vs ~9000 close", "best_regime": "Ultra-bearish consensus with the negative surprise already announced", "adjustments": "Exited or rolled by expiry; profit disclosed in a later review video", "risks": "Losses if the market breaks below the sold strikes; premium is the cap on profit"}
- {"name": "Put-selling ladder in collapsing-VIX rebound", "construction": "Sold puts across strikes from ~6,100 to 9,000 during April 2020 recovery", "numbers": "April profit 66,30,478 on ~95L capital; VIX 80-85 -> 55-60 -> ~40; June 9000PE sold at 500, closed 180", "best_regime": "post-crash VIX collapse with market refusing to make new lows", "adjustments": "not detailed in this episode", "risks": "windfall not repeatable; VIX normalizes; requires conviction view"}
- {"name": "Staggered index investing with cash-secured puts", "construction": "SIP into a Nifty 50 ETF; optionally place cash-secured puts at desired lower entries", "numbers": "Nifty PE ~16 (May 2020); historical buy zone 15-16, sell zone 28-30; Dow 1929 crash ~90%; 1982-2000 bull ~15x", "best_regime": "Post-crash pessimism; long horizon", "adjustments": "Add on further 5-10% falls", "risks": "Multi-year drawdowns; requires no-liquidity-needs capital"}
- {"name": "Cash-secured puts (ICICI 300PE, HDFC 840PE)", "construction": "Sell puts below market with full cash set aside for delivery", "numbers": "+33,000 ICICI and +28,000 HDFC in May 2020", "best_regime": "moderately bullish with stocks near support", "adjustments": "take delivery if assigned; roll if view changes", "risks": "sharp breakdown below strike forces delivery at loss"}

*Sources: 30 transcripts*
---


# Part II: How This Market Works

# Chapter 4: FII/DII Flows

Foreign Institutional Investor (FII) and Domestic Institutional Investor (DII) flows are the engine of Indian equity markets. Understanding who is buying and who is selling explains daily market behaviour more than any other single metric.

## Themes
- extraordinary dividend adjustment
- bank nifty underperformance
- primary vs secondary market
- narrative misinterpretation
- dividend capture arbitrage
- portfolio-level evaluation

## Strategies
- {"name": "Call ratio spread (financed directional)", "construction": "Long 1x 9400CE; short 2x 9800CE; short 1x 10000CE (300/600/300 qty), plus weekly far-OTM call sales to offset net debit", "numbers": "9400CE ~219; 9800CE ~80; 10000CE ~45; net ~-4300 before weekly sales (~+2800 after); max profit ~1,15,000 at 9800 expiry; loss begins ~10,080", "best_regime": "Mildly bullish, expect stay below written strikes", "adjustments": "Promised follow-up through expiry; weekly-call sales used to neutralize debit", "risks": "Unlimited above 10,080 (net short top strike); upside capped at 9800 zone"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}
- {"name": "Dividend capture via cash-futures arbitrage", "construction": "Buy stock in cash market before ex-date; short equal futures; collect dividend; square both legs post ex-date", "numbers": "ITC dividend >10 rupees on a ~200 rupee stock; ~5% return in days as stated", "best_regime": "Extraordinary dividends (>5% of market value) where futures still price the gross dividend", "adjustments": "Square up after ex-date convergence", "risks": "Futures may already price the dividend; margin on short futures; execution costs"}
- {"name": "Nifty long / Bank Nifty short pair", "construction": "Long 1 lot Nifty futures + short 1 lot Bank Nifty futures (25 lot size), rebalanced views weekly", "numbers": "One-week window: ~4,725 loss on Nifty leg vs ~12,775 profit on Bank Nifty leg; two-week window: net ~12,000+ profit; one-month window positive", "best_regime": "Index divergence phases - Bank Nifty underperforming Nifty for weeks", "adjustments": "Re-evaluate pair weekly; exit when the spread normalizes", "risks": "Correlation breakdown in crashes; both legs can lose if sized wrong; margin on two futures legs"}
- {"name": "Short-stock rescue ladder (firefighting)", "construction": "Short future + sold call went wrong; rescue = sold puts at 4,500/4,700/4,800/4,900/5,000/5,200 (4,500 qty total) + long Jan future + sold 5,500 call", "numbers": "Stock +250 (4,900->5,150); drawdown 3.5-4 lakh; ~1 crore extra margin; ~10 lakh margin per 1,000 qty; result +1.49 lakh", "best_regime": "When a short directional view is hit by a gap/momentum move you believe is temporary", "adjustments": "Ladder put sales into the spike, convert to hedged combo, keep averaging only with reserve capital", "risks": "Requires massive reserve margin; if the rally continues, losses compound - works only with deep pockets and fast execution"}

*Sources: 30 transcripts*
---

# Chapter 5: Volatility as a Regime

Volatility is not noise — it is the metronome of the market. The India VIX measures the expected 30-day movement in the Nifty, and its level dictates which strategies work and which fail.

## Themes
- diversification across strikes and expiries
- implied volatility term structure
- mean reversion after down years
- Supreme Court moratorium case
- valuation premium compression
- crisis cycle every 8-10 years

## Strategies
- {"name": "VIX-based expected-move strangle placement", "construction": "Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%", "numbers": "VIX 60 -> monthly band ~17.3%; spot 8,000 -> sell puts below ~6,500, calls above ~9,500; May 8,000 straddle ~1,600 (~20% for 37 trading days)", "best_regime": "Elevated VIX (crisis); recompute daily as VIX moves", "adjustments": "None stated - guideline framing, refresh band as VIX changes", "risks": "Band is statistical, not a wall; theta/other factors shift premiums; violent moves can exceed the band"}
- {"name": "Falling-VIX combo (call ratio + put ratio)", "construction": "Bought 8,200CE, sold 3x 9,000CE; bought 8,000PE, sold 7,400PE + 7,300PE (as stated)", "numbers": "Sold ~3x quantity on the far leg both sides", "best_regime": "Falling VIX with a directional view; benefits from vega collapse on the short legs", "adjustments": "Not stated", "risks": "Upside loss above 9,000 on the 3:1 call ratio; downside acceleration through 7,300 on the put ratio"}
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}

*Sources: 30 transcripts*
---

# Chapter 6: Reading the Option Chain

The option chain is the closest thing to a public order book for trader sentiment. It reveals where the crowd has placed its bets and, more importantly, at what price levels those bets become dangerous.

## Themes
- Supreme Court moratorium case
- bearish combo retrospective
- efficient market hypothesis
- index heavyweight catch-up
- stock lending & borrowing
- option selling placement

## Strategies
- {"name": "VIX-based expected-move strangle placement", "construction": "Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%", "numbers": "VIX 60 -> monthly band ~17.3%; spot 8,000 -> sell puts below ~6,500, calls above ~9,500; May 8,000 straddle ~1,600 (~20% for 37 trading days)", "best_regime": "Elevated VIX (crisis); recompute daily as VIX moves", "adjustments": "None stated - guideline framing, refresh band as VIX changes", "risks": "Band is statistical, not a wall; theta/other factors shift premiums; violent moves can exceed the band"}
- {"name": "Monthly short option + weekly protective hedge", "construction": "Sell far-month option; buy near-week option slightly OTM below breakeven; re-buy weekly", "numbers": "9,000PE July sold (>100 premium), 8,900PE weekly bought; margin ~50,000 vs >1,00,000 unhedged", "best_regime": "credit selling with black-swan protection", "adjustments": "roll weekly wing; broker far-strike restrictions are the friction", "risks": "weekly wing expires worthless after rallies; rollover cost creep"}
- {"name": "ATM straddle range projection", "construction": "Nearest strike to post-expiry close; add ATM call + put premiums to strike for upper bound, subtract for lower bound", "numbers": "Nifty 11,650 strike; call 220 + put 190 = 410; range 11,240-12,060 (rounded 11,200-12,100); ~65% probability", "best_regime": "Start of a monthly series, day after expiry", "adjustments": "Update if a large event (election/budget) reprices premiums mid-month", "risks": "Fat-tail months with news shocks breach the range; not a certainty"}
- {"name": "Bank Nifty rollover analysis", "construction": "Long (or short) futures rolled monthly", "numbers": "~100 pts typical next-month premium; ~1,200 pts (~5-6%) cost per year for longs; shorts collect it", "best_regime": "Long-term shorts benefit from rollover premium; long-term longs should buy cash instead", "adjustments": "Hedging is cheaper on futures than on cash positions", "risks": "Premium varies 40-200 pts monthly; longs underperform cash by the premium"}
- {"name": "Range-filtered PCR", "construction": "Sum put OI and call OI only for strikes within expected monthly range (spot +/-1,000 early in month, +/-700-800 mid-month); PCR = put OI / call OI", "numbers": "Dec 2020: raw PCR 1.81 vs filtered 1.12 (put 1.67 cr, call 1.49 cr in 12,800-14,200)", "best_regime": "Weekly/mid-month sentiment read before taking directional or option-selling positions", "adjustments": "Recompute as the expected range narrows through the month", "risks": "Range guess can be wrong in trending/volatile months; still an OI-based sentiment proxy, not a timing signal"}

*Sources: 25 transcripts*
---

# Chapter 7: Microstructure: Gaps, Expiries, Last Half Hour

Markets move in patterns that repeat because the participants and their incentives repeat. The anatomy of a gap open, an expiry day, or the last half hour of trading is consistent across years and regimes.

## Themes
- positional trading infrastructure
- system vs discretionary traders
- Supreme Court moratorium case
- margin unfairness to hedgers
- case study with daily data
- technical analysis limits

## Strategies
- {"name": "Hedged short put", "construction": "Sell near put + buy a further-OTM put same expiry", "numbers": "Speaker example: sold 9400-put style positions; hedge put cuts margin drastically and caps loss", "best_regime": "Any short-put view; mandatory insurance", "adjustments": "Not advised live; know risk-reward before entry", "risks": "Unhedged version: margin cascade and uncapped gap risk"}
- {"name": "Unhedged short straddle on a single stock", "construction": "Sell 1000 CE (49) + sell 1000 PE (39) on HDFC Bank, 2 lots (1000 qty), June 9 2020, hold to near expiry", "numbers": "Premium collected ~87,000; returned ~35,000; profit ~50,000; stock closed 1035 on June 25; daily combined premium stayed below 87 through expiry", "best_regime": "High IV with range-bound expectation around a support level (1000)", "adjustments": "None taken in this trade - held naked; would need firefighting if spot ran beyond breakevens", "risks": "Unlimited loss beyond 1087/913; a single-stock gap through breakevens is the failure mode"}
- {"name": "Bank Nifty rollover analysis", "construction": "Long (or short) futures rolled monthly", "numbers": "~100 pts typical next-month premium; ~1,200 pts (~5-6%) cost per year for longs; shorts collect it", "best_regime": "Long-term shorts benefit from rollover premium; long-term longs should buy cash instead", "adjustments": "Hedging is cheaper on futures than on cash positions", "risks": "Premium varies 40-200 pts monthly; longs underperform cash by the premium"}
- {"name": "Calendar inversion (long near-week straddle, short far-week straddle)", "construction": "Buy ATM call+put current weekly expiry; sell ATM call+put next weekly expiry", "numbers": "Capital ~\u20b930-35k; claimed backtest ~\u20b928-30k/year (~80% gross, ~50-55% after costs)", "best_regime": "Expecting violent moves (event seasons)", "adjustments": "Cut the losing far leg on a 10-15% premium move; trail the winner; re-buy the opposite leg on reversal", "risks": "Absolute sideways market decays both longs; near-week theta bleed"}
- {"name": "Collateral-funded far-OTM weekly selling (HNI pattern, warned)", "construction": "Hold ~1,000 crore shares; sell far-OTM weekly calls and puts near 1 rupee with a 5-rupee stop", "numbers": "~8 lakh/week per side on 100-crore collateral (~16 lakh/week, ~64 lakh/month); stop hit probability <0.1% except tail events like the 2019 corporate-tax-cut candle when a 1-rupee option went to 60-70", "best_regime": "Ultra-HNI zero-capital-cost premium harvesting; NOT for retail", "adjustments": "Sell both sides so net short/long classification nets to zero under the 500-crore rule", "risks": "Tail events blow through stops; surveillance margin can freeze released funds for two months; single-side selling triggers the net-short cap"}

*Sources: 30 transcripts*
---


# Part III: Options from First Principles

# Chapter 8: Why Derivatives Exist

Derivatives exist to transfer risk from those who do not want it to those who are willing to carry it. Futures and options are the tools, but the principle is as old as commerce itself.

## Themes
- covered interest arbitrage
- probability and premium
- market structure facts
- futures vs cash market
- transaction-cost math
- collateral efficiency

## Strategies
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Synthetic futures (long/short)", "construction": "Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs", "numbers": "Demo: June futures -222 vs synthetic -219 on a 222-point fall; cost base 7.5 lakh (futures) vs ~30,000 (synthetic) per lot at Nifty 10,000, lot 75", "best_regime": "Any directional view where collateral efficiency matters; far-month exposure", "adjustments": "Exit both legs together; unbalanced exit leaves a naked leg with higher margin", "risks": "Stock synthetics fail on deep-ITM liquidity; index only"}
- {"name": "Covered interest carry trade (1995 example)", "construction": "Borrow SGD at 3%, place INR NRNR deposit at 20%, hedge FX with a 3-year forward costing ~2%/yr", "numbers": "gross spread 17%; net ~15% riskless; 10 lakh -> ~17.5 lakh over 3 years", "best_regime": "large interest-rate differentials with hedged currency risk", "adjustments": "roll forward hedge; watch repatriation rules", "risks": "counterparty/country risk; hedge cost creep"}
- {"name": "ITM call instead of long futures", "construction": "Buy deep ITM call (e.g. SBI 200CE at Rs46 with spot 245, lot 3000) instead of 1 lot futures", "numbers": "Premium ~Rs1.38L vs futures margin ~Rs2.5L vs cash Rs7.35L; at 260: ~Rs45,000 gain all three; charges cash 1,684 / futures 174 / options 329", "best_regime": "Strong directional view with defined horizon; want futures-like exposure with capped risk", "adjustments": "Exit anytime before expiry; premium tracks underlying", "risks": "Max loss = premium paid; decay works against you if the move is delayed past expiry"}

*Sources: 21 transcripts*
---

# Chapter 9: Calls and Puts

Every options strategy is built from four basic actions: buy a call, sell a call, buy a put, sell a put. Master these building blocks and everything else is assembly.

## Themes
- extraordinary dividend adjustment
- American vs European options
- stock lending and borrowing
- dividend capture arbitrage
- liquidity and trading bans
- margin architecture reform

## Strategies
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "Cash Secured Put", "construction": "Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery", "numbers": "Bajaj Finance 1800PE sold at Rs.100 (2 lots, Rs.50,000 collected); Nifty Apr 7500PE ~Rs.57; Dec-2020 6000PE ~Rs.200; ~Rs.19 lakh premium collected; claimed Rs.45 lakh FY21 P&L in 3 weeks", "best_regime": "Sideways-to-up markets, or when you want a lower entry price in a quality stock", "adjustments": "Square off the put and buy shares in the open market instead of physical delivery; exit any time before expiry", "risks": "Profit capped at premium; stock can fall far below strike; requires full cash backing of the strike"}
- {"name": "OTM credit-sale adjustment on a losing ratio", "construction": "Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65", "numbers": "Pre-adjustment loss ~Rs 3,000; post-adjustment profit ~Rs 2,000 per lot", "best_regime": "After a results miss confirms the directional view is dead", "adjustments": "Collected credit exceeds the defined max loss; no further action needed unless stock reverses hard", "risks": "New short call adds upside risk; acceptable because view is now neutral-bearish"}
- {"name": "Synthetic futures (long/short)", "construction": "Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs", "numbers": "Demo: June futures -222 vs synthetic -219 on a 222-point fall; cost base 7.5 lakh (futures) vs ~30,000 (synthetic) per lot at Nifty 10,000, lot 75", "best_regime": "Any directional view where collateral efficiency matters; far-month exposure", "adjustments": "Exit both legs together; unbalanced exit leaves a naked leg with higher margin", "risks": "Stock synthetics fail on deep-ITM liquidity; index only"}
- {"name": "Collateral-funded option selling (HNI pattern)", "construction": "Pledge debt mutual funds/bank FDs as collateral; sell options against the margin; keep interest as primary return", "numbers": "Stated pattern: 6-7% interest on debt funds while trading on pledged limit", "best_regime": "Wealthy, income-focused sellers who accept trading as a bonus stream", "adjustments": "Not applicable - structural allocation", "risks": "Trading losses eat the collateral cushion; interest is not guaranteed against credit events"}

*Sources: 30 transcripts*
---

# Chapter 10: The Greeks, Demystified

The Greeks are the sensitivity measures that tell you how an option's price will change when the underlying moves, time passes, or volatility shifts. They are not theory — they are the mechanism.

## Themes
- theta and vega dominance
- option selling tail risk
- institutional programs
- probability-of-profit
- delta misconceptions
- option-selling-edge

## Strategies
- {"name": "Synthetic long future", "construction": "Buy ATM call + sell ATM put (same strike/expiry)", "numbers": "Worked day (8 Jul 2020): Nifty 10766 to 10682 (-82); 10800 CE fell 36, PE rose 44, synthetic loss ~80 vs future 82-84", "best_regime": "Directional long exposure with lower capital than futures; premium received on the put offsets", "adjustments": "Roll at new ATM as trend extends", "risks": "Early assignment is absent in India (European index options); margin on the short put leg"}
- {"name": "Put-selling vs call-buying scenario framework", "construction": "ATM put sold at premium P vs ATM call bought at premium C (Nifty 10,750; 30-Jul-2020 expiry)", "numbers": "Put sold at 212; call bought at 160; put seller loses only below 10,538; call buyer profits only above 10,910", "best_regime": "Teaching framework for choosing selling over buying under a mild directional view", "adjustments": "n/a (conceptual)", "risks": "Tail risk: seller's loss is open-ended beyond breakeven"}
- {"name": "Gamma awareness for expiry-week selling", "construction": "Short ATM options held into expiry vs square-off rule", "numbers": "ATM premium 50 \u2192 ~110 (more than doubled) on a 100-point sudden move; normal delta move would be 50\u219260", "best_regime": "Never for sellers in the final days unless hedged", "adjustments": "Close/roll before expiry week; keep far-OTM hedges as real hedges, not margin dummies", "risks": "Whipsaw doubles short-premium exposure in hours"}
- {"name": "Theta-aware expiry choice", "construction": "Buyers: options with \u22651 month left; sellers: write near expiries while managing gamma", "numbers": "\u20b9100 option loses ~\u20b92/day at 50 days, ~\u20b950/day at 2 days (all else equal)", "best_regime": "Seller: final expiry weeks; buyer: far-dated directional plays", "adjustments": "Buyers roll to next month rather than hold through final-week decay", "risks": "Near-expiry gamma can overwhelm theta for both sides on news shocks"}
- {"name": "TCS earnings call-ratio with financed wings", "construction": "Buy 2 lots 3800 call @~150.5; sell 3 lots 4000 call @~59.5; buy 1 lot each of two OTM calls (~19 and ~12 premium) to equalize; sell 2 lots 3700 put @31.85, buy 2 lots 3500 put @7.45", "numbers": "Breakevens 3,678 and 4,122; max profit ~36,000 (near 4,000 close); max loss ~53,000; margin ~1.5 lakh; ~4-5% return target in 2.5 weeks; IV-drop profit of 65,000 MTM already banked on the earlier identical position", "best_regime": "Mildly bullish into an event with inflated IV; expect support near a round level (3,700)", "adjustments": "Speaker notes further adjustments possible with extra capital (method kept proprietary in source)", "risks": "Gap beyond upper breakeven; assignment risk beyond 4,000 on 3:1 short ratio; liquidity in deep-ITM legs"}

*Sources: 12 transcripts*
---

# Chapter 11: Implied Volatility

Implied Volatility transforms an option from a directional instrument into a probabilistic one. When you understand IV, you stop predicting the market and start pricing risk.

## Themes
- implied volatility term structure
- mean reversion after down years
- implied volatility comparison
- VIX collapse as profit driver
- macro problem resolution
- annual targeting method

## Strategies
- {"name": "Falling-VIX combo (call ratio + put ratio)", "construction": "Bought 8,200CE, sold 3x 9,000CE; bought 8,000PE, sold 7,400PE + 7,300PE (as stated)", "numbers": "Sold ~3x quantity on the far leg both sides", "best_regime": "Falling VIX with a directional view; benefits from vega collapse on the short legs", "adjustments": "Not stated", "risks": "Upside loss above 9,000 on the 3:1 call ratio; downside acceleration through 7,300 on the put ratio"}
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "IndusInd Bank earnings hedged straddle (May series)", "construction": "Sell May 400CE @62 + 400PE @52; buy current-month 500CE @4.25 + 300PE @5.25 as protection", "numbers": "Net premium ~Rs.94.55/share = Rs.37,800 per lot; margin ~Rs.60,000; >50% return if IndusInd closes near 400 at May expiry", "best_regime": "High-IV stock ahead of results; next-month premium rich relative to risk", "adjustments": "Exit opportunity after the results; avoid holding the full month", "risks": "Very large move beyond the wings; one month is a long time in trading"}
- {"name": "Put-selling ladder in collapsing-VIX rebound", "construction": "Sold puts across strikes from ~6,100 to 9,000 during April 2020 recovery", "numbers": "April profit 66,30,478 on ~95L capital; VIX 80-85 -> 55-60 -> ~40; June 9000PE sold at 500, closed 180", "best_regime": "post-crash VIX collapse with market refusing to make new lows", "adjustments": "not detailed in this episode", "risks": "windfall not repeatable; VIX normalizes; requires conviction view"}
- {"name": "Long-dated index option buying on IV collapse", "construction": "Deployed 60-70 lakh across December 2020 Nifty options (puts and calls), holding 30-40 lakh cash for adjustments", "numbers": "+~1 lakh/day for three consecutive days (~3% on deployed capital) as IV fell from ~30 to ~20", "best_regime": "Post-panic IV compression with market stabilization", "adjustments": "Keep 30-40% dry powder for adjustments", "risks": "Time decay if IV stays low and market ranges; long options bleed without direction"}

*Sources: 22 transcripts*
---

# Chapter 12: Margins, Collateral and the Machinery

Margins are the capital required to hold a derivatives position. They are also the single biggest constraint on position sizing, and understanding them separates professional traders from amateurs.

*Sources: 0 transcripts*
---


# Part IV: The Strategy Library

# Chapter 13: Short Straddles & Strangles

Short straddles and strangles are the workhorses of the option seller. The principle is simple: collect premium and manage risk. The execution requires constant vigilance.

## Themes
- diversification across strikes and expiries
- technical vs fundamental analysis
- crude oil OMC inverse relation
- position movement with market
- limited-risk credit structure
- implied volatility comparison

## Strategies
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "VIX-based expected-move strangle placement", "construction": "Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%", "numbers": "VIX 60 -> monthly band ~17.3%; spot 8,000 -> sell puts below ~6,500, calls above ~9,500; May 8,000 straddle ~1,600 (~20% for 37 trading days)", "best_regime": "Elevated VIX (crisis); recompute daily as VIX moves", "adjustments": "None stated - guideline framing, refresh band as VIX changes", "risks": "Band is statistical, not a wall; theta/other factors shift premiums; violent moves can exceed the band"}
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Cash Secured Put", "construction": "Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery", "numbers": "Bajaj Finance 1800PE sold at Rs.100 (2 lots, Rs.50,000 collected); Nifty Apr 7500PE ~Rs.57; Dec-2020 6000PE ~Rs.200; ~Rs.19 lakh premium collected; claimed Rs.45 lakh FY21 P&L in 3 weeks", "best_regime": "Sideways-to-up markets, or when you want a lower entry price in a quality stock", "adjustments": "Square off the put and buy shares in the open market instead of physical delivery; exit any time before expiry", "risks": "Profit capped at premium; stock can fall far below strike; requires full cash backing of the strike"}

*Sources: 30 transcripts*
---

# Chapter 14: Controlled Direction: Spreads & Ratio Spreads

When the view is directional but not extreme, spreads limit both risk and reward. Ratio spreads tilt the payoff toward one side while keeping defined loss boundaries.

*Sources: 0 transcripts*
---

# Chapter 15: Calendar Spreads

Calendar spreads exploit the different rates at which near-term and far-term options decay. They are the purest expression of time as a trading edge.

## Themes
- technical vs fundamental analysis
- implied volatility term structure
- limited-risk credit structure
- index heavyweight catch-up
- stock lending & borrowing
- defined-risk structures

## Strategies
- {"name": "Bank Nifty rollover analysis", "construction": "Long (or short) futures rolled monthly", "numbers": "~100 pts typical next-month premium; ~1,200 pts (~5-6%) cost per year for longs; shorts collect it", "best_regime": "Long-term shorts benefit from rollover premium; long-term longs should buy cash instead", "adjustments": "Hedging is cheaper on futures than on cash positions", "risks": "Premium varies 40-200 pts monthly; longs underperform cash by the premium"}
- {"name": "ITM put calendar (low-VIX regime)", "construction": "sell current-month ITM put (16,000PE July), buy same strike far-month put (16,000PE December) as the hedge", "numbers": "July PE 350->150 (+200); Dec PE 580->490 (-90); net ~+110 = ~5,000 rupees/lot; margin ~50,000; ~10% in 3 weeks; back-office: sold 1,250 qty +1.1 lakh, bought 750 qty -54k, net +55k", "best_regime": "India VIX at multi-year lows, quiet drift up or sideways", "adjustments": "exit early if VIX regime turns; keep partial hedge ratio honest (he ran 1,250 short vs 750 long)", "risks": "sharp VIX spike hits the short leg; partial hedging leaves crash exposure; far-month liquidity is thin"}
- {"name": "Long-dated combo: call ratio + cash-secured put (Dec-2022 expiry)", "construction": "Sell ~500 qty 15,000PE; buy 250 qty 18,000CE; sell 500 qty 20,000CE (i.e., 1 call ratio + 1 cash-secured put)", "numbers": "Entered ~Nov 2021 with Nifty ~18,000; premiums ~350/1600/800; breakevens ~14,500 and ~22,700; margin ~\u20b91.5 lakh; target return 20-25% on margin", "best_regime": "Neutral-to-bullish one-year view with wide safety band", "adjustments": "Beyond 20,000-22,000, roll the short calls upward in stages to recapture upside ('a general adjustment technique taught in detail')", "risks": "Loss below ~14,500 (accepts assignment \u2014 wants to buy there); upside capped above 22,000 unless adjusted"}
- {"name": "Post-crash call ratio (Dec-2021)", "construction": "Buy 17,700CE, sell 2x 18,300CE after Nifty's ~900-point fall", "numbers": "Entered at equal premium (600 vs 300x2) \u2192 near-zero downside loss (~\u20b92,000 on current marks); profit if Nifty recovers up to ~18,800", "best_regime": "After a sharp fall when recovery odds are good", "adjustments": "If market rips beyond 18,800, roll or square the shorts", "risks": "Upside beyond upper strike; small absolute downside already built in"}
- {"name": "ETH long call ratio + short puts", "construction": "Buy 3000CE; sell 5000CE x3; sell 2000PE x2", "numbers": "Margin $1,200; +$420 (~35%) in under 3 months (~10%/month)", "best_regime": "Range-bound high-IV crypto", "adjustments": "None - held", "risks": "Upside caps at 5000; downside naked put x2"}

*Sources: 13 transcripts*
---

# Chapter 16: Butterflies & Condors

Butterflies concentrate the profit zone into a narrow range. They are the sniper's approach: precise, limited risk, and requiring a tight view on where the market will settle.

## Themes
- limited-risk structures
- position management
- long-term options
- volatility crush
- butterfly spread
- position review

## Strategies
- {"name": "Put back spread", "construction": "sell 1x ATM+100 put; buy 2x ATM-200 puts (Nifty ~13,600: sell 13,700PE, buy 2x 13,400PE)", "numbers": "lower breakeven ~13,253 vs straddle's 13,162; max loss ~Rs 20,000 vs straddle ~Rs 32,000; margin ~Rs 1 lakh", "best_regime": "bearish into event; profits only on large falls", "adjustments": "roll or convert with far put", "risks": "sideways market loses the debit; margin understated by platforms"}
- {"name": "Call back spread", "construction": "sell 1x ATM-100 call; buy 2x ATM+200 calls", "numbers": "profit begins ~14,000 vs straddle 14,050; max loss ~Rs 20,000", "best_regime": "bullish into event", "adjustments": "same mirror logic", "risks": "small loss on big fall; sideways loses"}
- {"name": "Put ratio spread", "construction": "buy 1x ATM put (~Rs 175); sell 2x puts ~250-350 lower", "numbers": "max profit ~Rs 18,000-19,000 near 13,300-13,350; loss begins below ~13,100 and is uncapped; upside loss ~Rs 1,000", "best_regime": "mildly bearish; expects limited fall", "adjustments": "buy far OTM put to cap risk (butterfly)", "risks": "crash below short strikes = uncapped loss"}
- {"name": "Put butterfly (capped ratio)", "construction": "put ratio + buy 1x far OTM put (12,800)", "numbers": "max loss ~Rs 23,000 only below 12,800 (-7.8% in a day - unlikely); upside loss ~Rs 1,000; margin ~Rs 54,000+/-10k", "best_regime": "defined-risk bearish event trade", "adjustments": "exit shorts on rally", "risks": "capped but wide loss zone"}
- {"name": "Call ratio spread", "construction": "buy 1x ATM call; sell 2x calls 200 higher; optional far OTM call for cap", "numbers": "loss begins above ~14,000; upside profit if rally exceeds upper strikes", "best_regime": "'budget like never before' bullish bets", "adjustments": "convert to butterfly", "risks": "uncapped loss above short strikes"}

*Sources: 5 transcripts*
---

# Chapter 17: Portfolio Hedges

A hedge that does not exist is no hedge at all. Real hedging costs money — and that cost must be budgeted as insurance, not as friction to be avoided.

## Themes
- crude oil OMC inverse relation
- multi-strategy capital pools
- margin unfairness to hedgers
- futures vs options overlay
- margin architecture reform
- defined-risk construction

## Strategies
- {"name": "Infosys earnings iron fly with financed wings", "construction": "Sell 650CE + 650PE (5 lots); buy 720CE + 580PE; sell 2x 750CE (10 lots) and 2x 550PE to finance the wings", "numbers": "650CE @31, 650PE @27.50, 720CE @7.35, 580PE @8.40, 750CE @4, 550PE @4.46; max profit ~Rs.3.58 lakh (~15%) if Infosys closes at 650; protection 710 up / 590 down", "best_regime": "Results eve with elevated implied volatility", "adjustments": "Exit after results or keep far wings with a stop-loss; watch volatility crush", "risks": "Beyond 750/550 the financing legs turn the risk unlimited again; overnight gap risk"}
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Futures + rolling short straddle on a long-term holding", "construction": "Long monthly future; sell ATM calls; convert to straddles; roll puts lower as market falls (1460->1440); add 1520C", "numbers": "entry 1422, May-2020 series; +159,186 total vs ~35-40k unhedged; margin <=5 lakh vs 15 lakh cash", "best_regime": "long-term bullish holding with two-way volatility", "adjustments": "square and re-strike puts on reversals; roll future at ~1 point cost in bearish tape", "risks": "gap risk on naked legs; assignment/roll slippage"}
- {"name": "Hedged short put", "construction": "Sell near put + buy a further-OTM put same expiry", "numbers": "Speaker example: sold 9400-put style positions; hedge put cuts margin drastically and caps loss", "best_regime": "Any short-put view; mandatory insurance", "adjustments": "Not advised live; know risk-reward before entry", "risks": "Unhedged version: margin cascade and uncapped gap risk"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}

*Sources: 30 transcripts*
---

# Chapter 18: Firefighting & Adjustments

No trade survives contact with the market. Firefighting — the art of adjusting a position under duress — is what separates professionals who lose slowly and recover from amateurs who lose permanently.

## Themes
- position movement with market
- case study with daily data
- futures vs options overlay
- portfolio diversification
- short strangle adjustment
- put selling into strength

## Strategies
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "IndusInd earnings-day iron-fly style combo", "construction": "Sell 400CE + sell 400PE, buy 500CE + buy 300PE (current month)", "numbers": "profit down 77% vs expected 95% fall; stock closed ~15-17% higher", "best_regime": "earnings day when heavy short positioning built up", "adjustments": "speaker's own adjustments not disclosed; states adjustments depend on additional capital", "risks": "big gap moves on expiry; adjustments need reserve capital"}
- {"name": "Call ratio spread (financed directional)", "construction": "Long 1x 9400CE; short 2x 9800CE; short 1x 10000CE (300/600/300 qty), plus weekly far-OTM call sales to offset net debit", "numbers": "9400CE ~219; 9800CE ~80; 10000CE ~45; net ~-4300 before weekly sales (~+2800 after); max profit ~1,15,000 at 9800 expiry; loss begins ~10,080", "best_regime": "Mildly bullish, expect stay below written strikes", "adjustments": "Promised follow-up through expiry; weekly-call sales used to neutralize debit", "risks": "Unlimited above 10,080 (net short top strike); upside capped at 9800 zone"}
- {"name": "OTM credit-sale adjustment on a losing ratio", "construction": "Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65", "numbers": "Pre-adjustment loss ~Rs 3,000; post-adjustment profit ~Rs 2,000 per lot", "best_regime": "After a results miss confirms the directional view is dead", "adjustments": "Collected credit exceeds the defined max loss; no further action needed unless stock reverses hard", "risks": "New short call adds upside risk; acceptable because view is now neutral-bearish"}
- {"name": "Cash-secured puts (ICICI 300PE, HDFC 840PE)", "construction": "Sell puts below market with full cash set aside for delivery", "numbers": "+33,000 ICICI and +28,000 HDFC in May 2020", "best_regime": "moderately bullish with stocks near support", "adjustments": "take delivery if assigned; roll if view changes", "risks": "sharp breakdown below strike forces delivery at loss"}

*Sources: 30 transcripts*
---


# Part V: Trading the Events

# Chapter 19: The Event Playbook

Markets behave differently around scheduled binary events: budgets, elections, central bank decisions, and macroeconomic data releases. The strategy must adapt to the event itself.

## Themes
- US politics as market catalyst
- FII taxation treaty arbitrage
- implied volatility comparison
- bearish combo retrospective
- narrative misinterpretation
- cash-settlement-vs-delivery

## Strategies
- {"name": "Infosys earnings iron fly with financed wings", "construction": "Sell 650CE + 650PE (5 lots); buy 720CE + 580PE; sell 2x 750CE (10 lots) and 2x 550PE to finance the wings", "numbers": "650CE @31, 650PE @27.50, 720CE @7.35, 580PE @8.40, 750CE @4, 550PE @4.46; max profit ~Rs.3.58 lakh (~15%) if Infosys closes at 650; protection 710 up / 590 down", "best_regime": "Results eve with elevated implied volatility", "adjustments": "Exit after results or keep far wings with a stop-loss; watch volatility crush", "risks": "Beyond 750/550 the financing legs turn the risk unlimited again; overnight gap risk"}
- {"name": "Post-earnings leg-by-leg review of the hedged straddle", "construction": "650CE/PE sold; 720CE/580PE long; 750CE/550PE sold 2x - each leg marked after the results", "numbers": "Total +8.95/share = Rs.10,740 per lot (lot 1200); margin ~Rs.7.24 lakh after benefits for the 5-lot structure; ~1.5% in a day; projected ~4% in two weeks", "best_regime": "Immediately after results, when volatility crush pays all sold legs", "adjustments": "Closed the 650/720 and 650/580 pairs; kept 750CE/550PE with a stop-loss", "risks": "Far wings are effectively naked beyond 750/550"}
- {"name": "IndusInd Bank earnings hedged straddle (May series)", "construction": "Sell May 400CE @62 + 400PE @52; buy current-month 500CE @4.25 + 300PE @5.25 as protection", "numbers": "Net premium ~Rs.94.55/share = Rs.37,800 per lot; margin ~Rs.60,000; >50% return if IndusInd closes near 400 at May expiry", "best_regime": "High-IV stock ahead of results; next-month premium rich relative to risk", "adjustments": "Exit opportunity after the results; avoid holding the full month", "risks": "Very large move beyond the wings; one month is a long time in trading"}
- {"name": "IndusInd earnings-day iron-fly style combo", "construction": "Sell 400CE + sell 400PE, buy 500CE + buy 300PE (current month)", "numbers": "profit down 77% vs expected 95% fall; stock closed ~15-17% higher", "best_regime": "earnings day when heavy short positioning built up", "adjustments": "speaker's own adjustments not disclosed; states adjustments depend on additional capital", "risks": "big gap moves on expiry; adjustments need reserve capital"}
- {"name": "ICICI Bank call ratio (1x2) for earnings", "construction": "Buy 1 lot 350CE at ~2,440; sell 2 lots 380CE at ~1,190", "numbers": "near-zero net cost (~40-50 paise paid); max loss downside ~825; max profit zone 350-380; unlimited risk above 410; margin ~1.5 lakh net (2.53 lakh naked 380CE)", "best_regime": "mildly bullish stock pinned below known resistance into results", "adjustments": "not shown in this episode; speaker flags adjustment need if it gaps above 410", "risks": "gap above the sold strike doubles exposure; earnings gaps both ways"}

*Sources: 30 transcripts*
---

# Chapter 20: Budgets and Elections

Budgets and elections are the two recurring events where policy intersects with markets most directly. The playbook for each is different, and the lessons from past cycles are directly applicable to the next one.

## Themes
- mean reversion after down years
- US politics as market catalyst
- valuation premium compression
- FII taxation treaty arbitrage
- crisis cycle every 8-10 years
- political stability premium

## Strategies
- {"name": "Budget-day posture rule", "construction": "close positions before Feb 1 unless skilled in adjustments", "numbers": "Bank Nifty fell 1,800 points in two days of profit booking; Nifty 14,660->14,250->14,780 swings", "best_regime": "before binary events", "adjustments": "skilled traders may hold and adjust", "risks": "event gap against the position"}
- {"name": "Long-dated Nifty short strangle (annual range)", "construction": "Sold December-2022 15,000 put and 21,000 call", "numbers": "Combined premium ~700 points (~35,000 per lot); margin ~1.8 lakh initially, easing to 80-90k later; already ~100 points in profit at recording", "best_regime": "Wide VIX-implied annual range with no intent to predict direction", "adjustments": "None needed unless a boundary approaches; long-dated structure ignores short-term news", "risks": "Both sides breached in an extreme year; margin lock-up for 12 months"}
- {"name": "TCS earnings call-ratio with double caps (iron-fly-like credit structure)", "construction": "Buy 1x 3,600 CE; sell 3x 3,800 CE; buy 2x 4,000 CE; sell 2x 3,400 PE; buy 2x 3,200 PE (10 lots total, basket order at market)", "numbers": "Margin ~Rs.1,22,000 (vs ~Rs.2 lakh uncapped); max profit ~Rs.30,000 at ~3,800 close (>30% on margin); POP ~68%; breakevens ~3,400-3,900; max loss ~Rs.59,000; profit zone 3,400-3,900", "best_regime": "Earnings week with an expected favorable result but capped macro upside (war + Fed overhang)", "adjustments": "Exit or run to expiry based on Tuesday's gap reaction; update promised on close", "risks": "Gap beyond 3,900 breaks the call wing; below 3,400 the put wing bleeds; earnings gaps are binary"}
- {"name": "VIX-implied annual range targeting", "construction": "Take India VIX % as expected annual move; apply to current Nifty level for upside target; confirm with ATM straddle premium (call+put sum)", "numbers": "VIX 15 -> 18,000 + 2,700 = ~20,700-21,000; 19,000 straddle collecting 2,100 -> upper risk 21,100; straddle sold @3,000 a month earlier", "best_regime": "Start-of-year positioning; also validates short-straddle strike selection", "adjustments": "If VIX rises, premiums and ranges expand; roll strikes accordingly", "risks": "VIX is symmetric - implies downside too; range 15,000-21,000 acknowledged"}
- {"name": "Long-dated short straddle + wings (position disclosed)", "construction": "Sold December-expiry 19,000 and 18,000 short straddles; sold 16,000 put and 20,000 call as wings", "numbers": "profit driven by falling India VIX and range-bound tape", "best_regime": "declining VIX, sideways-to-down market", "adjustments": "not stated", "risks": "big directional move breaks the straddle; wings cap tail loss"}

*Sources: 30 transcripts*
---

# Chapter 21: Wars, Crashes and Black Swans

Wars, global crashes, and black swan events test every assumption a trader holds. Survival in these moments depends on preparation, not prediction.

## Themes
- evidence and international support
- strength-to-weakness inversion
- US politics as market catalyst
- Supreme Court moratorium case
- national security commentary
- efficient market hypothesis

## Strategies
- {"name": "Multi-strike, multi-expiry put selling (April 2020)", "construction": "Sold put options spread across various strike prices and expiry periods rather than one strike", "numbers": "7500PE sold around Rs.75 during a morning dip; SGX Nifty ~9200 vs ~9000 close", "best_regime": "Ultra-bearish consensus with the negative surprise already announced", "adjustments": "Exited or rolled by expiry; profit disclosed in a later review video", "risks": "Losses if the market breaks below the sold strikes; premium is the cap on profit"}
- {"name": "Staggered index investing with cash-secured puts", "construction": "SIP into a Nifty 50 ETF; optionally place cash-secured puts at desired lower entries", "numbers": "Nifty PE ~16 (May 2020); historical buy zone 15-16, sell zone 28-30; Dow 1929 crash ~90%; 1982-2000 bull ~15x", "best_regime": "Post-crash pessimism; long horizon", "adjustments": "Add on further 5-10% falls", "risks": "Multi-year drawdowns; requires no-liquidity-needs capital"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}
- {"name": "Long-dated index option buying on IV collapse", "construction": "Deployed 60-70 lakh across December 2020 Nifty options (puts and calls), holding 30-40 lakh cash for adjustments", "numbers": "+~1 lakh/day for three consecutive days (~3% on deployed capital) as IV fell from ~30 to ~20", "best_regime": "Post-panic IV compression with market stabilization", "adjustments": "Keep 30-40% dry powder for adjustments", "risks": "Time decay if IV stays low and market ranges; long options bleed without direction"}
- {"name": "Long put (directional / insurance)", "construction": "Buy put below spot (e.g., Nifty 22,000 PE at ~\u20b9136 with spot ~22,358); or buy 1 put per portfolio lot before events", "numbers": "Max loss = premium (~\u20b913,600/lot as stated); breakeven 21,864; large downside profit", "best_regime": "Bearish catalysts: bad results, elections, macro shocks; or event insurance on holdings", "adjustments": "Exit into the crash or hold as hedge; roll down/out", "risks": "Time decay; quiet markets bleed premium; IV already high reduces payoff"}

*Sources: 30 transcripts*
---


# Part VI: A Market Chronicle 2018–2026

# Chapter 22: 2018–2020: Tariff Tantrums, a Crash, and a Miracle

The period from 2018 to 2020 saw a trade war, a domestic credit crisis, a global pandemic, and the fastest crash and recovery in market history. Each phase teaches something about how markets absorb shock.

*Sources: 0 transcripts*
---

# Chapter 23: 2021–2022: Liquidity Boom, Inflation Bust

The liquidity-driven bull run of 2021 gave way to the inflation-driven bust of 2022. FIIs sold more than ever before, yet the market found a floor each time. Understanding why is essential.

*Sources: 0 transcripts*
---

# Chapter 24: 2023–2024: The Bull Run and Its First Crack

The bull market matured in 2023-24 as VIX hit multi-year lows and Nifty climbed methodically. The post-election crash of June 2024 and the relentless FII selling revealed the structural churn beneath the surface.

*Sources: 0 transcripts*
---

# Chapter 25: 2025–2026: Tariffs, Jane Street and the New Regime

Tariffs reshaped global trade flows, Jane Street's regulatory case exposed loopholes in index arbitrage, and SEBI's F&O restrictions began reshaping Indian derivatives markets. The regime is changing.

*Sources: 0 transcripts*
---


# Part VII: Predators & Protectors

# Chapter 26: How Retail Gets Cheated

For every legitimate opportunity in markets, there is a predatory scheme designed to exploit retail traders. Understanding the mechanics of these schemes is the first defence.

## Themes
- evidence and international support
- margin unfairness to hedgers
- stock lending and borrowing
- romance and fake-app fraud
- business failure vs fraud
- influencer responsibility

## Strategies
- {"name": "Sell-half-keep-half IPO strategy", "construction": "Apply minimum at cutoff via ASBA; on listing at 2x, sell 50% to recover principal", "numbers": "Mazagon Dock: lot 103 (~\u20b914,935), retail cap 13 lots (~\u20b91.94L), band 135-145, listing 12 Oct 2020", "best_regime": "Hot primary markets with quality PSU/defence paper", "adjustments": "None - it's a one-decision rule", "risks": "Duds like Reliance Power (\u20b9450 effective \u2192 \u20b94) - hence cost recovery first"}
- {"name": "Hedged monthly book through expiry stress", "construction": "Directional futures/option legs + offsetting call hedges + occasional ratio spreads", "numbers": "Sep: BN -5.5L, hedges +1.5L, ratio +1.18L, ITC hedging +2.23L, Nifty +1.4L, SBI +38K, Sensex -2L \u2192 ~+10L on ~\u20b91 cr capital", "best_regime": "Volatile series where directional legs bleed", "adjustments": "Hedge in the next series when current-series data ends; move hedges to liquid proxies", "risks": "Illiquidity in new instruments (Sensex options) causes slippage and forced proxy hedging"}
- {"name": "High-beta stock short straddle with strike ladder", "construction": "1,540 short straddle, then 1,520 and ~1,530 straddles added as price fell; puts 1,400 strike in second account; 10 lots total across accounts", "numbers": "~18 lakh month profit on ~2 crore deployed (~9-10%/month); single straddle lot margin ~5 lakh; realized put losses -4.66 lakh and -4 lakh absorbed by ladder", "best_regime": "high IV, event-heavy large-cap stock", "adjustments": "re-center straddles as price moves; stagger across strikes/accounts; keep ~75% margin un-deployed for rescue", "risks": "single-stock crash through both strikes; physical settlement; ban-period lockouts"}
- {"name": "Crypto premium selling (beginner account)", "construction": "Sold BTC 55,000 put, bought 58,500 call; sold ETH 5,000 call (near expiry); sold BTC 48,000 put - all on a 2,000 USDT trading credit", "numbers": "Capital 2,000 USDT to ~2,900 in a month (~45%); gross 1,200, net 900 after ~300 in charges; BTC Mar-2022 100k call fell from ~5,000 to ~2,000; 20,000 put from ~500 to ~150; Dec 80,000 call ~687", "best_regime": "High-IV crypto markets; wide expected ranges", "adjustments": "None described - amateur discretionary selling", "risks": "Unregulated exchange, counterparty risk; premiums can expand violently (India ban news dropped local BTC/ETH 20% in a day); high fees"}
- {"name": "Cost-audit of a typical intraday iron-fly money-manager operation", "construction": "Sell ATM straddle + buy 1,000-1,500 point wings (Bank Nifty ~39,100); ~60,000 margin per lot set; 15 lot sets on 10 lakh capital; squared off daily", "numbers": "120 lots/day x 12 rupees brokerage = ~1,800/day = 4.5 lakh/year; STT+stamp ~3 lakh/year; slippage ~2.5 lakh/year; total ~10 lakh = entire capital; manager's own equivalent costs ~1,000/month", "best_regime": "Audit template for anyone evaluating a money manager", "adjustments": "N/A", "risks": "Client returns are negative before strategy risk even begins"}

*Sources: 30 transcripts*
---

# Chapter 27: The Regulator's Dilemma

SEBI faces a thankless task: protect the retail trader without strangling the market. The evolution of margin rules, expiry systems, and F&O regulations tells the story of this balancing act.

## Themes
- system vs discretionary traders
- FII taxation treaty arbitrage
- margin unfairness to hedgers
- intraday leverage phase-out
- banker's guarantee loophole
- margin architecture reform

## Strategies
- {"name": "Hedged short option (spread)", "construction": "Sell 10,000C / buy 10,200C (200pt); variants 300-400pt", "numbers": "~25,000-32,000 margin vs 80-90k naked; max risk = spread width", "best_regime": "any directional credit view", "adjustments": "roll wings as market trends", "risks": "max loss = width x lot; premium give-up"}
- {"name": "Short straddle with far wings", "construction": "Sell 9,500CE+9,500PE (July), buy 8,500PE+10,500CE (June weekly/next series)", "numbers": "margin ~45,000-55,000 after ~40-60k premium receivable; straddle premium >1,000 pts in July 2020", "best_regime": "high-IV months with distant wings affordable", "adjustments": "re-buy expired wings weekly", "risks": "gap through wings; weekly-wing rollover friction"}
- {"name": "ITM put calendar", "construction": "Sell 10,000PE current month, buy 10,000PE next month", "numbers": "margin <30,000", "best_regime": "neutral-to-mildly-bearish", "adjustments": "roll short leg at expiry", "risks": "fast rallies inflate long-leg decay loss"}
- {"name": "Weekly far-OTM short puts into expiry (illustrative)", "construction": "Sell ~1,000-point OTM index puts ~3 sessions before weekly expiry", "numbers": "14,000PE sold ~\u20b920 with Nifty ~15,000; even 12,150PE (3,000 points away) traded ~\u20b90.75-0.85", "best_regime": "elevated IV caused by margin-driven supply squeeze", "adjustments": "with intraday limits gone, pre-fund reversal legs; run fewer lots", "risks": "peak-margin penalty, gap-through-strike risk, one-day crashes exceed 1,000 points only in Lehman/COVID-class events"}
- {"name": "BTC short strangle (live demo)", "construction": "Sold BTC 68,000 call (~711 USDT, 100 contracts = 0.1 BTC, 25x leverage, margin ~273 USDT) and sold BTC 36,000 put (~255 USDT margin) for late-January expiry", "numbers": "Expecting BTC to stay between 36,000 and 68,000 dollars; combined margin ~528 USDT", "best_regime": "Range-bound high-IV crypto; one-month horizon", "adjustments": "Exchange-native take-profit and stop-loss settings due to 24-hour trading", "risks": "Full margin loss on a breach of either breakeven; exchange/counterparty risk; 0.05% fee drag"}

*Sources: 30 transcripts*
---

# Chapter 28: Taxes

Taxation is the trader's largest single expense. The complexity of India's F&O tax regime — business income vs speculative, presumptive taxation, the STT spiral — demands attention upfront.

## Themes
- capital gains vs business income
- corporate vs personal taxation
- FII taxation treaty arbitrage
- secular stagnation examples
- public services comparison
- time decay proportionality

## Strategies
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Covered call via futures leg (margin-optimized)", "construction": "Hold long futures instead of physical shares; sell calls against it", "numbers": "Stated: span margin zero for the covered call against long futures; exposure margin ~2% index, ~3.5% stock options", "best_regime": "Large holders wanting option income without physical-settlement complexity", "adjustments": "Roll calls up as futures rally", "risks": "Futures MTM swings; margin calls if exposure margin rules change"}
- {"name": "Collateral ladder for option sellers", "construction": "Pledge Liquid BeES/debt funds (~90% collateral value); keep a small cash buffer for debit legs", "numbers": "Buy-side premium debits settle immediately; sell-side credits arrive next day - keep cash for combos", "best_regime": "All option sellers using collateral", "adjustments": "Top up cash before multi-leg strategies", "risks": "Settlement timing on multi-leg entries; penalty on shortfall"}
- {"name": "ETH wide short strangle + double far-call", "construction": "Sell $1,000PE 10 ETH @ $45.5; sell $4,000CE 10 ETH @ $17.5; sell $5,000CE 20 ETH @ $11.4", "numbers": "Margin ~$2,000 + $1,800 = ~$3,800; premium ~$858 total (~$1,000 as stated); ~25% for 2 months (~15%/month); September expiry", "best_regime": "Post-crash stabilization with IV falling; willing to take delivery at $1,000 put", "adjustments": "Update promised till September end", "risks": "Delivery obligation if ETH falls to $1,000; unlimited risk above $4,000-5,000"}
- {"name": "Prop-desk funding model (explanatory)", "construction": "Trader pays \u20b91 security deposit, gets \u20b95 trading capital from prop desk; P&L is trader's; desk charges ~12% interest", "numbers": "Desk earns 12% funding + 6-7% FD yield on margin + exchange turnover incentives \u2248 ~20% risk-free; est. \u20b92-3 lakh crore of such capital in the system \u2248 \u20b925,000 cr/yr drain", "best_regime": "n/a - explains where retail losses flow", "adjustments": "n/a", "risks": "Retail traders absorb funding cost plus their own losses; SEBI studies count retail only, not prop desks"}

*Sources: 30 transcripts*
---


# Part VIII: Wealth Beyond the Screen

# Chapter 29: Investing vs Trading

Trading and investing are different games with different tools and different scorecards. Confusing them is the fastest way to lose at both.

## Themes
- time correction vs price correction
- crude oil OMC inverse relation
- IPO strategy for small capital
- crisis cycle every 8-10 years
- valuation premium compression
- technical analysis skepticism

## Strategies
- {"name": "FD/collateral-backed premium recycling", "construction": "~25 lakh FD pledged; premiums from option selling recycled to absorb small booked losses without touching the FD", "numbers": "Example: 25 lakh FD collateral (as stated)", "best_regime": "Option sellers running multiple small premium streams", "adjustments": "Net small booked losses against premium inflows from other positions", "risks": "If booked losses exceed total premium received, cash injection is mandatory"}
- {"name": "Cash Secured Put", "construction": "Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery", "numbers": "Bajaj Finance 1800PE sold at Rs.100 (2 lots, Rs.50,000 collected); Nifty Apr 7500PE ~Rs.57; Dec-2020 6000PE ~Rs.200; ~Rs.19 lakh premium collected; claimed Rs.45 lakh FY21 P&L in 3 weeks", "best_regime": "Sideways-to-up markets, or when you want a lower entry price in a quality stock", "adjustments": "Square off the put and buy shares in the open market instead of physical delivery; exit any time before expiry", "risks": "Profit capped at premium; stock can fall far below strike; requires full cash backing of the strike"}
- {"name": "Staggered index investing with cash-secured puts", "construction": "SIP into a Nifty 50 ETF; optionally place cash-secured puts at desired lower entries", "numbers": "Nifty PE ~16 (May 2020); historical buy zone 15-16, sell zone 28-30; Dow 1929 crash ~90%; 1982-2000 bull ~15x", "best_regime": "Post-crash pessimism; long horizon", "adjustments": "Add on further 5-10% falls", "risks": "Multi-year drawdowns; requires no-liquidity-needs capital"}
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Bharat Bond as trading collateral", "construction": "Buy Bharat Bond ETF units; pledge to broker as collateral for F&O margins", "numbers": "~7.6% indicative 10yr yield; 20% LTCG with indexation >3yr; 5% haircut; EBBETF 0423 ~1019, EBBETF 0430 ~1050 (May 2020)", "best_regime": "declining interest rates; idle capital awaiting trade opportunities", "adjustments": "n/a", "risks": "rising rates compress price; credit concentration in PSU issuers"}

*Sources: 30 transcripts*
---

# Chapter 30: Hard Assets

Real estate, gold, and bonds offer diversification but come with their own risk-reward math that is very different from equity markets.

## Themes
- strength-to-weakness inversion
- political overhang discount
- cash-settlement-vs-delivery
- time decay proportionality
- exchange product pipeline
- real estate as investment

## Strategies
- {"name": "Bharat Bond as trading collateral", "construction": "Buy Bharat Bond ETF units; pledge to broker as collateral for F&O margins", "numbers": "~7.6% indicative 10yr yield; 20% LTCG with indexation >3yr; 5% haircut; EBBETF 0423 ~1019, EBBETF 0430 ~1050 (May 2020)", "best_regime": "declining interest rates; idle capital awaiting trade opportunities", "adjustments": "n/a", "risks": "rising rates compress price; credit concentration in PSU issuers"}
- {"name": "Liquid BeES cash-component collateral", "construction": "Buy Liquid BeES; pledge as the cash component of margin", "numbers": "price ~1,000 +/- 1 paisa; interest via additional units monthly; no STT/stamp duty", "best_regime": "any time idle capital sits in a trading account", "adjustments": "n/a", "risks": "haircut 10%; liquidity depth"}
- {"name": "Collateral-funded option selling (HNI pattern)", "construction": "Pledge debt mutual funds/bank FDs as collateral; sell options against the margin; keep interest as primary return", "numbers": "Stated pattern: 6-7% interest on debt funds while trading on pledged limit", "best_regime": "Wealthy, income-focused sellers who accept trading as a bonus stream", "adjustments": "Not applicable - structural allocation", "risks": "Trading losses eat the collateral cushion; interest is not guaranteed against credit events"}
- {"name": "Reverse arbitrage on futures discount", "construction": "Sell physical shares held in demat, buy the discounted futures; converge at expiry and reverse both", "numbers": "Example: stock 1000 spot vs 990 futures captures ~10 points", "best_regime": "Futures at significant discount (e.g., Nifty futures 80-90 points under spot)", "adjustments": "Hold to convergence", "risks": "Only works if shares already held; capital locked; convergence timing"}
- {"name": "Covered call via futures leg (margin-optimized)", "construction": "Hold long futures instead of physical shares; sell calls against it", "numbers": "Stated: span margin zero for the covered call against long futures; exposure margin ~2% index, ~3.5% stock options", "best_regime": "Large holders wanting option income without physical-settlement complexity", "adjustments": "Roll calls up as futures rally", "risks": "Futures MTM swings; margin calls if exposure margin rules change"}

*Sources: 30 transcripts*
---

# Chapter 31: Crypto as a Satellite

Cryptocurrency markets offer volatility that makes equity look sedate. They are best treated as a satellite allocation — sized small, strategies defined, and taxation understood in advance.

## Themes
- capital gains vs business income
- influencer responsibility
- correlation with equities
- broker counterparty risk
- small consistent returns
- crypto lender bankruptcy

## Strategies
- {"name": "Crypto premium selling (beginner account)", "construction": "Sold BTC 55,000 put, bought 58,500 call; sold ETH 5,000 call (near expiry); sold BTC 48,000 put - all on a 2,000 USDT trading credit", "numbers": "Capital 2,000 USDT to ~2,900 in a month (~45%); gross 1,200, net 900 after ~300 in charges; BTC Mar-2022 100k call fell from ~5,000 to ~2,000; 20,000 put from ~500 to ~150; Dec 80,000 call ~687", "best_regime": "High-IV crypto markets; wide expected ranges", "adjustments": "None described - amateur discretionary selling", "risks": "Unregulated exchange, counterparty risk; premiums can expand violently (India ban news dropped local BTC/ETH 20% in a day); high fees"}
- {"name": "BTC short strangle (live demo)", "construction": "Sold BTC 68,000 call (~711 USDT, 100 contracts = 0.1 BTC, 25x leverage, margin ~273 USDT) and sold BTC 36,000 put (~255 USDT margin) for late-January expiry", "numbers": "Expecting BTC to stay between 36,000 and 68,000 dollars; combined margin ~528 USDT", "best_regime": "Range-bound high-IV crypto; one-month horizon", "adjustments": "Exchange-native take-profit and stop-loss settings due to 24-hour trading", "risks": "Full margin loss on a breach of either breakeven; exchange/counterparty risk; 0.05% fee drag"}
- {"name": "Ethereum call ratio financed by short puts (long-term)", "construction": "Buy 1x ETH June 3000 call; sell 3x ETH June 5000 calls; sell 2x ETH June 2000 puts", "numbers": "3000 call cost ~760 USDT; net structure profit zone 3,000-5,000; upper breakeven ~6,160; lower breakeven ~1,850; ETH spot ~3,200", "best_regime": "Bullish long-term view on an asset far below its all-time high with wide time buffer (5+ months)", "adjustments": "Above 5,000: buy back the 3 sold 5000 calls and sell 9x 7000 calls (martingale roll-up); below 2,000: accept delivery or adjust", "risks": "Violent downside break hurts the short puts; upside beyond 6,160 erodes profit"}
- {"name": "Bitcoin wide-breakeven combo (June)", "construction": "Buy 1x BTC 35,000 call; sell 2x 50,000 calls; sell 1x 55,000 call; buy 1x 25,000 put; sell 2x 20,000 puts", "numbers": "35,000 call ~7,500 USD premium; margin ~1,500 USD at 25x leverage (750 at 50x, 375 at 100x); expiry breakevens ~15,000 and ~60,000; T+1 profitable zone ~20,000-38,000", "best_regime": "Post-crash stabilization with elevated IV; expecting a wide range, not a breakout", "adjustments": "None detailed; monitor via what-if analysis", "risks": "Move beyond 60,000 (or below 15,000) creates losses; thin crypto option liquidity widens spreads"}
- {"name": "Short straddle - crypto vs index comparison", "construction": "Sell ATM call + ATM put at same strike (BTC 40,000 vs Bank Nifty ~37,500)", "numbers": "Bank Nifty ATM straddle ~2,400-2,500 pts premium; BTC ATM straddle ~$6-7K at $40K BTC; deep OTM premium ~100x richer on crypto (\u20b93 vs $331 at similar distance)", "best_regime": "range-bound high-IV markets; crypto especially rich due to new-asset risk premium", "adjustments": "rolling/adjustment process when trending; platform 'move contract' packages the straddle as one instrument", "risks": "violent moves beyond premium; crypto is more volatile - premium is compensation for real risk"}

*Sources: 30 transcripts*
---


# Appendices

## A. Glossary

*To be expanded*

## B. Strategy Quick-Reference Tables

*To be expanded*

## C. Timeline of Verified Market Events 2018–2026



## D. Sources & Verification Notes

*Verification performed via web search on OpenRouter, August 2026.*

## E. Correction Log

*Material speaker-claim corrections are noted per-chapter above.*
