# Chapter 8: The Option Contract – A Promise, Not an Obligation

## A Morning That Changed Everything

June 4, 2024. The counting of Lok Sabha votes was underway, and India’s stock markets were bracing for results. At 7:30 AM, GIFT Nifty futures indicated a gap-down of nearly 300 points. By 9:15 AM, when the cash market opened, Nifty was already down 2%. Then came the numbers: the BJP-led NDA looked short of a majority. Panic set in. Within minutes, Nifty crashed 8.5% from the previous close, touching a low of 21,281. The VIX—the fear index—shot up to 30. Options premiums exploded. A Nifty 22,000 Call that had traded at ₹35 the day before was suddenly worth ₹2. But a Nifty 22,000 Put? It had been a sleepy ₹15. By 10:30 AM, that same Put was trading at ₹600.

If you had bought that Put the night before, you would have made 40 times your money in a few hours. If you had sold it, you would have lost 40 times your margin. Same underlying. Same expiry. Same strike price. The difference was only this: one person held a *right*, the other a *promise*.

That is what this chapter is about.

---

## What Is an Option?

Let me start with a simple definition. An **option** is a contract that gives the buyer the right—but not the obligation—to buy or sell an underlying asset at a predetermined price on or before a specific date. The seller of the option, in contrast, has the *obligation* to fulfil that transaction if the buyer chooses to exercise the right.

Think of it like a deposit for a piece of land. You pay a small amount—say ₹1 lakh—to the seller to “lock” the price of a plot at ₹50 lakh for the next six months. If the plot’s market price rises to ₹60 lakh, you exercise your right: you buy it at ₹50 lakh and make ₹10 lakh profit (minus the deposit). If the price falls to ₹40 lakh, you walk away. You lose only the ₹1 lakh deposit. The seller, who collected your deposit, is now obligated to sell you the land at ₹50 lakh if you choose to exercise, even if the market price has gone up.

That deposit is the **premium**. That right is the option.

In Indian stock markets, the underlying can be a stock (like Reliance Industries), an index (Nifty or Bank Nifty), or an ETF. Nifty options are cash-settled—meaning no actual shares change hands, only the difference in cash. The lot size for Nifty options is 50 units (post-2019 consolidation), so one Nifty option contract represents 50 times the index value.

---

## Right vs. Obligation: The Core Asymmetry

The entire universe of derivatives can be divided into two categories: symmetric and asymmetric.

**Futures** are symmetric. When you buy a Nifty futures contract at 25,000, both you and the seller have obligations. You must buy at 25,000 on expiry; the seller must sell at 25,000. If Nifty goes to 26,000, you profit and the seller loses. If Nifty goes to 24,000, you lose and the seller profits. Both parties are equally exposed, and the profit/loss is linear.

**Options** are asymmetric. The buyer has the *right* to walk away. The seller has the *obligation* to perform. The buyer’s maximum loss is limited to the premium paid. The seller’s maximum loss is theoretically unlimited. This asymmetry is not a bug—it is the entire point.

Here is a table that makes the distinction clear:

| Feature | Futures Contract | Options Contract |
|---------|----------------|-----------------|
| **Position of buyer** | Obligation to buy | Right to buy (call) or sell (put) |
| **Position of seller** | Obligation to sell | Obligation to fulfil if exercised |
| **Upfront payment** | Margin (blocked funds) | Premium (non-refundable) |
| **Maximum loss for buyer** | Full contract value (minus margin) | Premium paid |
| **Maximum loss for seller** | Full contract value (minus margin) | Theoretically unlimited |
| **Profit potential for buyer** | Linear, unlimited | Theoretically unlimited |
| **Profit potential for seller** | Linear, unlimited | Limited to premium received |

Notice the asymmetry in risk. A futures buyer and seller are mirror images. An options buyer and seller are different animals altogether.

---

## The Two Flavors: Calls and Puts

An option comes in two forms:

- **Call option**: gives the buyer the right to **buy** the underlying at a fixed price.
- **Put option**: gives the buyer the right to **sell** the underlying at a fixed price.

The fixed price is called the **strike price** or **exercise price**. The date after which the option ceases to exist is the **expiry date**. In India, Nifty and Bank Nifty options expire every Thursday (or the previous trading day if Thursday is a holiday). Weekly expiries for individual stocks are also common.

Let’s take a concrete example using the Nifty 18,000 Call option. I will use this because it was a widely traded strike during the 2023–24 period.

**Example:**  
On January 2, 2024, Nifty is trading at 21,700. A trader buys one lot (50 units) of the Nifty 18,000 Call option expiring on January 25, paying a premium of ₹150 per unit. Total cost = 50 × ₹150 = ₹7,500.

What does this contract give the buyer?  
- The right to buy 50 units of Nifty at ₹18,000 on expiry (or before, if American-style—but Nifty options are European-style, exercisable only on expiry).  
- In practice, since Nifty is cash-settled, the payoff is calculated as: (Nifty settlement price – strike price) × lot size, if positive. Otherwise zero.

