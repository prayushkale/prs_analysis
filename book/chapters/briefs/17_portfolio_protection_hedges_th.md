# Chapter 17: Portfolio Protection: Hedges That Actually Hedge

*Source transcripts: 52*
*Top themes: hedging, covered calls, dividend yield, crypto options, broker selection*
*Strategy recipes: 8*
*Verified events matched: 0*

## Key Lessons (by frequency)
- [1×] Stop-loss is non-negotiable: hit it and you can recover; blow up and you cannot (slow poison vs quick poison)
- [1×] Square-off vs counter-strategy is decided by two questions: do you have additional capital and additional skill?
- [1×] The 50% cash-equivalent requirement applies at broker level; brokers may pass it to clients (Zerodha does)
- [1×] Cash equivalents: FD, Liquid BeES, liquid funds; Bharat Bond (~5% haircut) may qualify with some brokers
- [1×] Run many small strategies across instruments so a rescue in one can be funded by closing another
- [1×] In uncertainty a holder has only two choices: exit or hedge; hedging via futures avoids STT on both legs and preserves LTCG status.
- [1×] FII cash selling with falling futures shorts means exit, not hedge — treating falling shorts as bullish is a misread.
- [1×] Requires lot-multiples, collateral and margin; small or small-cap-only portfolios cannot hedge this way.

## Strategy Setups
- **Futures overlay hedge (pre-event)**: Hold portfolio; short equivalent notional in index/stock futures instead of selling cash
  - Risk: Basis/premium decay; margin call on gap-up; imperfect hedge for small/midcap-hea
  - Best regime: Before binary events for portfolios at least one futures lot, large-cap, collate
- **Long-dated Nifty short strangle (annual range)**: Sold December-2022 15,000 put and 21,000 call
  - Risk: Both sides breached in an extreme year; margin lock-up for 12 months
  - Best regime: Wide VIX-implied annual range with no intent to predict direction
- **Far-OTM safe option selling (fragmentary)**: Sell distant-month far OTM options with ~10% extra distance beyond the nominal safe strike
  - Risk: unrecoverable (tail loss if level breaks)
  - Best regime: High IV with strong support/resistance shelves
- **Bullion index equity hedge**: Long/short equity portfolio paired with same-direction or inverse position in MCX BULLDEX futures (70.52% gold / 29.48% silver)
  - Risk: Correlation breakdown; VaR-driven margin changes
  - Best regime: Portfolio-level diversification when equity-gold inverse correlation is intact
- **Futures-plus-collateral long-term long**: Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin
  - Risk: Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum l
  - Best regime: Large capital, long-term bullish, willing to manage monthly rollovers

## Verified Events
(none directly matched)

## Notable Quotes (cleaned)
- "People are looking for certainty in an uncertain market. And that's a wrong thing."
- "A 20-25% fall on a hung parliament is the right time to start your portfolio."
- "If you are walking home it takes ten minutes; if a dog chases you, three - adjustments are where the profit is."

## Enhancement Callouts
- Standard worked examples per editorial guide (payoff tables, margin math)
- Where strategy recipes exist: add construction, breakevens, max P/L table
