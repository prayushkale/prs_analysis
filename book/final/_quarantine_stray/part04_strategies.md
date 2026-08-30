# The Strategy Library

*Each strategy in this section is presented with its construction rules, breakeven points, risk profile, and the market conditions in which it works best. All returns are expressed as percentages of margin deployed or premium collected, reflecting the typical sizing used by experienced option sellers.*

---

## Chapter 13: The Seller's Edge — Short Straddles and Strangles

The short straddle is the most basic option-selling strategy — and for many traders, the only one they ever need. It consists of selling an ATM call and an ATM put at the same strike price. The seller collects a large upfront premium and profits as long as the underlying stays within a specific range until expiry.

### Construction

- **Short ATM Straddle:** Sell one ATM call + sell one ATM put at the same strike
- **Example (Nifty 25,000):** Sell 25,000 CE (premium ₹200) + Sell 25,000 PE (premium ₹180) = Total premium collected ₹380
- **Breakevens:** Upper breakeven = strike + total premium = 25,380; lower breakeven = strike − total premium = 24,620
- **Max profit:** Total premium collected (₹380 × 75 = ₹28,500 per lot)
- **Margin required:** Approximately ₹80,000–₹90,000 per lot

### When It Works

The short straddle profits from time decay. Every day the market stays within the breakeven range, the options lose value, and the seller's position becomes more profitable. The strategy works best when:

- India VIX is in the 15–30 range (moderate volatility)
- The market is consolidating within a known range
- There is no binary event scheduled (budget, election, RBI decision)

### The Risks

The short straddle has unlimited risk on both sides. A sharp market move in either direction can produce losses that exceed the premium collected. The gamma effect — the acceleration of losses as the market moves toward the breakeven — can make a short straddle feel safe one moment and terrifying the next.

The correct response to a short straddle that is threatened is not to double down. It is to adjust — by rolling one side to a further strike, by adding a hedge, or by taking the loss and re-entering at a more favourable strike.

### The Short Strangle

A short strangle is similar to a short straddle but uses OTM strikes. It collects less premium but has wider breakevens.

- **Short OTM Strangle:** Sell OTM call + sell OTM put at different strikes
- **Example:** Sell 25,500 CE (premium ₹80) + Sell 24,500 PE (premium ₹60) = Total premium ₹140
- **Breakevens:** Upper = 25,640; Lower = 24,360

The strangle gives the market more room to move before the position loses money. The trade-off is lower premium collected — roughly half that of a comparable straddle.

---

## Chapter 14: Controlled Direction — Spreads and Ratio Spreads

A vertical spread involves buying one option and selling another of the same type (both calls or both puts) at different strikes. The purchased option caps the loss on the sold option, creating a position with defined maximum risk.

### Bull Call Spread

- **Construction:** Buy ATM call + sell OTM call
- **Example:** Buy 25,000 CE (₹200) + Sell 25,500 CE (₹80) = Net debit ₹120
- **Max profit:** Spread width (500 points) − net debit (120) = 380 points
- **Breakeven:** Lower strike + net debit = 25,120
- **Max loss:** Net debit paid

The bull call spread profits if the market rises above the breakeven point. It is the defined-risk equivalent of a naked call purchase.

### Bear Put Spread

- **Construction:** Buy ATM put + sell OTM put
- **Example:** Buy 25,000 PE (₹180) + Sell 24,500 PE (₹60) = Net debit ₹120
- **Max profit:** 380 points
- **Breakeven:** 25,000 − 120 = 24,880

### Call Ratio Spread

A call ratio spread involves buying one call and selling two or more calls at a higher strike. The ratio creates a position that profits from a moderate rally but loses if the rally extends too far.

- **Construction:** Buy 1 × 25,000 CE (₹200) + Sell 2 × 25,500 CE (₹80 each)
- **Net credit/flat:** If the premiums offset, the position has zero initial cost (or a small credit)
- **Max profit:** Achieved if Nifty closes exactly at 25,500 at expiry

The ratio spread is the strategy of choice when a trader expects a move but does not believe it will extend beyond a specific level. It is especially useful around support or resistance that has been tested multiple times.

---

## Chapter 15: Time Is the Trade — Calendar Spreads

A calendar spread — also called a horizontal spread — involves buying and selling options of the same strike but different expiries. The seller collects premium from the near-month option and pays it for the far-month option, betting that time decay will work faster on the near-term leg.

### Call Calendar

- **Construction:** Sell near-month 25,000 CE + buy far-month 25,000 CE
- **Example:** Sell June 25,000 CE (₹180) + Buy July 25,000 CE (₹350) = Net debit ₹170
- **Max profit:** If Nifty closes at or near 25,000 at June expiry, the near-month option decays to zero while the far-month option retains significant value

