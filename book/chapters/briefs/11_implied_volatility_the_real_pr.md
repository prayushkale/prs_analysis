# Chapter 11: Implied Volatility: The Real Price of Options

*Source transcripts: 22*
*Top themes: implied volatility, market efficiency, LEAPS, option basics, call options*
*Strategy recipes: 8*
*Verified events matched: 0*

## Key Lessons (by frequency)
- [1×] Never deploy all margin in a strangle; spare cash lets you sell closer strikes without buying back the far leg at the worst price.
- [1×] Short strangle is called the most dangerous strategy - unlimited one-sided loss with both legs naked.
- [1×] Margin-release mechanics (square far leg, sell nearer leg) explain bid-ask distortions during panics.
- [1×] The ATM straddle premium as % of spot IS the market's expected move: sellers profit if the actual move stays inside it, buyers only outside it.
- [1×] Post-results IV crush can hand sellers profit even on a 2% gap because fear premium deflates faster than delta moves.
- [1×] Check the ADR/US listing reaction after hours before the next Indian session to pre-read the open.
- [1×] Implied volatility is almost always higher than historical volatility - paying full straddle premium around events is structurally losing.
- [1×] Across 10 budgets, Nifty never closed more than 2% from the prior close except the COVID-coinciding 2020 budget (-3.26%).

## Strategy Setups
- **Strangle roll-under-stress mechanics**: Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8
  - Risk: Forced buyback at inflated premiums; whipsaw if the market reverses immediately
  - Best regime: After violent directional moves when the losing leg must be repositioned
- **Earnings short straddle (framework)**: Sell ATM call + ATM put just before results; compare combined premium to spot to get expected move
  - Risk: Gap beyond expected move hits naked shorts hard; assignment/gap risk on single s
  - Best regime: When you believe realized move < implied move; high IV into events
- **Put back spread**: sell 1x ATM+100 put; buy 2x ATM-200 puts (Nifty ~13,600: sell 13,700PE, buy 2x 13,400PE)
  - Risk: sideways market loses the debit; margin understated by platforms
  - Best regime: bearish into event; profits only on large falls
- **Call back spread**: sell 1x ATM-100 call; buy 2x ATM+200 calls
  - Risk: small loss on big fall; sideways loses
  - Best regime: bullish into event
- **Put ratio spread**: buy 1x ATM put (~Rs 175); sell 2x puts ~250-350 lower
  - Risk: crash below short strikes = uncapped loss
  - Best regime: mildly bearish; expects limited fall

## Verified Events
(none directly matched)

## Notable Quotes (cleaned)
- "When IV is low, your buy option is cheaper - so a combination will work out."
- "The expectation will shoot up... though he has not hit the century, the premium rises as he scores more runs."
- "In IndusInd, the long strangle can be in the current month to reduce the cost."

## Enhancement Callouts
- Standard worked examples per editorial guide (payoff tables, margin math)
- Where strategy recipes exist: add construction, breakevens, max P/L table
