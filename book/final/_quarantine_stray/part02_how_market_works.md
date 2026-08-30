# How This Market Works

---

## Chapter 4: The Engine Room — FII/DII Flows

The single most useful piece of data for understanding what is happening in Indian equity markets on any given day comes from a table that appears on the NSE website a few hours after the close: the institutional cash-market flows. Two numbers — what Foreign Institutional Investors did and what Domestic Institutional Investors did — tell you more than any chart pattern or indicator.

### Reading the Flow

Consider a typical day in October 2024. FIIs sold roughly eight thousand crore rupees worth of Indian equities. DIIs bought roughly the same amount. The market closed almost flat. Two years earlier, in October 2022, the pattern looked similar: FIIs sold twenty-five thousand crore in a single month, DIIs matched the selling, and the market did not crash.

To anyone who learned their market history in the 2000s, this is a surprise. In 2008, when FIIs sold even a fraction of those amounts, the market fell several percent. The difference is scale. In 2008, FIIs dominated Indian market turnover. By 2022, domestic institutions — mutual funds, insurance companies, pension funds — had grown large enough to absorb FII selling.

This shift was not gradual. It happened in a sudden lurch between 2017 and 2021, driven by three forces: the systematic monthly investment of India's mutual-fund SIP culture, the growing allocation of insurance funds to equities, and the return of retail investors who had been scared away by the financial crisis.

### The Declining Significance of a Headline Number

A trader who watches FII flows every day and positions himself opposite the headline direction will be right roughly as often as they are wrong. The reason is that FII activity is itself a reaction, not a cause. FIIs sell when the dollar strengthens against the rupee, when US bond yields rise relative to Indian yields, when global risk appetite falls. Their selling is correlated to these external factors, and the domestic market has learned to decouple from it.

The most instructive example came in 2022. Over twelve months, FIIs sold roughly two lakh crore rupees worth of Indian equities — a figure that, in absolute terms, exceeded any previous record by a wide margin. And yet the Nifty, over that same twelve months, ended roughly flat. Every time FIIs sold, DIIs bought. The market absorbed unprecedented foreign selling without a crash.

This does not mean FII flows are irrelevant. It means they must be read in context. A month of heavy FII selling when DIIs are also selling — that is a danger signal. That happened in June 2024, when both groups sold during the election-day panic, and the market fell more than nine percent intraday. The combination matters more than either number alone.

### The F&O Positioning Layer

Cash-market flows are only half the story. FIIs also maintain large positions in index futures and options. Their futures long-short ratio — the proportion of their long futures positions to their short futures positions — is a useful sentiment indicator.

When this ratio moves above seventy percent long, it signals overcrowding and is typically followed by a correction. When it drops below fifty percent long, it signals extreme bearishness and is typically followed by a rally. The ratio works because FIIs, for all their sophistication, are subject to the same crowd psychology as retail traders. When they all pile into one side of the trade, the other side becomes a contrarian opportunity.

Some traders have built simple systems around this single data point: sell when the FII long ratio exceeds seventy, buy when it falls below fifty. The system is too simplistic to follow blindly, but it captures a genuine market dynamic.

---

## Chapter 5: Volatility as a Regime, Not a Number

Most traders think of volatility as a measurement — a number that tells them how much the market is moving. It is better understood as a regime. The difference matters because a regime influences every option price, every strategy, and every risk calculation in ways that a single number cannot capture.

### The VIX Bands

India VIX — the measure of implied volatility priced into Nifty options — has historically traded in three broad bands. Below fifteen, the regime is low volatility. Between fifteen and thirty, it is moderate volatility. Above thirty, it is high volatility, and above forty-five, the regime is crisis.

Each band demands a different approach:

- **Low VIX (below 15):** Option premiums are cheap. Selling options produces a small return per unit of risk. This is the most dangerous time to sell naked options, because a sudden volatility spike — even without a major price move — can double premium values overnight. The correct response is to pair every short option with a long option, creating a spread that cushions the volatility shock.

- **Moderate VIX (15–30):** This is the sweet spot for option selling. Premiums are high enough to produce meaningful returns but not so high that they reflect imminent crisis risk. Most of the strategies described in this book work best in this band.

- **High VIX (above 30):** Premiums are very high, but the risk of a tail event is elevated. This is a time to reduce position sizes and increase hedging. The high premium creates a temptation to sell aggressively — a temptation that has destroyed many traders who entered during the panic of March 2020.

### The Falling-VIX Signal

One of the most reliable regime indicators is the behaviour of VIX when the market falls. If VIX rises during a market decline, it confirms the selling is driven by fear and may continue. If VIX falls during a decline, it suggests the selling is technical (profit-booking, position-squaring) and likely to stabilise.

This pattern played out repeatedly in 2022. Every time Nifty had a sharp intraday fall, traders would check VIX. If VIX was also falling, they knew the dip was likely to be bought. If VIX was spiking, they knew the selling would probably accelerate.

