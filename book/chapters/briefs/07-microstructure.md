# Chapter 7: Microstructure: Gaps, Expiries and the Last Half Hour

## Source transcripts (20)
- **0041**: Explains the historic negative WTI print: contracts marked for physical delivery
- **0051**: Two case studies where technicians were trapped: RBI's May 2018 FII window openi
- **0052**: Argues index options beat stock options: indices cannot crash 50-60% in a day (D
- **0072**: Explains the 8,950PE flash spike (0.50 to ~20 in minutes) as a probable fat-fing
- **0075**: Full explainer on SGX Nifty: what it is, contract sizing (USD 2x index vs 75 sha
- **0086**: Euphoric gap-up morning (Nifty +200, Bank Nifty +500) fizzled: pre-market blog c
- **0087**: Where-to-find tutorial: BSE results calendar, NSE company pages, and Moneycontro
- **0088**: Q&A session: hedging as non-negotiable doctrine, SEBI lot-size revision mechanic
  + 12 more

## Key themes (92)
premium decay tracking  ·  case study with daily data  ·  overnight read-through  ·  storage constraints  ·  delisting  ·  SEBI regulation  ·  short squeeze  ·  systemic risk  ·  order errors  ·  liquidity

## Core lessons
1. Contracts expiring into physical delivery can print absurd prices when storage is exhausted - know delivery mechanics before holding.
2. Negative prices were contract-specific: the next-month contract kept trading at normal positive levels.
3. Look at everything - news, flows, regulation - never one indicator alone
4. When a known buying window opens, front-runners buy in cash and short futures; late chart-followers get trapped
5. Order-entry errors can crash markets 15% in minutes and reverse; stop-losses get hit both ways
6. If one system reliably worked, everyone would follow it and it would stop working
7. Return on margin matters, not how much the underlying moves - index gives 6-7% on margin vs 4% for a stock moving twice as much
8. Stocks can gap 50-70% overnight; indices are circuit-protected

## Strategies
- **Hedged short put**: Sell near put + buy a further-OTM put same expiry
- **Unhedged short straddle on a single stock**: Sell 1000 CE (49) + sell 1000 PE (39) on HDFC Bank, 2 lots (1000 qty), June 9 2020, hold to near expiry
- **Bank Nifty rollover analysis**: Long (or short) futures rolled monthly

## Enhancement candidates
- Table: what can be pledged as collateral across broker types (2020)
- Why FII caps break ADR-cash arbitrage (worked example with the 10% premium)
- Contract-spec table for the three index families
- Rights-entitlement fair-value math: intrinsic + financing value of deferred payments
- Rollover cost table for 12-month futures holding at varying premiums
- India-vs-US shorting framework table (SLB, circuits, margins, position limits)
- lower-circuit mechanics explainer
- explain circuit limits (10% NSE circuit) and what happens when they are breached

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
