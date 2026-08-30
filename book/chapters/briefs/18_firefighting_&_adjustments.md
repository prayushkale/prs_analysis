# Chapter 18: Firefighting & Adjustments
Part: IV The Strategy Library

## Source count
- Transcripts directly mapped: 47
- Unique IDs: 47

## Top themes
- position movement with market
- case study with daily data
- futures vs options overlay
- portfolio diversification
- short strangle adjustment
- put selling into strength
- adjustments-over-stoploss
- small consistent returns
- transparency-vs-trolling
- position diversification

## Key lessons
- [0115] A short straddle is a living position: when the market trends, shift the straddle to the new ATM instead of nursing the old strike - movement with the market is the edge backtests cannot capture.
- [0115] Ratio spreads with a defended support (9500) win in both directions: the long put lost 1.84 lakh as the market rallied, but repeated short-put rounds returned ~4.24 lakh plus weekly overlay.
- [1062] Crypto premiums are rich enough that disciplined straddle/strangle selling survives even violent swings - but positions need active adjustment, not set-and-forget.
- [0030] In violent moves, premiums behave abnormally because losing-side sellers are forced to square up and roll - not because the market 'should' behave that way.
- [0115] Late entrants should not chase a running trade: the risk-reward at entry is gone; wait for the next series and start fresh (genericized member guidance).
- [0412] Exchange operating-range bands (about +/-3% around last traded price) block market orders in illiquid strikes - a hidden protection and a hidden trap.
- [0487] No strategy is self-sufficient: a wrong directional view was rescued entirely by layered adjustments (multiple straddle strikes, staggered entries).
- [1142] After-results IV collapse crushes premiums - position before results so the decay pays you; keep a small long-call tail so a VIX spike doesn't hurt.
- [0122] Personal P&L screenshots are marketing, not evidence: audit capital trajectory and consistency, not single screenshots (inversion of the scam test).
- [0246] In violent markets, far-OTM options can move opposite to the index because traders buy them to cut margin - premium behavior beats price intuition.

## Strategies (if applicable)
- {"name": "Strangle roll-under-stress mechanics", "construction": "Short 9,000CE + 7,000PE written Friday around spot 8,000; on a violent rally, buy back 7,000PE (releasing margin) and sell 7,500/8,000PE instead", "numbers": "Legs 1,000 points either side of spot; roll targets 500-1,000 points closer", "best_regime": "After violent directional moves when the losing leg must be repositioned", "adjustments": "Roll the losing short leg closer using either spare cash (preferred) or margin released by squaring the far leg", "risks": "Forced buyback at inflated premiums; whipsaw if the market reverses immediately"}
- {"name": "IndusInd earnings-day iron-fly style combo", "construction": "Sell 400CE + sell 400PE, buy 500CE + buy 300PE (current month)", "numbers": "profit down 77% vs expected 95% fall; stock closed ~15-17% higher", "best_regime": "earnings day when heavy short positioning built up", "adjustments": "speaker's own adjustments not disclosed; states adjustments depend on additional capital", "risks": "big gap moves on expiry; adjustments need reserve capital"}
- {"name": "Call ratio spread (financed directional)", "construction": "Long 1x 9400CE; short 2x 9800CE; short 1x 10000CE (300/600/300 qty), plus weekly far-OTM call sales to offset net debit", "numbers": "9400CE ~219; 9800CE ~80; 10000CE ~45; net ~-4300 before weekly sales (~+2800 after); max profit ~1,15,000 at 9800 expiry; loss begins ~10,080", "best_regime": "Mildly bullish, expect stay below written strikes", "adjustments": "Promised follow-up through expiry; weekly-call sales used to neutralize debit", "risks": "Unlimited above 10,080 (net short top strike); upside capped at 9800 zone"}
- {"name": "OTM credit-sale adjustment on a losing ratio", "construction": "Existing: long 350CE, short 2x 380CE (max loss ~0.50/share ~ Rs 800/lot). Adjustment: sell 1x 400CE at ~3.65", "numbers": "Pre-adjustment loss ~Rs 3,000; post-adjustment profit ~Rs 2,000 per lot", "best_regime": "After a results miss confirms the directional view is dead", "adjustments": "Collected credit exceeds the defined max loss; no further action needed unless stock reverses hard", "risks": "New short call adds upside risk; acceptable because view is now neutral-bearish"}
- {"name": "Cash-secured puts (ICICI 300PE, HDFC 840PE)", "construction": "Sell puts below market with full cash set aside for delivery", "numbers": "+33,000 ICICI and +28,000 HDFC in May 2020", "best_regime": "moderately bullish with stocks near support", "adjustments": "take delivery if assigned; roll if view changes", "risks": "sharp breakdown below strike forces delivery at loss"}

## Enhancement candidates
- expectation-psychology sidebar for Part I
- Worked example: proxy-hedge demand distortion when a group has one shortable stock (short interest concentration, ban-day dynamics)
- 1:3 call-ratio payoff table with breakeven algebra
- Stop-loss-and-cost-revision straddle workflow
- straddle breakeven quick-math box

## Representative daily/weekly entries


## Verified events (relevant)


## Source IDs
0030
0050
0063
0064
0077
0078
0103
0104
0105
0115
0122
0126
0127
0129
0131
0165
0199
0246
0412
0487
0538
0654
0663
0664
0815
0978
0990
1002
1062
1142