### IV Rank and Percentile

Two related concepts are essential for option traders. Implied Volatility Rank tells you where current IV sits relative to its range over the past year. Implied Volatility Percentile tells you the percentage of days over the past year that IV was lower than today's level.

When IV Rank is below twenty percent, premiums are historically cheap, and buying options — or avoiding short options — makes sense. When IV Rank is above eighty percent, premiums are historically expensive, and selling options offers a favourable risk-reward ratio.

---

## Chapter 6: Reading the Option Chain

The option chain — the table of available strikes and their bid-ask prices, open interest, and implied volatility — is the single richest source of market information available to a trader in real time. A skilled reader can extract from it not just where the market *might* go, but where the largest and most sophisticated participants have positioned themselves.

### Max Open Interest as Crowd Consensus

The strike with the highest open interest for puts and the strike with the highest open interest for calls are, in aggregate, the market's best guess at two critical levels. The max-OI put strike tends to act as support; the max-OI call strike tends to act as resistance. This is not because these levels have any technical significance. It is simply because the largest concentration of option sellers will defend their strikes.

Consider a typical expiry cycle. If the max OI for puts is at 24,000 and the max OI for calls is at 25,000, the market is likely to oscillate within this range. If it approaches 24,000, the put sellers will begin hedging by buying futures, creating support. If it approaches 25,000, the call sellers will hedge by selling futures, creating resistance.

### The Breakeven Rule

An option seller's effective breakeven is not the strike price. It is the strike plus or minus the premium received. A trader who sells the 24,000 put for 200 rupees has a breakeven of 23,800 — giving them a 200-point cushion before they begin to lose money.

This simple arithmetic — strike minus premium received gives your true support level — is the foundation of every option-selling strategy. It also explains why markets sometimes behave strangely near expiry: the sellers' breakeven level acts as a magnetic floor or ceiling.

### Positioning Asymmetry

When the open interest is heavily tilted to one side — for instance, when everyone has written calls and no one has written puts — the market is positioned for an upside surprise. If the market rallies, the call sellers must cover, and their covering fuels further upside. This asymmetry is the mechanism behind many of the sharp, unexpected rallies that happen on expiry days.

An experienced option seller reads the chain looking for asymmetry. If the put side is virtually unwritten and the call side is heavily populated, the risk of a sharp rally is elevated. If both sides are roughly balanced, the market is expected to stay within its range.

---

## Chapter 7: Microstructure — Gaps, Expiries, and the Last Half-Hour

The daily routine of the Indian equity market has its own rhythms and quirks that are invisible to anyone who only looks at closing prices. Understanding these rhythms is essential for both directional trading and option positioning.

### Gap Taxonomy

A gap-up opening — where Nifty opens significantly higher than the previous day's close — can mean very different things depending on how it behaves in the first thirty minutes.

- **A gap up that sustains:** The market opens higher and stays higher through the morning. This signals genuine buying interest. The gap usually represents new institutional flows or a positive global cue.

- **A gap up that fades:** The market opens higher but quickly drifts back toward the previous close. This signals distribution. Someone is using the gap as an exit, and the underlying demand is absent.

- **A gap down that sustains:** The mirror image of the first case; genuine selling pressure.

- **A gap down that recovers:** The most instructive pattern of all. A sharp gap-down opening that is bought within the first hour is almost always a short-covering catalyst. The early sellers who created the gap are caught wrong-footed, and the covering of their positions can produce a remarkable intraday reversal.

### Expiry Anatomy

The behaviour of the market on expiry days — particularly on Thursdays, which are the weekly expiry for Nifty — follows a script that repeats with surprising regularity.

In the morning, the market feels tentative. Option writers who have collected premium all week are watching their positions nervously. By midday, if the market is near the max-OI strikes, the writers feel safe. Around 2:30 PM, volumes pick up sharply as traders who have been holding positions all week decide whether to roll them to the next series or let them expire. The last hour of expiry is when the day's largest moves typically happen.

The weekly-expiry system introduced around 2020 changed the rhythm. Before weekly expiries, traders had a full month to be right or wrong. With weekly expiries, the cycle compresses to seven days — which means faster theta decay for sellers and more frequent decision points for everyone.

### Last-Half-Hour Dynamics

A pattern that appears across years of transcript data is that the last thirty minutes of the trading session — and especially the last fifteen — are dominated by institutional flows rather than retail flows. A well-known trader aphorism captures this: "Amateurs open the market, professionals close it."

When you see a sharp move in the last half-hour, it is almost always institutional. A late-day rally suggests institutional accumulation; a late-day sell-off suggests institutional distribution. The morning session, by contrast, is shaped by overnight global cues and retail positioning, making it less reliable for directional reads.

A corollary: if the market rallies in the morning but fades in the last hour, the rally was probably a retail-driven reaction to positive news, and the fade was institutional selling into that strength. This "sell the rally" pattern is one of the most reliable signals of a market that is struggling to advance.

---

*End of Part II*