# Chapter 7: Microstructure: Gaps, Expiries, and the Last Half Hour

## How This Market Works

---

The Nifty opened at 22,794 on Thursday, January 18, 2024. The previous day's close had been 22,796. A gap of two points—essentially flat. Nothing unusual. By 9:30 AM, the index was down 150 points. By 11:00 AM, down 400. By 3:30 PM, HDFC Bank had lost ₹1,00,000 crore in market capitalization in a single session. The stock fell 8.5%, its worst day since the COVID crash of March 2020.

I remember watching the screen that afternoon. The bid stack on HDFC Bank looked like a staircase collapsing floor by floor. Every time a buyer appeared at ₹1,620, the stock found sellers at ₹1,615. Then ₹1,610. Then ₹1,600. The price didn't fall in a smooth line—it fell in chunks, with gaps between trades where no one was willing to step in.

This is the microstructure of Indian markets. Not the grand narratives of FII flows or GDP growth, but the mechanical reality of how prices actually move from one level to the next. Most traders spend their time studying charts and fundamentals. Few understand the plumbing. And the plumbing, as you will see, is where money is made and lost.

---

## The Anatomy of a Gap

A gap occurs when the opening price of a security is significantly higher or lower than its previous closing price, with no trades occurring in between. In theory, markets should be continuous. In practice, they are not.

Consider what happens overnight. From 3:30 PM to 9:15 AM the next day, no trades occur on the NSE. But during those 18 hours, events happen: US markets move, corporate results are announced, geopolitical news breaks. When trading resumes, all that accumulated information must be absorbed at once. The result is a gap.

There are four types of gaps, and each tells you something different about market structure:

**Common gaps** occur in low-liquidity stocks or during sideways markets. They get filled quickly—often within the same session. A stock trading at ₹500 closes at ₹502, opens at ₹498, and returns to ₹501 by noon. Nothing meaningful happened. The gap was noise.

**Breakaway gaps** occur when price breaks out of a trading range on high volume. In August 2024, when the Nifty finally cleared 25,000 after weeks of consolidation, it opened 150 points higher and never looked back. That gap was a signal that new information—in this case, strong DII inflows and stable FII positioning—had permanently shifted the equilibrium.

**Runaway gaps** occur in the middle of a strong trend. They indicate momentum so powerful that even overnight, buyers are willing to pay higher prices to get in. During the recovery from the June 4, 2024 crash, the Nifty gapped up seven times in ten sessions. Each gap was smaller than the last, but the pattern was unmistakable: the market was being repriced higher in discrete jumps.

**Exhaustion gaps** occur near the end of a trend. They look like runaway gaps but are accompanied by declining volume and a rapid reversal. In January 2023, the Nifty gapped up 200 points on low volume, then reversed to close flat. The gap was the last gasp of a dying move.

The key insight is this: gaps are not random. They are the market's way of processing information that arrived when the exchange was closed. The size of the gap tells you how surprised the market was. The volume after the gap tells you whether the surprise was permanent or temporary.

---

## The Expiry Trap

If gaps are about overnight information, expiries are about forced positioning. And nowhere is this more visible than in the weekly and monthly derivatives expiry on the NSE.

Let me walk you through a typical expiry day.

It is Thursday, May 30, 2024. The Nifty weekly expiry. Open interest data from the previous day shows massive put writing at 22,500. Thousands of retail traders have sold puts, collecting premium, confident the market will not fall below that level. The Nifty is trading at 22,800.

At 9:15 AM, the market opens flat. By 10:30 AM, it is down 50 points. By 12:00 PM, down 100. The put sellers are still comfortable—22,500 is 200 points away. By 1:30 PM, the Nifty is at 22,550. The put sellers are now nervous. Their positions are approaching the strike price. If the Nifty closes below 22,500, they will be forced to buy the index at a loss.

At 2:30 PM, the selling accelerates. The Nifty touches 22,510. The put sellers, now panicking, start buying back their positions to close them before expiry. But buying puts pushes the price of puts higher, which signals more fear, which triggers more selling of the underlying index. It is a feedback loop.

At 3:15 PM, the Nifty is at 22,480. The put sellers who sold at ₹50 premium are now looking at a loss of ₹200 per lot. They are trapped. They cannot close because the bid-ask spread has widened to 20 points. They cannot roll because the next week's expiry is too far away. They can only watch as the clock ticks toward 3:30 PM.

At 3:30 PM, the Nifty settles at 22,470. Every put seller who held to expiry is now short 50 points on a position they sold for 50 points of premium. They have lost their entire investment plus more.

This is not a hypothetical. It happens every week.

