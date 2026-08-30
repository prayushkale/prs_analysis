# Chapter 6: Reading the Option Chain

## How This Market Works

---

### The Day the Chain Spoke

On June 4, 2024, at 9:15 AM, the Nifty 50 opened at 23,200. By 10:30 AM, it was down 5%. By noon, it had touched 21,281 — a drop of nearly 8.5% from the previous close. The Lok Sabha election results were coming in, and the market was pricing in a far weaker mandate than expected. Panic was everywhere. But if you had looked at the option chain that morning, you would have seen something strange.

The 21,000 Put — a strike that seemed absurdly deep out-of-the-money just a day earlier — had suddenly accumulated over 1.2 crore shares of open interest. Someone was buying protection at levels no one thought possible. And by 1:30 PM, when the Nifty bounced back to 22,600, those puts were worth ten times their morning premium. The option chain had told the story before the news did.

That is what this chapter is about. Not just what an option chain is, but how to read it as a live map of where the smart money is positioning itself.

---

### What Is an Option Chain?

An option chain is a table that lists all available call and put options for a given underlying — Nifty, Bank Nifty, or a stock — across all strike prices and expiry dates. Every exchange in India publishes this data in real time. The NSE website, your broker’s platform, and most trading terminals show it in a format that looks like this:

| Strike | Call LTP | Call OI | Call Vol | Put OI | Put Vol | Put LTP |
|--------|----------|---------|----------|--------|---------|---------|
| 24000  | 450      | 15,000  | 2,500    | 120    | 8,000   | 1,200   |
| 24100  | 380      | 22,000  | 3,100    | 180    | 12,000  | 1,800   |
| 24200  | 310      | 18,000  | 2,800    | 250    | 16,000  | 2,400   |

Each row is a strike price. The columns show the last traded price (LTP), open interest (OI), and volume for both calls and puts. The chain is updated every few seconds during market hours.

But raw numbers are noise. The skill is in interpreting what the changes in OI and volume mean.

---

### First Principles: What Open Interest Really Tells You

Open interest is the total number of outstanding option contracts that have not been closed or exercised. It is not the same as volume. Volume is how many contracts changed hands in a given period. OI is the stock of open positions.

Think of OI as the number of tents pitched on a battlefield. Volume is the number of soldiers marching in and out. If OI is rising, new tents are being set up — new money is entering the trade. If OI is falling, tents are being dismantled — positions are being closed.

**Key rule:** Rising OI + rising price = new long positions being built (bullish). Rising OI + falling price = new short positions being built (bearish). Falling OI + price moving either way = existing positions being closed (unwinding).

This is the foundation. Everything else is built on it.

---

### The Anatomy of a Strike: Support, Resistance, and the Pin

Every strike price in the chain acts like a magnet. When a large number of call options are concentrated at a particular strike, that strike often acts as resistance. Why? Because the sellers of those calls — typically large institutions or market makers — will do everything to keep the price below that level so they don’t have to pay out. Similarly, a large concentration of put OI acts as support.

This is not a guarantee. Markets can blow through any level. But when you see a strike with 50,000+ contracts of OI on the call side, and the Nifty is approaching it, expect a fight.

**Example:** In late September 2024, the Nifty was rallying toward 26,000. The 26,000 Call had accumulated over 1.5 crore OI. Every time the index touched 25,950, selling pressure emerged. The index took three attempts over four days to finally break through. Once it did, that same strike flipped to support — because the call sellers had to cover, and new buyers stepped in.

This is the "pin" or "magnet" effect. The option chain shows you where the market is likely to pause, reverse, or accelerate.

---

### The Put-Call Ratio (PCR) — A Simple but Powerful Gauge

The PCR is the total open interest of all puts divided by the total open interest of all calls. It is usually calculated for the near-month expiry.

- PCR below 0.7: Too many calls relative to puts. Market is bullish but crowded. A reversal may be near.
- PCR between 0.8 and 1.2: Neutral zone.
- PCR above 1.3: Too many puts relative to calls. Market is bearish but crowded. A bounce may be near.

