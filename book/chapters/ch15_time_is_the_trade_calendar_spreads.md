# Chapter 15: Time Is the Trade: Calendar Spreads

## The Strategy Library

---

On June 4, 2024, Nifty fell 8.5% in a single session. The Lok Sabha counting day delivered a result that caught most of the market off guard—the BJP-led NDA looked short of a majority by midday. The index touched a low near 21,281 before recovering to close around 5.9% down. In that single day, option sellers who had been collecting small premiums for weeks saw those gains wiped out in hours. Some lost months of accumulated theta in one violent spike.

But here is what happened next. By late September 2024, Nifty had scaled record highs 32 times. The index recovered roughly 2,300 points from that June low. The traders who understood calendar spreads didn't just survive that day—they had positioned themselves to profit from the volatility that followed.

This chapter is about that positioning. It is about the difference between selling time and trading time.

---

## The Problem with Pure Theta

Every options trader learns early that time decay is the great equalizer. Sell an option, collect premium, watch it erode day by day. It sounds simple. In practice, it is the fastest way to blow up a trading account in Indian markets.

Consider what happened in 2013. The Federal Reserve's taper tantrum caught global markets by surprise. India VIX, which had been sitting at multi-year lows, exploded. Traders who had been selling strangles in that low-volatility environment—collecting what seemed like easy money—saw positions that had been profitable for months turn into losses exceeding ₹1 crore in a single day. The low-VIX regime had lulled them into a false sense of security.

Dhanraj learned this lesson the hard way in his early years. "I remember watching a trader I respected lose everything in one afternoon," he says. "He had been selling options for two years without a losing month. He thought he had cracked the code. What he had actually done was build a position that would survive only if nothing changed. Markets always change."

The fundamental problem with naked option selling is that your risk is asymmetric. You collect small, consistent premiums, but you are exposed to large, infrequent losses. One VIX spike can erase months of theta collection. This is not a flaw in the strategy—it is the strategy. The only way to fix it is to change the structure of the trade.

That is where calendar spreads enter the picture.

---

## What Is a Calendar Spread?

A calendar spread—also called a time spread or horizontal spread—involves buying and selling options of the same strike price but different expiration dates. The most common structure is to sell a near-term option and buy a longer-term option at the same strike.

Why would anyone do this? Because time decays at different rates for different expirations.

Think of it this way. A farmer has two fields of wheat. One field is ready to harvest next month. The other field will be ready in six months. The farmer can sell the wheat from the first field now, but he keeps ownership of the second field. If wheat prices rise, he still benefits from the second field. If wheat prices fall, he has already locked in some profit from the first sale.

The calendar spread works on the same principle. The near-term option decays faster than the long-term option. If the market stays relatively stable, the short option loses value more quickly than the long option, and the spread gains value. If the market moves sharply, the long option provides a hedge.

This is not a directional trade. It is a volatility and time trade. You are betting that the difference in time decay between two expirations will work in your favor.

---

## The Low-VIX Rule

The most important rule in calendar spreads comes from the 2013 taper tantrum lesson: when India VIX is at multi-year lows, always pair your sells with buys.

Low VIX is the most dangerous regime for pure option sellers. When volatility is compressed, premiums are cheap. Traders are tempted to sell more contracts to achieve the same income. This creates a bomb. One volatility spike—triggered by an election result, a central bank announcement, or a global shock—and those cheap premiums explode in value against the seller.

The calendar spread solves this by ensuring that every short option is backed by a long option at the same strike. You are not selling naked volatility. You are selling time while buying protection against volatility expansion.

Dhanraj puts it simply: "In low VIX, you must always mix buys with sells. If you cannot find a calendar that works, do not trade. The market is telling you that the risk is not worth the reward."

---

## The ITM Put Calendar: A Worked Example

Let us walk through a real trade structure that Dhanraj has used multiple times in Indian markets.

The setup: India VIX is at multi-year lows. Nifty is trading around 18,500. You expect the market to remain range-bound for the next few weeks, but you want protection against a sudden drop.

You construct an in-the-money (ITM) put calendar:

- **Sell** the July expiry 18,500 put at ₹350
- **Buy** the December expiry 18,500 put at ₹580

