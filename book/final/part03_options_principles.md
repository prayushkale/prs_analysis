# Options from First Principles

---

## Chapter 8: Why Derivatives Exist

Derivatives — contracts whose value derives from an underlying asset — were not invented by exchanges. They are as old as commerce itself. In seventeenth-century Japan, rice farmers sold forward contracts on their harvest to lock in prices and protect themselves from a bad season. In the Netherlands during the tulip mania of the 1630s, people traded options on tulip bulbs — the right to buy or sell a bulb at a fixed price — without realising they were participating in what would later be known as option trading.

Every derivative serves the same fundamental purpose: it transfers risk from someone who wants less of it to someone who is willing to accept more of it in exchange for compensation.

### The Forward Contract

The simplest derivative is a forward contract. Two parties agree today that one will buy and the other will sell an asset at a predetermined price on a future date. No money changes hands until the settlement date. The buyer bets the price will rise; the seller bets it will fall.

The problem with forwards is counterparty risk. If the price moves sharply against one party, they may not honour the contract. This risk led to the development of futures — standardised forward contracts traded on an exchange with a clearing corporation that guarantees performance.

### The Futures Contract

A futures contract is a forward that has been industrialised. The exchange defines the contract size, the expiry cycle, and the settlement procedure. Every night, profits and losses are settled in cash — a process called marking to market. This eliminates the build-up of large, unmanageable losses that could cause a default.

Futures traders are divided into three categories:

- **Hedgers** use futures to protect against adverse price movements. An exporter who will receive dollars in three months can sell dollar futures today, locking in the exchange rate. If the dollar falls, the profit on the futures offsets the loss on the export revenue.

- **Speculators** use futures to bet on price direction. They have no underlying exposure; they are simply trying to profit from correctly predicting a price movement.

- **Arbitrageurs** exploit price differences between related markets. They buy in one market and sell simultaneously in another, locking in a risk-free profit. Their activity keeps prices consistent across markets.

### The Stock Index Future

A stock index future such as Nifty or Bank Nifty is a futures contract on a portfolio of stocks. It allows a trader to take a directional view on the entire market — or to hedge a portfolio of equities — without buying or selling individual stocks.

The relationship between the index future and the index spot is governed by the cost-of-carry model. In normal markets, the future trades at a premium to the spot, because the future price includes the interest cost of holding the stocks until expiry. In periods of extreme bearishness, the future can trade at a discount — a condition called backwardation that signals intense short-term selling pressure.

---

## Chapter 9: Calls and Puts

A call option gives the buyer the right, but not the obligation, to buy the underlying asset at a specified price (the strike) on or before a specified date (the expiry). A put option gives the buyer the right to sell.

### Buying vs Selling

The buyer of an option pays a premium — a non-refundable fee — for the right to exercise the option if it becomes profitable. The seller (sometimes called the writer) receives the premium and accepts the obligation to fulfill the contract if the buyer exercises.

Consider a Nifty 25,000 call option trading at ₹200. The buyer pays ₹200 per lot (the lot size is 75, so ₹15,000 per contract) for the right to buy Nifty at 25,000. If Nifty is above 25,000 at expiry, the buyer can exercise and capture the difference. If Nifty is below 25,000, the option expires worthless and the buyer loses the entire premium.

The seller, by contrast, collects ₹15,000 and hopes that Nifty stays below 25,000. If it does, they keep the entire premium as profit. If Nifty rises above 25,000, the seller begins to lose money — and the loss increases point for point with the index rise.

This asymmetry — limited loss for the buyer, unlimited loss for the seller — is the defining feature of option markets. It is also why selling options is fundamentally an insurance business, while buying options is fundamentally a lottery: the buyer pays a small premium for a chance at a large payoff; the seller collects many small premiums in exchange for accepting the risk of rare but large payouts.

### ITM, ATM, and OTM

Options are classified by their relationship to the current market price. An in-the-money (ITM) option has intrinsic value: a call with a strike below the market price, or a put with a strike above it. An at-the-money (ATM) option has a strike equal to or very near the market price. An out-of-the-money (OTM) option has no intrinsic value.

The premium of an option consists of two components: intrinsic value (the amount by which the option is in the money) and time value (everything else). An OTM option has no intrinsic value — its entire premium is time value. This time value decays as expiry approaches, and it is this decay that option sellers are harvesting.

### Exercise and Assignment

When an option buyer exercises their right, the seller is assigned an obligation. The seller does not choose when this happens; the exchange assigns randomly among all sellers of that option.

At expiry, all ITM options are automatically exercised. This means that a trader who sold a put that expires ITM will automatically be assigned a long futures position — an outcome they may not have intended. Managing expiry risk — ensuring that no position is unintentionally exercised or assigned — is a critical skill for option sellers.

---

## Chapter 10: The Greeks, Demystified

Option prices move in response to changes in several underlying variables. The directional sensitivity is measured by a set of numbers called the Greeks.

### Delta

Delta measures how much an option's price changes for a one-point move in the underlying. A call with a delta of 0.5 will rise by roughly ₹0.50 for every one-point move in Nifty. An ATM option typically has a delta near 0.5; a deep ITM option has a delta approaching 1.0; a deep OTM option has a delta near zero.

Delta also represents the probability that the option will expire ITM, according to a simplified model. An option with a delta of 0.3 has roughly a thirty percent chance of expiring in the money.