But be careful. The PCR works best when it reaches extremes. A PCR of 0.5 or 1.5 is a stronger signal than 0.85 or 1.1. Also, look at the rate of change. If PCR jumps from 0.8 to 1.2 in one day, that is a faster shift than a gradual move over a week.

**Real-world example:** On January 16, 2024, HDFC Bank fell 8.5% in a single day — its worst drop since the COVID crash. The day before, the PCR for HDFC Bank options had fallen to 0.45, an extreme reading. The market was overly bullish on the stock after strong quarterly results. The crash came as a surprise to most, but the option chain had shown that the put side was almost empty — no protection. When the selling started, there was no floor. The chain had warned of vulnerability.

---

### Implied Volatility: The Fear Gauge

Implied volatility (IV) is the market’s expectation of how much the underlying will move over the life of the option. It is not a prediction of direction — only of magnitude.

When IV is high, options are expensive. When IV is low, options are cheap. You can see IV for each strike in the option chain, or as a single number for the entire chain (like the India VIX for Nifty).

**How to use IV:**

- If IV is spiking while the market is falling, fear is rising. Put options become expensive. This is often a sign of panic selling — and sometimes a bottom.
- If IV is falling while the market is rising, complacency is setting in. Call options become cheaper. This can be a sign of a mature rally.

**Anecdote from my own trading:** In March 2020, during the COVID crash, the India VIX hit 86. Options were so expensive that a 5% out-of-the-money put cost more than the stock itself. That was the peak of fear. Within two weeks, the market bottomed. The option chain was screaming "too much fear" — and those who bought calls at that point made a fortune. But you had to read the IV, not the price.

---

### Worked Example: Reading a Real Nifty Option Chain

Let’s take a hypothetical but realistic snapshot of the Nifty option chain on a random Tuesday, with the index trading at 24,500. We’ll look at the near-month expiry (say, 10 days away).

| Strike | Call LTP | Call OI | Call Chg OI | Put LTP | Put OI | Put Chg OI |
|--------|----------|---------|-------------|---------|--------|------------|
| 24400  | 180      | 85,000  | +12,000     | 45      | 62,000 | -5,000     |
| 24500  | 120      | 1,20,000| +25,000     | 70      | 90,000 | +8,000     |
| 24600  | 75       | 1,50,000| +30,000     | 110     | 1,10,000| +15,000    |
| 24700  | 40       | 95,000  | -10,000     | 180     | 1,30,000| +20,000    |
| 24800  | 20       | 60,000  | -8,000      | 280     | 1,00,000| +10,000    |

**What do we see?**

1. **Call side:** The 24,600 Call has the highest OI (1,50,000) and is adding 30,000 contracts. This is a resistance wall. The index at 24,500 is 100 points below. The market is likely to struggle to cross 24,600.

2. **Put side:** The 24,700 Put has the highest OI (1,30,000) and is adding 20,000 contracts. But note: the index is at 24,500, which is 200 points below 24,700. That put is in-the-money. Why are people buying deep ITM puts? They are likely hedging or taking a bearish view. But the real support is at 24,500 — the 24,500 Put OI is 90,000 and adding 8,000. That is the immediate floor.

3. **Change in OI:** The 24,600 Call added 30,000 contracts — aggressive call writing. The 24,700 Put added 20,000 — aggressive put buying. This is a clash. The market is torn between a resistance at 24,600 and support at 24,500. The range is narrowing.

4. **Max Pain:** The strike where the total premium paid by option buyers is lowest (the point where most options expire worthless) is often around the highest combined OI. Here, 24,600 has 1,50,000 calls + 1,10,000 puts = 2,60,000 contracts. That is the highest total OI. Max pain theory suggests the index will try to settle near 24,600 at expiry. But that is a statistical tendency, not a rule.

