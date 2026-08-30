# Part III: Options from First Principles

## Chapter 8 — Why Derivatives Exist

### From Farmer to Futures

A farmer plants wheat in November and expects to harvest it in April. Between planting and harvest, the price of wheat can move 30%. If it falls, the farmer loses money on every tonne before he even sells it.

A miller needs wheat in April. Between now and then, the price can rise 30%. If it rises, his costs explode before he makes a rupee.

Derivatives exist to solve this problem. The farmer and the miller agree today on a price for April delivery. That agreement — a forward contract — transfers price risk from both parties to the market. The farmer locks in his selling price; the miller locks in his buying price. Both can now focus on their core business, not on wheat price speculation.

### The Futures Standard

A forward contract between two people works until one of them defaults. The futures exchange solves this: it standardizes the contract (lot size, expiry date, underlying), requires margin from both parties, and provides daily settlement (mark-to-market, or M2M). The exchange becomes the counterparty to every trade.

A futures position is settled daily: if the price moves against you, you must add margin (margin call). If it moves in your favor, the profit is credited to your account overnight. This daily settlement is the innovation that made derivatives scalable — because no one trusts a stranger to pay next month.

### The Three Roles

Every derivatives market participant falls into one of three categories:

| Role | Motivation | Example |
|------|-----------|---------|
| **Hedger** | Reduces existing risk | A mutual fund buys Nifty puts to protect its portfolio. |
| **Arbitrageur** | Exploits price differences | Buys Nifty futures when they trade below cash Nifty, waits for convergence. |
| **Speculator** | Takes directional risk for profit | Sells Nifty calls because she expects the market to fall. |

The speculator is what most retail traders think they are. But the profitable retail trader thinks like a hedger-meets-arbitrageur: **they design positions with defined risk, structural edge, and hedging built in.** Pure speculation — buying naked calls hoping for a rally — is the 93% path.

### M2M (Mark-to-Market)

A crucial concept that trip up beginners. "When you buy a futures contract," Dhanraj explained, "you don't wait until expiry to gain or lose. Every evening, your broker calculates the profit or loss based on the closing price. If the futures moved ₹10 against you, ₹10 × lot size is deducted from your account that night."

The psychological impact of M2M losses is what kills novice futures traders. A well-constructed options position, by contrast, does not have daily M2M cash flows — the margin moves, not the cash — which is one reason options selling, with proper sizing, is less emotionally damaging than futures trading.

---

## Chapter 9 — Calls and Puts: The Building Blocks

### Call Option

A call option gives the buyer the right, but not the obligation, to **buy** the underlying at a fixed price (the strike) on or before a fixed date (expiry). The buyer pays a premium for this right.

- **Buyer's view**: Bullish. Profit starts when the underlying exceeds (strike + premium).
- **Seller's view**: Bullish-neutral or bearish. Profit as long as the underlying stays below (strike + premium).

### Put Option

A put option gives the buyer the right, but not the obligation, to **sell** the underlying at the strike on or before expiry.

- **Buyer's view**: Bearish. Profit starts when the underlying falls below (strike − premium).
- **Seller's view**: Bearish-neutral or bullish. Profit as long as the underlying stays above (strike − premium).

### Intrinsic Value and Time Value

An option's premium = **intrinsic value** + **time value**.

- **Intrinsic value**: How much the option is worth if exercised immediately. For an ATM or OTM option, intrinsic value is zero. For an ITM call, it is (spot − strike). For an ITM put, it is (strike − spot).
- **Time value**: Everything else. It decays toward zero as expiry approaches. The day before expiry, an ATM option has almost no time value; on expiry day, it has zero.

