# Chapter 11: Implied Volatility

## The Market's Fear Gauge

On June 4, 2024, I was sitting in my office in Andheri, watching the Nifty screen turn a shade of red I hadn't seen since March 2020. The index had opened near 23,300. By 11:30 AM, it was down over 1,800 points. Someone in the dealing room shouted that the 21,500 strike put option—which had traded at ₹80 the previous Friday—was now changing hands at ₹850.

That's a 960% increase in two trading sessions.

The stock hadn't moved 960%. The index hadn't moved 8%. So what had moved? The price of uncertainty itself.

That is implied volatility.

---

## What Implied Volatility Actually Is

Let me be direct: implied volatility is not the same as historical volatility. Historical volatility tells you how much the underlying asset *has* moved in the past. Implied volatility tells you what the market *expects* the asset to move in the future, as priced into option premiums.

Think of it this way: if you buy a house, the price reflects not just what the house is worth today, but what people believe it will be worth next year. Implied volatility is that same forward-looking expectation, but for the "wiggliness" of a stock or index.

When I buy a Nifty call option, I am paying for two things: the right to profit if Nifty goes up, and the insurance that the path to that profit won't be too bumpy. The bumpiness—the expected magnitude of price swings—is what implied volatility captures.

---

## The Mathematics (Simple Version)

Every option pricing model—Black-Scholes, Binomial, whatever—takes five inputs:

1. Current price of the underlying (spot)
2. Strike price
3. Time to expiry
4. Risk-free interest rate
5. **Volatility**

The first four are observable. You can look up the Nifty spot price. You know the strike. You know how many days remain until expiry. You can check the RBI's repo rate for the risk-free rate.

But volatility? That's the only input you cannot observe directly. It must be *implied* from the option's market price.

Here's the key insight: **implied volatility is not a cause. It is a consequence.**

Traders don't set implied volatility. They set option prices—bids and offers in the market. The pricing model then works backwards to figure out what volatility number would make those prices "fair." That backward-calculated number is implied volatility.

If a Nifty 22,000 call is trading at ₹200, and all other inputs are known, the model says: "To justify a ₹200 premium, the market must be expecting annualized volatility of X%." That X% is the implied volatility.

---

## The Iceberg Model Revisited

In Chapter 9, I introduced the iceberg model of option premium: intrinsic value is the visible tip, time value is the submerged mass.

Implied volatility is the temperature of the water surrounding that iceberg. When the water is warm (low IV), the iceberg melts slowly—time value decays gently. When the water is freezing (high IV), the iceberg grows—time value inflates.

But here's the part most beginners miss: **implied volatility affects the entire option chain, not just one strike.**

On that June 4 morning, every single Nifty put option—from 21,000 to 24,000—saw its premium explode. The 23,000 put, which was deep out-of-the-money at the open, suddenly became expensive. Why? Because the market was pricing in the possibility of a 10% crash. The implied volatility for the entire chain had jumped from 14% to over 40% in hours.

---

## A Worked Example: The June 4 Panic

Let me walk you through what happened, using real numbers (rounded for clarity).

**Before the event (June 3, close):**
- Nifty spot: 23,300
- Nifty 21,500 put (expiring June 27): ₹80
- Implied volatility: 14%

**During the panic (June 4, 11:30 AM):**
- Nifty spot: 21,500 (down 7.7%)
- Nifty 21,500 put: ₹850
- Implied volatility: 42%

Now, let's decompose that ₹850 premium:

**Intrinsic value:** The put is at-the-money (spot = strike), so intrinsic value = max(21,500 - 21,500, 0) = ₹0.

**Time value:** ₹850 - ₹0 = ₹850.

But wait—the option has 23 days to expiry. Even if Nifty stayed at 21,500, the time value should be much lower. Under normal conditions (14% IV), the time value for an ATM put with 23 days left would be roughly ₹120-150.

So why was the market paying ₹850?

Because the market was pricing in the possibility that Nifty could fall another 10% in the next three weeks. The implied volatility of 42% meant the market expected daily moves of roughly 2.6% (42% divided by √252 trading days). Under normal conditions (14% IV), the expected daily move was only 0.88%.

That extra ₹700 in premium was pure uncertainty premium—the market's fear of the unknown.

---

## The Volatility Smile and Skew

If you plot implied volatility against strike prices for a given expiry, you rarely get a flat line. You get a curve. In Indian markets, this curve typically shows higher IV for out-of-the-money puts than for out-of-the-money calls.

This is called the **volatility skew**.

Why does this happen? Because market participants are asymmetrically afraid. They fear crashes more than they hope for rallies. A 10% crash wipes out portfolios. A 10% rally is just a good day. So traders bid up out-of-the-money puts as insurance, driving their implied volatility higher.

On June 4, the skew became extreme. The 21,000 put (5% below spot) had an IV of 55%. The 24,000 call (12% above spot) had an IV of only 28%. The market was pricing in a 55% chance of a further crash but only a 28% chance of a recovery.

This asymmetry is not irrational. It is the market's collective wisdom about tail risks.

---

## How Implied Volatility Moves

Implied volatility does not move randomly. It follows patterns:

**1. Event-driven spikes:** Before major events (budget, RBI policy, election results), IV rises. After the event, IV collapses. This is called "volatility crush."

