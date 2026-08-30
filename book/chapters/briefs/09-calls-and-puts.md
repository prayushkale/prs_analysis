# Chapter 9: Calls and Puts

## Source transcripts (20)
- **0003**: Debunks the buyer-favorable myth: seller pays margin via collateral (no cash), w
- **0024**: Foundational primer: calls and puts taught through a Virat Kohli cricket-betting
- **0025**: Systematic demolition of the three buyer advantages (low premium, limited risk, 
- **0036**: Teaches the cash-secured put end to end: sell a put at a strike you are happy to
- **0052**: Argues index options beat stock options: indices cannot crash 50-60% in a day (D
- **0064**: Firefighting walkthrough on an ICICI Bank call-ratio position after a results mi
- **0068**: Q&A clarifying mechanics: buy/sell quantities are always equal (TV 'delivery buy
- **0073**: Q&A: age-percentage debt rule and SIP/SWP for a retiree down 35%; short straddle
  + 12 more

## Key themes (95)
transaction-cost math  ·  HNI collateral structure  ·  overnight read-through  ·  earnings reaction  ·  theta and vega dominance  ·  stop-loss-philosophy  ·  liquidity  ·  stock options risk  ·  delivery intent  ·  synthetic futures

## Core lessons
1. For every option bought one is sold - if buying were strictly better, no seller would exist.
2. Seller pays margin as collateral (FDs/shares), so cash outlay can be near zero; buyer pays premium in cash.
3. Probability decides long-run winners: buyer wins in only one of five market scenarios, seller in most.
4. Sellers can adjust/hedge a losing position (short futures, sell calls); a buyer has no equivalent fix.
5. Little money and losable: buy. Large capital and steady profit: sell.
6. An option is asymmetric betting: buyer risks only the premium; seller pays 1:1 per point beyond the strike.
7. Premium moves on expectation, not just price - a batter racing toward a century raises the 'premium' before the century exists.
8. Call buyers profit when market rises, put buyers when it falls - but volatility and time decay can still turn a right view into a loss.

## Strategies
- **Collateral-funded option selling (framework)**: Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker
- **Cash Secured Put**: Sell a put at the strike where you want to own the stock; keep the full cash ready for delivery
- **OTM credit-sale adjustment on a losing ratio**: Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65
- **Synthetic futures (long/short)**: Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs
- **Collateral-funded option selling (HNI pattern)**: Pledge debt mutual funds/bank FDs as collateral; sell options against the margin; keep interest as primary return

## Enhancement candidates
- worked example of strike adjustment arithmetic after a special dividend
- Decision tree: results-miss firefighting for ratio positions (when to sell OTM credit vs exit)
- Why FII caps break ADR-cash arbitrage (worked example with the 10% premium)
- Five-scenario outcome table (violent fall / mild fall / sideways / mild rise / violent rise) showing buyer-vs-seller P&L
- negative-sum math table: itemized cost drag per round trip
- probability-of-profit vs margin-requirement comparison
- QIP-demand signal checklist
- Worked expiry-settlement example: VWAP vs LTP deciding ITM/OTM

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
