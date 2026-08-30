# Chapter 27
## Content Stats
specials=59, dailies=0, weeklies=0
lessons=211, strategies=10, events_ref=0, verified_claims=105
## Strategies
- Read-only broker access (proposed fix)
- Long-short pair (SBI vs HDFC Bank)
- Weekly far-OTM short puts into expiry (illustrative)
- Short straddle with far wings
- Defensive-sector allocation at rich valuations
- Sovereign Gold Bond post-mortem (policy case study)
- BTC short strangle (live demo)
- ITM put calendar
- Collateral-funded far-OTM weekly selling (HNI pattern, warned)
- Hedged short option (spread)

## Key Lessons
- Under the new framework the margin system itself pays you to hedge: protection 200-300 points away cuts margin ~70%.
- Cross-margining makes a short straddle cost little more than its single costlier leg - portfolio margin logic arrives in
- Margin relief can seduce into over-sizing: four lots at 300-point risk recreates 1,200 points of exposure. Options tradi
- Index exposure carries structurally lower margins (2% vs 3.5% exposure) - another argument to avoid stock options.
- Pool pledging created rehypothecation risk - one client's blowup could cascade through the broker's entire pool.
- Direct-to-depository pledging (OTP-based) keeps shares in the client's demat; dividends flow straight to the client's ba
- Investor protection fund caps recovery at Rs 25 lakh - broker failure is a real tail risk; treat broker solvency as part
- Intraday margin scales with stock volatility: roughly 4.5x leverage on Reliance (~22%) but barely 1.3x on Idea (~77.5%) 
- From August 2020, selling shares you already hold also requires margin in the account - the exchange cannot tell an intr
- Settlement mechanics: T-day trade, T+1 funds/shares to broker/exchange, T+2 demat/money transfer; early pay-in avoids th
- A broker without early pay-in can cover a client's accidental short delivery via the auction market - the auction price 
- T+1 settlement was the likely direction for India (later implemented in Jan 2023).
- Peak-margin logic: your account must fund the worst intraday MTM excursion, not just the closing position - violent days
- The phase-out calendar (Dec 2020: ~3x intraday limit; +3 months: ~1x; +3 months: ~0.25x; by Aug-Sep 2021: none) forced t
- Freak trades printing far below market can fabricate MTM drawdowns; without an exemption, honest accounts eat penalties 