**2. Crash-induced expansion:** When markets fall sharply, IV explodes. When markets rise slowly, IV contracts. This is the leverage effect—falling prices increase financial leverage, which increases uncertainty.

**3. Time decay of uncertainty:** As expiry approaches, IV tends to decline for near-term options. The market becomes more certain about the near future.

**4. Mean reversion:** IV tends to revert to its long-term average. Extremely high IV eventually falls. Extremely low IV eventually rises.

I have seen traders lose fortunes buying options when IV was at 50%, expecting it to go to 60%. They forget that IV is like a rubber band—the more you stretch it, the harder it snaps back.

---

## The VIX: India's Fear Index

India Volatility Index (India VIX) is a measure of the implied volatility of Nifty options for the next 30 days. It is calculated using the order book of Nifty options, not a single strike.

When India VIX is at 12, the market is complacent. When it crosses 25, the market is nervous. When it crosses 35, the market is panicking.

On June 4, India VIX touched 32.5. It had been at 11.8 on June 1.

The VIX is not tradable directly (unlike the US VIX futures), but it is the single best indicator of market fear. I check it every morning before I look at any chart.

---

## Trading Implied Volatility: The Two Camps

There are two ways to trade options based on IV:

**Camp 1: Directional traders.** They buy calls when they expect Nifty to rise, or puts when they expect Nifty to fall. For them, IV is a cost of doing business. High IV means expensive options, which reduces potential profits.

**Camp 2: Volatility traders.** They don't care about direction. They care about whether IV is high or low relative to its history. When IV is high, they sell options (collect premium). When IV is low, they buy options (pay premium).

I have seen both camps make money. I have seen both camps lose money. The key is knowing which camp you belong to.

If you are a directional trader, do not ignore IV. A ₹200 call option on a stock with 20% IV is not the same as a ₹200 call option on a stock with 40% IV. The latter is priced for twice the expected movement. You need a bigger directional move just to break even.

If you are a volatility trader, remember: selling options when IV is high is not free money. It is selling insurance during a hurricane. You can collect premium for weeks, then lose it all in one bad day.

---

## The IV Trap

Let me tell you about a trader I'll call Rajesh. In early 2023, he noticed that India VIX was at 11—near its all-time low. He decided to buy Nifty options, expecting IV to rise.

He bought 22,000 calls and 22,000 puts (a straddle) for a total premium of ₹400. His logic: "IV can't go lower, it must go up."

For three months, IV stayed between 10 and 13. Rajesh's options decayed. He lost 60% of his capital.

Then, in September 2023, Nifty had a 3% correction. IV jumped to 18. Rajesh's options finally became profitable. But by then, he had already closed most of his positions in frustration.

The lesson: **IV can stay low longer than you can stay solvent.** Low IV does not mean IV will rise tomorrow. It means the market is calm. Calm markets can stay calm for years.

---

## Practical Rules for Using IV

Here are the rules I follow:

**Rule 1: Know the IV percentile.** Don't just look at the current IV. Look at where it stands relative to its own history. If Nifty's 30-day IV is at the 90th percentile (higher than 90% of past readings), it is expensive. If it is at the 10th percentile, it is cheap.

**Rule 2: IV is mean-reverting, but not on your timeline.** You cannot predict when IV will revert. You can only position for it.

**Rule 3: High IV favors sellers, low IV favors buyers.** When IV is high, consider selling options (credit strategies). When IV is low, consider buying options (debit strategies). But always manage risk.

**Rule 4: IV expansion is faster than IV contraction.** IV can double in a day (as on June 4). It takes weeks to come back down. This asymmetry means that buying options for IV expansion is a low-probability, high-payoff bet. Selling options for IV contraction is a high-probability, low-payoff bet.

**Rule 5: IV is not a predictor of direction.** High IV does not mean the market will crash. It means the market expects large moves in either direction. On June 4, high IV was justified by a crash. But in March 2020, high IV preceded a 30% rally.

---

## The Final Word

Implied volatility is the market's best guess at future uncertainty. It is not a crystal ball. It is a thermometer.

When the thermometer reads 104°F, you know the patient has a fever. You don't know if the fever will break tomorrow or turn into pneumonia. You just know that something is wrong.

Similarly, when India VIX reads 32, you know the market is feverish. You don't know if it will crash further or recover. You just know that uncertainty is high, and you should adjust your position sizing accordingly.

I have made my biggest profits trading IV dislocations. I have also made my biggest mistakes ignoring IV. The difference between a professional and an amateur is not whether they use IV—it is whether they respect it.

---

## Key Takeaways

1. **Implied volatility is the market's expectation of future price swings, derived from option prices—not a direct observation.** It is the "fifth input" that makes option pricing models work.

2. **IV spikes during crises and crashes, and contracts during calm periods.** The June 4, 2024 event saw Nifty put IV jump from 14% to 42% in hours.

3. **The volatility skew shows that out-of-the-money puts are usually more expensive than out-of-the-money calls**, reflecting the market's asymmetric fear of crashes versus rallies.

4. **India VIX is the benchmark for 30-day implied volatility of Nifty options.** It is a fear gauge, not a trading instrument.

5. **High IV favors option sellers; low IV favors option buyers.** But both strategies carry risk—selling during high IV is selling insurance during a hurricane, and buying during low IV can lead to time decay losses if volatility stays low.