# Chapter 15: Time Is the Trade: Calendar Spreads

*Source transcripts: 13*
*Top themes: put calendar, calendar spread, calendar spreads, call ratio, long-dated options*
*Strategy recipes: 8*
*Verified events matched: 0*

## Key Lessons (by frequency)
- [1×] Two supertrend lines (20-day/5-day) proxy monthly and weekly trends; alignment defines regime.
- [1×] Trends historically persisted 10-12 weeks; extensions beyond that signaled outsized continuation rallies (post-COVID, post-inflation).
- [1×] A deep-ITM put calendar converts a bullish view into low-margin, capped-risk exposure; roll-over cost (~₹3,500-4,000/month) is the real max risk.
- [1×] Effective margin = gross margin minus next-day premium credit - check net, not gross, returns.
- [1×] India VIX at multi-year lows is the most dangerous regime for pure option sellers - one VIX spike erases months of theta.
- [1×] In low VIX, always pair buys with sells so a volatility spike cushions both legs.
- [1×] Sell the in-the-money strike and hedge in a far month, not the adjacent month, when running put calendars.
- [1×] A calendar's max loss is bounded by the debit structure even in a crash - that is the point of the hedge.

## Strategy Setups
- **Deep-ITM put calendar (bullish, defined risk)**: Sell near-month 20,000PE (July), buy far-month 20,000PE (December), same strike
  - Risk: Max loss ≈ cumulative roll costs (~₹20,000 over 5 months); loss if market collap
  - Best regime: Bullish or range-up view; low VIX when naked put premiums are unattractive
- **ITM put calendar (low-VIX regime)**: sell current-month ITM put (16,000PE July), buy same strike far-month put (16,000PE December) as the hedge
  - Risk: sharp VIX spike hits the short leg; partial hedging leaves crash exposure; far-m
  - Best regime: India VIX at multi-year lows, quiet drift up or sideways
- **December double ratio**: Buy 19,000CE x1, sell 20,000CE x2 (call ratio); buy 21,000PE x1, sell 20,000PE x2 (put ratio)
  - Risk: pin risk at 20,000; unlimited beyond wings
  - Best regime: no directional view, elevated premiums
- **Results-day vol-crush strangle (SBI)**: Buy ~600PE @20; sell 550PE and 650CE around results
  - Risk: gap beyond wings on surprise results
  - Best regime: post-results IV crush
- **Reverse Call Calendar**: Sell near-month call option, buy far-month call option at same strike
  - Risk: If market makes a big sustained move, the far-month long call protects
  - Best regime: Before binary events when IV is elevated

## Verified Events
(none directly matched)

## Notable Quotes (cleaned)
- "The price from 140 to 105 did not come because of a normal correction - it was a bonus issue."
- "When you are inside the aeroplane you cannot see the aeroplane; step back to see the larger picture."
- "When the far month carries the event, do the calendar backwards: sell the near month, buy the far month."

## Enhancement Callouts
- Standard worked examples per editorial guide (payoff tables, margin math)
- Where strategy recipes exist: add construction, breakevens, max P/L table
