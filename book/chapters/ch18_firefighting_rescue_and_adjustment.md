# Chapter 18: Firefighting – Rescue and Adjustment

## The Strategy Library

---

The Adani Enterprises call option was bleeding ₹7,03,000. The stock had run from 1800 to 2400, and the short 2200 strike call that seemed so safe just days ago was now deep in the red. Most traders would have taken the loss, closed the position, and moved on. But for Dhanraj, this was not a failure—it was a problem waiting for a solution.

The market does not care about your comfort zone. When a position turns against you, the question is not "why did this happen?" but rather "what can I do about it now?" This is the art of firefighting: the systematic rescue and adjustment of positions that have gone wrong.

---

## The Psychology of a Losing Position

Let me share something honest with you. In my early years, I would sit and watch a losing position like a man watching his house burn from across the street. Paralyzed. Hoping the flames would somehow go out on their own. They never did.

The first lesson of firefighting is this: **do not sit passively on a losing position**. The moment you realize a trade has turned against you, your brain enters a fight-or-flight state. Most people freeze. The successful trader moves—not in panic, but with a plan.

Think of it this way: You are driving a car and suddenly a tire blows out. You do not close your eyes and pray. You grip the steering wheel, ease off the accelerator, and steer the car to safety. Trading adjustments work the same way. You take control of the skid.

---

## The Adani Enterprises Rescue: A Complete Anatomy

Let me walk you through a real rescue operation. This was a short call position in Adani Enterprises—specifically, a short 2200 call option that went horribly wrong when the stock surged from 1800 to 2400.

### The Setup

- **Initial position:** Short 2200 Call (sold for some premium)
- **Stock price move:** 1800 → 2400 (a 33% rise)
- **Initial loss on the call:** ₹7,03,000

Now, most retail traders at this point would accept defeat. But Dhanraj had a system. He did not see a loss—he saw a position that needed restructuring. The goal was not to eliminate the loss entirely, but to reduce it, and perhaps even turn it around.

### The Rescue Ladder: Step by Step

**Step 1: The Put Ladder**

When the stock was running up, instead of covering the call for a loss, Dhanraj started selling put options at lower strikes. The logic? If the stock continues to rise, the puts expire worthless, generating premium to offset the call loss. If the stock reverses, the puts will profit, and the call loss will shrink.

Here is what the put ladder looked like:

- Sold 1 lot of 2000 Put → collected ₹2,39,000
- Sold 1 lot of 1900 Put → collected ₹2,26,000
- Sold 1 lot of 1800 Put → collected ₹3,84,000
- Sold 1 lot of 1700 Put → collected ₹4,80,000

**Total put premium collected: ₹13,29,000**

At this point, the net position has changed. The original call loss of ₹7,03,000 is now offset by ₹13,29,000 in put premium. Net: +₹6,26,000 in your favor.

But wait—selling puts carries its own risk. If the stock reverses sharply below 1700, those puts will explode. So this is not a complete solution. It is a bridge.

**Step 2: The Ratio Spread**

To manage the risk of a sharp reversal, Dhanraj added a call ratio spread. This means buying one call at a higher strike and selling two calls at a lower strike.

The specific legs:
- Bought 2100 Call (paid premium)
- Sold 2 lots of 2400 Call (collected premium on both)

The ratio legs generated:
- First leg: +₹5,00,000
- Second leg: +₹6,00,000

**Total from ratio spread: ₹11,00,000**

Now let us check the full picture:

| Component | P&L |
|-----------|-----|
| Original short call loss | -₹7,03,000 |
| Put ladder premium | +₹13,29,000 |
| Ratio spread premium | +₹11,00,000 |
| **Net position** | **+₹17,26,000** |

A position that started as a ₹7 lakh loss was restructured into a ₹17 lakh potential profit. This is not magic. This is systematic adjustment.

---

## The Principles Behind the Rescue

