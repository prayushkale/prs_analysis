#!/usr/bin/env python3
"""Write batch_special_115.jsonl - analysis of transcripts 0075-0087."""
import json

rows = []

rows.append({
  "id": "0075", "date": "2020-05-25", "type": "special",
  "title_clean": "SGX Nifty Explained - Trading in India, Nifty 50 Relation, Trading Hours, Contract Size",
  "summary": "Full explainer of SGX Nifty mechanics: what it is, contract size (index x US$2), why OI figures differ from India, who can trade it, correct data sources, trading hours (T and T+1 sessions), and why investing.com shows stale prices vs moneycontrol.",
  "chapter_targets": ["7", "2"],
  "themes": ["SGX Nifty", "market microstructure", "data sources", "global cues"],
  "lessons": [
    "SGX Nifty is Nifty priced in Singapore: contract value = index x US$2, so 1 point = US$2 per contract; Indian OI counts shares, Singapore OI counts contracts - same headline OI does not mean same liquidity.",
    "investing.com freezes SGX Nifty updates at 11:30 pm IST (old SGX cutoff); moneycontrol tracks to 2:45 am - late-night SGX levels from investing.com are stale.",
    "SGX Nifty's plus/minus is quoted against SGX's own previous close, not India's close - a '+50' SGX print can be zero gap for Indian traders.",
    "Indian residents cannot trade overseas derivatives; NRIs can."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "SGX Nifty contract value = index level x 2 US dollars; 1 point move = US$2 per contract", "verify": True},
    {"claim": "Singapore Exchange extended SGX Nifty trading hours beyond 11:30 pm about a year before May 2020; investing.com never updated its cutoff", "verify": True},
    {"claim": "SGX Nifty T session runs 9:00 am-6:10 pm SGT (6:30 am-3:40 pm IST); T+1 session 6:40 pm SGT-5:15 am SGT (4:10 pm-2:45 am IST)", "verify": True},
    {"claim": "Indian residents are not permitted to trade derivatives on foreign exchanges; NRIs are exempt from this restriction", "verify": True},
    {"claim": "SGX official site data is delayed 15 minutes; moneycontrol and investing.com are real-time", "verify": False}
  ],
  "quotes": ["Singapore Nifty is like your girlfriend - will never let you sleep at night; Nifty next morning is like your wife - totally unpredictable."],
  "enhance": ["timeline diagram of SGX T/T+1 sessions in IST", "table comparing India vs SGX contract specs (size, OI unit, point value)"],
  "exclude_passages": [],
  "leaks": ["Hi, this is P.R. Sundar"],
  "quality": 5
})

rows.append({
  "id": "0076", "date": "2020-05-27", "type": "special",
  "title_clean": "Bharat Bond ETF - Unbelievably Good For LOW RISK Income + Other Perks",
  "summary": "Bharat Bond ETF explainer: India's first corporate bond ETF, invests only in PSU bonds, expense ratio 0.0005%, two maturities (Apr 2023, Apr 2030), indicative yields ~6.8%/7.6% hold-to-maturity, LTCG 20% with indexation after 3 years, 5% collateral haircut.",
  "chapter_targets": ["30", "29"],
  "themes": ["Bharat Bond", "ETF", "debt investing", "collateral"],
  "lessons": [
    "Bharat Bond is a debt ETF holding only PSU bonds maturing on or before scheme maturity; expense ratio 0.0005% - cheapest fund product in India.",
    "Post-tax return >7% in the long tranche after indexation benefit (20% LTCG rate after 3-year holding) - best risk-adjusted debt return available at the time.",
    "ETF structure gives exchange liquidity plus a low 5% haircut for pledging as F&O collateral - dual use as investment and margin backend."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "Bharat Bond ETF launched with 3-year (Apr 2023) and 10-year (Apr 2030) maturities; indicative yields ~6.38% short / ~7.75% long", "verify": True},
    {"claim": "Bharat Bond ETF expense ratio is 0.0005%, the cheapest mutual fund product in India", "verify": True},
    {"claim": "Debt fund LTCG: 20% of profit with indexation if held >3 years (pre-2023 rules)", "verify": True},
    {"claim": "Bharat Bond units accepted as collateral with only 5% haircut", "verify": True}
  ],
  "quotes": ["If the interest rate in the economy is going lower, these bonds will tend to do very well."],
  "enhance": ["indexation-benefit worked example (buy price, sale price, CII, tax)", "rate-cut scenario table for bond ETF NAVs"],
  "exclude_passages": ["I am informing my friends and clients to invest in Bharat bond (personal advisory framing)"],
  "leaks": ["Hi, this is P. R. Sundar", "I am informing my friends and clients"],
  "quality": 5
})

