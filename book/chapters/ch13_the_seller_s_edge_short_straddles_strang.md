# Chapter 13: The Seller’s Edge: Short Straddles & Strangles

On June 4, 2024, the Nifty 50 opened near 23,300. By mid-morning, it had crashed to 21,281 — an intraday fall of roughly 8.5%. For option sellers who had collected modest premiums the previous Friday, the day was a catastrophe. Margin calls flooded brokerages. One trader I know had sold a short straddle at 23,000 strike, collecting ₹18,000 per lot. By noon, his position was down ₹1.2 lakh per lot. He was wiped out before the index recovered 2,300 points over the following months.

That day is not an exception. It is the reason every option seller must understand the edge — and the cliff — that comes with short straddles and strangles.

## The Basic Idea: Selling Volatility

A short straddle is simple: sell one call and one put at the same strike price, same expiry. You collect two premiums. You profit if the underlying stays near that strike. You lose if it moves too far in either direction.

A short strangle is the same idea, but with the call sold at a higher strike and the put sold at a lower strike. The range is wider, the premium collected is smaller, and the probability of profit is higher — but the potential loss is still unlimited on the side that breaks out.

Think of it as an insurance company. You collect small, regular premiums from many policies. Most months, nothing happens and you keep the money. But once in a while, a hurricane hits. One event can wipe out years of premiums. The option seller’s job is not to avoid hurricanes — it is to survive them.

## The Low-VIX Trap

The most dangerous time to sell options is when the India VIX is at multi-year lows. In 2013, the VIX hovered around 12–14 for months. Traders grew comfortable selling strangles. Then came the taper tantrum in May 2013. The VIX spiked to 30 in days. One trader I know lost over ₹1 crore on a single strangle position. The premium he had collected over three months was erased in one afternoon.

Low VIX means low premiums. To earn a decent return, you must sell many contracts or take strikes very close to the current price. Both increase risk. When VIX is low, the market is complacent. Complacency is the mother of blow-ups.

The rule is simple: **In low VIX, always pair your sells with buys.** Use a calendar spread, a ratio spread, or buy a far-dated put as insurance. Never sell naked in a low-VIX regime.

## The Expected Range: Your First Tool

Before selling a straddle or strangle, you need to know the market’s own estimate of the likely range. The simplest way is to look at the ATM straddle premium.

Take Nifty at 22,000. The ATM call (22,000) is trading at ₹250. The ATM put (22,000) is trading at ₹230. The total straddle premium is ₹480. That 480 points is the market’s expectation of the absolute movement by expiry — not the direction, just the magnitude.

A rough rule of thumb: about 65% of the time, the underlying stays within the range of the ATM strike plus or minus the straddle premium. So for Nifty 22,000 with a ₹480 straddle, the expected range is 21,520 to 22,480. If you sell a straddle at 22,000, you are betting that Nifty will stay inside that band.

But remember: 35% of the time it will break out. And when it does, the losses can be severe.

## Worked Example: Short Straddle on Nifty

Let’s walk through a realistic trade.

**Date:** First week of the monthly expiry cycle.  
**Nifty spot:** 22,000  
**ATM strike:** 22,000  
**Call premium:** ₹250  
**Put premium:** ₹230  
**Total premium collected:** ₹480 per lot  
**Lot size:** 50  
**Premium received:** ₹480 × 50 = ₹24,000  
**Margin required:** Approximately ₹1,20,000 (varies by broker)  
**Maximum profit:** ₹24,000 (if Nifty closes exactly at 22,000)  
**Breakeven points:**  
- Upper breakeven: 22,000 + 480 = 22,480  
- Lower breakeven: 22,000 – 480 = 21,520  

**Scenario A – Nifty stays at 22,000:** You keep the entire ₹24,000. Return on margin: 20% in one month. Attractive, but unlikely.

**Scenario B – Nifty moves to 22,300:** The call is now worth ₹300 (intrinsic value 300, time value zero near expiry). The put is worth ₹0. Your position loss: (300 – 250) × 50 = ₹2,500 loss on call, plus you kept the put premium. Net profit: ₹24,000 – ₹2,500 = ₹21,500. Still good.

**Scenario C – Nifty moves to 22,800:** The call is worth ₹800. Loss on call: (800 – 250) × 50 = ₹27,500. Net loss: ₹27,500 – ₹24,000 = ₹3,500. You lose money even though the move is only 3.6%.

**Scenario D – Nifty crashes to 21,000:** The put is worth ₹1,000. Loss on put: (1,000 – 230) × 50 = ₹38,500. Net loss: ₹38,500 – ₹24,000 = ₹14,500. A 4.5% drop costs you 12% of your margin.

