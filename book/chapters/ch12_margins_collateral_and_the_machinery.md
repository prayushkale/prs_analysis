# Chapter 12: Margins, Collateral and the Machinery

## Options from First Principles

---

The phone rang at 3:15 PM on a Thursday. My friend, let's call him Vikram, had been trading options for six months. He'd made steady money selling Nifty puts—nothing flashy, just consistent ₹15,000 to ₹25,000 a month. That afternoon, his broker's risk desk was on the line.

"Sir, your margin is short by ₹2.3 lakh. You need to fund or we'll square off your positions."

Vikram had sold a Nifty 21,000 put at ₹80. The market had dropped 200 points in two hours. His margin requirement had ballooned from ₹1.2 lakh to ₹3.5 lakh. He had ₹1.8 lakh in his account. The math didn't work.

He scrambled, transferred money, and kept the position. The market recovered the next day. He made ₹12,000. But for four hours, he learned what every options seller eventually learns: **margin is not a suggestion. It is the machinery that keeps the system from breaking.**

---

## The Broker's Dilemma

When you buy an option, you pay the premium. That's your maximum loss. The broker doesn't worry about you defaulting—you've already paid your worst-case scenario upfront.

When you sell an option, you take on an obligation. If the market moves against you, the loss can be large. The broker sits between you and the exchange. If you cannot pay your loss, the broker must pay the exchange. The broker does not like this arrangement.

So the broker demands **margin**—a deposit that ensures you can cover potential losses.

This is not unique to options. Futures contracts also require margin. But options margin is more interesting because the obligation changes as the market moves.

---

## The Two Margins

In India, the exchange (NSE or BSE) sets margin rules. Every broker must follow them. There are two main components:

### 1. SPAN Margin (Standard Portfolio Analysis of Risk)

SPAN is a risk assessment system developed by the Chicago Mercantile Exchange. It looks at your entire portfolio of futures and options and asks: *"What is the worst one-day loss we might experience?"*

For a simple short option position, SPAN margin is calculated based on:

- **The option's premium** – If you sold at ₹100 and the premium rises to ₹150, you're losing ₹50 per share
- **The delta** – How much the option moves for each point in the underlying
- **Volatility** – Higher volatility means bigger potential moves
- **The underlying price** – A 1% move in Nifty at 22,000 is 220 points; at 18,000 it's 180 points

SPAN margin is recalculated multiple times during the trading day. When the market moves, your margin changes. This is why Vikram's requirement jumped from ₹1.2 lakh to ₹3.5 lakh.

### 2. Exposure Margin

This is an additional buffer, typically 3% to 5% of the contract value for options. It covers the gap between what SPAN calculates and what might actually happen in extreme conditions.

For a Nifty option with a lot size of 50, if the strike is 21,000 and Nifty is trading at 21,500, the contract value is:
- 21,500 × 50 = ₹10,75,000
- Exposure margin at 3% = ₹32,250

This is added to your SPAN margin.

---

## A Worked Example: Selling a Nifty Call

Let's say it is Tuesday morning. Nifty is at 22,000. You decide to sell a 22,500 Call (out-of-the-money) at ₹50 premium. The lot size is 50.

**Step 1: Calculate your premium income**
- Premium received: ₹50 × 50 = ₹2,500

**Step 2: Calculate initial margin**

The exchange has a formula. But roughly, for an OTM option sale:

- SPAN margin: Typically 8-12% of the contract value, adjusted for the option being OTM
- Let's say SPAN = 10% of (22,500 × 50) = ₹1,12,500, reduced by 30% because the option is OTM
- Adjusted SPAN = 0.7 × ₹1,12,500 = ₹78,750
- Exposure margin: 3% of (22,000 × 50) = ₹33,000
- Total margin required: ₹78,750 + ₹33,000 = **₹1,11,750**

**Step 3: Subtract premium received**
- Net margin you need to bring: ₹1,11,750 - ₹2,500 = **₹1,09,250**

You put up ₹1,09,250. The broker holds it. You have collected ₹2,500 premium.

**Step 4: The market moves**

Now imagine Nifty rises to 22,400 by Thursday. Your 22,500 Call is no longer far OTM. The delta has increased from 0.25 to 0.45. The premium has risen from ₹50 to ₹120.

- Your mark-to-market loss: (₹120 - ₹50) × 50 = ₹3,500
- The SPAN margin recalculates. Now the option is closer to ATM. The adjustment factor drops. SPAN might climb to ₹95,000
- Total margin requirement: ₹95,000 + ₹33,000 = ₹1,28,000

