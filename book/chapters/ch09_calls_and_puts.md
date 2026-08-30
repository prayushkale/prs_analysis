# Chapter 9: Option Premium – The Price of Possibility

## The Day the Market Lost Its Mind

I remember June 4, 2024, as if it were yesterday. The Lok Sabha election results were coming in, and the Nifty was in freefall. By mid-afternoon, the index had plunged nearly 8.5% from the previous close, touching a low near 21,281. Traders were scrambling. Phones were ringing off the hook. And in the options market, something extraordinary happened.

The Nifty 21,500 Put – a strike that had been comfortably out-of-the-money just a day earlier – was now trading at over ₹800. Let that sink in. A put option that gave you the right to sell Nifty at 21,500 was worth more than ₹800 per share when the index itself was at 21,281. Why? Because the option was now deep in-the-money. Its intrinsic value alone was ₹219 (21,500 – 21,281). But the premium was ₹800+. That extra ₹581 was pure fear – time value inflated by panic.

That day taught me more about option premiums than any textbook ever could. The premium is not just a number. It is a living, breathing thing – a price that reflects hope, fear, time, and mathematics all at once.

## The Iceberg Model

Every option premium has two components: **intrinsic value** and **time value**. Think of an iceberg floating in the ocean. The part above the water is the intrinsic value – visible, measurable, real. The massive chunk below the surface is the time value – invisible but powerful, and it melts away as you approach expiry.

**Intrinsic value** is the amount by which an option is in-the-money. For a call option, it is the difference between the spot price and the strike price, but never less than zero. For a put option, it is the difference between the strike price and the spot price, again floored at zero.

**Time value** is everything else. It is the premium you pay for the possibility that the option could become more valuable before expiry. It includes the cost of volatility, the time remaining, and the seller’s compensation for taking risk.

Let me give you a simple example. Suppose Nifty is trading at 18,200. You look at the 18,000 Call option. Its intrinsic value is ₹200 (18,200 – 18,000). But the option might be trading at ₹250. That extra ₹50 is time value. You are paying ₹50 for the chance that Nifty could go even higher before expiry.

Now look at the 18,500 Call. Nifty is at 18,200, so this option has zero intrinsic value – it is out-of-the-money. Yet it might trade at ₹30. That entire ₹30 is time value. You are paying for the possibility that Nifty will rise above 18,500 before the option expires.

## Moneyness: The Three States of an Option

Options are classified by their relationship to the current price. This is called **moneyness**. There are three states:

**In-the-money (ITM):** The option has intrinsic value. For a call, spot > strike. For a put, spot < strike. Example: Nifty at 18,200, 18,000 Call is ITM by ₹200.

**At-the-money (ATM):** The strike is closest to the current spot price. Usually, the two nearest strikes are considered ATM. Example: Nifty at 18,200, the 18,200 Call and 18,200 Put are ATM.

**Out-of-the-money (OTM):** The option has no intrinsic value. For a call, spot < strike. For a put, spot > strike. Example: Nifty at 18,200, the 18,500 Call is OTM.

Why does this matter? Because time value is highest for ATM options. Think about it. An ATM option has the most uncertainty – it could go either way. An ITM option already has value, so its time value is smaller relative to its premium. An OTM option has a lower probability of becoming ITM, so its time value is smaller in absolute terms but can be a large percentage of the premium.

On June 4, the 21,500 Put was ATM when Nifty was around 21,500 the previous day. When the crash happened, it became deep ITM. Its intrinsic value shot up, but its time value also exploded because volatility spiked. That is the double whammy of a market panic.

## A Worked Example: Decomposing a Premium

Let us take a real-world example from the Indian markets. Suppose it is a Tuesday in March. Nifty is trading at 22,000. You are looking at the 22,200 Call option expiring in 30 days. The option is trading at ₹120.

**Step 1: Calculate intrinsic value.**  
Spot = 22,000, Strike = 22,200. Since spot < strike, intrinsic value = ₹0. The entire ₹120 is time value.

**Step 2: Understand what you are paying for.**  
You are paying ₹120 for the right to buy Nifty at 22,200. For Nifty to be above 22,200 at expiry, it must rise by at least 200 points (0.9%). That seems plausible. But the option seller is betting that it won’t happen, or that the move will be smaller. The ₹120 compensates the seller for that risk.

**Step 3: Look at the same strike with 60 days to expiry.**  
The 22,200 Call with 60 days might trade at ₹200. Same intrinsic value (₹0), but more time value because there is more time for Nifty to move. Time value decays as expiry approaches – a phenomenon called **theta decay**.

**Step 4: Compare with an ITM option.**  
Now look at the 21,800 Call (same expiry, 30 days). Spot is 22,000, so intrinsic value = ₹200. The option might trade at ₹280. That means time value = ₹80. Notice that the time value is lower than the OTM option’s time value? Actually, ₹80 vs ₹120 – the OTM option has higher time value in absolute terms? No, wait. The OTM option had ₹120 time value, the ITM option has ₹80. That is because the ITM option already has a high intrinsic value, and the probability of it becoming even more ITM is lower than the probability of the OTM option becoming ITM. But this is not always the case – it depends on volatility and distance from spot.

The key point: time value is not constant across strikes. It peaks at ATM and declines as you move away.

