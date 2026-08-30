# Chapter 13: The Seller's Edge: Short Straddles & Strangles

## Source transcripts (20)
- **0003**: Debunks the buyer-favorable myth: seller pays margin via collateral (no cash), w
- **0025**: Systematic demolition of the three buyer advantages (low premium, limited risk, 
- **0027**: VIX masterclass during COVID: definition (expected 30-day movement, not a fear g
- **0030**: Explains the violent up-move anomaly: strangle sellers trapped by a ~10% rally a
- **0034**: P&L transparency episode: ~50% return in six April-2020 sessions driven by VIX c
- **0036**: Teaches the cash-secured put end to end: sell a put at a strike you are happy to
- **0037**: Replies to ROI/margin critics by showing scale: ~23 lakh quantity through one br
- **0040**: Pre-results Infosys structure: short straddle at 650, converted to an iron fly w
  + 12 more

## Key themes (92)
basket orders  ·  premium decay tracking  ·  adjustment volume  ·  position sizing  ·  case study with daily data  ·  hedging economics  ·  SEBI regulation  ·  risk sizing  ·  cash-secured puts  ·  forced square-offs

## Core lessons
1. For every option bought one is sold - if buying were strictly better, no seller would exist.
2. Seller pays margin as collateral (FDs/shares), so cash outlay can be near zero; buyer pays premium in cash.
3. Probability decides long-run winners: buyer wins in only one of five market scenarios, seller in most.
4. Sellers can adjust/hedge a losing position (short futures, sell calls); a buyer has no equivalent fix.
5. Little money and losable: buy. Large capital and steady profit: sell.
6. 'Limited risk, unlimited reward' always pairs with very low probability (lottery) or very high risk (robbery).
7. Seller's real risk is bounded by the trading capital actually deployed, not theoretical unlimited loss.
8. Buyer psychology fails at profit booking - 10 to 50 to zero on expiry day; seller's capped profit removes greed.

## Strategies
- **Collateral-funded option selling (framework)**: Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker
- **VIX-based expected-move strangle placement**: Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%
- **Strangle roll-under-stress mechanics**: Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and se
- **Strike-and-expiry put ladder (illustrative, high risk)**: Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-opt
- **Cash Secured Put**: Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery

## Enhancement candidates
- Step-by-step margin-flow diagram of the forced roll; before/after premium table for the far vs near put
- basket-order execution checklist for multi-leg event trades
- Five-scenario outcome table (violent fall / mild fall / sideways / mild rise / violent rise) showing buyer-vs-seller P&L
- 'margin relief trap' box: position-size inflation math
- explain efficient-market hypothesis with the March-2020 example as illustration
- daily combined-premium decay table for a single-stock straddle through a volatile month
- Ladder margin table (strike x expiry x premium x margin) showing how diversification compresses portfolio vega
- error-trade recovery sequence: margin impact of doubling a corrective leg

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
