# Chapter 10: The Greeks, Demystified

## Part: Options from First Principles

---

**June 4, 2024. 9:15 AM. The Nifty opened at 22,764.**

By 10:30 AM, it was down 1,200 points. By noon, 1,800. By 2:00 PM, the index had touched 21,281—a drop of nearly 8.5% from the previous close. The Lok Sabha election results were coming in, and the market was pricing in a scenario nobody had prepared for.

In a small office in Andheri, a trader named Ravi stared at his screen. He had sold a Nifty 23,000 Call option two weeks ago, collecting ₹85 in premium. The option was deep out-of-the-money—Nifty was at 22,500 when he sold it. What could go wrong?

Now Nifty was at 21,300. His 23,000 Call should have been worthless. Instead, it was trading at ₹12. He was still profitable, but the movement confused him. The option had lost 86% of its value, yes. But why hadn't it gone to zero? And why was it still moving ₹2 for every ₹100 Nifty moved?

Ravi was about to learn about the Greeks—the four letters that separate professionals from amateurs in the options market.

---

## The Four Pillars of Option Pricing

Every option price is a living, breathing thing. It changes with the underlying price, with time, with volatility, and with the strike you choose. The Greeks are simply the mathematical names for these sensitivities:

- **Delta (Δ):** How much the option price changes when the underlying moves ₹1
- **Gamma (Γ):** How much Delta changes when the underlying moves ₹1
- **Theta (Θ):** How much the option price decays each day
- **Vega (ν):** How much the option price changes when volatility changes 1%

Let me show you why these matter—not as formulas, but as tools for survival.

---

## Delta: The Speedometer

Delta tells you two things: how much your option will move, and what your directional exposure really is.

**The rule:** A Call option's Delta ranges from 0 to 1. A Put option's Delta ranges from -1 to 0.

**The intuition:** A Delta of 0.5 means your option moves ₹0.50 for every ₹1 move in Nifty. A Delta of 0.8 means it moves ₹0.80. A Delta of 0.2 means it barely budges.

On that June 4 morning, Ravi's 23,000 Call had a Delta of about 0.15 when Nifty was at 22,500. That meant for every 100-point drop in Nifty, his option lost only ₹15. Seemed safe.

But here's what Ravi didn't account for: Delta changes as the underlying moves. When Nifty crashed to 21,300, his 23,000 Call's Delta dropped to 0.02. The option was so far out-of-the-money that it barely responded to further drops. That's why it still had ₹12 of value—not because of directional movement, but because of something else.

**The practical truth:** Delta is your best friend when you know where the market is going. It's your worst enemy when you're wrong and the market accelerates against you.

**Worked Example:**

*Nifty at 22,500. You buy a 23,000 Call at ₹85. Delta = 0.35.*

- Nifty rises to 22,600 (+100 points): Option gains ~₹35, now worth ~₹120
- Nifty falls to 22,400 (-100 points): Option loses ~₹35, now worth ~₹50

*But if Nifty falls to 22,000 (-500 points):*