The net debit is ₹230 (₹580 - ₹350). This is your maximum risk per unit.

Now watch what happens over three weeks. The market drifts slightly lower but stays within a 300-point range. The July put, with only days to expiration, decays rapidly. It drops from ₹350 to ₹150. The December put, with months of time remaining, decays much more slowly. It moves from ₹580 to ₹490.

Your position is now:

- Short July put: gained ₹200 (₹350 to ₹150)
- Long December put: lost ₹90 (₹580 to ₹490)
- Net gain: ₹110 per unit

With a lot size of 50 (Nifty options), that is ₹5,500 per lot. Your margin requirement is approximately ₹50,000. In three weeks, you have earned roughly 11% on margin.

But here is the critical part. What if the market had crashed instead? Suppose Nifty dropped 500 points in a single day. The July put would have exploded to ₹800, creating a massive loss on the short leg. But the December put would also have risen—perhaps to ₹1,100. The long leg would have gained ₹520 while the short leg lost ₹450. Your net loss would be limited to the difference, plus the initial debit.

The calendar spread caps your downside. You cannot lose more than the initial debit plus a small amount of slippage. Compare that to a naked put sale, where a 500-point drop could cost you ₹25,000 per lot or more.

---

## The Call Calendar: After a Large Move

Calendar spreads are not just for range-bound markets. They are particularly effective after a very large single-direction move.

Consider what happened after the June 4, 2024 crash. Nifty had fallen 8.5% intraday. The market was in shock. Options premiums were inflated. Traders who had been short volatility were scrambling to cover.

This is the home regime for a call calendar. After a very large move, markets statistically consolidate or drift slightly in the opposite direction. The volatility spike subsides. Time decay accelerates for the near-term options that were priced for continued chaos.

Here is the structure Dhanraj used in a similar situation after a 1,000-point Nifty move:

- **Sell** the weekly 24,900 call at ₹29
- **Buy** the monthly 24,900 call at a price that makes the structure work

The margin requirement is approximately ₹45,000 to ₹50,000. The modeled maximum loss is around ₹10,000. The probability of profit is high because the near-term call, which was inflated by the volatility spike, will decay rapidly if the market stabilizes.

The key insight is that you are selling the market's overreaction. When everyone is panicking, options prices reflect fear. The calendar spread allows you to sell that fear while maintaining a hedge against further moves.

---

## The Bearish Put Ratio Combo: A Multi-Month View

Sometimes you have a mildly bearish view that extends over several months. You do not want to sell naked puts, but you also do not want to pay for expensive long puts. The solution is a ratio structure financed by the deep ITM long leg.

Dhanraj designed a December expiry structure for a slightly bearish view when Nifty was around 19,500:

- **Buy** 1 lot of 21,000 put (deep ITM)
- **Sell** 3 lots of 19,000 put
- **Sell** 2 lots of 21,000 call

The breakevens are approximately 18,000 on the downside and 21,000 on the upside. The probability of profit is around 66%. The maximum profit is approximately 40% of the margin, with an expected return of about 20% (roughly 4% per month).

The margin requirement is ₹1.35 to ₹2 lakh, depending on the broker. The structure works because the deep ITM long put provides intrinsic value that decays slowly, while the short options at different strikes generate premium income.

This is not a trade for beginners. It requires careful monitoring and an understanding of how gamma changes as the market moves. But for experienced traders, it offers a way to express a directional view without the asymmetric risk of naked options.

---

## The Muhurat Session Lesson

On November 3, 2021, the Federal Reserve announced its taper plan. Many traders expected a repeat of the 2013 taper tantrum. They positioned for a crash. They sold puts, bought VIX, and hedged aggressively.

The crash did not come. Markets rallied.

Dhanraj was trading during the Muhurat session that year. He watched as traders who had positioned for disaster saw their hedges decay worthless. The lesson was simple: markets do not crash twice for the same reason. The first time is a surprise. The second time is experience. Central banks learn from their mistakes.

This is why calendar spreads are superior to directional bets. They do not require you to predict whether the market will crash or rally. They only require you to understand the relationship between time and volatility.

---

## The Mechanics of Calendar Spreads

Let us get into the details of how these trades work mechanically.

**Margin Requirements**

