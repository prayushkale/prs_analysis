# Chapter 5: Volatility as a Regime
Part: II How This Market Works

## Source count
- Transcripts directly mapped: 287
- Unique IDs: 40

## Top themes
- diversification across strikes and expiries
- implied volatility term structure
- mean reversion after down years
- Supreme Court moratorium case
- valuation premium compression
- crisis cycle every 8-10 years
- bank nifty underperformance
- efficient market hypothesis
- secular stagnation examples
- relative underperformance

## Key lessons
- [0135] Vaccine/normalization news deflates the fear premium: metals crashed the day after Russia's August 2020 vaccine announcement while old-economy stocks with 'bad results' rallied.
- [0030] In violent moves, premiums behave abnormally because losing-side sellers are forced to square up and roll - not because the market 'should' behave that way.
- [0487] No strategy is self-sufficient: a wrong directional view was rescued entirely by layered adjustments (multiple straddle strikes, staggered entries).
- [0684] Ignore one-year point targets from brokerages (Citi's 10,000 for Mar-2021 vs actual ~15,000); emerging-market inflation drifts indexes up long-term.
- [0135] Falling IV collapses both call and put premiums - long-dated option buyers harvest theta-and-IV decay; position for IV regime, not direction alone.
- [0246] In violent markets, far-OTM options can move opposite to the index because traders buy them to cut margin - premium behavior beats price intuition.
- [1910] Indian proxy: Nifty futures premium collapsing from ~100 points toward zero/discount marks capitulation; futures discount = extreme bearishness.
- [0487] Stock options demand institutional-scale margin - one Adani straddle lot ~5 lakh; deploy only ~25% of capital and keep the rest for adjustments.
- [0154] Once a 15-30% correction makes prices attractive, new buyers arrive and markets stabilize - sell-offs without news are opportunities, not exits.
- [1520] Short sellers compound MTM profits by re-shorting lower - 4000 to 2000 to 1000 doubles the short each leg; that is how stocks glide toward zero

## Strategies (if applicable)
- {"name": "VIX-based expected-move strangle placement", "construction": "Sell puts below spot - (VIX/sqrt(12))% and calls above spot + (VIX/sqrt(12))%", "numbers": "VIX 60 -> monthly band ~17.3%; spot 8,000 -> sell puts below ~6,500, calls above ~9,500; May 8,000 straddle ~1,600 (~20% for 37 trading days)", "best_regime": "Elevated VIX (crisis); recompute daily as VIX moves", "adjustments": "None stated - guideline framing, refresh band as VIX changes", "risks": "Band is statistical, not a wall; theta/other factors shift premiums; violent moves can exceed the band"}
- {"name": "Falling-VIX combo (call ratio + put ratio)", "construction": "Bought 8,200CE, sold 3x 9,000CE; bought 8,000PE, sold 7,400PE + 7,300PE (as stated)", "numbers": "Sold ~3x quantity on the far leg both sides", "best_regime": "Falling VIX with a directional view; benefits from vega collapse on the short legs", "adjustments": "Not stated", "risks": "Upside loss above 9,000 on the 3:1 call ratio; downside acceleration through 7,300 on the put ratio"}
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "Strike-and-expiry put ladder (illustrative, high risk)", "construction": "Sold puts at 6,500 / 7,000 / 7,300 / 7,400 / 7,500 / 7,800 / 8,500 across weekly, May and June expiries; small stock-option positions (IndusInd 800 qty @22.52; ~2,300PE on a NBFC stock, 4 lots @220)", "numbers": "Capital ~95 lakh -> ~45 lakh profit in 6 sessions (~50%); sold Jun 7,000PE @475, May 6,500PE @210 (closed 80), May 7,000PE @324 (closed 117)", "best_regime": "Extreme high VIX with stabilizing market (COVID April 2020)", "adjustments": "Laddered entries across expiries instead of single-strike concentration", "risks": "Aggressive directional sizing; a renewed crash through the ladder strikes would produce large losses; explicitly not replicable by retail"}
- {"name": "Hedged put sale (index)", "construction": "Sell 1600 put, buy 1500 put (June expiry); Bank Nifty call ladder 21500/22000/22500/23000 with weekly hedges", "numbers": "FII context: -6000 crore in 4 sessions; VIX 30+", "best_regime": "High-VIX range with defined support", "adjustments": "Weekly hedge rolls to cut margin", "risks": "Range break below support"}

## Enhancement candidates
- crash-vs-correction checklist table: VIX behavior, news flow, breadth, position unwinds
- Liquidity-premium explanation: why far legs gap
- Table: VIX regime (11-15 low) vs strategy pairing rules
- News-quadrant table (good/very-good x bad/very-bad -> expected market behavior) with dated examples
- Worked example: reading Nifty futures premium/discount as a fear gauge

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
0027
0028
0030
0031
0034
0091
0135
0154
0171
0181
0203
0237
0246
0285
0429
0481
0487
0684
0772
0816
1425
1436
1470
1520
1534
1547
1560
1797
1910
2022