What happened in the Adani trade is not a trick. It is a framework you can apply to any bad position. Let me break down the principles.

### Principle 1: Divide and Conquer

Notice that Dhanraj did not make one big adjustment. He made a ladder of put sales across multiple strikes. Why? Because a single put sale concentrates risk. A ladder spreads the risk across different price levels. If the stock reverses, only one or two of the puts will get hit, not all of them.

> **Real-world analogy:** When fighting a forest fire, you do not dump all your water in one spot. You create firebreaks—multiple lines of defense at different distances from the main fire.

### Principle 2: The Transfer Tactic

When you have a losing position, the worst thing you can do is stay in the same strike and hope. The better approach is to **transfer the risk to a different instrument** or expiration.

In the Adani rescue, the original short call was a directional bet that went wrong. Dhanraj transferred the risk:
- From a single short call → to a multi-leg structure
- From directional → to range-bound
- From high vega (sensitive to volatility) → to lower vega

The put ladder and ratio spread together created a structure that profits if the stock stays in a range, rather than requiring it to fall.

### Principle 3: Never Pay Out of Pocket

This is perhaps the most important rule in rescue operations. **Every adjustment should either collect premium or be structured as a net credit.**

Look at what happened: every single adjustment step collected money. The put ladder collected ₹13,29,000. The ratio spread collected ₹11,00,000. At no point did Dhanraj pay money to open a new leg.

Why is this critical? Because a rescue is already a stressful situation. If you have to pay money to enter a rescue, you are adding financial pressure to psychological pressure. By collecting premium, you give yourself breathing room.

---

## The Nifty Long-Term Hedge: A Different Kind of Rescue

Not all firefighting is about salvaging a losing trade. Sometimes, it is about protecting a winning position that you want to keep.

In December 2022, Dhanraj was long 10 lots of Nifty futures at 17,200. The market was bullish, but he wanted to protect this position for an entire year without paying expensive put premiums.

### The Funded Protective Put Structure

Here is how he did it:

**The Setup:**
- Long 10 lots Nifty Dec-2022 futures @ 17,200
- Buy 10 lots Dec-2023 17,000 Put @ ₹1,410 (cost: ~₹7,05,000)
- Sell 10 lots far-OTM calls to fund the put

**The funding mechanism:**
By selling out-of-the-money call options that were far from the current price, Dhanraj collected enough premium to pay for the put. The exact calculation:

- Put cost: ~₹7,05,000
- Call premium collected: ~₹7,00,000
- **Net cost of protection: ₹5,000** (effectively zero)

### How It Works

This structure is called a "funded protective put" or "collar spread." The key insight is that options pricing allows you to trade time and volatility.

- The far-dated put (December 2023) is expensive because it has 12 months of time value.
- The short calls are OTM and also have time value, but less because they are further from the money.
- The net credit/zero cost structure means you have unlimited upside (through the futures) with a defined downside (through the put).

**The outcome:**
- Futures MTM gain: +₹8,00,000 (as Nifty moved higher)
- Put MTM loss: -₹5,00,000 (time decay and lower volatility)
- Short calls MTM: +₹22,000 (they expired worthless)
- **Net profit: ~₹5,00,000+**

The position was protected for a full year at virtually no cost. The put acted as an insurance policy, while the futures captured the market rise.

---

## The Deep ITM Straddle: An Advanced Rescue

There is an even more sophisticated rescue technique that Dhanraj used when he wanted protection but also wanted to collect premium upfront.

### The Setup

**The trade:**
- Sell a deep in-the-money (ITM) September 17,000 straddle (combined premium ~₹689)
- Buy a December 17,000 put (premium ~₹678)
- **Net credit at entry: ~₹11**

Why would anyone do this? Because it creates a **free hedge**.

### The Logic

A deep ITM straddle means selling both a call and a put at the same strike, where the strike is significantly above or below the current price. In this case, 17,000 was deep ITM relative to the current market price (around 15,000 at the time).

