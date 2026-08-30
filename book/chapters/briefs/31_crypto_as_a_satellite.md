# Chapter 31: Crypto as a Satellite
Part: VIII Wealth Beyond the Screen

## Source count
- Transcripts directly mapped: 33
- Unique IDs: 33

## Top themes
- capital gains vs business income
- influencer responsibility
- correlation with equities
- broker counterparty risk
- small consistent returns
- crypto lender bankruptcy
- exchange bonus mechanics
- capital allocation order
- defined-risk structures
- banking crisis flows

## Key lessons
- [0863] Exchange margin netting differs by jurisdiction: selling both call+put is one risk, and portfolio margining on net positions (coming to the platform Mar 2022) reduces capital needs.
- [2185] Synthetic longs (long call + short put) can replicate cash exposure while sidestepping cash-market tax rules, mirroring how FPIs avoid Indian capital-gains tax via derivatives.
- [1118] Every centralized crypto exchange carries custody/counterparty risk; there is no independent depository to verify holdings, so registration jurisdiction and regulation matter.
- [1062] Crypto premiums are rich enough that disciplined straddle/strangle selling survives even violent swings - but positions need active adjustment, not set-and-forget.
- [1118] Fraud means taking money unfairly and disappearing; a genuine business failure with transparent records is not fraud - investors must learn the difference.
- [2185] Crypto cash-market trading in India is structurally penalized (per-speaker: 1% TCS per funding, GST on purchase, flat 30% tax, no cross-coin loss offset).
- [1144] India's 30% flat tax + 1% TDS per trade makes frequent crypto trading structurally penalized for residents; zero-tax domiciles change the math entirely.
- [1598] Zero-credit-zero-debit construction: sells sized to equalize the long leg's premium; 1:3 ratio used because spare margin allowed lower per-unit risk.
- [0747] Crypto options offer daily expiries and rich premiums, but add unregulated-exchange counterparty and systemic risk that index options do not have.
- [2197] Leverage on derivatives can reach 10x-500x with CFD brokers vs ~Rs 1 lakh margin for one NSE short option - leverage multiplies both outcomes.

## Strategies (if applicable)
- {"name": "Crypto premium selling (beginner account)", "construction": "Sold BTC 55,000 put, bought 58,500 call; sold ETH 5,000 call (near expiry); sold BTC 48,000 put - all on a 2,000 USDT trading credit", "numbers": "Capital 2,000 USDT to ~2,900 in a month (~45%); gross 1,200, net 900 after ~300 in charges; BTC Mar-2022 100k call fell from ~5,000 to ~2,000; 20,000 put from ~500 to ~150; Dec 80,000 call ~687", "best_regime": "High-IV crypto markets; wide expected ranges", "adjustments": "None described - amateur discretionary selling", "risks": "Unregulated exchange, counterparty risk; premiums can expand violently (India ban news dropped local BTC/ETH 20% in a day); high fees"}
- {"name": "BTC short strangle (live demo)", "construction": "Sold BTC 68,000 call (~711 USDT, 100 contracts = 0.1 BTC, 25x leverage, margin ~273 USDT) and sold BTC 36,000 put (~255 USDT margin) for late-January expiry", "numbers": "Expecting BTC to stay between 36,000 and 68,000 dollars; combined margin ~528 USDT", "best_regime": "Range-bound high-IV crypto; one-month horizon", "adjustments": "Exchange-native take-profit and stop-loss settings due to 24-hour trading", "risks": "Full margin loss on a breach of either breakeven; exchange/counterparty risk; 0.05% fee drag"}
- {"name": "Ethereum call ratio financed by short puts (long-term)", "construction": "Buy 1x ETH June 3000 call; sell 3x ETH June 5000 calls; sell 2x ETH June 2000 puts", "numbers": "3000 call cost ~760 USDT; net structure profit zone 3,000-5,000; upper breakeven ~6,160; lower breakeven ~1,850; ETH spot ~3,200", "best_regime": "Bullish long-term view on an asset far below its all-time high with wide time buffer (5+ months)", "adjustments": "Above 5,000: buy back the 3 sold 5000 calls and sell 9x 7000 calls (martingale roll-up); below 2,000: accept delivery or adjust", "risks": "Violent downside break hurts the short puts; upside beyond 6,160 erodes profit"}
- {"name": "Bitcoin wide-breakeven combo (June)", "construction": "Buy 1x BTC 35,000 call; sell 2x 50,000 calls; sell 1x 55,000 call; buy 1x 25,000 put; sell 2x 20,000 puts", "numbers": "35,000 call ~7,500 USD premium; margin ~1,500 USD at 25x leverage (750 at 50x, 375 at 100x); expiry breakevens ~15,000 and ~60,000; T+1 profitable zone ~20,000-38,000", "best_regime": "Post-crash stabilization with elevated IV; expecting a wide range, not a breakout", "adjustments": "None detailed; monitor via what-if analysis", "risks": "Move beyond 60,000 (or below 15,000) creates losses; thin crypto option liquidity widens spreads"}
- {"name": "Short straddle - crypto vs index comparison", "construction": "Sell ATM call + ATM put at same strike (BTC 40,000 vs Bank Nifty ~37,500)", "numbers": "Bank Nifty ATM straddle ~2,400-2,500 pts premium; BTC ATM straddle ~$6-7K at $40K BTC; deep OTM premium ~100x richer on crypto (\u20b93 vs $331 at similar distance)", "best_regime": "range-bound high-IV markets; crypto especially rich due to new-asset risk premium", "adjustments": "rolling/adjustment process when trending; platform 'move contract' packages the straddle as one instrument", "risks": "violent moves beyond premium; crypto is more volatile - premium is compensation for real risk"}

## Enhancement candidates
- Payoff chart walkthrough: ratio sizing math for surplus short quantity
- Comparison table: index vs crypto options (trading hours, gap risk, margins, premium richness)
- slippage math: market vs limit orders on thin crypto option chains
- Comparison table: index option premiums vs crypto option premiums for equivalent moneyness
- full crypto ratio-spread worked example with payoff table

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0630
0709
0747
0799
0825
0844
0863
0879
0883
0921
0967
1001
1062
1118
1144
1204
1251
1305
1334
1367
1494
1585
1598
1678
1679
1683
1967
2185
2197
2408
