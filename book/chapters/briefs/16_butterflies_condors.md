# Chapter 16: Butterflies & Condors

*Source transcripts: 5*
*Top themes: crypto, Bitcoin, call butterfly, event strategy, back spread*
*Strategy recipes: 8*
*Verified events matched: 0*

## Key Lessons (by frequency)
- [1×] Long-term, non-directional trades with wide breakevens can out-return fast weekly decay trades.
- [1×] When the trend flips, close the old view - a bullish combo closed at +8% funded the bearish book.
- [1×] Run double ratios (call ratio + put ratio) when direction is unknown; margin ~Rs 1.5L for ~13% in a month.
- [1×] Review every posted trade publicly - wins and losses - to build trust.
- [1×] Implied volatility is almost always higher than historical volatility - paying full straddle premium around events is structurally losing.
- [1×] Across 10 budgets, Nifty never closed more than 2% from the prior close except the COVID-coinciding 2020 budget (-3.26%).
- [1×] Back spreads cut max loss by a third versus long straddles and win big only on large moves in one direction.
- [1×] If worried about uncapped ratio-spread risk, buy one far OTM option and convert to a butterfly.

## Strategy Setups
- **December double ratio**: Buy 19,000CE x1, sell 20,000CE x2 (call ratio); buy 21,000PE x1, sell 20,000PE x2 (put ratio)
  - Risk: pin risk at 20,000; unlimited beyond wings
  - Best regime: no directional view, elevated premiums
- **Results-day vol-crush strangle (SBI)**: Buy ~600PE @20; sell 550PE and 650CE around results
  - Risk: gap beyond wings on surprise results
  - Best regime: post-results IV crush
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
- "Create a strategy, but you need not hold it to expiry — if there is good profit in between, come out or adjust."
- "The implied volatility is always higher than the historical volatility."
- "The market did not go anywhere. It has been just consolidating between $81,000 and $95,000"

## Enhancement Callouts
- Standard worked examples per editorial guide (payoff tables, margin math)
- Where strategy recipes exist: add construction, breakevens, max P/L table