### Gamma

Gamma measures the rate of change of delta. It is the most important Greek for option sellers to understand, because it tells them how quickly their directional exposure will change as the market moves.

When you sell an option, you are short gamma. A short-gamma position benefits when the market is quiet — delta stays where it was, and your position does not require adjustment. But if the market makes a large move, your delta exposure changes more rapidly than you might expect. The gamma effect is why option sellers who appear to have a well-hedged position can suffer large, unexpected losses during a sharp breakout.

Gamma is highest for ATM options and declines as you move away from the money. It is also highest for short-dated options — which is why near-expiry positions can behave unpredictably.

### Theta

Theta measures time decay — how much value an option loses each day as expiry approaches. For an option seller, theta is the most friendly Greek. Every day that passes with the market staying within the expected range earns the seller a small profit.

Theta is highest for ATM options close to expiry. This is why option sellers prefer to sell near-expiry options: the decay accelerates dramatically in the final weeks and days.

### Vega

Vega measures sensitivity to changes in implied volatility. An option with a vega of eight will gain or lose roughly eight rupees for every one-point change in implied volatility.

Vega is important because it introduces a second dimension of risk. A short option position that is perfectly hedged against directional moves is still exposed to volatility risk. If implied volatility spikes — as it often does during a crash — even a well-positioned short option can lose money.

The practical implication is that option sellers should avoid selling options when IV is low (because they collect little premium per unit of vega risk) and should consider selling when IV is elevated (because they collect more premium for the same vega exposure).

### Rho

Rho measures sensitivity to interest rates. For short-dated options, this effect is negligible, and most Indian retail traders ignore it. For long-dated options — those with expiries a year or more away — rho can become significant.

---

## Chapter 11: Implied Volatility — The Real Price of Options

If options were only about delta and theta, the market would be relatively simple. What makes option trading interesting — and profitable — is the interplay with implied volatility.

### IV vs Historical Volatility

Historical volatility measures how much the underlying has actually moved in the past. Implied volatility measures how much the market expects it to move in the future. The difference between them is a measure of market sentiment.

When IV is above historical volatility, options are expensive relative to the actual movement of the underlying. This typically happens during periods of uncertainty — before elections, budget announcements, or central-bank meetings. The premium reflects not the movement that actually happens but the movement that is feared.

When IV is below historical volatility, options are cheap. This happens during periods of complacency — when the market has been quiet for an extended time and traders have stopped buying protection.

### The IV Smile and Skew

For a given expiry, options at different strikes trade at different implied volatilities. OTM puts typically trade at higher IV than ATM calls, especially in Indian markets. This is called the skew — a persistent premium for downside protection that reflects the market's asymmetric fear of crashes.

The existence of the skew has a practical implication: selling OTM puts is more profitable, per unit of risk, than selling ATM calls, because the put premiums include a "fear premium" that the call side does not have.

### IV Collapse

One of the most profitable scenarios for an option seller is an IV collapse — a situation where implied volatility falls sharply after a period of elevated uncertainty. This happens after elections, after budget announcements, and after major economic data releases. The event passes, the uncertainty resolves, and the option premiums deflate rapidly.

A trader who sold options at elevated IV before a binary event, and who survives the event itself, can capture profits from two sources: the directional move (if it is favourable) and the IV collapse (which multiplies the premium decline).

---

## Chapter 12: Margins, Collateral, and the Machinery

Options trading in India operates within a framework of margin requirements that have evolved significantly over the past decade. Understanding this framework is essential for planning position sizes and managing risk.

### SPAN and Exposure Margin

Every option position in India requires two types of margin. SPAN margin (Standard Portfolio Analysis of Risk) covers the risk of a one-day extreme move based on a statistical model. Exposure margin is an additional buffer imposed by the exchange for short option positions.

For a short ATM Nifty straddle — selling both an ATM call and an ATM put — the total margin requirement is typically in the range of eighty thousand to one lakh rupees per lot (75 units). This margin is returned when the position is closed.

### The 50% Cash Rule

In late 2024, SEBI introduced a requirement that at least fifty percent of the margin for option positions must be maintained in cash — not in collateral such as shares or mutual funds. This rule dramatically reduced the amount of leverage that traders could obtain from their existing investments.

The rule was designed to curb the growth of what the regulator called "gambling-like behaviour" in the options market. Its effect was to push many leveraged traders — particularly those who had been using stock holdings as collateral to fund option positions — to reduce their position sizes or exit entirely.

### The Lot-Size Mechanism

Nifty option contracts are standardised in lots of 75 units. Each lot controls 75 shares of the underlying index. When Nifty is at 25,000, the notional value of one lot is roughly nineteen lakh rupees — but the margin requirement to sell an option is only a fraction of that.

The lot size has changed over time. In 2021, it was 50; earlier, it was 75 for some series and 25 for others. These changes affect the capital required to trade and the margin-efficiency of various strategies.

### Settlement and Exercise

All index options in India are cash-settled. At expiry, the difference between the settlement price and the strike price is paid in cash; no actual shares or index units change hands. This means that a put seller who is assigned does not receive shares — they receive a cash debit equal to the loss on the option.

Physical settlement applies to stock options (options on individual equities). A trader who exercises a stock call option must actually buy the shares, and the seller must deliver them. Physical settlement introduces additional operational complexity, and most retail traders avoid stock options for this reason.

---

*End of Part III*