# Chapter 27: The Regulator's Dilemma

No regulator in the world has a harder job than the Securities and Exchange Board of India (SEBI) in the post-2020 era. On one hand, the explosion in retail F&O trading — encouraged by zero-brokerage platforms, pandemic-era liquidity, and the sheer convenience of betting on index moves through a mobile phone — has turned options into a national pastime. On the other hand, every piece of data SEBI publishes confirms the same grim statistic: the vast majority of retail participants lose money, often catastrophically. The regulator must protect these participants without killing the derivatives market that provides liquidity, price discovery, and hedging for the institutions that make the real economy function. This chapter traces the arc of that dilemma from 2020 to 2026.

## The Study That Changed Everything

SEBI's 2023 study on F&O trading laid the problem bare. Across the financial year ended March 2023, **89% of individual F&O traders lost money**. The study was updated for FY2024 with an even sharper result: **93% of individual traders lost money, and only 1% made more than ₹1 lakh in net profit per annum**. Worse, the bottom 3.5% of traders lost an average of ₹28 lakh per year. These were not market-makers, hedgers, or institutions — they were retail individuals, mostly trading in their own names, many of them students, salaried professionals, and small business owners.

> "Nine out of ten people always lose money — professional traders are not those nine. That is the difference."

The report created a political storm. Media headlines called options trading a "national addiction." The finance ministry directed SEBI to act. But the data also had a problem: it could not distinguish between pure speculators, hedgers (who may lose premium on protective puts while their cash portfolio gains), and traders using options as part of a diversified strategy that includes cash-market positions. A trader who buys a ₹5,000 put to protect a ₹10 lakh equity portfolio and lets it expire worthless appears in the "100% loss" column, but their real portfolio is protected. Nonetheless, the headline numbers were too stark to ignore, and SEBI prepared a comprehensive response.

## The October 2024 Framework

At its board meeting on 30 September 2024, SEBI approved a six-point framework to curb speculative retail F&O activity. The measures, phased from 20 November 2024, included:

1. **One weekly expiry per exchange.** Previously, Monday was Midcap Select, Tuesday was FinNifty, Wednesday was Bank Nifty, Thursday was Nifty, and Friday was Sensex — five expiries across the week. The new rule limited each exchange to one weekly expiry, compressing the event-based speculation cycle.

2. **Increased lot sizes.** Nifty options lot size was raised from 25 to 75 effective 20 November 2024, tripling the capital required to enter a single-lot position. A trader who previously needed ₹2,500 for a far-OTM call now needed ₹7,500. The intent: push the smallest speculators out of the market. The effect: traders who stayed shifted to even farther-out-of-the-money strikes to keep absolute premium affordable, which further reduced their probability of profit.

3. **Additional expiry-day margin (2% extreme-loss margin).** Option sellers on expiry day faced an additional margin charge that eliminated the calendar-spread benefit for intraday positions on expiry Thursdays. This specifically targeted the short-straddle strategy — by far the most popular retail option-selling approach — which relied on thin margins to deploy large quantities of contracts.

4. **Upfront premium collection.** Brokers were required to collect option premiums from buyers upfront, eliminating the practice of funding option purchases with margin from other positions.

The market's immediate reaction was a sharp drop in volumes. Index-options premium turnover, which had peaked at roughly ₹4 lakh crore per month, dropped by more than half within six months. Active retail F&O trader counts fell by approximately 18–20%. The cooling was dramatic, and SEBI had achieved its stated goal.

## The Jane Street Episode

No single case better illustrates the regulator's dilemma than the Jane Street matter. In July 2025, SEBI barred Jane Street — one of the world's largest quantitative trading firms — from Indian markets and ordered it to disgorge ₹4,843 crore (approximately $566 million) for index manipulation through large, concentrated derivatives positions on expiry days. The scale of the operation was staggering: SEBI's order described positions that deployed tens of thousands of crores in notional exposure to move index settlement prices.

> "When a big player manipulates expiry, the entire market's settlement is distorted. Retail short-straddle sellers who sold at-the-money options to capture theta get crushed because the settlement point was engineered, not discovered."

Jane Street later deposited approximately $567 million to secure an order that allowed it to resume Indian operations, while disputing the findings. The case revealed a structural vulnerability in India's expiry mechanism: if a single entity could concentrate enough volume in the final hour — and especially in the newly introduced closing auction session (CAS, effective August 2026) — the manipulation risk shifted from the VWAP-window to the random-freeze auction. SEBI's response was to tighten position limits further and introduce the CAS random close designed to make settlement-price manipulation computationally impossible. Whether the measure will be effective remains an open question.

## The Lot-Size Puzzle

SEBI's lot-size policy has an internal contradiction. The regulator wants every index-derivative contract to be valued between ₹5 lakh and ₹10 lakh — enough to limit casual speculation but not so high as to exclude serious retail participants. Yet by raising Nifty lot size from 25 to 75 in 2024, a single-lot entry now costs roughly ₹20–24 lakh in notional exposure and about ₹1.2–1.5 lakh in margin for a basic short straddle. That price point excludes a significant portion of the very retail participants SEBI is trying to protect.

The December 2025 revision partially acknowledged this: Nifty lot size was reduced from 75 to 65 (effective 30 December 2025), and Bank Nifty from 35 to 30. The concession was marginal: a 13% reduction, far from the 67% increase that preceded it. The effect on trader participation was muted.

## The Evolution of India VIX and the Regime Change

One unintended consequence of the regulatory tightening was a structural shift in options pricing. India VIX, which had traded below 15 for much of 2023 and early 2024 — a regime that made option selling attractive and option buying a losing proposition — started to behave differently as the new rules took effect. Fewer retail participants on the sell side meant less premium supply, which meant higher implied volatility for equivalent strikes. By 2025–2026, India VIX was trading in the 18–22 range even during periods of market calm — a full 5–7 points above where it would have been under the old participation regime. The very thing SEBI was trying to prevent — retail losses on the buy side — became more likely as premiums widened.

This is the regulator's perpetual bind. Every measure that protects traders from themselves also makes the market less efficient, less liquid, or more expensive for those who remain. The correct response is not to condemn SEBI but to understand the rules as they evolve and design positions that survive each new constraint.

## Key Takeaways

- **The empirical case for regulation**: SEBI's own data (89–93% retail losses, bottom 3.5% losing ₹28L/year) made regulatory action politically necessary and substantively justified.
- **The October 2024 framework** cut volumes by >50% but pushed remaining speculators to riskier strikes — a known behavioral response.
- **The Jane Street case** exposed expiry-day manipulation at institutional scale; CAS (closing auction session, random close, August 2026) is SEBI's answer, but its effectiveness is unproven.
- **India VIX structurally re-rated** 5–7 points higher post-2024 as premium suppliers left the market, making option buying permanently more expensive.
- **Trade the rules, not against them**: the intelligent retail trader now hedges as a matter of regulatory cost-efficiency, not optional discipline.