- Delta drops to ~0.15 (because you're now further OTM)
- Option loses only ~₹75 total, not ₹175
- New price: ~₹10

This non-linearity is the first secret of options. The further you go against your position, the slower your losses grow—but only if you have time remaining.

---

## Gamma: The Accelerator

Gamma is Delta's rate of change. It tells you how fast your directional exposure is shifting.

**The rule:** Gamma is highest for at-the-money options and lowest for deep in/out-of-the-money options. Gamma explodes near expiry.

**The intuition:** Think of Gamma as the second derivative of your P&L. When Gamma is high, small moves in the underlying cause large shifts in your Delta. This is why near-expiry options can double or halve in hours.

On June 4, the Nifty 22,000 Put (which was at-the-money when Nifty was at 22,000) had a Gamma of 0.008. That meant for every 100-point drop in Nifty, its Delta increased by 0.8. If Nifty dropped another 100 points, the Put's Delta would go from 0.5 to 1.3—meaning it would start moving almost point-for-point with Nifty.

This is the Gamma trap that catches option sellers.

**The June 4 example in detail:**

Consider the Nifty 22,000 Put expiring June 6 (just two days after the crash).

- On June 3 (close): Nifty at 23,200. Put is deep OTM. Premium: ₹5. Delta: 0.05. Gamma: 0.001.
- On June 4 (10 AM): Nifty at 22,000. Put is ATM. Premium: ₹250. Delta: 0.50. Gamma: 0.008.
- On June 4 (2 PM): Nifty at 21,300. Put is ITM. Premium: ₹720. Delta: 0.92. Gamma: 0.002.

A trader who sold that Put at ₹5 on June 3 was sitting on a loss of ₹715 per option by 2 PM on June 4. And because Gamma was high, the losses accelerated as Nifty fell.

**The lesson:** Gamma rewards direction but punishes stagnation. If you're selling options, Gamma is your enemy near expiry. If you're buying, Gamma is your friend—but only if you get the direction right.

---

## Theta: The Silent Erosion

Theta is the daily decay of an option's time value. It's the one Greek that is always working against the buyer and for the seller.

**The rule:** Theta is negative for long options and positive for short options. Theta accelerates as expiry approaches.

**The intuition:** An option is like an ice cube melting in the sun. The melting is slow at first, then rapid near the end. Theta measures that melt rate.

**The non-linearity of time decay:**

- 50 days to expiry: Option loses ~2% of its value per day
- 30 days to expiry: Option loses ~3% per day
- 10 days to expiry: Option loses ~10% per day
- 5 days to expiry: Option loses ~20% per day
- 2 days to expiry: Option loses ~50% per day

**Worked Example:**

A Nifty 23,000 Call with 50 days to expiry is trading at ₹100. Theta = -₹2.

- Day 1: Option loses ₹2 → ₹98
- Day 2: Option loses ₹2 → ₹96
- ...
- Day 40: Option is at ₹60. Theta = -₹4.
- Day 41: Option loses ₹4 → ₹56
- ...
- Day 48: Option is at ₹20. Theta = -₹10.
- Day 49: Option loses ₹10 → ₹10
- Day 50 (expiry): Option is worth only intrinsic value.

Now compare with the same option when only 5 days remain:

- Option at ₹50. Theta = -₹25.
- Day 1: Option loses ₹25 → ₹25
- Day 2: Option loses ₹12 → ₹13
- Day 3: Option loses ₹6 → ₹7
- Day 4: Option loses ₹3 → ₹4
- Day 5 (expiry): Option at intrinsic value.

**The practical truth:** Theta is why option sellers prefer to sell with 30-45 days to expiry and buy back at 7-10 days. The decay is fastest in that final week, and they want to capture it. Option buyers, conversely, should buy with 60+ days to expiry to minimize theta drag.

---

## Vega: The Volatility Tax

Vega measures how much an option's price changes when implied volatility (IV) changes by 1%.

**The rule:** Vega is highest for at-the-money options with longer expiry. Vega is lowest for deep in/out-of-the-money options with short expiry.

**The intuition:** Volatility is the market's fear gauge. When fear rises, options get expensive. When fear subsides, options get cheap. Vega captures this.

On June 4, the India VIX (the market's volatility index) spiked from 14 to 32 in a single day. That 18-point jump in volatility added significant premium to every option—even those that were far from the money.

**Worked Example:**

A Nifty 23,000 Call with 30 days to expiry has a Vega of ₹8. IV is at 15%.

- IV jumps to 20% (+5%): Option gains ₹40 (5 × ₹8)
- IV drops to 10% (-5%): Option loses ₹40

Now consider the same option with 5 days to expiry. Vega = ₹2.

- IV jumps to 20%: Option gains only ₹10
- IV drops to 10%: Option loses only ₹10

**The June 4 Vega effect:**

Ravi's 23,000 Call had a Vega of ₹6 when Nifty was at 22,500. IV was 14%. When IV spiked to 32%, his option gained ₹108 in pure volatility premium—even though Nifty was moving against his position.

That's why his option was still worth ₹12 when it should have been ₹0. The volatility spike kept it alive.

**The practical truth:** Vega is why options can be expensive even when the market is calm. It's also why you should never sell options when IV is low—you're not being compensated for the risk of a spike.

---

## The Greeks in Action: A Real Trade

Let me walk you through a complete trade to see how all four Greeks interact.

**The Setup:**

- Date: May 15, 2024
- Nifty: 22,500
- Trade: Buy Nifty 23,000 Call, expiry June 27 (43 days)
- Premium paid: ₹85
- Greeks at entry: Delta 0.35, Gamma 0.004, Theta -₹1.50, Vega ₹7

**Scenario A: Nifty rises slowly to 23,000 by June 10 (25 days later)**

- Nifty gain: 500 points (+2.2%)
- Delta effect: +₹175 (500 × 0.35)
- Gamma effect: Delta increased to 0.55, so additional +₹100
- Theta effect: -₹37.50 (25 days × ₹1.50)
- Vega effect: IV stable at 15%, so ₹0
- Total P&L: +₹237.50
- Option value: ₹322.50

**Scenario B: Nifty crashes to 21,500 by June 4 (20 days later)**

- Nifty loss: -1,000 points (-4.4%)
- Delta effect: -₹350 (1,000 × 0.35)
- Gamma effect: Delta dropped to 0.10, so losses slowed
- Theta effect: -₹30 (20 days × ₹1.50)
- Vega effect: IV spiked to 32%, so +₹119 (17% × ₹7)
- Total P&L: -₹261
- Option value: Still ₹85 - ₹261 = negative? No—option can't go below zero. Actual value: ₹12 (intrinsic zero + time value from Vega)

**The key insight:** In Scenario B, the Vega spike saved the option from going to zero. Without the volatility jump, the option would have been worth ₹0. With it, the trader recovered ₹12 per option—a small consolation, but a real one.

---

## The Greeks Cheat Sheet for Indian Markets

| Greek | What It Measures | When It's High | When It's Low | Trader's Rule |
|-------|-----------------|----------------|---------------|--------------|
| Delta | Directional exposure | ATM options, long expiry | Deep OTM/ITM, short expiry | "Delta is your bet size" |
| Gamma | Delta's rate of change | ATM options, near expiry | Deep OTM/ITM, far expiry | "Gamma is your risk accelerator" |
| Theta | Time decay | Near expiry, ATM options | Far expiry, deep OTM/ITM | "Theta is the seller's paycheck" |
| Vega | Volatility sensitivity | ATM options, long expiry | Deep OTM/ITM, short expiry | "Vega is the fear premium" |

---

## The Professional's Approach to Greeks

After years of trading, here's how I use the Greeks:

**1. Delta for sizing.** I never risk more than 2% of my capital on a single Delta exposure. If my Delta is 500 (meaning I'm long 500 Nifty futures equivalent), I know my daily P&L swing is roughly ₹50,000 per 100-point move.

**2. Gamma for exit timing.** When Gamma is high (last 7-10 days before expiry), I either reduce position size or switch to next-month options. The risk of a Gamma squeeze is too high.

**3. Theta for strategy selection.** I sell options when Theta is high (30-45 days to expiry) and buy when Theta is low (60+ days). This maximizes the decay I collect or minimizes the decay I pay.

**4. Vega for volatility trading.** I buy options when IV is below its 20-day average (cheap volatility) and sell when IV is above its 20-day average (expensive volatility). This is a separate trade from directional views.

---

## The Greeks and the June 4 Lesson

Let's return to Ravi. He sold a 23,000 Call at ₹85 with 43 days to expiry. His Greeks were:

- Delta: -0.35 (short call = negative Delta)
- Gamma: -0.004 (short Gamma)
- Theta: +₹1.50 (positive Theta, collecting decay)
- Vega: -₹7 (short Vega)

When Nifty crashed, here's what happened to his position:

- **Delta effect:** Nifty fell 1,200 points. His short call gained ₹420 (1,200 × 0.35). Good.
- **Gamma effect:** As Nifty fell, his Delta became less negative (from -0.35 to -0.10). His gains slowed. Good.
- **Theta effect:** He collected ₹64.50 in time decay (43 days × ₹1.50). Good.
- **Vega effect:** IV spiked 18%. His position lost ₹126 (18 × ₹7). Bad.

Net P&L: +₹420 + ₹64.50 - ₹126 = +₹358.50 per option.

He made money. But he could have made more if he had understood Vega. The volatility spike cost him ₹126—nearly 20% of his potential profit.

**The real lesson:** Ravi was lucky. He sold a far OTM option that became even further OTM. But if Nifty had only fallen to 22,500 (still above his strike), his Delta would have been -0.35, and he would have lost money on the directional move while still getting crushed by Vega.

---

## Key Takeaways

1. **Delta is your directional exposure, not your position size.** A short call with Delta -0.35 is equivalent to being short 35 Nifty futures. Know your equivalent futures exposure at all times.

2. **Gamma is the accelerator of risk.** Near expiry, Gamma explodes. A 100-point move can double or halve your Delta. Size down or roll forward when Gamma is high.

3. **Theta is the seller's edge, but it's not free.** You collect time decay, but you're selling insurance. One bad event can wipe out months of decay collection. Always ask: "Am I being compensated for the tail risk?"

4. **Vega is the hidden variable.** Most traders focus on Delta and Theta but ignore Vega. In volatile markets, Vega can dominate your P&L. Check IV before entering any trade.

5. **The Greeks work together, not in isolation.** A trade that looks good on Delta and Theta can be destroyed by Vega. A trade that looks bad on Delta can be saved by Gamma. Always run the full Greek profile before committing capital.

---

*In the next chapter, we'll explore how to combine these Greeks into trading strategies that work across market conditions—from trending to range-bound, from low volatility to high.*