# Chapter 6: Reading the Option Chain

## Source transcripts (20)
- **0027**: VIX masterclass during COVID: definition (expected 30-day movement, not a fear g
- **0044**: Shows how to compute FII positioning from NSE's participant-wise open-interest r
- **0068**: Q&A clarifying mechanics: buy/sell quantities are always equal (TV 'delivery buy
- **0084**: Q&A: debunks the short-selling 'ban' (practical cap ~500 crore plus margin), war
- **0092**: India-China border clash hits mid-session: Bank Nifty gap-up 700 then -1200 then
- **0146**: Simple monthly range method: after expiry, take the nearest strike to Friday's c
- **0149**: Debunks the 10x OI jump in far-OTM Nifty 12,500CE (42k to ~19 lakh contracts) as
- **0155**: Rapid-fire Q&A: REIT collateral limits, cost of rolling Bank Nifty futures for a
  + 12 more

## Key themes (86)
indicator-distortion  ·  efficient market hypothesis  ·  liquidity  ·  geopolitical knee-jerk  ·  straddle premium  ·  option-premium signal  ·  breakeven  ·  COVID 2020  ·  calendar spreads  ·  data literacy

## Core lessons
1. VIX measures expected one-month movement; it can fall in a falling market when the fall is narrow (heavyweights only, breadth positive).
2. Monthly expected move = VIX / sqrt(12); place short strikes beyond that band (example: VIX 60 -> ~17% band).
3. VIX is derived from option prices - the straddle premium is a live cross-check of the VIX-implied range.
4. High VIX favors sellers who keep distance; low VIX means the market is priced for calm and strikes must come closer.
5. Compute FII long/short percentages from NSE participant-wise open-interest reports instead of relying on TV sound bites.
6. Extreme FII index-short positioning (~85%) historically marks bottoms; read index and stock futures together for the true picture.
7. Futures: daily MTM cash transfer. Options: buyer pays premium once; seller's margin floats with the option's price.
8. Expiry settlement price is the weighted average of the last half hour - an ITM option can expire worthless despite a favorable last traded price.

## Strategies
- **VIX-based expected-move strangle placement**: Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%
- **Monthly short option + weekly protective hedge**: Sell far-month option; buy near-week option slightly OTM below breakeven; re-buy weekly
- **ATM straddle range projection**: Nearest strike to post-expiry close; add ATM call + put premiums to strike for upper bound, subtract for lower bound
- **Bank Nifty rollover analysis**: Long (or short) futures rolled monthly
- **Range-filtered PCR**: Sum put OI and call OI only for strikes within expected monthly range (spot +/-1,000 early in month, +/-700-800 mid-mont

## Enhancement candidates
- 2x2 price/OI state table with the Bajaj Finance dates as worked rows
- OI-addition read (66 lakh put OI added at three strikes) as a worked example
- Rollover cost table for 12-month futures holding at varying premiums
- Side-by-side IV rank vs IV percentile example where one spike day misleads rank
- Margin-netting arithmetic walkthrough (span zeroing with paired shorts)
- OI arithmetic walkthrough (volume 150 -> OI 50 vs 150)
- Buyer-vs-seller risk/margin comparison table
- expiry-anatomy case study box: Sep-24 vs Oct-15 behaviour

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