The mechanism is simple: option sellers, particularly retail traders, tend to sell out-of-the-money puts for small premiums. They believe the market will not fall. But on expiry day, if the market approaches their strike, they are forced to cover. Their covering pushes the market lower, which forces more covering, which pushes the market lower still. The result is a cascade that can move the Nifty 200-300 points in the last hour of expiry.

I have seen this pattern repeat hundreds of times. The expiry day gap-down is almost always a self-fulfilling prophecy. The market does not fall because of bad news. It falls because option sellers are forced to buy back their positions, and their buying creates the very price movement they were trying to avoid.

---

## The Last Half Hour

The final thirty minutes of trading—from 3:00 PM to 3:30 PM—are unlike any other period in the Indian market day. This is when institutional players execute their end-of-day adjustments, when arbitrageurs close their positions, and when the settlement price for derivatives is determined.

Consider the volume profile. On a normal day, the first hour (9:15 AM to 10:15 AM) accounts for about 25% of total volume. The last hour accounts for another 25%. The middle four hours account for the remaining 50%. But on expiry days, the last hour can account for 40% or more of total volume.

Why? Because the settlement price for futures and options is calculated based on the average price of the underlying between 3:00 PM and 3:30 PM. This means that every trader with an expiring position has an incentive to influence that average price in their favor.

Here is how it works:

A large trader holds 10,000 lots of Nifty futures long. He wants to close his position before expiry. If he sells all 10,000 lots at once, he will push the price down and get a worse average price. So he spreads his selling across the last half hour, selling 500 lots every two minutes. The market absorbs his selling without moving too much.

But another trader, holding 10,000 lots short, wants to buy back his position. He also spreads his buying across the last half hour. The two traders are effectively trading against each other, and the net effect on price is neutral.

Now consider the option writers. A trader who sold 22,500 puts wants the Nifty to close above 22,500. If the Nifty is at 22,480 at 3:00 PM, he has a problem. He can either buy back his puts at a loss, or he can buy Nifty futures to push the index higher. Buying futures is cheaper than buying back puts, so he buys futures. His buying pushes the Nifty up. Other put sellers see the Nifty moving up and feel relief. They stop selling. The Nifty moves higher still.

This is the last half hour in action. It is not a random walk. It is a battle between traders with expiring positions, each trying to manipulate the settlement price in their favor. The result is often a sharp move in one direction, followed by a reversal in the final minutes as the manipulation unwinds.

---

## Worked Example: The Gap-Down Expiry

Let me give you a concrete example with numbers.

**Setup:**
- Nifty closes Wednesday at 22,800.
- Open interest data shows 2,00,000 lots of 22,500 puts outstanding for Thursday expiry.
- Average premium collected: ₹50 per lot.
- Total notional exposure: 2,00,000 × 50 × 22,500 = ₹22,500 crore.
- Total premium collected: 2,00,000 × 50 × ₹50 = ₹50 crore.

**Thursday morning:**
- Overnight, US markets fall 2% on weak economic data.
- Nifty opens at 22,650, a gap-down of 150 points.
- The 22,500 puts, which were 300 points out of the money, are now only 150 points away.
- Put sellers are nervous but not panicking.

**Thursday afternoon:**
- By 2:00 PM, the Nifty is at 22,550.
- The 22,500 puts are now 50 points away from being in the money.
- Put sellers start covering. Each lot they buy back costs ₹100 (the put is now trading at ₹100).
- Their loss per lot: ₹100 - ₹50 = ₹50.
- Total loss so far: 2,00,000 × 50 × ₹50 = ₹50 crore. They have lost their entire premium.

**Thursday 3:00 PM:**
- The Nifty is at 22,520.
- Put sellers are desperate. They start buying Nifty futures to push the index higher.
- Each lot of Nifty futures they buy pushes the index up by approximately 0.5 points.
- If 10,000 lots of futures are bought, the Nifty moves up 5,000 points? No. The calculation is more complex. Each Nifty futures lot represents 50 units of the index. Buying 10,000 lots means buying 5,00,000 units. The total market capitalization of Nifty 50 stocks is approximately ₹2,00,00,000 crore. A buy order of 5,00,000 units represents 0.00025% of the market. It moves the index by approximately 0.5 points.

**Thursday 3:15 PM:**
- The Nifty is at 22,530.
- Put sellers have bought 20,000 lots of futures, pushing the index up 10 points.
- But now, other traders who were short futures see the buying and start covering their shorts.
- Their covering adds to the buying pressure.
- The Nifty moves to 22,540.

**Thursday 3:25 PM:**
- The Nifty is at 22,545.
- Put sellers have spent ₹50 crore buying futures.
- They have pushed the index up 25 points from the low.
- But the 22,500 puts are still 45 points out of the money.
- The put sellers need the Nifty to close above 22,500.
- They continue buying.