Calendar spreads require margin, but significantly less than naked options. For a typical Nifty calendar spread, margin is approximately ₹45,000 to ₹55,000 per lot. Compare that to a naked short option, which might require ₹1.5 lakh or more for the same strike.

The reduced margin comes from the fact that the long option acts as a hedge. The exchange recognizes that your maximum loss is limited to the initial debit plus a small buffer.

**Rolling the Short Leg**

The most important skill in calendar spreads is rolling. As the near-term expiration approaches, you must decide whether to close the short leg, roll it to the next week, or let it expire.

The general rule is to roll when the short leg has lost most of its time value. If you sold a weekly option at ₹29 and it is now trading at ₹5 with two days to expiration, the remaining premium is not worth the risk. Close the short leg and sell the next week's option at the same strike.

This is called "rolling forward." It allows you to collect additional theta while maintaining the same long-term protection.

**Early Assignment Risk**

Calendar spreads carry early assignment risk on the short leg. If the short option goes deep ITM, the buyer may exercise it early. This is particularly relevant for put calendars when the market drops sharply.

The solution is to monitor the position daily and close it if the short option approaches deep ITM territory. Do not wait for assignment. The cost of closing early is small compared to the chaos of an unexpected exercise.

---

## Real Market Application: HDFC Bank, January 2024

On January 17, 2024, HDFC Bank shares plunged 8.5%. It was the stock's worst day since the COVID crash. Investors lost over ₹1 lakh crore in market capitalization in a single session.

For a calendar spread trader, this was not a disaster. It was an opportunity.

Consider a trader who had established a put calendar on HDFC Bank before the crash. They had sold a near-term put and bought a longer-term put at the same strike. When the stock crashed, the near-term put went deep ITM and lost value rapidly. But the longer-term put also gained value, offsetting much of the loss.

The net result was a small loss—perhaps 10-15% of the initial debit. Compare that to a naked put seller, who would have lost 100% of their margin or more.

After the crash, the same trader could establish a new calendar. With volatility elevated, the near-term options were priced for continued chaos. The trader could sell those inflated premiums while buying longer-term protection. Over the following weeks, as HDFC Bank stabilized, the calendar would have generated steady profits.

This is the power of the calendar spread. It does not require you to predict the direction of the market. It only requires you to understand that volatility is mean-reverting and time decay is predictable.

---

## Common Mistakes

**Mistake 1: Trading Calendars in High VIX**

Calendar spreads work best when volatility is low or falling. In high VIX environments, the long option is expensive and the short option decays slowly. The spread may not generate enough theta to justify the risk.

**Mistake 2: Ignoring Dividend and Interest Rate Effects**

In Indian markets, dividends and interest rates affect option prices. A stock that goes ex-dividend during the life of the calendar can distort the pricing. Always check the corporate action calendar before establishing a position.

**Mistake 3: Over-Leveraging**

Because margin requirements are low, traders are tempted to take large positions. A 10% return on ₹50,000 is ₹5,000. A 10% return on ₹5 lakh is ₹50,000. The temptation is to scale up. But a single bad week can wipe out months of gains. Keep position sizes small relative to your capital.

**Mistake 4: Not Rolling on Time**

The short leg must be rolled before it becomes too short-dated. If you wait until the last day, you may be forced to close at unfavorable prices. Set a rolling schedule and stick to it.

---

## The Dhanraj Rule for Calendar Spreads

After years of trading calendars in Indian markets, Dhanraj has distilled the approach into a single rule:

*In low VIX, always pair buys with sells. In high VIX, wait for the spike to subside. After a large move, sell the overreaction. Never sell naked.*

This rule has saved him more times than he can count. It is the difference between being a trader who survives and a trader who blows up.

---

## Key Takeaways

1. **Calendar spreads solve the asymmetric risk problem of naked option selling.** By pairing a short near-term option with a long longer-term option at the same strike, you cap your downside while retaining the benefits of time decay.

2. **Low VIX is the most dangerous regime for pure option sellers.** Always use calendar spreads or other hedged structures when India VIX is at multi-year lows. One volatility spike can erase months of gains.

3. **After a very large single-direction move, call calendars are particularly effective.** The market's overreaction inflates