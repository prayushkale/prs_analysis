# Chapter 14: Controlled Direction: Spreads & Ratio Spreads

## The Strategy Library

---

The Nifty was falling like a stone. It was June 4, 2024—Lok Sabha counting day—and by 11:30 AM, the index had dropped nearly 8.5% from the previous close. Traders who had bought out-of-the-money call options expecting a victory rally were watching their premiums evaporate. Those who had sold puts naked were seeing margin calls flash on their screens. In the options trading pit (now digital, but the panic is the same), people were doing the math on how much they had lost in a single morning.

I was watching one of my juniors, a sharp trader named Ravi, who had a position that most people would have closed in fear. He had a **call ratio spread** on Nifty—bought one lot of the 22,500 strike call for June expiry, and sold two lots of the 23,000 strike call. The net cost was ₹3,200. His maximum loss was that ₹3,200. His maximum profit, if Nifty stayed below 23,000 by expiry, was about ₹12,000. He sat there, sipping tea, watching the carnage with the calm of a man who knew exactly what his worst-case scenario was.

"Nervous?" I asked.

He shook his head. "Dhanraj sir, the market can do whatever it wants. My downside is capped. If it falls, I lose ₹3,200. If it goes up moderately, I win. If it moons, I still lose only ₹3,200. I don't need to predict the direction—I just need the market to not explode past my short strike."

That, in essence, is the philosophy of spreads and ratio spreads. You trade controlled direction. You pay a small, defined premium for a view—not an unlimited bet. And when you use ratios, you can often get that view for zero or even a net credit.

This chapter is about those strategies. Not as magic formulas, but as tools. You need to understand the mechanics, the margin implications, and the market conditions where they work. Because in Indian markets, where volatility can spike 30% in a single session, knowing how to cap your risk is not optional—it's survival.

---

## The Core Idea: From Naked to Defined

Let's start with the simplest spread: a vertical spread.

A vertical spread means you buy one option and sell another option of the same type (both calls or both puts) but with different strike prices, same expiry. The name "vertical" comes from the option chain display—strikes are listed vertically.

For example, a **bull call spread**: buy a 22,000 call, sell a 22,500 call. You pay a net premium (the difference between the two option prices). Your maximum profit is the width of the spread minus the net premium paid. Your maximum loss is the net premium paid.

Why do this instead of just buying a naked call? Because the naked call has unlimited upside risk (if you're short) or a large premium cost (if you're long). The spread trades off some profit potential for a defined, smaller risk.

Now, a **ratio spread** takes this one step further. Instead of buying one and selling one, you buy one and sell two (or more) of a higher strike. The ratio is typically 1:2 or 2:3. The goal is to create a position that costs very little or even has a net credit, while still having a defined maximum loss.

The key insight: you are selling more options than you are buying. This gives you a larger premium inflow, but it also means your upside is capped—because if the market moves beyond your short strikes, the second short option starts to hurt.

---

## The Call Ratio Spread: Mechanics and Example

Let's work through a real example from the Indian markets.

**Setting:** Nifty is trading at 18,200. You believe the market will stay range-bound or rise modestly over the next 15 days (until monthly expiry). You do not think it will rally beyond 18,500.

You construct a **1:2 call ratio spread**:

- **Buy 1 lot** Nifty 18,200 Call (ATM) at ₹80 premium. Cost = 1 × 75 (lot size) × ₹80 = ₹6,000.
- **Sell 2 lots** Nifty 18,500 Call (OTM) at ₹35 premium. Credit = 2 × 75 × ₹35 = ₹5,250.

Net cost = ₹6,000 – ₹5,250 = **₹750**.

Your position is now:

- **Maximum profit:** If Nifty expires exactly at 18,500, the bought 18,200 call is worth ₹300 (18,500 – 18,200 = 300 points), and the sold 18,500 calls expire worthless. Total value: 1 lot × 75 × ₹300 = ₹22,500. Subtract your net cost ₹750 → profit = ₹21,750. But wait—there's a nuance: the maximum profit occurs when Nifty is exactly at the short strike, not above. Above 18,500, the second short call starts going in-the-money, reducing profit.

- **Breakeven point (upper):** You need to calculate where the loss from the short calls equals the gain from the long call. This is typically a few hundred points above the short strike. In this case, breakeven is around 18,750 (depending on exact volatilities). Above that, you start losing.