rows.append({
  "id": "0077", "date": "2020-05-29", "type": "special",
  "title_clean": "How I Made Rs 76 Lakhs in 2 Months - My Trades in May 2020",
  "summary": "Monthly P&L showcase: Rs 76.2L profit on Rs 95L capital in two months (April + May 2020); May added ~Rs 10L despite three large losses (Nifty futures -5.76L, 9150CE -3.28L, 9200CE -4.67L); March series profit Rs 43L; IndusInd straddle returned ~80% in a month.",
  "chapter_targets": ["2", "13", "18", "14"],
  "themes": ["P&L transparency", "position sizing", "index-only trading", "ratio spread", "expectation management"],
  "lessons": [
    "Never compare month-to-month results - the market is like God: you take what it gives; April's extreme VIX paid, May's smaller win is still >10% on capital.",
    "Trade only Nifty/Bank Nifty: stocks add volatility, physical-settlement and margin problems for no extra edge; stocks only via cash-secured puts or deliberate earnings trades.",
    "A ~Rs 12L cluster of losses (futures + two long calls) cut monthly profit from ~Rs 22L to Rs 10L - uncontrolled directional bets, not sold options, caused the damage.",
    "Patience, not call accuracy, made the IndusInd 400 straddle work: sold at 105, spot closed 385, kept ~90 points - 'people lose because they do not want to lose'."
  ],
  "strategies": [
    {"name": "Put ratio spread (9100PE buy / 8500PE sell)", "construction": "buy Nifty 9100 put, sell Nifty 8500 put", "numbers": "+Rs 2.06L on the month", "best_regime": "mildly bearish with floor", "adjustments": "none described", "risks": "unlimited above short strike if spot rallies through it"},
    {"name": "Cash-secured puts (ICICI 300PE, HDFC 840PE)", "construction": "sell puts below market with cash set aside for delivery", "numbers": "+Rs 33K ICICI, +Rs 28K HDFC as market reversed late May", "best_regime": "want to own the stock lower", "adjustments": "rolled with reversal", "risks": "assignment at strike"},
    {"name": "IndusInd 400 short straddle", "construction": "sell 400CE + 400PE, collect 105; psychological stops at 505/295", "numbers": "+90 points ~80% return for the month", "best_regime": "range-bound expiry week", "adjustments": "stops never hit; held to expiry", "risks": "gap beyond breakevens"}
  ],
  "event_claims": [
    {"claim": "SEBI margin framework effective June 1, 2020 reduces margins for hedged index positions and raises them for stock options", "verify": True},
    {"claim": "Two-month P&L: Rs 76.2L profit on Rs 95L capital (~80%); May profit Rs 10L; March-series profit Rs 43L", "verify": False},
    {"claim": "Nifty moved ~500 points and Bank Nifty ~2,300-2,400 points from Wednesday low to Thursday high in late May 2020", "verify": True}
  ],
  "quotes": ["People lose money because they do not want to lose money."],
  "enhance": ["worked example of netting: why broker 'net amount' display can invert short-futures P&L", "position-sizing math on the Rs 12L loss cluster"],
  "exclude_passages": ["whole back-office demo (CRF 4450, son's company account)", "Jaguar car anecdote", "Twitter follower framing"],
  "leaks": ["Hi, this is PR Sunder", "my son's company account", "CRF 4450", "I sold my Jaguar car", "posted in Twitter", "my followers"],
  "quality": 4
})

