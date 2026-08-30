# Chapter 18: Firefighting: Rescue and Adjustment

*Source transcripts: 47*
*Top themes: firefighting, position sizing, short straddle, adjustments, hedging*
*Strategy recipes: 8*
*Verified events matched: 0*

## Key Lessons (by frequency)
- [1×] In violent markets, far-OTM options can move opposite to the index because traders buy them to cut margin - premium behavior beats price intuition.
- [1×] After a global selloff, any good news triggers violent short covering - position for the squeeze, not the narrative.
- [1×] Small-net-credit ratio structures can carry 81% probability with a few-thousand-rupee payoff - size for the risk, not the reward.
- [1×] When everything hinges on one event, that event is the only variable worth tracking (budget, budget, budget).
- [1×] Never deploy all margin in a strangle; spare cash lets you sell closer strikes without buying back the far leg at the worst price.
- [1×] Short strangle is called the most dangerous strategy - unlimited one-sided loss with both legs naked.
- [1×] Margin-release mechanics (square far leg, sell nearer leg) explain bid-ask distortions during panics.
- [1×] In a downtrend, a 100-125 point intraday bounce with no change in global cues is a short entry; mirror rule in uptrends.

## Strategy Setups
- **Budget-day ratio structure (live)**: sold 10x 14,700CE @8; sold 10x 13,500PE @137; bought 5x 13,800PE @avg 245
  - Risk: loss beyond 13,155 downside / 14,720 upside
  - Best regime: range-bound event day with bullish tilt
- **Strangle roll-under-stress mechanics**: Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8
  - Risk: Forced buyback at inflated premiums; whipsaw if the market reverses immediately
  - Best regime: After violent directional moves when the losing leg must be repositioned
- **Intraday fade-the-bounce rule**: Trend down: short 100-125 pts above intraday low; trend up: long 100-125 pts below intraday high
  - Risk: fails on trend-change days; news-driven reversals
  - Best regime: established trend, no fresh catalyst
- **Long-dated call ratio (bullish, financing legs)**: Buy 1 lot 16,000CE Dec-2023 @~2,450; sell 2 lots 20,000CE @~700 each; sell 3 lots 13,000PE @~285 (later rolled to 15,000PE as mark
  - Risk: Market below 13,000 breaks the put financing; above ~22,000 the short-call ratio
  - Best regime: Steady bull market with falling VIX; months of patience
- **Bank Nifty butterfly via basket order (demonstration)**: Buy 1 lot 39,700CE; sell 5 lots 40,300CE; buy 4 lots 40,800CE — all at market in one basket
  - Risk: Market-order slippage on illiquid far strikes
  - Best regime: Range-bound or mildly directional underlying

## Verified Events
(none directly matched)

## Notable Quotes (cleaned)
- "Create a strategy, but you need not hold it to expiry — if there is good profit in between, come out or adjust."
- "Option trading is a double-sided knife: drastic moves either way can cause unlimited loss."
- "If you are walking home it takes ten minutes; if a dog chases you, three - adjustments are where the profit is."

## Enhancement Callouts
- Standard worked examples per editorial guide (payoff tables, margin math)
- Where strategy recipes exist: add construction, breakevens, max P/L table
