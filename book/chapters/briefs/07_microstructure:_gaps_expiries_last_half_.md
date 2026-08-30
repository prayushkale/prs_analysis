# Chapter 7: Microstructure: Gaps, Expiries, Last Half Hour
Part: II How This Market Works

## Source count
- Transcripts directly mapped: 50
- Unique IDs: 50

## Top themes
- positional trading infrastructure
- system vs discretionary traders
- Supreme Court moratorium case
- margin unfairness to hedgers
- case study with daily data
- technical analysis limits
- stock lending & borrowing
- index concentration risk
- option selling tail risk
- futures expiry mechanics

## Key lessons
- [2756] Regulators release combined buyer-seller loss data; the honest question is what share of losers are option buyers versus sellers - pressure on sellers shrinks supply and raises premiums, hurting buyers more.
- [0130] Settlement mechanics: T-day trade, T+1 funds/shares to broker/exchange, T+2 demat/money transfer; early pay-in avoids the shortfall but forfeits the auction-market rescue for short deliveries.
- [0136] When FII ownership hits the sectoral cap, arbitrage breaks: the ADR can hold a 10% premium indefinitely because FIIs cannot buy more in India - so the premium is information, not free money.
- [2748] Retail collateral rules cap net short exposure (500-crore rule), yet one foreign entity held ~45,000 crore of options - limits must apply at ultimate-beneficiary-owner level, not per entity.
- [2756] Bank Nifty with 12 stocks where four hold ~80% (HDFC Bank ~30%) can be moved by a 1,000-crore order in two names - index design itself enables manipulation; want 15+ stocks, max 10% each.
- [0585] Stop-loss-market orders are structurally dangerous near crowded strikes: when everyone's trigger fires at once, your fill lands wherever liquidity is - within the day's legal price band.
- [2219] Hedge-fund playbook (as alleged): quietly accumulate cheap puts and sell calls, then slam the underlying with simultaneous heavyweight sell orders, covering instantly lower.
- [0810] Gamma effect: in the final week a 10-30 rupee option can multiply 5-10x on a violent move - buyers must exit on momentum; sellers holding to expiry can still be destroyed.
- [1901] Extended-hours benefit is mostly operational: margin releases immediately after expiry, letting sellers roll to next expiry without intraday-margin lock or exit costs.
- [0072] Resting limit orders far from spot can get filled by flash spikes; square off immediately - such dislocations vanish in seconds and cannot be systematically captured.

## Strategies (if applicable)
- {"name": "Hedged short put", "construction": "Sell near put + buy a further-OTM put same expiry", "numbers": "Speaker example: sold 9400-put style positions; hedge put cuts margin drastically and caps loss", "best_regime": "Any short-put view; mandatory insurance", "adjustments": "Not advised live; know risk-reward before entry", "risks": "Unhedged version: margin cascade and uncapped gap risk"}
- {"name": "Unhedged short straddle on a single stock", "construction": "Sell 1000 CE (49) + sell 1000 PE (39) on HDFC Bank, 2 lots (1000 qty), June 9 2020, hold to near expiry", "numbers": "Premium collected ~87,000; returned ~35,000; profit ~50,000; stock closed 1035 on June 25; daily combined premium stayed below 87 through expiry", "best_regime": "High IV with range-bound expectation around a support level (1000)", "adjustments": "None taken in this trade - held naked; would need firefighting if spot ran beyond breakevens", "risks": "Unlimited loss beyond 1087/913; a single-stock gap through breakevens is the failure mode"}
- {"name": "Bank Nifty rollover analysis", "construction": "Long (or short) futures rolled monthly", "numbers": "~100 pts typical next-month premium; ~1,200 pts (~5-6%) cost per year for longs; shorts collect it", "best_regime": "Long-term shorts benefit from rollover premium; long-term longs should buy cash instead", "adjustments": "Hedging is cheaper on futures than on cash positions", "risks": "Premium varies 40-200 pts monthly; longs underperform cash by the premium"}
- {"name": "Calendar inversion (long near-week straddle, short far-week straddle)", "construction": "Buy ATM call+put current weekly expiry; sell ATM call+put next weekly expiry", "numbers": "Capital ~\u20b930-35k; claimed backtest ~\u20b928-30k/year (~80% gross, ~50-55% after costs)", "best_regime": "Expecting violent moves (event seasons)", "adjustments": "Cut the losing far leg on a 10-15% premium move; trail the winner; re-buy the opposite leg on reversal", "risks": "Absolute sideways market decays both longs; near-week theta bleed"}
- {"name": "Collateral-funded far-OTM weekly selling (HNI pattern, warned)", "construction": "Hold ~1,000 crore shares; sell far-OTM weekly calls and puts near 1 rupee with a 5-rupee stop", "numbers": "~8 lakh/week per side on 100-crore collateral (~16 lakh/week, ~64 lakh/month); stop hit probability <0.1% except tail events like the 2019 corporate-tax-cut candle when a 1-rupee option went to 60-70", "best_regime": "Ultra-HNI zero-capital-cost premium harvesting; NOT for retail", "adjustments": "Sell both sides so net short/long classification nets to zero under the 500-crore rule", "risks": "Tail events blow through stops; surveillance margin can freeze released funds for two months; single-side selling triggers the net-short cap"}

## Enhancement candidates
- Worked example: proxy-hedge demand distortion when a group has one shortable stock (short interest concentration, ban-day dynamics)
- Why futures can go negative: delivery obligations plus storage economics, contrasted with cash-settled contracts
- Timeline table: the Jane Street episode (order, volumes impact, ban, settlement)
- worked example: the cash-buy + futures-short hedge that funds ran during the HDFC Bank FII window and its payoff
- Liquidity-premium explanation: why far legs gap

## Representative daily/weekly entries
- [0004|2018-09-25] Panic morning selling found support at 10,900 (62.8% Fibonacci retracement and Friday low); Nifty sh
- [0479|2021-07-16] Post-ATH consolidation setup; Japan COVID worry pre-Olympics but India may outperform (waves reverse
- [0788|2022-01-17] HDFC Bank/HCL Tech results weekend; 'who blinks first' F&O positioning day; Infosys overtook HDFC Ba
- [1114|2022-07-14] Post-9.1%-CPI morning: US recovered from lows as energy base effects ease (crude below $100). SGX -6
- [1476|2023-01-31] Budget-eve flat close (Bank Nifty +1%, IT -1%); PSU banks +4% led by SBI as FPO fully subscribed on 
- [1802|2023-08-01] Chop day (-20): Power Grid -5% post-results, Maruti fell despite good results (priced in), Hero Moto
- [2100|2024-02-06] China rebound → short covering; RBI's 'HDFC Group can raise stakes to 9.5% in six banks' headlines c
- [2303b|2024-08-19] Asia recovered after early weakness; GIFT +80. Nifty inching toward filling the 24,720 gap from the 
- [2647|2025-04-23] Volatile monthly-expiry eve: Bank Nifty high 55,900 (same as yesterday) then fell ~700; IT index +4%
- [2946|2025-12-19] December series consolidating 26,000±300; Infosys ADR spiked ~38-56% intraday in US with repeated tr

## Verified events (relevant)


## Source IDs
0041
0051
0052
0072
0075
0086
0087
0088
0097
0105
0130
0136
0141
0155
0171
0186
0197
0239
0243
0250
0388
0470
0518
0585
0785
0810
0895
1050
1074
1172