rows.append({
  "id": "0078", "date": "2020-05-30", "type": "special",
  "title_clean": "My Reliance Investment - Follow Up #1",
  "summary": "Live follow-up of the Reliance 'core investment + hedging' project: long June/Reliance futures at 1422, layered option hedges/straddles turned a ~Rs 35-40K directional gain into Rs 1.6L within ~2-3 weeks on <=Rs 5L margin, with the Rs 15L core parked in debt instruments as collateral.",
  "chapter_targets": ["17", "18", "29"],
  "themes": ["hedged investing", "collateral efficiency", "core-satellite", "adjustments"],
  "lessons": [
    "Core-satellite design: park the full investment value in interest-bearing collateral (debt fund/FD/Bharat Bond), run the equity exposure through futures on ~one-third margin.",
    "Hedging sequence shown: long futures -> sell 1460CE -> convert to 1460 straddle -> add 1520CE -> roll put 1460->1440 -> straddle 1440 -> sell 1420PE on reversal; each adjustment follows the tape, not a script.",
    "Same directional view: pure futures made ~Rs 35-40K; hedged/adjusted version made Rs 1.6L - the spread between them is the value of adjustment skill.",
    "Long-term investing means buying and forgetting; trading skill accelerates the path to the target number of shares."
  ],
  "strategies": [
    {"name": "Hedged futures accumulation (Reliance)", "construction": "long futures 1422; sold 1460CE->straddle; sold 1520CE; rolled puts down to 1440; sold 1440CE->straddle; sold 1420PE", "numbers": "+Rs 159,186 in <3 weeks vs ~Rs 35-40K unhedged; margin <=Rs 5L of Rs 15L collateral", "best_regime": "trend with two-way swings", "adjustments": "straddle conversions and put rolls as spot reverses", "risks": "gap risk between adjustments; margin calls in violent moves"}
  ],
  "event_claims": [
    {"claim": "New SEBI margin rules effective June 1, 2020 make long futures cheaper than cash-market holding for hedged retail positions", "verify": True},
    {"claim": "Reliance Industries consolidated ~2008-2018 then broke out (the 2017-2018 re-rating)", "verify": True}
  ],
  "quotes": ["If you keep on looking at the investment every day, the investment will not grow."],
  "enhance": ["step-by-step payoff diagram sequence of the adjustment ladder", "margin comparison: cash buy vs futures+collateral"],
  "exclude_passages": ["'my company account, not my son's company account' framing", "Tamil channel launch promise", "live-session logistics (2000 people joined, question collation)"],
  "leaks": ["Hi, this is PR Sunder", "my son's company account", "launching a Tamil channel soon"],
  "quality": 4
})

rows.append({
  "id": "0080", "date": "2020-06-01", "type": "special",
  "title_clean": "F&O Traders Can Now Earn 3X Money - New Margin Rules by SEBI",
  "summary": "Hands-on margin arithmetic under SEBI's June-2020 framework: naked ATM call margin rises to ~Rs 1.13L; short straddle margins net to ~Rs 1.05L (not the sum of legs); adding 1,000-point wings cuts effective margin to ~Rs 45-55K per straddle; ITM put calendar under Rs 30K.",
  "chapter_targets": ["12", "13", "2"],
  "themes": ["margin system", "span/exposure", "defined-risk sizing", "netting"],
  "lessons": [
    "Margin netting is the silent profit center: sell ATM call (Rs 1.13L) + ATM put (Rs 1.05L) costs ~Rs 1.05L combined, not Rs 2.18L - the short straddle is margin-efficient by design.",
    "Buying protection slashes margin: ATM straddle + 1,000-point wings = ~Rs 55K effective (June-expiry wings), ~Rs 45K with July straddle + June wings; wings bought in the cheaper series.",
    "SEBI's new framework nudges everyone to defined-risk index trades: 2% exposure margin for indices vs 3.5% for stocks, higher base margins for stock options.",
    "Defined risk is not low risk: 4 lots x 300-point max loss = 1,200 points of total risk - position sizing, not strike choice, decides survival."
  ],
  "strategies": [
    {"name": "Margin-optimized short straddle with far wings", "construction": "sell ATM straddle (Jul), buy 1,000-pt wings in the near series; roll wings monthly", "numbers": "straddle alone ~Rs 1.05L; with wings ~Rs 45-55K effective; premium received ~800-1,000+ points", "best_regime": "high IV, low expected drift", "adjustments": "re-buy wings weekly as they decay", "risks": "gap through both wings in a black swan; weekly wing churn cost"},
    {"name": "ITM put calendar", "construction": "sell current-month 10000PE, buy next-month 10000PE", "numbers": "margin <Rs 30K", "best_regime": "mildly bullish to neutral", "adjustments": "n/a", "risks": "front-month pin risk"}
  ],
  "event_claims": [
    {"claim": "Post-June-2020 rules: naked ATM option margin ~Rs 1.0-1.2L (was ~Rs 80-90K); exposure margin 2% for indices, 3.5% for stocks", "verify": True},
    {"claim": "Pre-2017 era: SPAN ~3% + exposure ~3% (often waived by brokers) meant ~Rs 18K margin per Nifty lot at ~9,000 index level; max OI on single strikes then exceeded 1 crore shares", "verify": True},
    {"claim": "Two years before 2020, margin per lot was ~80-90K after earlier SEBI tightening", "verify": True}
  ],
  "quotes": ["Options trading is not about which strike price you are selling. It is all about risk management, margin management and position sizing."],
  "enhance": ["margin-netting arithmetic walk-through with a real straddle", "table: margin vs wing distance (200/300/400/1000 points)"],
  "exclude_passages": ["'I advise my followers' framing"],
  "leaks": ["Hi, this is P. R. Sunder", "my followers"],
  "quality": 5
})