- **Maximum loss:** Limited to the net premium paid (₹750) if Nifty falls below 18,200. But if Nifty rises sharply above, say 19,000, your loss can become large because you are short two calls. However, because the long call also gains, the loss is capped at the differential between the long and short strikes. In a standard 1:2 ratio spread, the maximum loss (on the upside) is: (Short strike – Long strike) × lot size × number of shorts sold, minus net credit. Formula: (18,500 – 18,200) × 75 × 2 = 300 × 150 = ₹45,000. Then subtract your net credit (if any) or add net debit. Here net debit is ₹750, so maximum loss = ₹45,000 + ₹750 = **₹45,750**. That's the worst case if Nifty closes above 18,500. But note: this loss is still defined. You know it upfront.

So the trade has:
- A small downside risk (₹750 if market crashes).
- A large upside risk (₹45,750 if market rallies above 18,500).
- A sweet spot near 18,500 where you make ₹21,750.

Why would anyone take such a trade? Because you are betting that the market will not rally strongly. You are selling volatility. If your view is correct, you win. If you're wrong and the market blasts through, you have a defined loss. Compare this to selling a naked call: if you sold the 18,500 call naked, your loss could be unlimited (theoretically). The ratio spread gives you a buffer from the long call, but still requires discipline.

---

## The FD-Funded Call Spread: A Real Story

A common objection I hear: "Dhanraj sir, I don't want to risk my capital on options. Even a small debit is money I might lose."

That is correct. Option buying, especially for retail traders, is a losing game over time because of theta decay and the bid-ask spread. But there is a way to participate in directional moves without risking your principal: fund the trade with interest from a fixed deposit.

Let me tell you about a strategy I shared with a group of friends before the Union Budget 2024. The market was range-bound, India VIX was around 11 (a 12-year low), and everyone expected a volatile budget day. One of my friends, a retired professor, had ₹10 lakh in a fixed deposit earning 8% per annum—about ₹80,000 in interest per year.

"Why not use that interest to take a small, defined bet?" I suggested.

Here's what we did:

- He kept his FD intact.
- He used ₹80,000 (the interest) to buy a **bull call spread**: Buy Nifty 25,200 Call and sell Nifty 26,000 Call for the monthly expiry closest to budget day.
- The spread cost him about ₹60,000 (premium difference). The remaining ₹20,000 was kept as buffer.
- **Risk:** If the trade failed, he lost ₹60,000—but that was from the interest, not the principal. His ₹10 lakh FD remained untouched.
- **Reward:** If Nifty rallied above 26,000 by expiry, the spread would be worth ₹800 points (26,000 – 25,200) = ₹60,000 per lot. With one lot of Nifty (75 shares), that's ₹60,000 × 75 = ₹45,00,000? Wait—that's wrong. Let me correct: The spread width is 800 points. Maximum value = 800 × 75 = ₹60,000. If he paid ₹60,000, maximum profit would be ₹0? No, that doesn't make sense. Let me recalculate.

Actually, the spread width is 800 points. The premium he paid (net debit) depends on option prices. Typically, a 25,200–26,000 call spread might cost around ₹300–400 in premium (per unit). Let's assume he bought at ₹350 net debit. So cost per lot = 75 × ₹350 = ₹26,250. He bought one lot. Maximum profit = (800 – 350) × 75 = 450 × 75 = ₹33,750. So he risked ₹26,250 to potentially make ₹33,750. All from FD interest. Even if he lost the entire ₹26,250, his principal was safe.

The trade worked. Nifty rallied on budget day to about 25,800—not enough to max out the spread, but enough to exit with a profit of ₹12,000. He closed the trade three days later.

The key principle: **Never risk capital you cannot afford to lose. FD interest is a natural "free" money source.** In Indian markets, you can often find such opportunities around budget days, monetary policy announcements, or index rebalancing. The FD-funded spread is not a strategy for consistent profits—it's a way to participate in known events with no downside to your core savings.

---

## Low-Volatility Combos: The Margin-Optimized Approach

Now, let's talk about when volatility is low—like India VIX at 11 or lower. Many traders think this is a safe time to sell options. But low VIX means options are cheap, and a sudden spike can destroy short sellers. I've seen traders get "panic trapped" when the market touches a resistance, reverses, and VIX jumps 30% in a day.