Now, why would anyone pay ₹7,500 for the right to buy Nifty at 18,000 when Nifty is already at 21,700? Because the buyer believes Nifty will go *even higher*. If Nifty rises to 23,000 by expiry, the option’s intrinsic value is 23,000 – 18,000 = ₹5,000. Multiply by lot size: ₹5,000 × 50 = ₹2,50,000. Subtract the premium paid of ₹7,500, net profit = ₹2,42,500. That is a 32x return.

But if Nifty stays at 21,700 or falls, the option expires worthless. The buyer loses the entire ₹7,500.

---

## Payoff Diagram: Seeing Asymmetry

A payoff diagram plots the profit or loss of a position at expiry against the price of the underlying. For the Nifty 18,000 Call bought at ₹150, the diagram looks like this:

- **Below 18,000**: The option expires worthless. Loss = ₹150 per unit (premium).  
- **Between 18,000 and 18,150**: The option has some intrinsic value, but not enough to cover the premium. Loss reduces gradually.  
- **At 18,150**: Breakeven. Intrinsic value = ₹150 exactly offsets the premium.  
- **Above 18,150**: Profit. Every 1-point rise in Nifty adds ₹1 per unit (₹50 per lot) to profit, theoretically unlimited.

The shape is an “elbow”: flat on the left (limited loss), sloping upward on the right (unlimited gain). That is the signature of a long call option.

Now contrast with a futures position. A long futures contract at 21,700 has a straight diagonal line: if Nifty goes to 22,700, profit = ₹1,000 per unit. If Nifty goes to 20,700, loss = ₹1,000 per unit. No plateau. No limited loss.

This asymmetry is why options exist: they allow you to define your risk precisely. You cannot lose more than the premium. In exchange, the premium decays to zero if the market does not move in your direction before expiry.

---

## The Seller’s Side: Writing Options

If the buyer pays a premium to acquire a right, the seller (also called the *writer*) receives that premium and takes on the obligation. In our Nifty 18,000 Call example, the seller collects ₹7,500. In return, he must deliver the payoff if Nifty closes above 18,000.

At expiry, if Nifty closes at 19,000, the seller must pay the buyer (19,000 – 18,000) × 50 = ₹50,000. Since the seller already received ₹7,500 premium, the net loss is ₹42,500. If Nifty closes at 25,000, the loss balloons to (25,000 – 18,000) × 50 – 7,500 = ₹3,42,500.

The seller’s maximum profit is the premium collected. The maximum loss is unbounded. That is why exchanges and brokers impose strict margin requirements on option sellers. On June 4, 2024, many sellers of Nifty 24,000 Calls who had collected a few hundred rupees per lot saw their margins evaporate as Nifty crashed and volatility spiked. Some were forced to square up at massive losses.

Selling options is like picking up pennies in front of a steamroller—most days you collect small profits, but one wrong move can flatten you.

---

## Why Options Exist: The Insurance Function

Why do these contracts exist at all? The textbook answer is price discovery and hedging. The real answer is that options are the purest form of risk transfer.

Consider a mutual fund manager holding ₹50 crore worth of Nifty stocks in June 2024. She is worried about the election results. She can sell futures to hedge, but that would cap her upside if the market rallies. Instead, she buys Nifty 21,000 Puts at a cost of ₹80 per unit (₹4,000 per lot). If Nifty tanks to 20,000, the puts pay her (21,000 – 20,000) × 50 = ₹50,000 per lot. She can buy enough lots to cover her portfolio. If Nifty rallies, she loses only the premium—her portfolio gains more than offsets it.

The option allows her to buy insurance *without* losing upside. That is the killer application.

On the other side, a speculator who believes volatility will remain low may sell those puts, collecting premium income day after day—until a black swan arrives.

Options exist because different market participants have different risk appetites, time horizons, and views. The option contract bridges them.

---

## A Note on Cash Settlement

Nifty and Bank Nifty options are cash-settled. This means on expiry day, no shares are delivered. Instead, the clearing corporation calculates the settlement price (the average of the last half-hour of trading) and credits or debits the difference to your trading account.

If you hold a Nifty 18,000 Call and Nifty settles at 18,500, you receive (18,500 – 18,000) × 50 = ₹25,000 in cash. That’s it. There is no actual purchase of Nifty shares—because Nifty is an index, not a stock you can buy directly.

Cash settlement simplifies the process, eliminates delivery risk, and makes options accessible to retail traders who do not want to deal with physical shares.

---

## Key Takeaways

1. **An option is a right, not an obligation.** The buyer chooses to exercise; the seller must comply. This asymmetry is the defining feature of options versus futures.

2. **Premium is the price of the right.** It is non-refundable and determines the buyer’s maximum loss. Options allow you to define your maximum downside *before* entering the trade.

3. **Calls give the right to buy; puts give the right to sell.** Use calls when you expect the underlying to rise, puts when you expect it to fall. Both are tools for directional bets or hedging.

4. **Option sellers have unlimited risk.** Selling options generates income but requires robust risk management and sufficient capital. One adverse move can wipe out months of premium collected.

5. **Nifty options are cash-settled with a lot size of 50.** No delivery of shares—only cash differences. Expiry is weekly (Thursdays) for indices, with monthly expiries for many stocks.

---

In the next chapter, we will dissect the premium itself—what it is made of, why some options are cheap and others expensive, and how time eats away at option prices like rust on an iron beam. That is where the real art of options begins.