# Chapter 16: Butterflies & Condors

## The Strategy Library

---

The October morning of 2021 felt different. Reliance Industries had been grinding higher for weeks, touching new all-time highs with a quiet persistence that made traders nervous. I was sitting in my office, watching the pre-open screen flicker, when a young trader I'd been mentoring called me.

"Dhanraj sir, Reliance results are tomorrow. Should I buy a straddle?"

I could hear the excitement in his voice. He'd read about earnings plays, about volatility crush, about making quick money when a stock moves big after results. Every YouTube channel, every Telegram group was buzzing with the same advice: "Buy options before results, make a killing."

I asked him one question: "What's the implied volatility right now?"

Silence.

"Sir, I don't know. But everyone says it's a sure-shot trade."

I invited him to my office. We pulled up the options chain for Reliance October 2021 expiry. The at-the-money straddle was priced at roughly ₹1,200. The stock was trading around ₹2,700. That meant the market was expecting a move of about ₹1,200 in either direction by expiry—roughly 44%. For a single day's earnings event.

"Does that seem reasonable to you?" I asked.

He looked at the numbers. "That's... a lot."

"It is. And that's exactly why buying options before events is a losing game over time. The market prices in the expected move. You're paying for volatility that rarely materializes."

That conversation led us to a different kind of trade—one that doesn't bet on direction, doesn't bet on volatility, but instead exploits the structure of options pricing itself. A trade with a strange name that sounds more like something you'd see in a zoo than in a trading terminal: the butterfly.

---

## The Anatomy of a Butterfly

Let me start with a confession: when I first heard the term "butterfly spread," I thought it was some Wall Street insider jargon designed to confuse retail traders. The truth is simpler. The name comes from the shape of the profit-loss diagram—it looks like a butterfly with its wings spread.

But before we get to the visual, let's understand what a butterfly actually is.

A butterfly spread combines four option contracts—either all calls or all puts—at three different strike prices. The structure is always the same: buy one contract at a lower strike, sell two contracts at a middle strike, and buy one contract at a higher strike. The strikes are equally spaced.

For a call butterfly on a stock trading at ₹2,700, you might use strikes of ₹2,600, ₹2,800, and ₹3,000. You buy one ₹2,600 call, sell two ₹2,800 calls, and buy one ₹3,000 call. All with the same expiry.

The key insight is this: the two short options at the middle strike generate premium that offsets the cost of the two long options at the wings. If structured correctly, the maximum loss is limited to the net premium paid, and the maximum profit occurs if the stock closes exactly at the middle strike at expiry.

Let me show you with real numbers from that Reliance trade.

---

## The Reliance Butterfly: A Worked Example

On October 21, 2021, Reliance Industries was trading at approximately ₹2,700, having touched all-time highs in the preceding days. The October 28 weekly expiry was approaching, and Q2 results were due on October 22.

I proposed a 1-5-4 call butterfly—a variation where the ratio of buys to sells isn't 1-2-1 but 1-5-4. This is called a "ratio butterfly" or "broken wing butterfly." The principle remains the same: you're betting the stock stays near a specific range, but the ratio adjusts the risk-reward profile.

Here's the actual trade structure:

**Entry (October 22, 2021):**
- Buy 1 lot of ₹2,600 Call at ₹155
- Sell 5 lots of ₹2,800 Call at ₹65 each
- Buy 4 lots of ₹3,000 Call at ₹25 each

Let's calculate the net premium:

Cost of long calls: (1 × ₹155) + (4 × ₹25) = ₹155 + ₹100 = ₹255
Premium received from short calls: 5 × ₹65 = ₹325
Net credit: ₹325 - ₹255 = ₹70 per unit

Wait—this trade actually gave us a net credit. We received ₹70 per unit to enter the trade. That means even if the stock did nothing, we'd keep that ₹70. But there's a catch.

**Maximum loss calculation:**
The maximum loss occurs if the stock moves beyond the wings. Let's say Reliance crashes to ₹2,500. All options expire worthless. We keep the ₹70 credit. That's a profit, not a loss.

