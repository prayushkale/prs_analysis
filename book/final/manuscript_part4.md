# Part IV: The Strategy Library

*Each strategy in this section follows a consistent structure: construction → breakevens → best regime → adjustments → risk boundary.*

## Chapter 13 — The Seller's Edge: Short Straddles & Strangles

### The ATM Short Straddle

**Construction:** Sell one ATM call + sell one ATM put at the same strike and expiry.

**Logic:** The market will not move enough to exceed the combined premium collected. The seller profits as long as the underlying stays within (strike − combined premium) on the downside and (strike + combined premium) on the upside.

**Example:** Nifty at 24,000. ATM call premium ₹350, ATM put premium ₹300. Combined premium = ₹650. BreakEven range = 23,350 to 24,650. If Nifty stays within this range by expiry, the seller keeps the full ₹650. Maximum profit = ₹650 × lot size. Maximum loss = theoretically unlimited (in practice, limited by stop-loss or adjustment).

**Best regime:** VIX 15–30. At low VIX, the combined premium is too small to justify the risk.

**Adjustments:** When one side is threatened, buy that side's option as a hedge (converting the short straddle into a short strangle with a bought wing). Do NOT add to the losing side — add a hedge.

### The Short Strangle

**Construction:** Sell OTM call + sell OTM put at different strikes (both OTM).

**Logic:** Same as straddle but with a wider, safer breakeven range and lower premium. Preferred by experienced sellers.

**Example:** Nifty at 24,000. Sell 24,500 call for ₹150 + sell 23,500 put for ₹120 = ₹270 credit. Breakeven: 23,230 to 24,770. Safer than straddle (wider range) but lower return.

**Best regime:** High IV (VIX > 25). The wide breakeven makes it resilient to sharp intraday moves.

### The Deep-ITM Straddle + Far-Month Put (Credit-Funded Disaster Hedge)

**Construction:** Sell a deep-ITM near-month straddle (call is deep ITM, put is deep OTM) + buy a far-month OTM put. The credit from the sale finances the far-month put.

**Logic:** The deep-ITM near-month call captures directional exposure; the far-month put caps the tail risk. As long as the net is a credit, the seller has zero cash at risk.

"This is my preferred approach for long-term bullish views," Dhanraj said in a key video. "You enter a credit trade that has a disaster hedge built in. The worst case is the difference between the two put strikes minus the credit — and it is fully funded."

---

## Chapter 14 — Controlled Direction: Spreads & Ratio Spreads

### Bull Call Spread (Debit)

**Construction:** Buy ATM call + sell OTM call (1:1 ratio).

**Logic:** Pay debit for the ATM call; fund it partially by selling the OTM call. Max profit = (difference between strikes − debit). Max loss = debit paid.

**Example:** Nifty 24,000 call costs ₹350. Sell 24,500 call for ₹150. Net debit = ₹200. Max profit at 24,500 = (500 − 200) = ₹300. Loss capped at ₹200.

### Bear Put Spread (Debit)

**Construction:** Buy ATM put + sell OTM put (1:1 ratio).

**Logic:** Mirror of bull call spread for bearish views.

### Call Ratio Spread (Credit)

**Construction:** Buy 1 ATM call + sell 2 (or 3) OTM calls.

**Logic:** Net credit on entry. Profit if the market stays below the short strikes. Loss if the market gaps through the short strikes (unlimited at expiry).

"Heading mildly bullish, this is the structure," Dhanraj said. "You collect a small credit with a wide safety zone. The risk is a sharp breakout above your short strikes."

### Put Ratio Spread (Credit)

**Construction:** Buy 1 ATM put + sell 2 (or 3) OTM puts.

**Logic:** Net credit on entry. Best when mildly bearish.

---

## Chapter 15 — Time Is the Trade: Calendar Spreads

### Call Calendar

**Construction:** Sell near-month call + buy same-strike far-month call.

**Logic:** The near-month call decays faster than the far-month call. Profit if the underlying stays near the strike (both calls lose time value, but the near-month loses more). Loss if the underlying moves sharply away or toward.

"The best time to use a calendar," Dhanraj taught, "is after a very big move. After a 1,000-point rally in Nifty, the market is likely to consolidate. That consolidation is perfect for calendars — the near-month decays fast, the far-month holds value."

