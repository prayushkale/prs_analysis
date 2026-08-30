# Chapter 27: The Regulator's Dilemma

## Source transcripts (20)
- **0080**: Walks through SEBI's new margining on real examples: naked ATM options now ~1.0-
- **0125**: Explains the new pledge system: previously shares moved to the broker's pool dem
- **0130**: Explains SEBI's cash-market margin changes effective 1 August 2020: upfront marg
- **0134**: Critique of SEBI's peak-margin framework: intraday leverage phased out (from Dec
- **0137**: Mechanics of the F&O ban (Market Wide Position Limit): MWPL = 20% of free-float 
- **0150**: Explains the COVID loan-moratorium interest-waiver case before the Supreme Court
- **0158**: SEBI's 25/25/25 multi-cap mandate is skewered with a cake-fairness analogy: top-
- **0250**: Why India is nearly immune to GameStop-style squeezes: illiquid SLB (lending inc
  + 12 more

## Key themes (85)
market reform  ·  policy overhang  ·  hedging economics  ·  SEBI regulation  ·  tax asymmetry  ·  pledging-system  ·  block-order mechanics  ·  exchange mechanics  ·  double taxation  ·  broker leverage

## Core lessons
1. Under the new framework the margin system itself pays you to hedge: protection 200-300 points away cuts margin ~70%.
2. Cross-margining makes a short straddle cost little more than its single costlier leg - portfolio margin logic arrives in India.
3. Margin relief can seduce into over-sizing: four lots at 300-point risk recreates 1,200 points of exposure. Options trading is risk and position management, not strike selection.
4. Index exposure carries structurally lower margins (2% vs 3.5% exposure) - another argument to avoid stock options.
5. Pool pledging created rehypothecation risk - one client's blowup could cascade through the broker's entire pool.
6. Direct-to-depository pledging (OTP-based) keeps shares in the client's demat; dividends flow straight to the client's bank account.
7. Investor protection fund caps recovery at Rs 25 lakh - broker failure is a real tail risk; treat broker solvency as part of risk management.
8. Intraday margin scales with stock volatility: roughly 4.5x leverage on Reliance (~22%) but barely 1.3x on Idea (~77.5%) at the time.

## Strategies
- **Hedged short option (spread)**: Sell 10,000C / buy 10,200C (200pt); variants 300-400pt
- **Short straddle with far wings**: Sell 9,500CE+9,500PE (July), buy 8,500PE+10,500CE (June weekly/next series)
- **ITM put calendar**: Sell 10,000PE current month, buy 10,000PE next month
- **Weekly far-OTM short puts into expiry (illustrative)**: Sell ~1,000-point OTM index puts ~3 sessions before weekly expiry
- **BTC short strangle (live demo)**: Sold BTC 68,000 call (~711 USDT, 100 contracts = 0.1 BTC, 25x leverage, margin ~273 USDT) and sold BTC 36,000 put (~255 

## Enhancement candidates
- STT history and rate table
- Timeline table of SEBI peak-margin phase-in (Dec 2020 - 2022) with each step's effective date
- before/after pledging-flow diagram
- Case box: IRCTC circular — announcement, one-day −25%, withdrawal; total value destroyed vs revenue gained
- Ban lifecycle diagram (95% entry, 80% release, square-off-only window)
- India-vs-US shorting framework table (SLB, circuits, margins, position limits)
- 'margin relief trap' box: position-size inflation math
- Timeline table of STT changes on futures and options with effective dates

## Relevant verified events: {len(events)} total (use events/events_verified.jsonl directly)

## Redundancy note
{len(records)} transcripts mapped; deduplicate overlapping pre/post market reports to strongest statement per concept.

## Writing instructions
- Use voice_guide.md for tone and term conventions.
- Apply banned_terms.md scrub rules.
- Enhancement: include worked numerical examples and payoff tables where concepts are abstract.
- Keep each chapter 3,000-6,000 words target.