rows.append({
  "id": "0081", "date": "2020-06-02", "type": "special",
  "title_clean": "Taxation for Trading Income - Intraday, F&O, Long-Term",
  "summary": "Trading tax primer: cash-market STCG 15% and LTCG 10% beyond Rs 1L; F&O profits are business income taxed at slab rates with full expense deduction; individual vs corporate account trade-off (top personal rate ~42% vs 22-25% corporate) complicated by MAT and loss set-off rules.",
  "chapter_targets": ["28"],
  "themes": ["taxation", "business income", "capital gains", "corporate vs individual"],
  "lessons": [
    "F&O is business income: taxed at slabs but every business expense (broadband, office, salaries, depreciation) is deductible - unlike flat 15%/10% capital-gains rates with no expense offset in cash market.",
    "Big profits favor a corporate account (top personal ~42% vs 22-25% corporate), but MAT (~18%) limits loss set-off to the excess, and dividend distribution tax applies when profits leave the company.",
    "Loss carry-forward favors individuals: a Rs 1Cr loss year can offset the next Rs 1Cr profit entirely; in a company the same offset is blunted by MAT.",
    "Small-capital traders are better as individuals: slab rates plus exemptions beat a flat 25% corporate rate."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "Cash-market STCG 15%; LTCG 10% on gains above Rs 1 lakh (introduced Budget 2018; zero before)", "verify": True},
    {"claim": "F&O income is treated as non-speculative business income in India", "verify": True},
    {"claim": "Top individual slab + surcharge ~42% at >Rs 5Cr profit; corporate rate 22% (22% regime may exclude those carrying forward losses - speaker unsure)", "verify": True},
    {"claim": "Minimum Alternate Tax ~18% for corporates; corporate loss set-off limited", "verify": True},
    {"claim": "Individual business-loss carry-forward period ~8 years (speaker unsure 7 vs 8)", "verify": True}
  ],
  "quotes": ["Go and make profit first, then come to me - I will answer all your questions."],
  "enhance": ["individual vs corporate after-tax comparison table at Rs 10L / Rs 1Cr / Rs 5Cr profit", "MAT and set-off worked example", "expense-deduction checklist for F&O traders"],
  "exclude_passages": ["'I met an income tax officer' anecdote framing", "'I am also trading in corporate account... my family company' disclosure"],
  "leaks": ["Hi, this is PR Sunder", "Recently, I met an income tax officer", "my auditor", "it is my family company"],
  "quality": 4
})