### Put Calendar

**Construction:** Sell near-month put + buy same-strike far-month put.

**Logic:** Same as call calendar but for mild bearish or sideways expectations.

### Calendar with Event Risk (Budget Strategy)

**Construction:** Before a binary event (budget, election), sell near-month OTM call + buy far-month OTM call.

**Logic:** The event (budget) makes near-month IV high. After the event, IV collapses. The near-month IV collapse + theta decay benefit the short leg, while the far-month holds more value.

---

## Chapter 16 — Butterflies & Condors

### Call Butterfly

**Construction:** Buy 1 OTM call (low), sell 2 ATM calls, buy 1 OTM call (high). Net debit.

**Logic:** Profit if the underlying settles at the middle strike. Max loss = net debit. Max profit = distance between lower and middle strike − debit.

**Best regime:** Low VIX (<15). When the market is not expected to move much, butterflies collect premium with defined risk.

### Put Butterfly

**Construction:** Buy 1 OTM put, sell 2 ATM puts, buy 1 OTM put. Net debit.

### Iron Condor

**Construction:** Sell OTM call spread (sell lower OTM call + buy higher OTM call) + sell OTM put spread (sell higher OTM put + buy lower OTM put). Net credit.

**Logic:** Profit if the underlying stays between the two short strikes. The iron condor is the safest defined-risk strategy for range-bound markets. "This is the condominium of option strategies," Dhanraj joked. "Everyone lives in a defined space, no one gets evicted suddenly."

---

## Chapter 17 — Portfolio Protection: Hedges That Actually Hedge

### The Nifty BeES + Protective Put

**Construction:** Buy Nifty BeES (ETF equivalent of 1 Nifty lot) + buy a far-dated ATM or slightly OTM put.

**Logic:** The BeES tracks Nifty. The put caps the downside. If Nifty falls below the put strike, the put gains enough to offset the BeES loss.

"This is a zero-risk strategy if held to expiry of the put," Dhanraj explained. "You invest ₹18-20 lakh in BeES, buy a 1-year 24,000 put for about ₹1,000. Your worst case: if Nifty goes to zero, you lose ₹1,000 (the put costs) — but Nifty will not go to zero. The real worst case: if Nifty falls to 24,000, you lose the BeES premium above spot but the put pays for itself. Net? Near zero."

### Correction Ladder

**Construction:** Deploy capital in tranches: 50% at −10% correction, 50% at −20% drawdown.

**Logic:** "Correction = 10% fall. Bear market = 20% fall. Historically, India has had >50% drawdowns only in 2008 (Lehman), ~40% in 2020 (COVID), and ~30% in 2004. Within two years, all recovered." The ladder ensures you buy the bottom, not the falling knife.

### What Is NOT a Hedge

Buying a far-OTM call + selling a far-OTM put for margin reduction is not a hedge. "Most people buy a far OTM call and a far OTM put, and they call it hedging. That is not hedging. That is margin reduction. If the market makes a 1,000-point move, that 100-point OTM call does nothing for you. You are still exposed."

---

## Chapter 18 — Firefighting: Rescue and Adjustment

### The Adjustment Decision Tree (simplified)

Position losing and...
- View still intact → Add a hedge (buy opposite wing).
- View has changed → Close immediately. "I have made my biggest losses by hoping a wrong view would correct itself."
- IV spiking → Sell more premium at the higher IV (the vega trade).
- Size is small → Hold and wait for the view to materialize.
- Size is large → Scale down first, adjust second.

There is an important caveat: "Do not adjust too quickly. An options position has natural range — it can lose ₹10,000 intraday and recover before close. That is noise. Adjust only when the data — not the P&L — tells you the view is wrong."

---

## Endnotes (Part IV)

[^8] Strategy construction tables: The exact premium numbers and breakeven ranges used in examples are for illustration; actual premiums depend on spot level, IV, time to expiry, and lot size. The lot size for Nifty options changed from 75 to 25 in November 2024 (SEBI circular SEBI/HO/MRD/DRMNP/CIR/2024/173), which multipled the notional calculation. All examples use pre-Nov-2024 convention for simplicity; traders must adjust for current lot sizes.