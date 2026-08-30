# Chapter 8: Why Derivatives Exist

On 20 April 2020, the world watched a financial impossibility. The May futures contract for West Texas Intermediate crude oil — one of the most traded commodities on the planet — settled at **negative $37.63 per barrel** by the close. For a few surreal minutes, producers were paying buyers to take delivery.

The event was not a glitch. It was a lesson in **what derivatives are, how they work, and why fail-safe assumptions can kill you when you ignore their structure**. Futures contracts obliged holders to take physical delivery of crude oil into storage tanks that were already full. Traders who had bought May futures expecting to sell them before expiry discovered that there were no buyers for the actual barrels. To get out, they had to pay.

That day separated two kinds of market participants: those who understood what a futures contract *actually* was, and those who treated it as a glorified bet. This chapter is about how you join the first group.

## What Is a Derivative?

A derivative is a financial contract whose value is derived from an underlying asset — a stock, an index, a commodity, a currency, or even an interest rate. The contract itself is the tradable instrument; the underlying is what the contract references.

In India, the largest derivative market by volume is the NSE's Futures & Options segment, where contracts reference the Nifty 50, Bank Nifty, Fin Nifty, and hundreds of individual stocks. The daily turnover in NSE's F&O segment regularly exceeds ₹60 lakh crore — roughly four times the daily turnover of the entire Indian cash-equity market. That ratio tells you almost everything about how modern markets work: the tail (derivatives) wags the dog (the underlying).

## The Bridge from Forwards to Futures

Before exchanges existed, forwards were private contracts between two parties. A wheat farmer and a miller would agree in March: in June, the farmer would deliver 100 tonnes of wheat at ₹2,000 per quintal. No money changed hands at signing. The price was locked. Both parties slept easier, each having eliminated the price risk they were least equipped to handle.

But forwards had two problems:
- **Counterparty risk**: if the farmer defaulted or the miller went bankrupt, the other side had no recourse beyond a lawsuit.
- **No exit**: the contract was custom-made and illiquid. If the miller needed to close early, there was no one to sell the contract to.

Futures solve both problems by standardising the contract and routing it through a central clearing counterparty (the Clearing Corporation of India or NSE Clearing). Every futures contract has fixed specifications: lot size, maturity date, tick size. And the clearing house becomes the buyer to every seller and the seller to every buyer, guaranteeing performance through a daily margin mechanism called **mark-to-market** (MTM).

## Mark-to-Market: The Daily Reckoning

Here is where most retail traders get tripped up. A futures position is not like buying a stock, where you pay the full price once and wait. Every trading day, the exchange calculates the day's profit or loss on your futures position and transfers it to or from your account in cash — before the position closes.

Consider an example:

**Date: 5 June 2022**  
Buy 1 lot Nifty futures (lot size 75) at 16,500.  
Margin required: approximately ₹1.50 lakh (roughly 8–10% of the contract value of ₹12,37,500).

| Day | Nifty Future Close | Daily P&L | Cumulative P&L | Cash Outflow/Inflow |
|-----|-------------------|-----------|----------------|---------------------|
| 5 Jun | 16,500 (entry) | — | — | Margin paid: ₹1.50 lakh |
| 6 Jun | 16,680 | +180 pts × 75 = +₹13,500 | +₹13,500 | ₹13,500 credited to account |
| 7 Jun | 16,450 | −230 pts × 75 = −₹17,250 | −₹3,750 | ₹17,250 debited from account |
| 8 Jun | 16,600 | +150 pts × 75 = +₹11,250 | +₹7,500 | ₹11,250 credited |
| 9 Jun | 16,200 (close position) | −400 pts × 75 = −₹30,000 | −₹22,500 | −₹30,000 debited; margin released |

**Net result**: loss of ₹22,500 (300 points × 75). But notice the *pattern*. On day 6 the account gained cash even though the position was still open. On day 7 it lost cash. Each day's settlement was real, not notional. This is MTM.

The consequence is brutal for undercapitalised traders: a sequence of daily losses can deplete the cash balance *before* the position reaches its expiry. The exchange does not wait for the final reckoning. It collects losses daily. This is why futures are said to be cash-settled daily — the option seller's dream (margin against collateral) does not apply here.

## Three Kinds of Participants

Derivative markets need all three groups to function:

**Hedgers** are the reason derivatives exist. A mutual fund holding ₹100 crore of equity wants protection against a market fall. It can buy index put options. An exporter expecting dollar receipts in three months wants protection against rupee appreciation. It can sell USD-INR futures. Hedgers transfer risk they do not want.

**Speculators** take on that risk in exchange for potential profit. They are not gambling — they are expressing a view backed by research, positioning, and risk management. They provide liquidity and depth.

**Arbitrageurs** exploit price discrepancies between related instruments. When Nifty futures trade at a premium to the spot Nifty that exceeds the cost of carry, an arbitrageur buys spot Nifty 50 stocks (or Nifty BeES) and sells the futures, locking in a risk-free return. Arbitrage activity keeps prices aligned across markets.

In India, FIIs are typically hedgers or speculators depending on the regime, while the vast majority of retail participants are speculators — a fact that becomes relevant in Chapter 27, when we examine the SEBI data that shows 93% of individual F&O traders lose money.

## Forward vs Future at a Glance

| Feature | Forward | Future |
|---------|---------|--------|
| **Trading venue** | OTC (bank/counterparty) | Exchange (NSE/BSE) |
| **Standardisation** | Custom | Fixed lot, expiry |
| **Counterparty risk** | Direct — both parties | None — clearing house |
| **Daily settlement** | No | Yes (MTM) |
| **Liquidity** | Zero (custom) | Deep in indices |
| **Margin** | None or negotiated | SPAN + Exposure |
| **Regulation** | Light | Full (SEBI) |
| **India availability** | Only for corporates/FIIs | All traders |

## Why This Matters Before You Move to Options

Futures are the simplest derivative — linear payoff, no time decay, no volatility input. If you cannot manage a futures position *through its MTM cashflows*, you should not be trading options. The option seller's margin mechanism is more forgiving (losses rest against collateral until booked), but the underlying risk mathematics is identical.

The crude oil crash of April 2020 was a futures settlement event. The lesson spread to option sellers in May 2020, when the Franklin Templeton debt-fund closure — the subject of Chapter 12 — revealed that even collateral can evaporate overnight.

## Key Takeaways

- A derivative is a contract whose value depends on an underlying asset. It is not the asset itself.
- Futures are standardised, exchange-traded forwards with daily MTM settlement and zero counterparty risk.
- MTM means profit or loss is realised in cash every day, not at expiry. Manage your cash balance, not just your position P&L.
- Derivatives serve three roles: hedgers transfer risk, speculators provide liquidity, arbitrageurs keep prices honest.
- The same risk math applies whether you hold futures or sell options. Understand MTM before you trade either.