rows.append({
  "id": "0082", "date": "2020-06-04", "type": "special",
  "title_clean": "Liquid BeES vs Nifty BeES for LOW RISK Investment - Which is BEST",
  "summary": "ETF comparison: Nifty BeES = equity ETF mirroring Nifty returns; Liquid BeES = debt ETF in government securities that pays interest as additional units, trades flat at ~Rs 1,000 with no STT/stamp duty, and ironically carries a higher collateral haircut (10%) than Nifty BeES (5%).",
  "chapter_targets": ["30", "29", "12"],
  "themes": ["ETF", "collateral", "debt vs equity", "costs"],
  "lessons": [
    "Liquid BeES converts interest into additional units monthly and trades at ~Rs 1,000 +/- 1 paisa with zero STT/stamp duty - a cash-component workhorse for pledged collateral.",
    "Puzzling margin rules: riskier Nifty BeES gets a 5% haircut while government-securities-backed Liquid BeES gets 10% - know each broker's haircut schedule before choosing collateral.",
    "Dividend reality check: Nifty BeES has barely paid dividends (last cited 2015) - total return comes from NAV."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "Liquid BeES invests only in government securities; pays interest as bonus units instead of cash", "verify": True},
    {"claim": "Nifty BeES collateral haircut 5% vs Liquid BeES 10%", "verify": True},
    {"claim": "Liquid BeES has no STT, no stamp duty, no NSE transaction charges; price pinned near Rs 1,000", "verify": True},
    {"claim": "Nifty BeES last declared a dividend in 2015", "verify": True}
  ],
  "quotes": [],
  "enhance": ["collateral haircut table across instruments (equity shares, Nifty BeES, Liquid BeES, Bharat Bond, FDs)", "yield math of unit-accrual interest"],
  "exclude_passages": [],
  "leaks": ["Hi, this is P. R. Sundar"],
  "quality": 4
})

rows.append({
  "id": "0084", "date": "2020-06-06", "type": "special",
  "title_clean": "Q&A: Second Wave of Selling, FII Data During Market, Weekly Hedge",
  "summary": "Q&A batch: confirmation bias around a 'second wave' crash (June-expiry poll said crash, market rallied); short selling has no practical ban (naked shorting allowed to ~Rs 500Cr); options MTM losses adjust against collateral but booked losses need cash; margin-shortfall penalty schedule 0.5%/1%/5%; FII data is end-of-day only.",
  "chapter_targets": ["1", "2", "12", "13"],
  "themes": ["confirmation bias", "short selling", "collateral mechanics", "margin penalties", "capital requirements"],
  "lessons": [
    "Confirmation bias is the pattern-trader's disease: after 2008, everyone 'knew' June 2020 would crash on 7,500 breakdown - the market rallied; trade the tape, not the pattern.",
    "There is no practical short-selling ban in India: naked shorting to ~Rs 500Cr, beyond that with equivalent holdings or extra margin.",
    "Collateral asymmetry: options MTM losses can be adjusted against pledged collateral if not booked; futures MTM is cash-settled daily.",
    "Never square only the hedge leg with thin capital: leaving a naked short triggers margin shortfall penalties - 0.5%/day under Rs 1L shortfall, 1%/day above, 5%/day from the 6th session.",
    "Small capital (Rs 40-50K) belongs in mutual funds, not F&O."
  ],
  "strategies": [
    {"name": "Monthly short option with weekly hedge roll", "construction": "sell monthly option, buy 100-point-away weekly hedge (e.g., sold 9000PE Jul, bought 8900PE weekly)", "numbers": "margin ~Rs 50K with weekly hedge vs >Rs 1L naked", "best_regime": "range-bound with weekly rolls", "adjustments": "re-buy hedge each week as it expires worthless", "risks": "many brokers block far-OTM weekly buys; roll churn"}
  ],
  "event_claims": [
    {"claim": "Naked short selling allowed up to ~Rs 500 crore; beyond that requires equivalent holdings or higher margin", "verify": True},
    {"claim": "Margin shortfall penalty: 0.5%/day if shortfall <Rs 1L, 1%/day if >Rs 1L, 5%/day from 6th trading session", "verify": True},
    {"claim": "June 2020 expiry-week poll: majority expected a crash; market instead rallied sharply", "verify": False},
    {"claim": "FII/DII trade data is published by exchanges only after market close", "verify": True}
  ],
  "quotes": ["There is no holy grail formula in the market."],
  "enhance": ["worked example: hedge-leg square-off margin shortfall timeline with penalties", "collateral-vs-cash settlement matrix (options vs futures)"],
  "exclude_passages": ["broker endorsement passage naming specific discount brokers (Zerodha, 5paisa, Alice Blue)"],
  "leaks": ["Hi, this is P. R. Sunder", "Zerodha", "5 paisa capital", "Alize Blue (Alice Blue)"],
  "quality": 5
})

