# Chapter 8: Why Derivatives Exist

## Source transcripts (20)
- **0071**: Quantified case for taking long-term equity exposure via futures plus a debt col
- **0072**: Explains the 8,950PE flash spike (0.50 to ~20 in minutes) as a probable fat-fing
- **0089**: Teaches synthetic futures: long = buy ATM call + sell ATM put; short reversed. D
- **0182**: Announcement/preview of the free Mission Options options-basics course: scope (d
- **0183**: Foundational lesson: derivatives defined via milk-to-butter and crude-to-petrol 
- **0185**: Classifies derivatives participants into arbitrageurs, hedgers, speculators; tea
- **0188**: Futures = forward with price set at execution, not today; the sell-first-buy-lat
- **0189**: Margin anatomy via a live Zerodha calculator: ACC long/short costs the same ~1.7
  + 12 more

## Key themes (66)
mark to market  ·  gambling-vs-hedging  ·  exposure margin  ·  covered interest arbitrage  ·  regulation  ·  futures vs cash market  ·  cash vs futures  ·  transaction-cost math  ·  market reform  ·  membership tiers

## Core lessons
1. For large capital, long futures funded by pledged debt instruments beats cash buying: interest income exceeds the cost-of-carry premium.
2. A short call against a long futures position needs only incremental margin - cash-market holders pay far more to run the same hedge.
3. Leverage is not inherently gambling: buying with Rs 100 while committing only Rs 20, keeping the rest safe, is capital efficiency.
4. Futures gains are business income (expenses deductible); cash equity gets 10% LTCG / 15% STCG - pick the instrument with the tax profile you prefer.
5. Resting limit orders far from spot can get filled by flash spikes; square off immediately - such dislocations vanish in seconds and cannot be systematically captured.
6. A month can be violently volatile intraday yet flat close-to-close: distance-based option selling harvests the chaos.
7. Staggered-payment instruments (rights entitlements) can rationally trade above intrinsic because of embedded financing value.
8. Synthetic long = buy ATM call + sell ATM put; replicates the futures payoff almost exactly.

## Strategies
- **Futures-plus-collateral long-term long**: Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin
- **Synthetic futures (long/short)**: Long: buy ATM call + sell ATM put (same expiry). Short: reverse legs
- **Covered interest carry trade (1995 example)**: Borrow SGD at 3%, place INR NRNR deposit at 20%, hedge FX with a 3-year forward costing ~2%/yr
- **ITM call instead of long futures**: Buy deep ITM call (e.g. SBI 200CE at Rs46 with spot 245, lot 3000) instead of 1 lot futures

## Enhancement candidates
- leverage math table (margin % vs P&L amplification)
- Rights-entitlement fair-value math: intrinsic + financing value of deferred payments
- forward-contract payoff worked example with the 75-rupee dollar case
- Side-by-side table: cash buy vs futures+collateral (capital, carry, hedge margin, tax, effort)
- Rollover calendar workflow
- five-derivative-types table (forwards/futures/options/swaps/swaptions)
- Table: insurance analogy mapped to options (insured/hedger, insurer/seller, premium, claim payoff)
- Side-by-side table: forward vs futures (counterparty risk, margining, standardization, settlement)

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