But your account has:
- Initial margin deposited: ₹1,09,250
- Less MTM loss: -₹3,500
- Plus premium collected: ₹2,500 (already counted)
- Available balance: ₹1,05,750

Margin call: ₹1,28,000 - ₹1,05,750 = **₹22,250**

You need to add ₹22,250. Or close the position.

---

## Collateral: What You Can Pledge

You don't always need cash. The exchange allows certain securities as margin. This is called **collateral**.

In India, you can pledge:

| Asset | Percentage Value Considered | Notes |
|-------|---------------------------|-------|
| Cash | 100% | Instant liquidity |
| Fixed Deposits | 90-95% | Must be lien-marked to broker |
| Equity Shares (Nifty 50) | 50-85% | Haircut depends on volatility |
| Equity Shares (Other) | 20-50% | Higher haircut for smaller stocks |
| Mutual Funds (Liquid/ Debt) | 80-90% | Fund-specific |
| Gold ETFs | 70-80% | Subject to price fluctuations |
| Government Bonds | 90-95% | Lowest haircut |

The "haircut" is the discount applied. If you pledge ₹1 lakh worth of HDFC Bank shares, the broker might consider only ₹75,000 as margin value. The remaining ₹25,000 is the haircut—protection against the shares falling in value while pledged.

### How Pledging Works

You don't physically transfer shares. You create a **lien** through your broker. The shares stay in your demat account but are marked as pledged to the broker. You cannot sell them until the lien is released.

If you fail to meet margin obligations, the broker can invoke the pledge and sell the shares to recover dues.

---

## The Strange Case of ITM Options at Expiry

Here is where many traders get hurt.

For **index options** (Nifty, Bank Nifty, Finnifty), all options are cash-settled. If your option expires in-the-money, the exchange simply credits or debits cash. No shares change hands.

For **stock options**, ITM options result in **physical delivery**. If you sold a call on Reliance that expires ITM, you must deliver the actual shares. If you don't have them, the broker will buy them in the market and deliver them—at your cost.

This creates a liquidity nightmare on expiry day.

Consider this scenario: It's the last Thursday of the month. You sold a Reliance 2,500 Call at ₹30. Reliance closes at ₹2,520. Your option is ITM by ₹20 per share.

- You must deliver: ₹20 × lot size (250) = ₹5,000 loss
- Plus you need to deliver 250 shares of Reliance

If you don't own Reliance shares, the broker will:
1. Buy 250 shares in the market at ₹2,520
2. Deliver them to the option buyer
3. Charge your account ₹6,30,000 + brokerage + STT

This is not a margin call. This is a **delivery obligation**. Many traders who sell stock options without holding the underlying have learned this lesson the hard way.

---

## The Cost of Carry

When you use borrowed money or pledged securities for margin, there is a cost. Your broker charges interest on the margin funding. Typically, this is 12-18% per annum.

But here's a smarter way some traders use:

**Case Study: Anand's Fixed Income Collateral**

Anand had ₹10 lakh in a fixed deposit earning 7.5% per year. He wanted to trade Nifty options but didn't want to keep cash idle.

He pledged the FD to his broker as collateral. The broker accepted it at 90% value (₹9 lakh margin). Anand could now sell options worth up to ₹9 lakh in margin requirement.

His FD continued earning 7.5% interest. His broker charged him 2% for using the collateral facility. Net cost: 2% per annum on the margin used.

For a short-term trade of 15 days:
- Margin used: ₹3 lakh
- Cost: ₹3,00,000 × 2% × (15/365) = ₹246

Compare this to keeping ₹3 lakh in cash, which would have earned nothing.

The trick works only if:
- Your FD interest covers the broker's fee
- You don't over-leverage
- You understand the FD is locked until you release the pledge

---

## The SEBI Rule That Changed Everything

In 2021, SEBI implemented a rule that shook the market: **Trading members cannot carry forward clients' positions without collecting at least 50% cash component of the margin.**

Earlier, traders could pledge shares worth ₹2 lakh and trade with full ₹2 lakh margin. The broker held the shares but didn't need actual cash.

The new rule required that at least 50% of the total margin must be in cash. The remaining 50% could be collateral.

For a margin requirement of ₹1,00,000:
- Cash needed: ₹50,000
- Collateral (shares, FDs, etc.): ₹50,000

This reduced leverage significantly. Many traders who relied entirely on pledged shares found their positions being closed because they didn't have enough cash.

A friend of mine with ₹1.3 crore in shares couldn't trade after this rule. His entire margin was shares. He needed to bring in ₹65 lakh in cash just to maintain his positions. He didn't have it.