rows.append({
  "id": "0086", "date": "2020-06-08", "type": "special",
  "title_clean": "Escaping Market Risks - June 8 Market Report",
  "summary": "Euphoric gap-up day (Nifty +200, Bank Nifty +500) faded exactly as the bull-market-lifecycle aphorism warns; a blog-published hunch that Nifty would break 10,200 at least once played out; Doji close after weighted-average explanation; FIIs bought Rs 813Cr while DIIs sold Rs 1,238Cr.",
  "chapter_targets": ["2", "5", "6", "7"],
  "themes": ["euphoria fading", "gap behavior", "Doji", "FII/DII data", "technical levels"],
  "lessons": [
    "Bull markets die of euphoria: the biggest gap-up days are profit-booking magnets - fade enthusiasm, not the trend.",
    "NSE 'close' is the last half-hour weighted average - a 'flat close' can hide a 50-point last-30-minute slide (Doji after a smash = indecision, not strength).",
    "Divergence day reading: Reliance/Bank heavyweights sold from highs while indices held - distribution under a calm surface.",
    "Pre-market hunches can be published and falsifiable: 'Nifty future will trade below 10,200 at least once' - the value is in stating levels, not vibes."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "June 8, 2020: Nifty gapped up ~200 points, Bank Nifty >500; both faded - Nifty broke 10,200 intraday and closed via weighted average near prior close (Doji)", "verify": True},
    {"claim": "June 8, 2020 flows: FIIs bought Rs 813Cr; DIIs sold Rs 1,238Cr", "verify": True},
    {"claim": "RBI permitted IndusInd Bank promoters to buy shares in the open market (June 2020); stock rallied", "verify": True},
    {"claim": "Reliance hit all-time high around June 8, 2020 and was sold from the highs; HDFC Bank/Kotak fell >Rs 50 intraday", "verify": True},
    {"claim": "DAX recovered from ~12,671 to ~12,866 during the Indian afternoon; Dow futures +200", "verify": True}
  ],
  "quotes": ["A bull market is born out of pessimism, grows out of skepticism, matures out of optimism and dies out of euphoria."],
  "enhance": ["weighted-average close mechanics with a candle diagram", "gap-fade statistics by gap size"],
  "exclude_passages": ["'I mentioned in my blog' self-reference (genericize)"],
  "leaks": ["Hi, this is P R Sunder", "I write in my blog", "my blog pre-market point number 11"],
  "quality": 3
})

rows.append({
  "id": "0087", "date": "2020-06-10", "type": "special",
  "title_clean": "Corporate Earnings Results Schedule & Dividends - How, When, Where to Check",
  "summary": "Practical data guide: BSE/NSE results calendars, moneycontrol earnings calendar with expected announcement times (only D+0/D+1), why F&O traders care (IV crash after results), dividend/bonus/split calendar with ex-dates, and aggregate earnings-season scoreboard.",
  "chapter_targets": ["9", "11", "19"],
  "themes": ["earnings calendar", "IV crush", "dividends", "corporate actions"],
  "lessons": [
    "Results timing is a tradable input: moneycontrol shows expected announcement windows (today/tomorrow only) - premium sellers position just before, capture the post-result IV crash.",
    "Corporate-action calendars (dividend, split, bonus with ex-dates) are on BSE/NSE/moneycontrol - never be surprised by an ex-date.",
    "Aggregate earnings trackers (4,248 companies; 493 declared at the time) give the market-wide earnings season scoreboard, not just single stocks."
  ],
  "strategies": [],
  "event_claims": [
    {"claim": "After results, implied volatility crashes and option premiums fall - the basis of pre-result premium-selling trades", "verify": True},
    {"claim": "Titan results expected 1:15-2:15 pm; Hero MotoCorp next day 11 am-12 noon (June 2020); expected times shown only for current and next day", "verify": True},
    {"claim": "Infosys declares results almost exactly at the announced time", "verify": False},
    {"claim": "Colgate-Palmolive India declared a 1,600% dividend (ex-date June 1, 2020); GE Shipping 27%; Sinclairs Hotels stock split 2:10 (ex-date June 17, 2020)", "verify": True},
    {"claim": "Earnings season scoreboard: 4,248 companies tracked, 493 results declared (June 2020)", "verify": True}
  ],
  "quotes": [],
  "enhance": ["IV-crash-before/after worked example (premium table around a results day)", "corporate-actions impact table (dividend adjustment, split adjustment in F&O)"],
  "exclude_passages": ["'I write in my blog' framing"],
  "leaks": ["my timeline", "I write in my blog"],
  "quality": 4
})

with open("/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_115.jsonl", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(rows), "records")