**Thursday 3:30 PM:**
- The Nifty settles at 22,535.
- The 22,500 puts expire worthless.
- Put sellers have lost their ₹50 crore premium plus an additional ₹20 crore in futures losses.
- Total loss: ₹70 crore.

This is the expiry trap. The put sellers were correct that the market would not fall to 22,500. But the gap-down forced them to defend their positions, and their defense cost them more than the premium they collected.

---

## The Role of Circuit Breakers

Indian markets have a unique feature: circuit breakers. When a stock moves beyond a certain percentage (typically 10% for most stocks, 20% for some), trading is halted for a period. This is designed to prevent panic selling or buying.

But circuit breakers have a dark side. They create artificial gaps.

Consider a stock trading at ₹1,000. Bad news breaks. The stock opens at ₹950, a 5% gap-down. Selling continues. At ₹900, the lower circuit is hit. Trading stops. No one can sell. No one can buy.

The next day, the stock opens at ₹850, another gap-down. The circuit is hit again. This continues until the stock reaches a price where buyers are willing to step in.

The problem is that circuit breakers prevent price discovery. The stock might have found buyers at ₹800, but because trading was halted at ₹900, no one could test that level. The gap-downs are forced, not natural.

I have seen this pattern in small-cap stocks during market corrections. A stock falls 10% in one day, hits circuit, and then falls another 10% the next day. The total decline is 20% over two days, but the stock might have only needed to fall 12% to find equilibrium. The circuit breakers stretched the decline over two days, creating gaps that trapped sellers at higher prices.

---

## The SGX Nifty and Overnight Gaps

Before the NSE opens at 9:15 AM, the SGX Nifty (now the Nifty 50 Futures on the Singapore Exchange) trades for 18 hours. This is the overnight market for Indian equities.

The SGX Nifty is not a perfect proxy for the cash market. It has lower liquidity and wider spreads. But it gives you a sense of where the market might open.

Here is the key insight: the SGX Nifty gap is not random. It is driven by the same forces that drive the cash market—FII flows, US market movements, and global news. But because the SGX Nifty has lower liquidity, it tends to overreact. A 1% move in the Dow might translate to a 1.5% move in the SGX Nifty. When the cash market opens, the gap often partially fills as arbitrageurs step in.

I have traded this gap for years. The pattern is consistent: if the SGX Nifty is down 1% at 8:00 AM, the cash market will open down 0.8% to 1.2%. If the SGX Nifty is down 2%, the cash market will open down 1.5% to 2.5%. The larger the gap, the more likely it is to partially fill in the first hour.

But there is a catch. On expiry days, the gap behaves differently. Option writers, trapped in their positions, will defend the gap. If the SGX Nifty is down 1% on expiry day, the cash market might open down only 0.5% because put sellers are buying futures to push the index higher. The gap is compressed by forced positioning.

---

## Practical Lessons

What does all this mean for you as a trader?

First, **never trade a stock on its result day**. The gap between the close and the next day's open is too unpredictable. You are trading against people who have better information than you. Wait for the dust to settle.

Second, **respect the expiry**. If you are short options, understand that the last half hour can destroy you. If you are long options, understand that time decay accelerates as expiry approaches. The microstructure of expiry is brutal to the unprepared.

Third, **use limit orders, not market orders, during gaps**. When a stock gaps down 5%, the bid-ask spread widens. A market order will execute at the worst possible price. A limit order gives you control. I have seen traders lose 2-3% on a single trade because they used a market order during a gap.

Fourth, **watch the last half hour**. This is when the smart money positions for the next day. If the Nifty is up 100 points at 3:00 PM but falls to flat by 3:30 PM, that is a bearish signal. The institutions are selling into strength. If the Nifty is down 100 points at 3:00 PM but recovers to flat by 3:30 PM, that is a bullish signal. The institutions are buying into weakness.

Fifth, **understand that gaps are not always filled**. The common wisdom is that "gaps always get filled." This is false. Breakaway gaps and runaway gaps often remain unfilled for months or years. The only gaps that reliably fill are common gaps and exhaustion gaps. Do not assume a gap will fill just because it exists.

---

## Key Takeaways

1. **Gaps are information events.** The size of the gap tells you how surprised the market was by overnight news. The volume after the gap tells you whether the surprise is permanent or temporary.

2. **Expiry day moves are driven by forced positioning, not fundamentals.** Option sellers defending their strikes can move the market 200-300 points in the last hour. Do not confuse this with genuine price discovery.

3. **The last half hour is the most important period of the trading day.** This is when settlement prices are determined and institutional positioning occurs. Watch it closely.

4. **Circuit breakers create artificial gaps.** They prevent price discovery and can stretch a decline over multiple days. Be cautious when trading stocks near circuit limits.

5. **Never use market orders during gaps.** The bid-ask spread widens significantly, and you will pay a premium for immediacy. Use limit orders and be patient.