The time value is what the option seller collects. The intrinsic value is what the option buyer hopes to capture. The seller's edge is that time passes, and time value decays. The buyer's edge is that price moves — but price is binary (it either moves enough or it doesn't), while time is deterministic (it always passes).

### Exercise and Assignment

If you are long an option that is ITM at expiry, you are automatically exercised (physical settlement for stock options, cash settlement for index options). If you are short an option that is ITM, you are assigned — you must fulfill the contract.

For index options in India, settlement is **cash-based**: the difference between the strike and the settlement price is transferred. For stock options, it is **physical** — shares move. "Physical settlement in stock options," Dhanraj warned repeatedly, "is the source of countless horror stories. If you sell a stock option that expires ITM, you must deliver the shares. If you do not have them, you pay the difference at market price. That difference can be enormous."

---

## Chapter 10 — The Greeks, Demystified

*(Enhanced: each Greek with intuition and worked example)*

### Delta

Delta measures how much the option price changes when the underlying moves ₹1. A call option has positive delta (0 to 1); a put option has negative delta (0 to -1). ATM options have delta ~0.5.

**Intuition:** Delta is rough probability of expiring ITM. A 0.5 delta call has roughly a 50% chance of being in-the-money at expiry. Delta increases as expiry approaches for ITM options (approaches 1) and decreases for OTM options (approaches 0).

**Worked example:** Nifty at 24,000. A 24,000 call (ATM) has delta 0.5. Nifty moves to 24,050. The option price rises by approximately 0.5 × 50 = 25 points (₹625 at ₹25/point).

### Gamma

Gamma measures how much delta changes when the underlying moves ₹1. High gamma = delta changes rapidly. Gamma is highest for ATM options near expiry.

**Intuition:** Gamma measures "convexity" — the tendency of options to accelerate in value as they move ITM. Near expiry, an ATM straddle with high gamma can swing wildly on a 50-point move, earning or losing more than the premium itself.

**Worked example:** A weekly ATM option 3 days before expiry may have gamma of 0.05. Nifty is at 24,000, the ATM call delta = 0.5. Nifty moves to 24,020. Delta is now approximately 0.5 + (0.05 × 20) = 1.5? No — gamma of 0.05 means delta changes by 0.05 for each point move. So delta goes from 0.5 to 0.5 + (0.05 × 20) = 1.5? That's physically impossible because delta can't exceed 1. In reality, gamma near expiry is not linear — it's a second-order effect that works in small increments. The gamma effect means that a rapidly moving market close to expiry can deliver much larger gains (or losses) than delta alone predicts.

### Vega

Vega measures how much the option price changes when IV changes by 1%. Long options have positive vega; short options have negative vega.

**Intuition:** Vega is the option buyer's enemy and the seller's friend. When IV is low and you buy an option, you are paying cheap premium — but if IV rises, your option gains from vega. When IV is high and you sell an option, you are collecting rich premium — any IV decline adds to your profit.

**Worked example:** A 30-day ATM option with vega 0.20. IV rises from 15% to 20% (+5%). The option price increases by approximately 0.20 × 5 = 1 point (₹25). Not huge for a single day, but over multiple days, a 10% IV swing moves option prices significantly.

**Key insight:** "Vega is the real source of the poverty of option buyers," Dhanraj said. "You buy an option at 15% IV. The market moves in your favor. But IV falls to 12%. Your option gains nothing — or even loses — despite the correct direction."

### Theta

Theta measures how much the option price decays per day. Options sellers have positive theta (they gain from time passing); buyers have negative theta (they lose).

**Intuition:** Theta is the most reliable Greek. Time always passes. An ATM option with 30 days to expiry decays slowly at first and accelerates in the last 10 days.

**Worked example:** A 30-day ATM option with theta -0.15. You own the option. Tomorrow, assuming nothing else changes (same spot, same IV), the option price falls by ₹3.75 (0.15 × ₹25). Over a week, that's ₹26 of decay — on a premium of ~₹100 (for a 30-day ATM). One-quarter of your premium gone in a week with zero price movement.

### The Greeks at a Glance Table

| Greek | Measures | Who Benefits | Typical ATM 30-day | Near Expiry Behavior |
|-------|----------|-------------|-------------------|---------------------|
| Delta | Price change per ₹1 move | Call buyer wins on up moves; put buyer on down moves | 0.5 (call), -0.5 (put) | Approaches 1 or 0 for ITM/OTM |
| Gamma | Delta change per ₹1 move | Both sides; accelerates ITM moves | 0.03–0.05 | Explodes for ATM; tiny for OTM/ITM |
| Vega | Price change per 1% IV change | Option buyer (long vega) | 0.15–0.25 | Collapses near expiry |
| Theta | Daily decay | Option seller (positive theta) | -0.10 to -0.20 | Accelerates in last 10 days |
| Rho | Price change per 1% rate change | Mostly neglected for <1yr options | ~0.01 | Negligible |

---

## Chapter 11 — Implied Volatility: The Real Price of Options

### IV vs. Historical Volatility

Historical volatility (HV) measures how much the underlying has actually moved in the past. Implied volatility measures how much the option market **expects** it to move in the future. When IV > HV, options are expensive. When IV < HV, they are cheap.

The comparison is the most basic edge in options trading. "When everyone is using the same strategy at the same time, the IV is high," Dhanraj explained. "You sell into high IV. You buy (if you must buy) into low IV."

### IV Rank and Percentile

- **IV rank** = Where current IV stands relative to the past year's range. IV rank of 20% means IV is higher than 20% of days in the past year.
- **IV percentile** = Similar but more granular.

Rule of thumb: IV rank below 20% → premiums are historically cheap (sell fewer options, hedge more). IV rank above 80% → premiums are historically expensive (sell aggressively with appropriate hedges).

### The Skew

OTM puts consistently have higher IV than OTM calls. This is called the **skew** — the market's perception that a crash is more likely than a melt-up (consistent with the fat-tailed distribution of stock returns). The skew is steepest during crises and flattest during bull markets.

"Never compare a put premium to a call premium at the same strike," Dhanraj advised. "The put will always be more expensive. That's skew, not a directional signal."

---

## Chapter 12 — Margins, Collateral and the Machinery

### SPAN and Exposure

When you sell an option, the exchange demands margin — not a down payment, but a performance bond.

- **SPAN margin** = Worst-case loss estimated by the exchange's risk model for a single day. For a Nifty ATM short straddle, ~₹1.2 lakh.
- **Exposure margin** = Additional buffer, typically 3–5% of contract value. For Nifty ATM options, ~₹15,000–25,000.

### The 50% Cash Rule

SEBI's 50% cash component rule, implemented from the early 2020s, requires that at least 50% of the total margin must be deposited as cash — shares, mutual funds, and other collateral cannot cover more than 50%. "This rule killed the leverage game for thousands of traders," Dhanraj said. "They had ₹1 crore worth of shares and assumed they could trade with ₹1 crore margin. Now they can trade with only ₹50 lakh. Cash component is the bottleneck."

### Margin Netting

When you have multiple positions in the same underlying that offset each other — a long call + a short put with different strikes — the exchange recognizes the offset and reduces margin. A short straddle has lower total margin than the sum of the two individual positions because the maximum loss occurs on one side only (the other side becomes ITM but reduces risk).

"Margin netting is the option seller's best friend," Dhanraj noted. "If you can pair your sells with buys that offset the risk — even at different strikes — the exchange charges you less, and your return on margin improves."

---

## Endnotes (Part III)

[^6] The Greeks tables and worked examples are synthesized from the "Mission Options" series, specifically episodes E18 (Delta), E19 (Gamma), E20 (Vega), E21 (Theta & Rho), and E22 (IV). The speaker's spoken examples have been translated into formal payoff tables for clarity.

[^7] SEBI's peak margin framework: Effective September 2020 with phased implementation through June 2021. Key rule: 50% of required margin must be cash; end-of-day margin utilization capped at 100% of available margin. Source: SEBI circular SEBI/HO/MRD/DRMNP/CIR/P/2020/165.