- The put leg is ITM (intrinsic value)
- The call leg is OTM (only time value)
- Combined premium is high because the put has substantial intrinsic value

By selling this straddle and immediately buying a far-dated put, you create a structure where:
- You collect more premium than you pay for protection
- You benefit from time decay (theta)
- You have defined risk

### The Margin Consideration

This structure requires higher margin because the deep ITM straddle is capital-intensive. But for traders with sufficient capital, it offers a near-zero-cost way to enter a hedged position.

**Key takeaway:** Enter hedged structures only on net credit. Never pay out of pocket to open a protection trade. If the math does not work for a credit, the trade is not worth doing.

---

## The June 4, 2024 Crash: A Firefighting Case Study

On June 4, 2024, Lok Sabha election counting day, Nifty fell approximately 8.5% intraday to a low near 21,281. The BJP-led NDA looked short of a majority, and panic selling ensued. The index closed around 5.9% down.

What happened that night? TDP's Chandrababu Naidu and JDU's Nitish Kumar pledged support to form the NDA government. The next day, markets recovered partially, and over the following months, Nifty set record highs 32 times in 2024, reaching approximately 26,000 by late September.

For traders who were positioned for a rally, this day was a firefighting test.

### The Rescue Opportunity

Those who had bought Nifty futures at higher levels faced severe MTM losses. But here is what the disciplined firefighter did:

**Step 1: Do not panic-close the futures.**
Selling futures at the bottom locks in the loss. Instead, buy put options to hedge further downside.

**Step 2: Sell call options at higher strikes.**
If you are long futures and the market crashes, selling OTM calls collects premium to offset the loss. This creates a covered call structure.

**Step 3: Wait for recovery.**
The Nifty eventually recovered 2,300 points from the June 4 low. Those who held their futures and added protective structures came out ahead.

### The Counter-Example: HDFC Bank

On January 17, 2024, HDFC Bank shares plunged 8.5%—their worst day since the COVID crash. Investors lost over ₹1 lakh crore in market capitalization.

For a value investor, this might seem like a buying opportunity. But Dhanraj's approach is different: **do not catch a falling knife with your face**.

The correct firefighting approach for HDFC Bank holders:
- If you were long HDFC Bank before the crash: do not sell in panic. Wait for the price to stabilize. The stock may need days or weeks to find support.
- If you were not holding: do not buy immediately. Let the dust settle. A 8.5% crash often leads to further weakness as stop-losses trigger and margin calls force selling.

---

## The Portfolio View: Firefighting Across 10-15 Strategies

Dhanraj does not rely on any single trade. His capital is divided into 10-15 parallel strategies running simultaneously. This structure itself is a firefighting technique.

**Why this matters:**

- One bad trade is a small fire, not a house fire.
- When a rescue operation is needed, you have the capital and mental bandwidth to execute it.
- You do not become emotionally attached to any single position.

Think of it like a hospital emergency room. You do not have one doctor handling every patient. You have a team. Each trade is a patient. Some need minor care (adjustments), some need major surgery (full rescue), and some are beyond saving (close and move on).

---

## When to Abandon Ship

Not every position can be rescued. Here are the signs that a trade is beyond saving:

**1. The thesis is broken.**
If the fundamental reason you entered the trade no longer exists—a company's earnings collapse, a government policy changes the sector dynamics—do not try to adjust. Close the trade.

**2. The position is too large.**
If you are at 50% or more of your trading capital in a single position, rescue operations become dangerous. You are fighting with borrowed confidence. Reduce size first, then adjust.

**3. The adjustment would require paying money.**
Remember the rule: every adjustment should collect premium. If the only way to "save" the trade is to pay more money, you are doubling down on a losing bet. Close it.

**4. Emotional exhaustion.**
If you cannot sleep, cannot focus, or feel physical anxiety when you look at the position, you have lost objectivity. Close the trade. Your sanity is worth more than any potential recovery.