5. **Volume vs OI:** If you saw that the 24,500 Call had volume of 50,000 but OI change of only +8,000, that means a lot of intraday trading — day traders flipping positions. The OI change is the real signal of conviction.

**Trade interpretation:** The market is range-bound between 24,500 and 24,600. A break above 24,600 with rising OI on calls would be a breakout. A break below 24,500 with rising OI on puts would be a breakdown. Until then, sell options at the edges — sell 24,600 Calls and 24,500 Puts — to collect premium. But that is an advanced strategy. For now, just reading the chain tells you where the battle lines are drawn.

---

### The Skew: How Far-OTM Strikes Reveal Tail Risk

Not all strikes are equal. The far out-of-the-money strikes — say, 25,000 Call or 23,000 Put when Nifty is at 24,500 — often have very low OI and high IV. But when they suddenly see a spike in OI, it means someone is hedging against a black swan.

**Example:** In the weeks before the June 4 crash, the 21,000 Put had negligible OI. On the morning of June 4, as the results started coming in, OI in that strike exploded from 5,000 to 1.2 crore contracts within two hours. That was institutional hedging. The chain was screaming "something is wrong." If you were watching, you could have bought those puts for ₹5 and sold them for ₹150 by afternoon.

The skew — the difference in IV between OTM puts and OTM calls — tells you whether the market is pricing in more downside risk or upside risk. A steep put skew (puts much more expensive than calls) means fear of a crash. A flat skew means complacency.

---

### Common Mistakes When Reading the Chain

1. **Confusing volume with OI.** Volume is noise. OI change is signal. A strike with 1 lakh volume but no OI change is just day trading. Ignore it.

2. **Looking only at the current OI, not the change.** A strike with 2 lakh OI that is unchanged from yesterday is less interesting than a strike with 50,000 OI that added 40,000 today. The change tells you where new money is flowing.

3. **Ignoring the expiry.** OI builds up as expiry approaches. A strike with high OI 30 days out is more significant than the same OI 3 days before expiry, when many positions are being rolled.

4. **Assuming max pain is a target.** Max pain is a statistical tendency, not a guarantee. In strong trending markets, the index can close far from max pain. Use it as one input, not the only one.

5. **Not checking the underlying’s price action.** The option chain is a map, but the price is the terrain. Always confirm chain signals with price action. A resistance level in the chain that is being tested three times with decreasing momentum is more reliable than one being tested once with a strong breakout.

---

### How to Build a Daily Option Chain Routine

I recommend spending five minutes every morning looking at the option chain for the index or stock you trade. Here is a simple checklist:

- Note the top three strikes by OI on the call side and put side.
- Check the change in OI for those strikes — are they building or unwinding?
- Calculate the PCR (total put OI / total call OI) for the near-month expiry.
- Look at the IV for the at-the-money strike — is it high or low relative to the last 10 days?
- Identify any unusual activity in far-OTM strikes.

Do this for a week, and you will start seeing patterns. The chain is not a crystal ball. It is a ledger of where the big money is placing its bets. And in the Indian stock market, where retail participation in options has exploded, the chain often reveals the herd before it stampedes.

---

### Key Takeaways

1. **Open interest change is more important than absolute OI.** Look for strikes where OI is rising sharply — that is where new money is committed.

2. **High OI on calls acts as resistance; high OI on puts acts as support.** These levels are self-reinforcing until broken with conviction.

3. **The Put-Call Ratio (PCR) at extremes (below 0.7 or above 1.3) signals a potential reversal.** Use it as a contrarian indicator, not a directional one.

4. **Implied volatility spikes during fear and drops during complacency.** When IV is very high, options are expensive — consider selling premium. When IV is very low, options are cheap — consider buying.

5. **Far-OTM strikes with sudden OI buildup are red flags.** They indicate hedging against tail risks — often a precursor to a big move.

---

*The option chain is the market’s collective diary. Every day, it records who is betting on what, and at what price. Learn to read it, and you will never trade blind again.*