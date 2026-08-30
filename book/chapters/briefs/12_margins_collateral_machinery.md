# Chapter 12: Margins, Collateral, Machinery
Part: III Options from First Principles

## Source count
- Transcripts directly mapped: 89
- Unique IDs: 89

## Top themes
- multi-strategy capital pools
- banker's guarantee loophole
- intraday leverage phase-out
- stock lending and borrowing
- margin architecture reform
- time decay proportionality
- liquidity and trading bans
- defined-risk construction
- profit booking psychology
- stock lending & borrowing

## Key lessons
- [2767] Span margin equals maximum risk plus exposure margin; an option buyer pays only premium (max risk known) while a seller pays ~50,000 for a 10,000-rupee max-risk position - exposure margin is a policy choice, not a risk measure.
- [2767] India offers Nifty options to 5 years but stock options only 3 months with poor liquidity; long-dated stock options and futures would let investors earn premium on holdings, as US covered-call practice shows.
- [2780] Because the protected position cannot lose, you can ladder new collars every further 5% of market fall using debt-fund tranches (20% at -10%, then each -5%) - courage without conviction-destroying drawdowns.
- [2780] A collar funded by equal premiums (buy 25,000PE, sell 28,000CE on Dec-2026) gives zero downside and ~3,400 points of capped upside (~13-14% over ~17 months) - slightly better than FD with full protection.
- [2767] If the goal is moving traders from short-dated frenzy to long-dated calm, penalize intraday daily (not just expiry days) and reward long tenure by removing the 9-month extra margin and exposure margin.
- [0111] Time decay is proportional to remaining time: a one-week option loses ~20% of its value on day one, but ~100% on expiry day - expiry-day selling harvests decay that weekly sellers spread across days.
- [0111] India charges full span+exposure margin on covered calls against demat shares (no cash-F&O link); holding a long future instead cuts the short call's span to zero - only exposure margin applies.
- [0130] Settlement mechanics: T-day trade, T+1 funds/shares to broker/exchange, T+2 demat/money transfer; early pay-in avoids the shortfall but forfeits the auction-market rescue for short deliveries.
- [0111] Bond yields falling means older bonds trade at a premium (Bharat Bond 1 near 1080-1090 vs 1000 face); pledging older listed bonds can beat waiting for new issues to clear collateral approval.
- [2780] India charges span + exposure + extra >9-month margin even on hedged ETF positions, where the US charges nothing for covered calls - friction that keeps zero-risk capital out of the market.

## Strategies (if applicable)
- {"name": "Collateral-funded option selling (framework)", "construction": "Sell options against collateral: bank FD, shares, mutual funds or bank guarantee pledged to the broker", "numbers": "Buyer pays 2,000-3,000 premium cash vs seller margin ~80,000-90,000 (as stated) but pledgable in kind", "best_regime": "Traders with large capital seeking steady returns", "adjustments": "Losing short can be adjusted via short futures or selling calls on the other side", "risks": "Margin calls on booked losses; losses can exceed premium received if unhedged"}
- {"name": "FD/collateral-backed premium recycling", "construction": "~25 lakh FD pledged; premiums from option selling recycled to absorb small booked losses without touching the FD", "numbers": "Example: 25 lakh FD collateral (as stated)", "best_regime": "Option sellers running multiple small premium streams", "adjustments": "Net small booked losses against premium inflows from other positions", "risks": "If booked losses exceed total premium received, cash injection is mandatory"}
- {"name": "Post-earnings leg-by-leg review of the hedged straddle", "construction": "650CE/PE sold; 720CE/580PE long; 750CE/550PE sold 2x - each leg marked after the results", "numbers": "Total +8.95/share = Rs.10,740 per lot (lot 1200); margin ~Rs.7.24 lakh after benefits for the 5-lot structure; ~1.5% in a day; projected ~4% in two weeks", "best_regime": "Immediately after results, when volatility crush pays all sold legs", "adjustments": "Closed the 650/720 and 650/580 pairs; kept 750CE/550PE with a stop-loss", "risks": "Far wings are effectively naked beyond 750/550"}
- {"name": "Futures-plus-collateral long-term long", "construction": "Buy 1 lot long futures; park notional value in FD/Bharat Bond; pledge for collateral margin", "numbers": "Reliance example: ~7.5L notional; premium ~Rs 5/share/month (~30k/yr); interest ~50k/yr at 7-7.5%; net saving ~10-20k/yr; incremental short-call margin ~50k vs 1.75L for cash holder", "best_regime": "Large capital, long-term bullish, willing to manage monthly rollovers", "adjustments": "Sell one OTM call monthly against the long for income; exit stock/futures on strength if assigned economics improve", "risks": "Monthly rollover discipline; gap/MTM risk on the futures leg; lot-size minimum locks ~7.5L capital"}
- {"name": "Bharat Bond as trading collateral", "construction": "Buy Bharat Bond ETF units; pledge to broker as collateral for F&O margins", "numbers": "~7.6% indicative 10yr yield; 20% LTCG with indexation >3yr; 5% haircut; EBBETF 0423 ~1019, EBBETF 0430 ~1050 (May 2020)", "best_regime": "declining interest rates; idle capital awaiting trade opportunities", "adjustments": "n/a", "risks": "rising rates compress price; credit concentration in PSU issuers"}

## Enhancement candidates
- Margin friction comparison: India ETF+collar vs US covered call
- Margin math: hedged vs naked leg span comparison
- Box: why positional stop-losses differ structurally in India vs US markets
- Timeline box: upfront margin rules 2020→peak margin penalty evolution→client-refund circulars
- Tax-asymmetry case: 3.5L cash loss + 4L futures profit = 50k net but ~1.5L tax

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0003
0025
0026
0042
0049
0052
0056
0059
0061
0068
0071
0073
0076
0080
0082
0084
0088
0089
0094
0098
0100
0106
0111
0121
0125
0130
0132
0134
0137
0145