---

## The Mechanics of a Good Rescue

Let me give you a step-by-step checklist for executing a rescue operation.

### Step 1: Assess the Damage

Calculate the exact P&L of the position. Not in percentage terms—in rupees. How much have you lost? How much margin is blocked?

### Step 2: Identify the Risk

What is the market doing that is hurting you?
- Directional risk? (Stock moving against you)
- Volatility risk? (IV expanding and crushing your short options)
- Time risk? (Not enough time for the trade to work)

### Step 3: Choose Your Weapon

Based on the risk type:
- **Directional risk:** Add opposing options (call or put) to create a spread.
- **Volatility risk:** Use calendar spreads (sell near-term, buy longer-dated options).
- **Time risk:** Roll the position to a later expiration.

### Step 4: Execute in Stages

Do not try to rescue with one massive adjustment. The market is dynamic. Enter in stages:
- First, neutralize the directional risk.
- Then, collect premium to offset losses.
- Finally, wait for price to stabilize.

### Step 5: Set a Stop-Loss on the Rescue

Yes, even your rescue needs a plan for failure. Decide beforehand: if the adjusted position loses another X%, you will close everything. This prevents the rescue from becoming a deeper hole.

---

## A Worked Example: Rescuing a Short Nifty Call

Let me walk you through a hypothetical but realistic scenario.

**The Starting Position:**
- Sold 1 lot Nifty 25,000 Call
- Nifty spot: 24,500
- Premium collected: ₹50 per share (50 x 75 = ₹3,750)
- Expiry: 30 days away

**The Problem:**
Nifty rallies to 25,200 in 10 days.
- The 25,000 call is now ITM
- Loss: approximately (25,200 - 25,000) x 75 = ₹15,000
- Plus, the initial premium collected is now lost

**Total loss: ₹15,000 - ₹3,750 = ₹11,250**

### Rescue Plan

**Step 1: Buy a higher strike call (cap the upside)**
Buy 1 lot Nifty 25,500 Call
Premium paid: ₹30 per share (30 x 75 = ₹2,250)
This caps your loss at (25,500 - 25,000) = 500 points = ₹37,500 maximum loss on the call spread.

**Step 2: Sell a put (collect premium)**
Sell 1 lot Nifty 24,000 Put
Premium collected: ₹45 per share (45 x 75 = ₹3,375)

**The net position:**
- Short 25,000 Call (loss: -₹15,000)
- Long 25,500 Call (cost: -₹2,250)
- Short 24,000 Put (collected: +₹3,375)
- Net premium collected so far: ₹3,750 (original) + ₹3,375 - ₹2,250 = ₹4,875

**The new risk profile:**
- Maximum loss: (25,500 - 25,000) x 75 = ₹37,500 minus net premium collected ₹4,875 = ₹32,625 loss at expiry if Nifty > 25,500
- Maximum profit: Net premium collected if Nifty < 24,000 = ₹4,875
- Breakeven: Between 24,000 and 25,000

The position is now a **short call spread with a put credit**. It has defined risk and defined reward. You can sleep at night.

---

## The Final Word on Firefighting

The ability to rescue a position is what separates seasoned traders from gamblers. A gambler prays for the market to move in their favor. A trader builds structures that work across multiple scenarios.

Remember the story of the Adani rescue. A ₹7 lakh loss turned into a profitable structure—not because the market cooperated, but because the trader had a system for adjustment.

When you face a losing position, do not panic. Do not freeze. Do not hope. Instead, ask yourself:

- Can I transfer risk to a different strike or expiration?
- Can I collect premium to offset the loss?
- Can I divide the risk across multiple legs?

If the answer to any of these is yes, you have a rescue path. If all answers are no, close the trade and preserve your capital for the next opportunity.

Firefighting is not about never getting burned. It is about knowing how to put out the fire before it destroys the house.

---

## Key Takeaways

1. **Never