Call calendars work best when the market has recently made a large move and is expected to consolidate. The large move creates elevated IV in the near-term options, which the seller collects; the consolidation allows time decay to erode the near-term premium.

### Put Calendar

The reverse of the call calendar. Sell near-month put, buy far-month put. Best used when the market is expected to maintain support at a level and consolidate.

### Calendar for Binary Events

A variation known as the reverse call calendar is specifically designed for binary events such as budget announcements or elections. The trader sells a far-month option (high IV from event uncertainty) and buys a near-month option that expires before the event. This captures the IV spike without taking event-direction risk.

---

## Chapter 16: Butterflies and Condors

Butterflies and condors are multi-leg strategies that define a profit zone and limit risk on both sides. They are the strategies of choice for traders who expect the market to land in a specific range.

### Call Butterfly

- **Construction:** Buy 1 × lower strike call + Sell 2 × middle strike calls + Buy 1 × upper strike call
- **Example:** Buy 24,800 CE + Sell 2 × 25,000 CE + Buy 25,200 CE
- **Net debit (typically):** Small — the two sold options finance the two bought options
- **Max profit:** Achieved if Nifty closes exactly at 25,000
- **Max loss:** Net debit paid

The butterfly works when the trader has high conviction that the market will land at a specific level by expiry. The premium cost is minimal, and the potential profit is several times the cost.

### Iron Condor

- **Construction:** Sell OTM put + buy further OTM put + sell OTM call + buy further OTM call
- **Example:** Sell 24,500 PE + Buy 24,000 PE + Sell 25,500 CE + Buy 26,000 CE
- **Net credit:** The two sold options collect more premium than the two bought options cost
- **Profit zone:** Between the two short strikes

The iron condor is the go-to strategy in range-bound markets with moderate volatility. It profits from time decay while capping loss exposure on both sides.

---

## Chapter 17: Portfolio Protection — Hedges That Actually Hedge

A hedge is a position taken to offset the risk of another position. The simplest hedge — buying a put against a long equity portfolio — is also one of the most expensive, because it must be constantly renewed.

### The BeES + Protective Put

For a long-term equity portfolio, the most capital-efficient hedge is the Nifty BeES (an ETF that tracks Nifty), combined with a long-dated put option.

- **Step 1:** Buy Nifty BeES equal to one Nifty lot (the position is long the market)
- **Step 2:** Buy a far-dated ATM put on Nifty (the hedge)

The structure works because the BeES positions and the put positions are financed out of different capital. The put premium acts as an insurance cost; if the market falls, the put pays out enough to offset the loss on the BeES. The cost of the put can be partially offset by selling an OTM call against it.

### What Is Not a Hedge

Buying a far-OTM option for a few rupees and calling it a hedge is not a hedge. It is a lottery ticket. A real hedge either covers the risk exposure or it does not. A 27,000 put on Nifty at 25,000 is not a hedge — it is so far out of the money that it will expire worthless unless the market makes an unprecedented move.

A related error is the "margin-reduction hedge" — buying a far-OTM option not to reduce risk but to reduce the margin required for a short position. This is a dangerous practice because it creates the illusion of protection without providing it.

---

## Chapter 18: Firefighting — Rescue and Adjustment

No trading strategy works perfectly every time. The ability to recognise when a position is under threat and to adjust it — rather than letting it run to its maximum loss — is the most important practical skill an option seller can develop.

### The Adjustment Ladder

When a short option position moves against the seller, there are several levels of response:

- **Level 1 — Roll:** Close the threatened option and open a new one at a further strike, using the time value of the current option to fund the roll. This buys time for the market to recover.

- **Level 2 — Add a Hedge:** If the market is approaching your breakeven, add a complementary position — buy a put if the call side is threatened, buy a call if the put side is threatened.

- **Level 3 — Reverse:** If the original view is clearly wrong, close the entire position and open the opposite position. This is the hardest to do emotionally but sometimes the correct action.

- **Level 4 — Accept the Loss:** If the position is deeply underwater and the market shows no sign of reversing, accept the loss and preserve the remaining capital for the next trade.

### The Reconstruction Trade

One of the most elegant firefighting techniques is the reconstruction trade. Suppose a trader sold a short straddle at 25,000 and Nifty rallies to 25,500. The call side is losing money, but the put side is now very profitable. The trader can buy back the put at a tiny profit, use that profit to fund rolling the call to a higher strike, and effectively reconstruct the straddle at the new level — giving themselves room to recover.

This technique works because the market typically oscillates rather than trends in a straight line. A move that threatens one side of a straddle almost always makes the other side more profitable.

### When Not to Adjust

The most common mistake in firefighting is adjusting too early, or adjusting based on intraday moves that reverse within hours. A general rule: do not adjust a short option position on an intraday move alone. Give the market at least one full trading day to show you that the move is structural, not transient.

---

*End of Part IV*