---

## The Expiry Day Trap

Options sellers love to collect small premiums at the start of the month and watch them decay. The last few days before expiry, the time value collapses. It seems like easy money.

But expiry day carries special margin requirements. The exchange increases margins to account for the volatility of the final hours.

For index options on expiry day:
- Short options at 1% away from the current price might require **40-60% margin** of the contract value
- At 2% away: 25-35%
- Beyond 3%: Standard margin applies

This is why some traders who sell far-OTM options for tiny premiums get destroyed. They sold a 22,000 put when Nifty was at 22,200, collecting ₹10 premium. On expiry day, if Nifty drops to 22,050, that put is now worth ₹50. The loss is ₹2,000 per lot. The margin requirement jumps to 50% of the contract value. They are forced to exit at a loss.

The lesson: **Selling options for very small premiums is not free money.** The margin machinery will catch you if the market breathes in your direction.

---

## Leverage: The Double-Edged Sword

Margin allows leverage. With ₹1,09,250, you sold a Nifty call covering ₹11,00,000 worth of exposure. That's roughly 10x leverage.

If Nifty stays below 22,500, you keep the ₹2,500 premium and release the margin. Your return on capital: ₹2,500 / ₹1,09,250 = 2.3% in one week.

But if Nifty rises 2% to 22,440, your option goes from OTM to nearly ATM. The premium jumps from ₹50 to perhaps ₹180. Your loss: (₹180 - ₹50) × 50 = ₹6,500. That's 5.9% loss on capital, for a 2% move in the underlying.

If Nifty rises 4% to 22,880, your option is deep ITM. Premium ~₹380. Loss: (₹380 - ₹50) × 50 = ₹16,500. That's 15% loss on capital, for a 4% move.

The leverage multiplies both gains and losses.

---

## How to Manage Margin

Here are practical steps I have learned from years of trading and teaching:

**1. Never use 100% of your margin capacity**

If the exchange says you can trade up to ₹10 lakh margin, use only ₹5-6 lakh. This gives you room for margin increases when the market moves against you.

**2. Keep cash buffer of 30-40%**

Even with pledged collateral, keep at least 30% of your margin requirement in cash. This handles most margin calls without needing to liquidate positions.

**3. Understand peak margin rules**

SEBI now requires brokers to report your "peak margin" across the day. You cannot use high leverage intraday and bring it down by close. The peak matters.

**4. Close positions before expiry if you don't want delivery**

For stock options, never hold short ITM options into expiry unless you want the shares. Close them on the Thursday before expiry.

**5. Use margin calculators**

Every major broker provides a margin calculator. Before entering a trade, check the margin requirement at different price levels. Plan for adverse moves.

---

## The Machinery Keeps the Market Safe

Margin requirements seem restrictive. They tie up capital. They force liquidations at the worst times.

But they exist for a reason. In 2008, before SPAN margins were fully implemented, some US brokers allowed customers to trade with 50:1 leverage or more. When markets crashed, customers couldn't pay. Brokers went bankrupt. The domino effect reached the entire financial system.

Indian markets have been relatively stable because the margin machinery is conservative. You cannot build massive positions with tiny capital. When the market moves, the system adjusts margin requirements in real-time.

This is not bureaucracy. This is the fire extinguisher that stops small fires from becoming infernos.

---

## A Final Analogy: Margin as Security Deposit

Think of margin like the security deposit you pay when renting an apartment. The landlord (exchange) wants to ensure you won't damage the property (default on losses). They keep your deposit. If you cause damage, they take from the deposit.

But unlike a rental deposit, margin changes every day. If the market becomes more volatile, the landlord asks for more deposit. If it calms down, they return some.

This is not punishment. It is prudent management of risk. The market does not care about your thesis. It does not care about the premium you collected. It only cares about one thing: **can you pay your losses?**

Margin is the answer to that question. It is the machinery that ensures the answer is always "yes".

---

## Key Takeaways

1. **Margin is not a suggestion.** It is a real-time risk calculation that changes as the market moves. Failure to maintain margin leads to automatic position closure.

2. **SPAN margin + Exposure margin** form the total requirement. SPAN looks at portfolio risk; Exposure covers extreme moves.

3. **Pledged securities can be used as collateral**, but with haircuts (discounted values). SEBI requires at least 50% cash component in total margin.

4. **ITM index options settle in cash; ITM stock options trigger physical delivery.** Never hold short stock options ITM into expiry unless you want the shares.

5. **Maintain a buffer of 30-40% cash** over your margin requirement. The machinery works against you when you are fully leveraged—always keep breathing room.