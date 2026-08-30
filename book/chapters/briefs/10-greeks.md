# Chapter 10: The Greeks, Demystified

## Source transcripts (12)
- **0110**: Debunks the 'two 0.5-delta calls equal a 1-delta future' fallacy. A synthetic fu
- **0124**: Foundational payoff teaching: selling a put is not buying a call. Across five sc
- **0401**: Curriculum episode defining delta as the option-price change per unit move in th
- **0427**: Gamma explained as the rate of change of delta: on violent news (corporate-tax-c
- **0441**: Theta as non-uniform time decay: ~2%/day with 50 days left vs ~50% with 2 days; 
- **0455**: Foundational lesson on implied volatility: definition, put-vs-call IV asymmetry,
- **0778**: Pre-earnings TCS structure built live: a 1:3 call ratio (buy 3800C, sell three 4
- **0810**: Explains the gamma effect - violent premium multiplication in expiry week (a 28-
  + 4 more

## Key themes (44)
delta misconceptions  ·  theta  ·  earnings strategy  ·  expiry risk  ·  technical analysis  ·  option selling tail risk  ·  trend indicator  ·  option greeks  ·  institutional programs  ·  volatility-events

## Core lessons
1. Delta equivalence is not payoff equivalence: two ATM calls match a future's delta but accumulate time decay; the synthetic future matches the payoff itself.
2. On any single day the two calls may lose less than the future - the difference appears over weeks of churn, when decay compounds.
3. Greeks act together; judging a position by one Greek (delta) is the most common retail options error.
4. Selling a put profits in 4 of 5 scenarios (~80%); buying a call profits in 1 of 5 (~20%) - the structural seller's edge.
5. Seller's cushion = premium collected: loss begins only beyond strike minus premium.
6. Option buying can be 'operation successful, patient dead' - the view lands and the position still loses.
7. Selling a call is likewise not buying a put; the asymmetry is identical on the bearish side.
8. Delta = change in option price per 1-point move in the underlying: ATM ~0.5, deep ITM ~1, far OTM near 0.

## Strategies
- **Synthetic long future**: Buy ATM call + sell ATM put (same strike/expiry)
- **Put-selling vs call-buying scenario framework**: ATM put sold at premium P vs ATM call bought at premium C (Nifty 10,750; 30-Jul-2020 expiry)
- **Gamma awareness for expiry-week selling**: Short ATM options held into expiry vs square-off rule
- **Theta-aware expiry choice**: Buyers: options with ≥1 month left; sellers: write near expiries while managing gamma
- **TCS earnings call-ratio with financed wings**: Buy 2 lots 3800 call @~150.5; sell 3 lots 4000 call @~59.5; buy 1 lot each of two OTM calls (~19 and ~12 premium) to equ

## Enhancement candidates
- Side-by-side IV rank vs IV percentile example where one spike day misleads rank
- Month-end FII selling pattern table
- Payoff diagram for put-debiased strangle; gamma-by-expiry table justifying far-month entries
- Delta ladder table: ITM/ATM/OTM delta values with payoff examples; absolute vs percentage return distinction
- Table comparing American vs European exercise rights across NSE/BSE and US markets
- probability-of-profit vs margin-requirement comparison
- Gamma multiplication worked example (spot path vs premium path)
- Delta-vs-strike table (OTM/ATM/ITM) with payoff implications

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
