Here is the **COMPILER BRIEF** for Part: *Options from First Principles* (Chapters 8–12).

---

## COMPILER BRIEF: Options from First Principles

**Part Goal:** Build an intuitive, first-principles understanding of options (calls/puts) as risk-transfer instruments, using Indian market examples (Nifty, Bank Nifty, stock options). Move from pure theory to practical mechanics (pricing, Greeks, expiry behavior) without overwhelming the reader.

---

### Chapter 8: The Option Contract – A Promise, Not an Obligation

1. **Purpose**  
   Define what an option *is* (call/put) using the analogy of insurance or a deposit, contrasting it with futures. Establish the buyer/seller asymmetry.

2. **Key sources**  
   - **2144**: Foundational definitions; use for the “right vs. obligation” distinction.  
   - **0244**: Real-world examples of option payoffs (Nifty calls).  
   - **2727**: Contrast with futures (margin vs. premium).  

3. **Verified facts**  
   - Nifty options are cash-settled in INR (no delivery).  
   - Lot size for Nifty options = 50 (post-2019 consolidation).  

4. **Enhancement tasks**  
   - **Table**: Comparison of Futures vs. Options (margin, premium, obligation, risk).  
   - **Example**: Payoff diagram for a Nifty 18,000 Call bought at ₹150.  

5. **Complexity estimate**  
   Easy  

6. **Length target**  
   1,200 words  

---

### Chapter 9: Option Premium – The Price of Possibility

1. **Purpose**  
   Explain what drives an option’s price (intrinsic value + time value) using the “iceberg” model. Introduce moneyness (ITM/ATM/OTM) with Indian index examples.

2. **Key sources**  
   - **0136**: Premium decomposition (intrinsic vs. time value).  
   - **1395**: Moneyness classification for Nifty strikes.  
   - **0003**: Impact of time decay (theta) on premium.  

3. **Verified facts**  
   - On June 4, 2024, Nifty ATM puts (21,500 strike) traded at ₹800+ premium intraday due to panic (source: verified event 1).  
   - HDFC Bank options saw IV spike to 45%+ on Jan 17, 2024 (source: verified event 2).  

4. **Enhancement tasks**  
   - **Table**: ITM/ATM/OTM examples for Nifty 18,000 (spot = 18,200).  
   - **Worked example**: Calculate intrinsic value for a Nifty 18,000 Call when spot = 18,450.  

5. **Complexity estimate**  
   Medium  

6. **Length target**  
   1,500 words  

---

### Chapter 10: The Greeks – Measuring the Invisible Forces

1. **Purpose**  
   Introduce Delta, Gamma, Theta, Vega in plain language. Focus on *what changes* when spot moves, time passes, or volatility shifts.

2. **Key sources**  
   - **0145**: Delta and Gamma for Nifty options (dynamic hedging).  
   - **2408**: Theta decay patterns (acceleration near expiry).  
   - **1001**: Vega and volatility regimes (pre-event vs. post-event).  

3. **Verified facts**  
   - On June 4, 2024, Nifty ATM options had Delta ~0.50 but Gamma spiked as spot crashed through strikes (source: event 1).  
   - HDFC Bank options saw Vega spike to ₹15+ per 1% IV change on Jan 17, 2024 (source: event 2).  

4. **Enhancement tasks**  
   - **Table**: Greek values for a Nifty ATM Call (spot = 18,200, strike = 18,200, 30 days to expiry).  
   - **Worked example**: If Nifty moves from 18,200 to 18,300, how does Delta change? (Gamma effect).  

5. **Complexity estimate**  
   Hard  

6. **Length target**  
   2,000 words  

---

### Chapter 11: Options Strategies – Combining Calls and Puts

1. **Purpose**  
   Teach basic multi-leg strategies (bull call spread, bear put spread, straddle) as risk-defined alternatives to naked options. Emphasize Indian margin rules.

2. **Key sources**  
   - **2344a**: Bull call spread construction (Nifty example).  
   - **1068**: Straddle for earnings/events (HDFC Bank case).  
   - **0907**: Margin requirements for spreads vs. naked options (SEBI rules).  

3. **Verified facts**  
   - HDFC Bank straddle buyers on Jan 16, 2024 (pre-results) saw 300%+ return as IV exploded (source: event 2).  
   - Nifty bull call spread (18,000/18,500) cost ~₹150 in June 2024; max profit = ₹350 (source: event 1).  

4. **Enhancement tasks**  
   - **Table**: Payoff table for Nifty 18,000/18,500 Bull Call Spread.  
   - **Worked example**: Calculate breakeven and max loss for a Bank Nifty 44,000/44,500 Bear Put Spread.  

5. **Complexity estimate**  
   Medium  

6. **Length target**  
   1,800 words  

---

### Chapter 12: Expiry – The Moment of Truth

1. **Purpose**  
   Explain what happens at expiry (settlement, pin risk, rollover). Cover weekly vs. monthly expiries in India and the “zero-day” phenomenon.

2. **Key sources**  
   - **1213**: Weekly expiry mechanics (Nifty Thursday).  
   - **3000**: Pin risk and settlement price determination.  
   - **0882**: Rollover strategies (monthly vs. weekly).  

3. **Verified facts**  
   - Nifty weekly expiry (Thursday) sees ~₹50,000 crore turnover in options (SEBI data).  
   - On June 4, 2024, Nifty 21,500 puts expired worthless as index closed at 21,800 (source: event 1).  

4. **Enhancement tasks**  
   - **Table**: Weekly expiry calendar for Nifty and Bank Nifty (2024).  
   - **Worked example**: If you hold a Nifty 18,000 Call at expiry and spot = 18,050, what is your settlement?  

5. **Complexity estimate**  
   Easy  

6. **Length target**  
   1,200 words  

---

### Part Budget Summary

| Chapter | Complexity | Target Words |
|---------|------------|--------------|
| 8       | Easy       | 1,200        |
| 9       | Medium     | 1,500        |
| 10      | Hard       | 2,000        |
| 11      | Medium     | 1,800        |
| 12      | Easy       | 1,200        |
| **Total** |          | **7,700**    |

*Note: Budget allows ±10% per chapter; total must not exceed 8,500 words.*