**Scenario E – Nifty gaps to 20,000 overnight:** The put is worth ₹2,000. Loss: (2,000 – 230) × 50 = ₹88,500. Net loss: ₹64,500. That is more than half your margin. And if the gap continues, you face unlimited losses.

This is the reality. A short straddle can give you a 20% monthly return in calm markets, but a single 5% move can wipe out months of profits. A 10% move can wipe out your account.

## The Strangle: Wider Net, Smaller Catch

A short strangle reduces the probability of a blow-up by widening the range. Instead of selling at the same strike, you sell an OTM call and an OTM put.

**Example:**  
Nifty at 22,000.  
Sell 22,500 call at ₹120.  
Sell 21,500 put at ₹110.  
Total premium: ₹230 per lot = ₹11,500 per lot.  
Margin: ~₹80,000.  
Breakevens: 21,270 to 22,730.  
Maximum profit: ₹11,500.

The range is wider (1,460 points vs 960 points for the straddle), so the probability of staying inside is higher. But the premium is half. And the loss profile is still asymmetric: a move to 23,000 gives a call loss of (500 – 120) × 50 = ₹19,000, net loss ₹7,500. A move to 20,000 gives a put loss of (1,500 – 110) × 50 = ₹69,500, net loss ₹58,000.

The strangle is safer than the straddle, but not safe. It is a different trade-off: lower income, higher probability, but still exposed to tail risk.

## The June 4, 2024 Lesson

That day, Nifty fell from 23,300 to 21,281 intraday — a drop of 2,019 points. Any short straddle or strangle sold within 1,000 points of the open was destroyed. The sellers who survived were those who had bought protection.

One common hedge is the **ITM put calendar**. In a low-VIX regime, you buy a far-dated put (say, December expiry) and sell a near-dated put (July expiry) at the same strike. The idea: the near-dated put decays faster, and the far-dated put acts as insurance against a crash.

For example, in July 2024, with Nifty around 24,000, you could buy a December 24,000 put for ₹580 and sell a July 24,000 put for ₹350. Net cost: ₹230. If Nifty stays flat, the July put decays to zero, and you keep the December put for free. If Nifty crashes, the December put gains value faster than the July put loses, giving you a net profit. This is a low-cost hedge that can be layered with short straddles.

## The Promoter Holding Factor

One nuance specific to Indian markets: promoter holdings affect volatility. Stocks with high promoter holding (like many PSUs) tend to have lower liquidity and sharper moves on news. Selling strangles on such stocks is riskier because the gap risk is higher. For example, a stock like PFC (with promoter holding above 50%) can gap 5–10% on a policy announcement. The option seller has no time to react.

Always check the promoter holding pattern before selling options on individual stocks. For index options, the risk is more diversified but still present — as June 4 showed.

## The Monthly Range Method

A practical approach used by many traders is the **monthly expected range** based on the ATM straddle at the start of the expiry cycle.

On the Friday after expiry, note the Nifty close. Take the nearest strike. Add the ATM call and put premiums. That sum is the expected range. Sell a strangle at strikes outside that range.

Example from a real month:  
Nifty close: 11,647. Nearest strike: 11,650.  
ATM call: ₹220. ATM put: ₹190. Total: ₹410.  
Expected range: 11,240 to 12,060 (rounded to 11,200–12,100).  
Sell a strangle: 12,100 call and 11,200 put.  
Premium collected: maybe ₹80–100 each side.  
Probability of staying inside: roughly 65%.

This method is not a guarantee. It is a framework. You still need to manage the position daily.

## The Golden Rule: Always Mix Buys with Sells

The single most important lesson from decades of option selling in India is this: **never be a pure seller.** Always have a bought option somewhere in your portfolio. It could be a far-dated put, a calendar spread, or a small long volatility position. The cost of this insurance is the premium you pay. That premium is your survival budget.

In 2013, the traders who survived the taper tantrum were those who had bought puts or had long vega positions. Those who were net short vega were wiped out.

## Key Takeaways

- **Short straddles and strangles are high-probability, low-magnitude strategies that carry tail risk.** One bad day can erase months of gains.
- **Low VIX is the most dangerous regime for option sellers.** Always pair sells with buys — use calendars, ratio spreads, or long-dated puts as insurance.
- **The ATM straddle premium gives a rough expected range.** About 65% of the time, the underlying stays within that range. But the other 35% can be brutal.
- **Promoter holding patterns matter for stock options.** High promoter holding stocks can gap more violently; prefer index options for cleaner risk.
- **Never sell naked.** The premium you collect is not yours until expiry. Until then, it is borrowed money that can be taken back by the market at any moment.