What if Reliance rallies to ₹3,200? The ₹2,600 call is worth ₹600, the ₹2,800 calls are worth ₹400 each (we're short 5, so that's -₹2,000), and the ₹3,000 calls are worth ₹200 each (we're long 4, so +₹800). Net: ₹600 - ₹2,000 + ₹800 = -₹600. Plus we received ₹70 credit. Net loss: ₹530 per unit.

But here's the thing—the maximum loss is capped. It cannot exceed a certain amount because the long options at the wings protect us from unlimited downside (or upside, depending on the structure).

**Maximum profit calculation:**
The maximum profit occurs if the stock closes exactly at ₹2,800 at expiry. At ₹2,800:
- ₹2,600 call is worth ₹200
- ₹2,800 calls expire worthless (we keep the premium)
- ₹3,000 calls expire worthless
- Net: ₹200 + ₹325 (premium received) - ₹155 (cost of ₹2,600 call) - ₹100 (cost of ₹3,000 calls) = ₹270 per unit

The actual trade was scaled up significantly. The trader who executed this—a friend I'd been coaching—started with 500 units (1 lot = 250 shares in Reliance options at that time). That's a position size of:
- 500 ₹2,600 calls
- 2,500 ₹2,800 calls (short)
- 2,000 ₹3,000 calls

Maximum loss on this scale: approximately ₹1,51,000 (₹530 × 285 units, adjusted for lot size)
Maximum profit: approximately ₹76,950 (₹270 × 285 units)

The trade was later scaled to 20x: 5,000 / 25,000 / 20,000 quantities. The margin required was substantial—around ₹5-6 lakhs—but the risk was strictly defined.

**What happened?**
Reliance opened flat after results, traded in a narrow range around ₹2,750-2,800 for the next few days, and the butterfly decayed in value. The trader closed the position for a profit of approximately ₹1.2 lakhs on the scaled-up version—a return of about 20% on margin in one week.

Not a home run. But a clean, controlled trade that didn't require predicting direction or hoping for a massive move.

---

## Why Butterflies Work in Indian Markets

Indian markets have a peculiar characteristic that makes butterflies particularly effective: option premiums are often inflated relative to realized volatility. This is especially true around events like earnings, budget announcements, and RBI policy meetings.

Consider this: across 10 years of budget day data, the average close-to-close move in Nifty has been under 2%. The only exception was the COVID budget of 2020, which saw a -3.26% move—and that wasn't even budget-related. Yet every year, traders rush to buy straddles before the budget, paying premiums that imply a 3-4% move.

The structural edge is clear: implied volatility is almost always higher than historical volatility. By selling options (which butterflies do, through the short middle strikes), you capture this premium over time.

But there's a smarter way to play this than simply selling naked options. The butterfly structure limits your risk. You know exactly how much you can lose before you enter the trade. That's invaluable for position sizing and mental peace.

---

## The Condor: A Wider Net

If the butterfly is a precise bet on a specific price, the condor is a bet on a range. Think of it this way: a butterfly says "the stock will be exactly here." A condor says "the stock will be somewhere in this zone."

A condor uses four strikes, but instead of selling two at the same middle strike, you sell one at a lower middle strike and one at a higher middle strike. You then buy one at an even lower strike and one at an even higher strike.

For example, on Nifty at 18,000:
- Buy 1 17,600 Put
- Sell 1 17,800 Put
- Sell 1 18,200 Put
- Buy 1 18,400 Put

This creates a profit zone between 17,800 and 18,200. The maximum profit is earned if Nifty stays anywhere in that 400-point range. The maximum loss is limited to the net premium paid.

The condor sacrifices maximum profit potential (compared to a butterfly) in exchange for a wider profit zone. It's like fishing with a wider net—you catch more fish, but each fish is smaller.

---

## Real Market Application: The August 2023 Paper Trades

In August 2023, I ran a series of paper trades to test various non-directional strategies. The results were instructive.

**Trade 1: Bearish October Combo**
A bear put spread on Nifty for October expiry. Entry on August 1, exit after two weeks. Profit: +5% on margin of ₹1.2 lakhs. Nothing spectacular, but the trade worked because the market was range-bound.

**Trade 2: August Combo**
A short strangle on Bank Nifty for August expiry. Entry on August 2, held for three weeks. Profit: +13-14% on margin of ₹1.27 lakhs. The key was that Bank Nifty stayed within a predictable range during that period.

**Trade 3: December Double Ratio**
A put ratio spread on Nifty for December expiry. Margin approximately ₹1.5 lakhs. Profit: +13% in about one month. This was the best return of the month, achieved by selling more puts than buying, creating a net credit.

**Trade 4: Results-Day Vol-Crush Strangle on SBI**
State Bank of India was reporting quarterly results. Instead of buying a straddle like everyone else, I sold a strangle—betting that the move would be smaller than what the options market was pricing. Margin approximately ₹4.5 lakhs. Profit: approximately ₹59,000 in two days. That's a 13% return on margin in 48 hours.

The common thread? None of these trades required predicting direction. They all exploited the gap between implied volatility (what options cost) and realized volatility (what actually happened).

---

## The Trap of Event Trading

Let me be blunt: buying options before events is structurally losing. I've seen it destroy more retail accounts than almost any other strategy.

Here's why. When you buy a straddle before earnings or budget, you're paying for the "expected move." The market makers have already calculated the probability distribution and priced it in. For you to profit, the actual move must be larger than what the market expects. That's a negative expectancy game.

Think of it like betting on a coin flip where you need the coin to land on its edge to win. It happens sometimes—and those stories get shared on social media—but the math is against you.

The alternative is to sell premium before events. But selling naked options carries unlimited risk. A gap move against your position can wipe out months of profits.

This is where butterflies and condors shine. They allow you to sell premium (through the short strikes) while capping your risk (through the long strikes). You're still betting that the move will be smaller than implied, but your downside is strictly defined.

---

## Building Your Own Butterfly

Let me walk you through the process of constructing a butterfly for a real trade.

**Step 1: Identify the underlying and timeframe**
Choose a stock or index with liquid options. Nifty, Bank Nifty, Reliance, and HDFC Bank are good starting points. Decide on your timeframe—weekly, monthly, or quarterly expiry.

**Step 2: Determine the expected range**
Use technical analysis, support/resistance levels, or implied volatility to estimate where the stock might trade. For a butterfly, you want a narrow range. For a condor, a wider range.

**Step 3: Select strikes**
For a standard call butterfly, choose three strikes equally spaced. The middle strike should be where you expect the stock to be at expiry. The wings should be far enough that the probability of the stock reaching them is low.

**Step 4: Calculate the net premium**
Add the cost of your long options, subtract the premium from your short options. If the result is a debit (you pay to enter), that's your maximum loss. If it's a credit (you receive premium), that's your maximum profit if the stock stays within range.

**Step 5: Check the Greeks**
Delta should be near zero (direction-neutral). Theta should be positive (you benefit from time decay). Vega should be negative (you benefit from falling volatility).

**Step 6: Size the position**
Never risk more than 2-3% of your capital on any single butterfly. The maximum loss is known upfront—use it to calculate position size.

---

## The Psychology of Non-Directional Trading

The hardest part of trading butterflies isn't the math—it's the mindset.

Most traders are addicted to direction. They want to be "right" about where the market is going. Butterflies require you to give up that need. You're not predicting; you're positioning. You're saying, "I don't know where the market will go, but I know where it won't go."

This is deeply uncomfortable for many traders. I've seen brilliant analysts struggle with butterflies because they couldn't stop themselves from having a directional view. They'd construct a perfect butterfly, then watch the market move toward one wing and panic, closing the trade for a loss—only to see it revert to the center the next day.

The antidote is to trust the structure. If you've built the butterfly correctly, you know your maximum loss. You know the probabilities. You've done the work. Now let the trade work itself out.

---

## When Butterflies Fail

No strategy is perfect. Butterflies have their weaknesses.

**Early assignment risk:** If the short options go deep in-the-money, you might get assigned early. This is rare in Indian markets but can happen. Always monitor your positions.

**Low probability of max profit:** The butterfly's maximum profit occurs only if the stock closes exactly at the middle strike. The probability of this is low. Most profitable butterflies are closed early for a partial profit.

**Commission costs:** With four legs, commissions can eat into profits. Use brokers with low per-lot charges.

**Liquidity issues:** Not all strikes have sufficient open interest. Stick to the most liquid strikes near the current price.

---

## Key Takeaways

1. **Butterflies and condors are non-directional strategies** that profit from time decay and volatility contraction, not from predicting market direction.

2. **The maximum loss is known upfront**, making position sizing straightforward and risk management automatic.

3. **Implied volatility is almost always higher than realized volatility** in Indian markets, especially around events—this creates a structural edge for premium-selling strategies like butterflies.

4. **Start with liquid underlyings** like Nifty, Bank Nifty, or large-cap stocks with active options chains. Avoid illiquid strikes.

5. **Close trades early** when you've captured 50-70% of the maximum profit. Waiting for the maximum profit at expiry increases the risk of the trade turning against you.

---

The young trader who called me that October morning? He's now one of the most consistent non-directional traders I know. He doesn't chase earnings moves. He doesn't buy straddles before budgets. He builds butterflies and condors, collects premium, and sleeps well at night.

Sometimes the best trades are the ones that don't require you to be right about anything except the math.