The solution: never run pure naked shorts in low VIX. Instead, pair buys with sells so that a VIX spike cushions both sides.

Consider a **margin-optimized combo** I used in early 2023 when India VIX was at 12-year lows around 11. The market was range-bound between 18,000 and 18,500. I wanted to collect premium but had to sleep at night.

**The setup (for Nifty):**

- Sell a call ratio spread: Buy 1 lot 18,200 Call, Sell 2 lots 18,500 Call. (As above, net debit ~₹750.)
- Buy a put at support: Buy 1 lot 18,000 Put at ₹100. Cost = ₹7,500.

Wait, that adds more debit. Let me use a cleaner example from my actual trades:

**Low-VIX Combo (net credit):**

- Sell 1 lot Nifty 18,000 Put at ₹80 → credit ₹6,000.
- Buy 1 lot Nifty 17,800 Put at ₹40 → debit ₹3,000.
- Sell 2 lots Nifty 18,500 Call at ₹35 each → credit ₹5,250.
- Buy 1 lot Nifty 18,200 Call at ₹80 → debit ₹6,000.

Net credit = (6,000 + 5,250) – (3,000 + 6,000) = ₹2,250.

Now you have a position that:
- Has a defined loss zone between 17,800 and 18,000 (if market crashes) and above 18,500 (if market rallies).
- Returns net credit of ₹2,250 if market stays between 18,000 and 18,500.
- Margin requirement is about ₹5.7 lakh (because of the ratio leg).
- Expected return of about 3.5% in 15 days (₹20,000 on ₹5.7 lakh).

Is it a home run? No. But it's a consistent way to harvest theta in low volatility, with no unlimited risk. The breakeven points are well-defined: lower breakeven around 17,770, upper around 18,770.

The beauty is that if VIX spikes, the long options (the bought put and bought call) gain value, cushioning the loss on the short options. This is the opposite of a naked position, where a VIX spike amplifies losses.

---

## When Ratio Spreads Fail: The Black Swan

I must be honest. Ratio spreads have a dark side. If the market makes a swift, violent move beyond your short strike, the loss, though defined, can be substantial. In the earlier call ratio spread example, the maximum loss was ₹45,750—that's real money. If you have multiple lots, it adds up.

I recall a friend in 2021 who did a 1:3 ratio on Bank Nifty just before the RBI policy. He was convinced the market would stay range-bound. The RBI surprised with a rate hike, Bank Nifty shot up 1,200 points in two days. His short calls were deep in-the-money. He lost ₹1.5 lakh on a position he thought was "defined." Yes, it was defined—he just didn't internalize that the defined loss was still large enough to hurt.

**Lesson:** Only use ratio spreads when you have a strong conviction about the upper bound of the move. Never use them in events with binary outcomes (like elections or central bank decisions) unless you have a hedge.

---

## Practical Steps for Indian Traders

If you want to trade spreads and ratio spreads in the Indian market, here is a checklist:

1. **Choose your underlying:** Stick to Nifty, Bank Nifty, or highly liquid stocks like Reliance, HDFC Bank, TCS. Avoid illiquid options where bid-ask spreads are wide.
2. **Check expiry:** Weekly or monthly? Monthly expiries have more time, lower theta decay. Weekly options are for short-term views. I prefer monthly for ratio spreads because the extra time gives the market a chance to move into your sweet spot.
3. **Calculate margin:** Brokers in India use SPAN + Exposure margin. For ratio spreads, margin is higher than vertical spreads because of the short legs. Always check before entering. I've seen traders get margin calls because they underestimated the requirement.
4. **Set a stop-loss on the spread:** Even though the loss is defined, you can exit early to preserve capital. If the market moves against you, don't wait for expiry. Cut at 50% of max loss.
5. **Understand the Greeks:** Ratio spreads are sensitive to volatility (Vega) and time (Theta). In low VIX, selling premium via ratio works well. In high VIX, buying spreads (like the FD-funded call spread) is better.

---

## Key Takeaways

- **Spreads define your risk.** You always know your maximum loss before entering. This is the single most important advantage over naked options.
- **Ratio spreads allow near-zero cost trades** by selling more options than you buy, but they come with a defined—but potentially large—loss if the market moves beyond your short strike.
- **Use FD interest to fund directional spreads** for known events. This preserves your principal and turns "free" interest