## The Forces That Shape Time Value

Three main factors determine how much time value an option carries:

**1. Time to expiry (theta):** More time means more uncertainty, hence higher time value. As expiry approaches, time value decays at an accelerating rate. The last 30 days see the fastest decay. This is why option sellers love time decay and buyers fear it.

**2. Volatility (vega):** Higher expected volatility increases time value. When markets are calm, options are cheap. When fear spikes, premiums explode. On June 4, the India VIX – a measure of expected volatility – shot up from around 12 to over 30. That alone can double or triple option premiums, even without a move in the underlying.

**3. Interest rates (rho):** This is a minor factor for short-dated options, but it matters for longer-dated ones. Higher interest rates increase call premiums and decrease put premiums slightly. In India, with rates around 6-7%, the effect is small but not zero.

Let me give you a concrete example of volatility’s impact. In early 2024, HDFC Bank options saw implied volatility spike to 45% during a sharp sell-off. A 30-day ATM put that would normally trade at ₹50 was suddenly trading at ₹120. The intrinsic value hadn’t changed much – the stock had fallen, yes – but the bulk of the increase was due to fear. Traders were willing to pay a huge premium for protection because they didn’t know how low the stock could go.

## The Buyer’s Dilemma

Here is the uncomfortable truth about option premiums: **time value is the enemy of the buyer.** Every day that passes, a small piece of your premium evaporates. If the market doesn’t move in your direction quickly enough, your option loses value even if the underlying stays flat.

Consider this: You buy a Nifty 22,000 Call with 30 days to expiry for ₹150. Nifty is at 22,000. After 15 days, Nifty is still at 22,000. Your option is now worth maybe ₹80 – you have lost ₹70 even though the index hasn’t moved. That is theta decay at work.

To profit as an option buyer, you need the underlying to move enough to overcome both the time decay and the premium you paid. Statistically, most options expire worthless. Studies show that roughly 70-80% of all options held to expiry end up as zero. The buyer’s advantage of limited risk and unlimited reward comes with a very low probability of success.

This is why I often tell new traders: “Option buying is like buying a lottery ticket with a slightly better chance of winning – but you still have to be right about direction, timing, and magnitude.”

## The Seller’s Perspective

Now flip the coin. The option seller collects the premium upfront. Their profit is limited to the premium received, but their risk can be large. However, the probability of the option expiring worthless is in their favour. This is why many experienced traders prefer selling options – especially when volatility is high.

On June 4, those who had sold the 21,500 Put before the crash faced massive losses. But those who sold it after the panic, when premiums were inflated, could have profited handsomely as the market recovered over the following months. The key is to sell when fear is high and buy when fear is low.

## A Practical Framework for Evaluating Premiums

When you look at an option premium, ask yourself three questions:

1. **How much of this premium is intrinsic value?** If the option is ITM, you are paying for real value. If it is OTM, you are paying purely for possibility.

2. **How much time value am I paying?** Compare the premium to the intrinsic value. If the option is OTM, the entire premium is time value. Is that reasonable given the time left and volatility?

3. **Is volatility high or low?** Check the India VIX or the implied volatility of the option itself. If IV is above its historical average, premiums are expensive. If it is low, they are cheap.

Let me walk you through a real trade I made in late 2023. Nifty was around 19,800. I wanted to buy a 20,000 Call with 15 days to expiry. The premium was ₹45. Intrinsic value was zero (OTM). Time value was ₹45. The India VIX was 12 – low. I felt the premium was reasonable given low volatility. Nifty rallied to 20,200 within a week. The option became ITM with intrinsic value of ₹200, and even with time decay, it was worth around ₹180. I booked a profit of ₹135 per share (₹45 to ₹180). That is a 300% return. But I was lucky – the move happened quickly and was large enough.

If Nifty had only moved to 20,050, the option might have been worth ₹60 – barely a profit after decay. Timing matters enormously.

## The Iceberg Melts

As expiry approaches, time value shrinks. In the last week, options that are far OTM often trade for just a few rupees. The iceberg has melted. Only the intrinsic value remains for ITM options. ATM options in the last week have very little time value – they are pure gambling on the final move.

This is why you will see Nifty weekly options (expiring every Thursday) with premiums that seem tiny for far OTM strikes. A 22,500 Call with two days to expiry might cost just ₹5 when Nifty is at 22,000. That ₹5 is pure time value – a lottery ticket. And most of those tickets expire worthless.

## Key Takeaways

- **Every option premium has two parts: intrinsic value (the money you would get if you exercised now) and time value (the price of possibility).** Intrinsic value is never negative; time value decays to zero at expiry.

- **Moneyness determines the composition of the premium.** ATM options have the highest time value. ITM options have high intrinsic value. OTM options are pure time value.

- **Time decay (theta) is the biggest enemy of the option buyer.** The closer to expiry, the faster the decay. Buyers need large moves to overcome theta.

- **Volatility (vega) can inflate or deflate premiums dramatically.** On panic days like June 4, 2024, premiums can double or triple even without a proportional move in the underlying. Selling when volatility is high can be profitable, but carries risk.

- **Always decompose the premium before trading.** Ask: What is intrinsic? What is time? Is volatility high or low? Do I have a genuine edge in direction and timing? Without that analysis, you are just gambling.