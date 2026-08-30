# Chapter 16: Butterflies & Condors
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 5
- Unique IDs: 5

## Top themes
- limited-risk structures
- position management
- long-term options
- volatility crush
- butterfly spread
- position review
- strategy series
- Delta Exchange
- earnings trade
- short straddle

## Key lessons
- [0244] Even across seven major crises (Lehman, Greece, taper tantrum, China devaluation, demonetization+Trump, Brexit, Feb-2018 US flash crash), Nifty never gapped more than 400 points except Lehman and COVID; Bank Nifty max 1,200.
- [0244] Implied volatility is almost always higher than historical volatility - paying full straddle premium around events is structurally losing.
- [0654] Butterflies cap downside loss if the stock crashes, but upside loss beyond the upper strike is real money — hedge or manage it.
- [0244] Across 10 budgets, Nifty never closed more than 2% from the prior close except the COVID-coinciding 2020 budget (-3.26%).
- [0654] A strategy need not be held to expiry — exit into post-event strength or adjust; firefighting beats stubbornness.
- [0244] Back spreads cut max loss by a third versus long straddles and win big only on large moves in one direction.
- [1854] Run double ratios (call ratio + put ratio) when direction is unknown; margin ~Rs 1.5L for ~13% in a month.
- [0654] In a butterfly, buys and sells must balance (1-5-4) — only then is risk limited and margin benefits apply.
- [0654] Anchor strategy legs to the stock's all-time high: profit zone below the ATH, limited loss above it.
- [1854] When the trend flips, close the old view - a bullish combo closed at +8% funded the bearish book.

## Strategies (if applicable)
- {"name": "Put back spread", "construction": "sell 1x ATM+100 put; buy 2x ATM-200 puts (Nifty ~13,600: sell 13,700PE, buy 2x 13,400PE)", "numbers": "lower breakeven ~13,253 vs straddle's 13,162; max loss ~Rs 20,000 vs straddle ~Rs 32,000; margin ~Rs 1 lakh", "best_regime": "bearish into event; profits only on large falls", "adjustments": "roll or convert with far put", "risks": "sideways market loses the debit; margin understated by platforms"}
- {"name": "Call back spread", "construction": "sell 1x ATM-100 call; buy 2x ATM+200 calls", "numbers": "profit begins ~14,000 vs straddle 14,050; max loss ~Rs 20,000", "best_regime": "bullish into event", "adjustments": "same mirror logic", "risks": "small loss on big fall; sideways loses"}
- {"name": "Put ratio spread", "construction": "buy 1x ATM put (~Rs 175); sell 2x puts ~250-350 lower", "numbers": "max profit ~Rs 18,000-19,000 near 13,300-13,350; loss begins below ~13,100 and is uncapped; upside loss ~Rs 1,000", "best_regime": "mildly bearish; expects limited fall", "adjustments": "buy far OTM put to cap risk (butterfly)", "risks": "crash below short strikes = uncapped loss"}
- {"name": "Put butterfly (capped ratio)", "construction": "put ratio + buy 1x far OTM put (12,800)", "numbers": "max loss ~Rs 23,000 only below 12,800 (-7.8% in a day - unlikely); upside loss ~Rs 1,000; margin ~Rs 54,000+/-10k", "best_regime": "defined-risk bearish event trade", "adjustments": "exit shorts on rally", "risks": "capped but wide loss zone"}
- {"name": "Call ratio spread", "construction": "buy 1x ATM call; sell 2x calls 200 higher; optional far OTM call for cap", "numbers": "loss begins above ~14,000; upside profit if rally exceeds upper strikes", "best_regime": "'budget like never before' bullish bets", "adjustments": "convert to butterfly", "risks": "uncapped loss above short strikes"}

## Enhancement candidates
- Why 5:4 sell:buy ratio instead of symmetric butterfly — margin equalization math
- Crypto option strategy sizing guidelines
- Crypto option strategy payoff tables
- Bitcoin consolidation-to-breakout pattern
- Payoff tables for back spread vs straddle side-by-side

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0244
0654
1854
2911
2935
