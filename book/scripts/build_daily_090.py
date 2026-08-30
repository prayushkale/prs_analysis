#!/usr/bin/env python3
"""Build batch_daily_090.jsonl - structured extraction of transcripts 3112-3141 (May-Jun 2026)."""
import json

R = []

def add(id, date, type, summary, levels, events, lessons, quote="", dup="", leaks=None):
    R.append({"id": id, "date": date, "type": type, "summary": summary,
              "levels": levels, "events": events, "lessons": lessons,
              "quote": quote, "dup_flag": dup, "leaks": leaks or []})

BASE_LEAKS = ["this is Pia/Pierre/PR Sundar (name variants)", "sponsored by Delta.exchange"]

# 3112 13-May-2026 pre
add("3112", "2026-05-13", "pre_market",
    "Severe selloff continues: Nifty fell nearly 400 points day after PM crisis statement; Sensex down about 2500 in two sessions; IT worst index; speaker calls it overreaction since DII inflow exceeded FII outflow; maps supports 23200/23000 and Fibonacci resistances 24300/24800; gold import duty hiked 9%.",
    {"nifty": 23430, "banknifty": None, "vix": None, "fii_cr": -2000, "dii_cr": 8000},
    [{"claim": "Prime Minister stated India faces a major crisis (worst in 10 years), triggering two straight days of heavy falls (Nifty -400 on 12-May; Sensex -2500 over two sessions)", "verify": True},
     {"claim": "FII sold over 8000 crore on 11-May; DII bought about 8000 crore on 12-May with net institutional inflow above 6000 crore yet market fell", "verify": True},
     {"claim": "Government of India increased gold/silver import duty by 9% (announced overnight 12-13 May 2026)", "verify": True},
     {"claim": "US inflation data released 12-May was highest in 2-3 years though US market reaction was mild", "verify": True}],
    ["Repeated support tests eventually break (tin-and-hammer analogy); a technically-long market that fails to rally within a month signals distribution",
     "When DII inflows exceed FII outflows and the market still falls, the fall is positioning-driven (expiry), not flow-driven"],
    "Nifty would not have broken 24000 if not for the Prime Minister statement.", 
    "Repeats 3111 post-market content (PM statement, Iran, FII/DII data); adds gold tax + levels",
    BASE_LEAKS + ["returned to Chennai after 1 month in US/Canada", "no dosa no idli weight loss story", "wife-chosen colorful shirts joke", "Hope you enjoyed watching"])

# 3113 14-May-2026 pre
add("3113", "2026-05-14", "pre_market",
    "Five straight down days while global markets rally; gap-up attempt sold into; speaker argues market is extremely oversold (RSI ~40) and needs to consolidate before reversing; April-8 ceasefire gap looms as magnet; week range 23000-24000 with 24000 call highest open interest.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "On April 8, 2026 ceasefire news, GIFT Nifty indicated a 1500-2000 point (6-8%) gap; Nifty spot still has gap-fill pending toward 23260 area", "verify": True},
     {"claim": "Nifty fell over 4% in four sessions while US markets made fresh all-time highs daily", "verify": True},
     {"claim": "In 2019 markets expected Amit Shah as finance minister (context anecdote)", "verify": False}],
    ["Markets take good news and bad news but cannot take uncertainty",
     "After an accident the patient must rest: brutal falls need consolidation and a base before reversal, not V-turns"],
    "Markets are always subject to headline news.",
    "Repeats 3112; new: oversold RSI, gap mechanics", 
    BASE_LEAKS + ["jet-lag travel Vancouver-Toronto-London-Chennai", "age 62 disclosed", "business class travel", "BJP friend anecdote"])

# 3114 14-May-2026 post
add("3114", "2026-05-14", "post_market",
    "Bottoming-out volatility: gap-up wiped, Bank Nifty fell 500 then shot up 1200; Infosys down 45% and TCS down 50% from all-time highs with fresh 52-week lows; market recovered on unconfirmed news that government may cut taxes on FII interest income from government securities (RBI recommendation to finance ministry).",
    {"nifty": 23800, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Infosys down more than 45% and TCS down more than 50% from all-time highs; TCS, Infosys, HCL Tech hit fresh 52-week lows on 14-May-2026", "verify": True},
     {"claim": "RBI recommended to finance ministry a cut in taxes on FII interest income from government securities; Bloomberg carried the report; unconfirmed", "verify": True},
     {"claim": "Speaker: if FII selling stops, Nifty can return to 26000-26500 by end of December 2026", "verify": False}],
    ["After a five-day fall, extreme two-way volatility signals bottoming, not continuation",
     "Regulators ignoring FII sentiment prolongs selling; policy accommodation flips flows"],
    "If you do not make FIIs happy, they will continue to sell.",
    "New events (IT lows, FII G-Sec tax news)", 
    BASE_LEAKS + ["Bangalore workshop promotion with early-bird offer", "contact our office"])

# 3115 15-May-2026 pre
add("3115", "2026-05-15", "pre_market",
    "US S&P above 7500 at all-time high but GIFT Nifty euphoria wiped out; Nvidia rallied 4.5% on China chip-restriction removal; petrol-diesel hiked only Rs 3 vs feared Rs 20-25, ending uncertainty; weekly PCR rose to 1.22 as put selling resumed; Adani SEC settlement seen positive.",
    {"nifty": None, "banknifty": 1200, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "US removed chip-sale restrictions on Nvidia for China; Nvidia stock rose about 4.5%", "verify": True},
     {"claim": "Petrol and diesel prices hiked by Rs 3 (15-May-2026), far below speculated Rs 20-25", "verify": True},
     {"claim": "Gautam Adani agreed to settle a US SEC case by paying about 18 million dollars", "verify": True},
     {"claim": "Weekly option put-call ratio rose to 1.22; 23700 straddle sold near 350 points implying 23350-24050 range", "verify": False}],
    ["Markets can absorb bad news but not uncertainty; a smaller-than-feared hike is positive",
     "Same penalty event reads negative for small companies and positive for giants - sentiment, not logic, prices news"],
    "This uncertainty has been going on for a long time. Today that uncertainty has ended.",
    "Repeats FII tax news from 3114; adds fuel hike, Adani",
    BASE_LEAKS + ["weekend last-hour trading advice"])

# 3116 15-May-2026 post
add("3116", "2026-05-15", "post_market",
    "Friday last-hour selloff: Nifty fell 250 points in the final 90 minutes as global chip stocks (Samsung -8%, Korean market -7/8%) crashed; rupee hit fresh all-time low above 96; Nifty still outperformed Bank Nifty; 23700 straddle sellers profited over 2000 per lot; Tuesday red candle still uncaptured.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "South Korean market fell about 7-8% and Samsung about 8% in a day (mid-May 2026) leading a global semiconductor selloff", "verify": True},
     {"claim": "Indian rupee crossed 96 against the US dollar - fresh all-time low (May 2026)", "verify": True},
     {"claim": "23700 short straddle (taken 15-May area, ~350 point premium) yielded over 2000 rupees profit per lot within days", "verify": False}],
    ["South Korea's ±5% daily swings make it the second-most volatile options market after India",
     "Weekend risk compresses Friday last-hour prices; squaring decides the close"],
    "All the three green candles could not wipe out one red candle.",
    "Repeats 3115 levels; adds Korea crash, rupee record",
    BASE_LEAKS + ["Bengaluru workshop end-of-month promotion", "Saturday video teaser", "Hope you enjoyed watching"])

# 3119 18-May-2026 pre
add("3119", "2026-05-18", "pre_market",
    "Weekend escalation: drones targeted Saudi Arabia (3 intercepted) and UAE (one hit near a nuclear facility); crude spiked; Trump's China visit produced no Iran breakthrough and US indices fell; speaker details the Strait of Hormuz crisis (day ~78-79 vs 4-5 months in 1980) and warns Indian markets stay hostage to it.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": 1300, "dii_cr": -1900},
    [{"claim": "Iran launched drones at Saudi Arabia (3 intercepted) and UAE (1 hit near a nuclear facility) over the weekend before 18-May-2026", "verify": True},
     {"claim": "US S&P 500 rallied from 6300 to above 7500 and NASDAQ ~30% in four-five weeks before the Trump-China meeting disappointment", "verify": True},
     {"claim": "Wipro may be removed from Nifty 50 with BSE possibly replacing it; NSE IPO planning cited", "verify": True},
     {"claim": "Government imposed windfall tax on petrol, diesel and ATF exports pressuring Reliance", "verify": True}],
    ["A headline-driven market makes technicals unreliable; trade intraday or stay far away",
     "One red candle unreclaimed for eight sessions defines the trend regardless of bounce days"],
    "Our concern is only the Strait of Hormuz - it must be open and without any toll charges.",
    "Repeats week narrative; new: drone attacks, Hormuz timeline, Wipro/BSE index news",
    BASE_LEAKS + ["friend bought EMC2/MCX shares at 8000 doubled", "BSE recommendation 2021 at 500 now 4000 personal track record"])

# 3120 18-May-2026 post
add("3120", "2026-05-18", "post_market",
    "Most volatile day of the series: Sensex and Bank Nifty each fell over 1000 points then rallied over 1000; India VIX crossed 20 and exceeded the US VIX (historic inversion); Iran sent a peace proposal via Pakistan with maximalist demands; Nifty closed green on IT value-buying while SBI crashed 25% from its recent high.",
    {"nifty": None, "banknifty": -1000, "vix": 20, "fii_cr": None, "dii_cr": None},
    [{"claim": "India VIX crossed 20 on 18-May-2026, trading above the US VIX (usually ~30-35% below)", "verify": True},
     {"claim": "Iran sent a peace proposal via Pakistan to the US demanding sweeping concessions including Hormuz toll rights; 6 drones had been launched 24 hours earlier", "verify": True},
     {"claim": "State Bank of India fell more than 25% from its recent high (about 10250 to about 9200) in about a month", "verify": True},
     {"claim": "Brent crude crossed 111 dollars before easing to about 110", "verify": True}],
    ["High VIX is a gift for premium sellers: 1.25% weekly yield on far strikes even in a falling market",
     "When index rises on one sector (IT) while breadth falls, the rally is masking distribution"],
    "High weeks means the premiums are high - there is nothing to complain about high weeks.",
    "New: VIX inversion, SBI crash, peace proposal",
    BASE_LEAKS + ["Bangalore workshop 2-week promotion"])

# 3121 19-May-2026 pre
add("3121", "2026-05-19", "pre_market",
    "Expiry-day preview built on an unprecedented futures-premium anomaly: next-month Nifty future at only 70-75 points premium versus the normal ~150 (risk-free-rate equivalent), unseen in 17 years including COVID and Lehman; both FII and DII bought over 2500 crore each for the first time in months; Iran crisis (started Feb 28) keeps VIX near 20.",
    {"nifty": None, "banknifty": None, "vix": 20, "fii_cr": 2800, "dii_cr": 2900},
    [{"claim": "Next-month Nifty future premium collapsed to 70-75 points vs the usual ~150 (annualized risk-free equivalent), an anomaly never seen in 17 years, not even during COVID or Lehman", "verify": False},
     {"claim": "First time in many months both FIIs and DIIs were net buyers above 2500 crore each (~2800-2900 crore each) on 18-May-2026", "verify": True},
     {"claim": "US announced relaxation of the oil export ban on Iran; Brent touched 112 then fell 2% to ~109", "verify": True},
     {"claim": "Trump postponed a planned attack on Iran after Saudi Arabia, Qatar and UAE requested negotiations", "verify": True}],
    ["Futures premium is the market's fear gauge: a shrunken next-month premium implies structural bearishness and depressed call pricing",
     "When both FII and DII buy together, institutions believe specific sectors have bottomed"],
    "Even during coronavirus and Lehman collapse time also I have never seen this phenomena.",
    "Repeats 3120 volatility; adds premium anomaly, FII+DII joint buying",
    BASE_LEAKS + ["workshop participants struggling", "17 years of stock market experience", "methodology-not-advisory disclaimer", "Bangalore workshop promotion"])

# 3122 19-May-2026 post
add("3122", "2026-05-19", "post_market",
    "The daily 200-point reversal tradition struck again: a steady day until 2:30pm then a 200-point fall; the cause was FIIs selling about 2500 crore after one day of buying; IT index had rallied 8% in three sessions; rupee hit a fresh low; four red candles remain unreclaimed.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": -2500, "dii_cr": 2500},
    [{"claim": "IT index rallied about 8% in three sessions (Fri +2%, Mon +2%, Tue +4% intraday) off the 14-May bottom", "verify": True},
     {"claim": "FIIs sold about 2500 crore on 19-May after buying the previous day; DIIs bought more than FIIs sold yet market fell", "verify": True},
     {"claim": "Rupee hit a fresh record low on 19-May-2026", "verify": True}],
    ["Intraday stability early in the session is bait: the May-2026 tape reversed 200+ points daily regardless of morning direction",
     "Premium behavior (put bias, call premium shrinkage) telegraphs the bearish undertone before price does"],
    "People are buying call options but call option prices keep falling - that is the reality.",
    "Repeats 3121; adds FII selling day",
    BASE_LEAKS + ["tired/jet-lag comments"])

# 3123 20-May-2026 pre
add("3123", "2026-05-20", "pre_market",
    "GIFT Nifty down 400 points overnight as US falls a third day; NVIDIA results after the US close are framed as the decisive global catalyst; Fed minutes dismissed as a non-event; speaker details why put buyers (not call buyers) profit in such regimes and revises the consolidation zone to 23200/300-23800.",
    {"nifty": 23400, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "GIFT Nifty fell about 400 points overnight (from ~23780 to ~23400) ahead of NVIDIA results", "verify": True},
     {"claim": "Nifty has oscillated violently between 23300 and 23800 since the previous Tuesday with each level tested multiple times", "verify": True},
     {"claim": "Speaker entered equity mutual funds in Dec-2024 after a 10% fall; position is roughly cost-to-cost now", "verify": False}],
    ["In falling markets put buyers win and call buyers lose because IV spikes on the way down and collapses on weak bounces",
     "Waiting for a single stock's results (NVIDIA) to resolve an entire market is event risk concentrated"],
    "People who bought put options have made money, not the people who bought call options.",
    "Repeats ranges; adds NVIDIA setup",
    BASE_LEAKS + ["personal July 25000 call trade squared at profit", "mutual fund purchase Dec-2024 personal", "weekend video teaser"])

# 3124 20-May-2026 post
add("3124", "2026-05-20", "post_market",
    "Morning fall of 250 points met the afternoon rally of 300+ - the 200-point reversal rule held; Nifty closed +41 while the 23500 put fell Rs 50 as futures premium expanded into the close; Fed minutes and NVIDIA results tonight; Parle-Melody chocolate misread as Parle Industries +5% illustrates market irrationality.",
    {"nifty": None, "banknifty": -800, "vix": None, "fii_cr": -1000, "dii_cr": 2000},
    [{"claim": "Nifty made ~2% intraday swings daily through May 2026 (about 40% cumulative movement over the series)", "verify": False},
     {"claim": "Prime Minister gifted an Italian counterpart a Parle Melody chocolate; traders misread it as Parle Industries and the stock rose about 5%", "verify": True},
     {"claim": "After the PM statement Nifty fell about 800 points in two sessions from the 24000-24600 zone into 23300-23800", "verify": True}],
    ["Options price the futures, not the spot: premium expansion in the last 15 minutes can move OTM puts more than the index itself",
     "The first three volatile weeks predict an even more volatile expiry week"],
    "Markets are always irrational - that is a side joke but a real lesson.",
    "Repeats; adds Parle anecdote, premium mechanics",
    BASE_LEAKS + ["Bangalore workshop promotion"])

# 3125 21-May-2026 pre
add("3125", "2026-05-21", "pre_market",
    "Trump tweets negotiations are in final stages; NVIDIA posts good results that merely meet elevated expectations, so the stock dips (sell-the-news); Nifty future stuck below last Tuesday's 23785 close-basis level; RBI $5 billion swap injection announced for expiry Tuesday; Nifty is -10% over a year while South Korea is +180%.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "NVIDIA results beat/matched expectations but the stock fell slightly on 20-May-2026 as results only met lofty expectations", "verify": True},
     {"claim": "RBI announced a 5-billion-dollar swap window for 26-May-2026 (expiry day) to inject liquidity and support the rupee", "verify": True},
     {"claim": "Nifty is down about 10% over one year while South Korea's index is up about 180%", "verify": True},
     {"claim": "Nifty future high last Thursday was 23877.5; last Tuesday's close-basis high 23785 remains unreclaimed", "verify": False}],
    ["A crying-tiger market: repeated false alarms make traders ignore the real deal when it finally arrives",
     "For the world's number-one stock, meeting expectations is no longer enough - positioning demands beats"],
    "So many Jane Street players have come into the Indian markets.",
    "Repeats; adds NVIDIA outcome, RBI swap",
    BASE_LEAKS + ["wife chose my shirt joke", "Tamil tiger-crying-boy story", "Jane Street reference", "Bangalore workshop"])

# 3126 21-May-2026 post
add("3126", "2026-05-21", "post_market",
    "Even a genuine gap-up with good global cues fell 250+ points; futures premium collapsed 65 points intraday (from +35 to -30 discount); after the close Iran-uranium headlines cut another 200 points; repo-rate-hike speculation to defend the rupee drove the day; speaker is openly confused by the tape.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Nifty futures premium swung 65 points in one session (from +35 premium to 30-point discount) on 21-May-2026", "verify": False},
     {"claim": "Rumor circulated that RBI may raise the repo rate to contain rupee depreciation, pressuring the market", "verify": False},
     {"claim": "US 30-year treasury yields about 5.2% vs India ~7% - only a 1.8% differential, the speaker's argument for structural rupee depreciation", "verify": True},
     {"claim": "South Korea's market rose about 8% the same day India fell", "verify": True}],
    ["A 65-point premium collapse despite good news is institutional selling speaking louder than headlines",
     "Interest-rate differentials anchor long-run currency depreciation; flows follow the carry"],
    "Everything positive for India, but still we ended negative - I am totally confused.",
    "Repeats; adds premium collapse, FM-change rumors",
    BASE_LEAKS + ["wife shirt joke and wife-is-always-right joke", "traveling abroad plans", "Sensex expiry comments"])

# 3127 22-May-2026 pre
add("3127", "2026-05-22", "pre_market",
    "Overnight whipsaw: Iran supreme-leader uranium headline knocked 200 points off GIFT, later declared fake; US closed green on intense-negotiation reports; speaker warns the weekend brings either a signed deal or a war start and advises abandoning short-term positions for far-dated, hedged June/July structures.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": -2000, "dii_cr": None},
    [{"claim": "Iran supreme leader declared uranium/enrichment will stay in Iran (22-May headline), later reported as fake news", "verify": True},
     {"claim": "Unless crude falls below 85-80 dollars the Indian market cannot sustain recovery", "verify": False},
     {"claim": "Next-month options: 22300 put and 25000 call each near 100 rupees; hedged June structures yield about 10% for the month", "verify": False}],
    ["Before a binary weekend (deal or war), close positions or migrate to next-month series - time value out there is generous",
     "Over-hedge deliberately: buying 2-5 far lots against 1 short lot converts tail risk into tail profit (the technique that saved him on the Feb deal-day gap)"],
    "The most important thing in the stock market is that you should know when to stay away from the market.",
    "Repeats; adds weekend binary warning, hedge ratios",
    BASE_LEAKS + ["workshop promotion x2", "Feb trade-deal-day personal save anecdote", "mood-based exits admission", "I do not follow my own advice admission"])

# 3128 22-May-2026 post
add("3128", "2026-05-22", "post_market",
    "Nifty pierced 23800 intraday but could not close above last Tuesday's 23757; global markets rallied on near-deal optimism while India lagged; FIIs sold over 4000 crore; rate-sensitives outperformed defensives; speaker teases a big-crash video and stays bullish only above a 24000 spot close.",
    {"nifty": 23757, "banknifty": None, "vix": None, "fii_cr": -4000, "dii_cr": 4000},
    [{"claim": "US and Iran reportedly close to striking a deal (22-May-2026); Iran constrained by full oil storage, US by aircraft losses", "verify": True},
     {"claim": "FIIs sold over 4000 crore on 22-May; DIIs bought more, keeping the close positive", "verify": True},
     {"claim": "June series 22000 put near 65 and 25000 call near 100 rupees - rich far premiums", "verify": False}],
    ["Eight sessions unable to reclaim one red candle is the definition of a fragile market",
     "Bank Nifty moving double the Nifty marks high-beta rotation into rate-sensitives - typical of early recovery attempts"],
    "Entire global markets are rallying... but we are just struggling. This is the power of the Prime Minister statement.",
    "Repeats; adds deal optimism, rotation",
    BASE_LEAKS + ["Bangalore workshop next weekend", "tomorrow big-crash video teaser"])

# 3131 25-May-2026 pre
add("3131", "2026-05-25", "pre_market",
    "Fourth petrol-diesel hike (+Rs 3, cumulative ~Rs 8) lands on a day crude fell 5%; RBI policy June 3 may hike rates; speaker caps any Iran-deal rally near +4% (April-8 precedent) and repeats the COVID comparison (wave1 -40% vs wave2 -10%); framework: long-term bearish, short-term headline-driven.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Petrol and diesel hiked about Rs 3 on 25-May-2026 - fourth hike in 10-12 days, cumulative about Rs 8", "verify": True},
     {"claim": "Crude oil fell about 5% to about 95 dollars the same day", "verify": True},
     {"claim": "RBI policy due June 3, 2026 with rate-hike probability after fuel-led inflation", "verify": True},
     {"claim": "April 8 ceasefire rallied Nifty about 4%; a second agreement should not exceed that single-day move (markets do not react twice at full intensity)", "verify": False}],
    ["Markets never repeat the same reaction to the same news: first COVID wave -40%, deadlier second wave -10%",
     "Bearish long-term view does not mean down every day; compounding math (26,000 start and end = zero return) separates trend from noise"],
    "If every day the market goes down, in a few months Nifty has to go to zero.",
    "Repeats weekend binary; adds hike cadence, COVID analogy",
    BASE_LEAKS + ["personal 23000 put conviction position", "two videos mentioned (crash + gap up)", "long-term bearish stance repeated"])

# 3132 25-May-2026 post
add("3132", "2026-05-25", "post_market",
    "First no-reversal day of the May series: the gap-up held all session; India VIX fell 7%; massive last-half-hour short covering pushed the future to a 70-point premium (from discount days earlier); the dreaded Tuesday red candle was finally reclaimed; Bank Nifty outperformed 2.3% vs 1.3%.",
    {"nifty": None, "banknifty": 2.3, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "India VIX fell about 6.74% on 25-May-2026 after repeated 5%+ daily declines", "verify": True},
     {"claim": "Nifty future closed at a 70-point premium one day before expiry after trading at a discount most of the series", "verify": False},
     {"claim": "Bank Nifty rose 2.3% vs Nifty 1.3% led by short covering in HDFC Bank and ICICI Bank; all sectors green except FMCG", "verify": True}],
    ["A sustained gap-up after weeks of failed ones is the first objective evidence of regime change",
     "Premium expansion into expiry (from discount to +70) signals institutional conviction in a further gap"],
    "The gap up sustained - that is one significant thing.",
    "Repeats; adds VIX collapse, candle reclaim",
    BASE_LEAKS + ["Bangalore workshop weekend announcement"])

# 3133 26-May-2026 pre
add("3133", "2026-05-26", "pre_market",
    "Expiry-day setup: euphoria fading (GIFT -80) with no signed deal and reports of US strikes on Iran; the pivotal news is the finance minister saying she is open to discussions on taxation and will take inputs from market participants; speaker shifts his own view from bearish to neutral and trims strikes.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Finance minister said she is open to discussions on taxation and ready to take inputs from stock-market participants (25-26 May 2026)", "verify": True},
     {"claim": "Next-month (June) future traded only about 30 points above the current-month future, collapsing June put premiums", "verify": False},
     {"claim": "Reports of US strikes on Iran although broader talks continue", "verify": True},
     {"claim": "Rupee approaching 100 per dollar - a psychological and political red line for the government", "verify": True}],
    ["When a regulator-fearing government faces election math, market pressure eventually produces policy - 2019 corporate-tax cut was exactly this setup",
     "Roll strikes toward the money (24,000 call to 24,200; 23,500 put to 23,800) when the regime shifts rather than exiting"],
    "The market does not want a finance minister who listens. It wants a finance minister who acts.",
    "Repeats; adds FM statement (key), view flip",
    BASE_LEAKS + ["personal strikes: sold 24000 call + 23500 put, rolled", "December series positions", "workshop participants struggling comment"])

# 3134 26-May-2026 post
add("3134", "2026-05-26", "post_market",
    "Market gives the FM statement a thumbs-down: Nifty follows the 200-point expiry tradition, closes below 24000 and then 23900 for the first time in 8-9 sessions; Taiwan's market cap overtakes India's; extended STT critique (taxing losses is absurd) via the wife-as-STT joke.",
    {"nifty": 23900, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Taiwan's stock market capitalisation overtook India's (late May 2026) despite a population of about 23 million vs 1.4 billion", "verify": True},
     {"claim": "Nifty closed below 24000 and 23900 on 26-May-2026, first time in 8-9 sessions despite the FM statement", "verify": True},
     {"claim": "An influencer filed a Supreme Court case against STT on losing trades (context; case drags for years)", "verify": True},
     {"claim": "STT was sharply increased on February 1 (2026 budget cycle per speaker)", "verify": True}],
    ["Taxing transactions regardless of profit or loss (STT) is unique to India and structurally suppresses liquidity",
     "Good news rejected by the tape is the strongest bearish confirmation available"],
    "Nowhere in the world does the government collect tax when you lose money.",
    "Repeats FM; adds Taiwan cap milestone, STT critique",
    BASE_LEAKS + ["wife-as-STT divorce joke", "travel to Bangalore Friday", "Chennai and Bangalore favorite workshop cities"])

# 3135 27-May-2026 pre
add("3135", "2026-05-27", "pre_market",
    "New-series day one defies the 90%-positive historical pattern: GIFT indicates -100 and FIIs sold even after the FM statement; Nasdaq 100 crossed 30000 with S&P and Nasdaq at record highs while India lags; June straddle math implies a 23000-25000 range; advice: no naked positions, roll weeklies a day early.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Nasdaq 100 crossed 30000; S&P 500 and Nasdaq hit fresh all-time highs (26-27 May 2026)", "verify": True},
     {"claim": "FIIs were net sellers on the first trading day of the June series despite the FM statement", "verify": True},
     {"claim": "June series: five weeks, two holidays, 18 sessions; 24000 straddle ~800 combined implies a 3-3.5% monthly range; with buffer, 23000-25000", "verify": False},
     {"claim": "June-July futures premium shrank from the normal 150 points to about 100", "verify": True}],
    ["First-day-of-series direction is a crowdsignal, but a 90% base rate is not a guarantee - GIFT overrides",
     "Weekly hedges lose margin benefit on expiry day; roll hedges one day before or pay up"],
    "24,000 call and put put together about 800 points - that is the June range the market is pricing.",
    "Repeats Taiwan/FM; adds June structure math",
    BASE_LEAKS + ["correction of his own prior holiday error", "sell calls 4-5% away rule"])

# 3136 27-May-2026 post
add("3136", "2026-05-27", "post_market",
    "A 45-crore compliance issue at HDFC Bank (deposit-interest capping passed off as marketing expense) erased 24000 crore of market cap: HDFC fell about 2%, dragging Bank Nifty ~500 points and Nifty ~70; ITC went ex-dividend; India VIX fell over 5% for a fourth straight day and closed below 15.",
    {"nifty": None, "banknifty": -500, "vix": 15, "fii_cr": None, "dii_cr": None},
    [{"claim": "HDFC Bank deposit-interest/marketing-expense compliance issue worth about 45 crore erased about 24000 crore of market cap (27-May-2026)", "verify": True},
     {"claim": "HDFC Bank fell about 2%, causing ~500-point Bank Nifty and ~70-point Nifty decline; clarification ignored", "verify": True},
     {"claim": "India VIX fell more than 5% for four consecutive days, briefly touching 20 earlier and closing below 15 - a 25%+ collapse", "verify": True},
     {"claim": "ITC turned ex-dividend adjusting about 20 Nifty points", "verify": True}],
    ["Micro news on the highest-weight stock moves the index more than macro - weight, not severity, prices impact",
     "A VIX collapse below 15 (from 20) during a market fall is premium sellers winning - a floor-forming signal"],
    "45 crore is the damage but the market cap fell by 24,000 crore.",
    "Repeats FM, adds HDFC Bank event (key), VIX crash",
    BASE_LEAKS + ["Nirmala Sitharaman candle reference", "sell puts below 23000 / calls above 25000 rule", "personal ratio spread profitable both sides"])

# 3137 29-May-2026 post
add("3137", "2026-05-29", "post_market",
    "The wildest tape of the series: Nifty crossed 24000, then a 3pm cascade took 500 points off the high including a 300-point fall in ten minutes, with the future oddly holding a 225-point premium; MSCI rebalancing blamed; Wipro's AI-deal IT bounce (Infosys +5%) also reversed; HDFC Bank closed 10 points above its 52-week low.",
    {"nifty": 23500, "banknifty": -500, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "On 29-May-2026 Nifty fell over 500 points from high to low in the last hour, including ~300 points between 3:00-3:10pm, then recovered 120 points in the final five minutes", "verify": True},
     {"claim": "MSCI index rebalancing was the attributed cause; speaker doubts rebalancing alone explains 5-minute selling", "verify": True},
     {"claim": "Nifty future held a 225+ point premium while spot broke 23500 - an extreme, unexplained dislocation", "verify": True},
     {"claim": "HDFC Bank touched 735 vs a 52-week low of 725 and a January high above 1000; HDFC+Reliance cut ~90 Nifty points, HDFC+ICICI ~500 Bank Nifty points", "verify": True}],
    ["When futures premium decouples (225 points) from a crashing spot, either index-arb players are trapped or something structural (rebalance flows) is happening - do not average blindly",
     "Five-minute 300-point moves with news explanations that do not add up = flow-driven microstructure, not fundamentals"],
    "Who has the profit to book? People are only booking losses.",
    "Key session; MSCI setup for 3139/3140",
    BASE_LEAKS + ["family function absence", "traveling to Bangalore immediately", "Hope last month low holds"])

# 3139 01-Jun-2026 pre
add("3139", "2026-06-01", "pre_market",
    "MSCI-rebalance post-mortem: estimated ~1 billion outflow but FIIs sold over 20000 crore on Friday with ~2 lakh crore volume suggesting HFT opportunism; a data mixup (NSE vs all-exchange feeds) is corrected; calls trade 4-5 times puts - never seen in 16-17 years; resistance cut from 24800 to 24500.",
    {"nifty": 23550, "banknifty": None, "vix": None, "fii_cr": -20000, "dii_cr": None},
    [{"claim": "FIIs sold over 20000 crore on 29-May-2026 (NSE) / ~21000 crore across exchanges on MSCI rebalancing day, vs an estimated ~1 billion dollar rebalance need; FII volume ~2 lakh crore suggests HFT", "verify": True},
     {"claim": "Call premiums 400-500 points away trade 4-5 times higher than equivalent puts - unprecedented in 16-17 years, later linked to anticipated MSCI selling", "verify": True},
     {"claim": "US closed at all-time high Friday; Japan and Korea at fresh highs Monday while GIFT wobbles", "verify": True},
     {"claim": "Export duty cut on petroleum products announced; Reliance in focus", "verify": True}],
    ["Headline FII numbers need exchange-consolidation checks: NSE-only feeds overstate moves that BSE offsets",
     "Structural flows (index rebalancing) explain option-premium anomalies that sentiment cannot"],
    "The police comes only in the last scene - tax cuts will come only after everything is destroyed.",
    "Repeats MSCI; adds data correction, premium explanation",
    BASE_LEAKS + ["16-17 years trading experience", "I will show you data when back in Chennai", "Bangalore travel"])

# 3140 02-Jun-2026 pre
add("3140", "2026-06-02", "pre_market",
    "Pattern recognition: PM statement then -400/-400; MSCI Friday -300/Monday -300 (future), now GIFT -150 more with the May low 23262 under threat; mega-caps (HDFC Bank 6 years, HUL 5-6, ITC 3, TCS 5-6) have delivered roughly zero returns; speaker's demand hierarchy: abolish STT first, LTCG second; personal call rolls to 24300.",
    {"nifty": 23262, "banknifty": None, "vix": None, "fii_cr": -4000, "dii_cr": 5100},
    [{"claim": "HDFC Bank delivered roughly zero return over six years; HUL five-six years; ITC about three years; TCS five-six years (as of mid-2026)", "verify": True},
     {"claim": "Monday FII sold ~4000 crore (NSE ~3791 / all-exchange ~3900) while DII bought ~4700-5100 crore", "verify": True},
     {"claim": "Friday 29-May FII selling: 20000 crore on NSE, ~21000 crore across all three exchanges (corrected figures)", "verify": True},
     {"claim": "Traders' consensus demand to the finance ministry: abolish STT first (it killed F&O liquidity with 10-15 point spreads), reduce LTCG second", "verify": True}],
    ["The bluest chips returning zero for 3-6 years while taxes rise is the structural case for bearishness - not war headlines",
     "A 1000-point gap buffer rule: sell calls no closer than the largest plausible gap (April deal-day was +1000)"],
    "Whether you make profit or loss you pay STT - that has killed the F&O business.",
    "Repeats MSCI; adds zero-return roll-call, STT hierarchy",
    BASE_LEAKS + ["personal strikes: 23000 put sold, calls rolled 24800-24600-24300", "buy gold comment by PM anecdote", "climax-police metaphor"])

# 3141 02-Jun-2026 post
add("3141", "2026-06-02", "post_market",
    "The double-bottom thesis worked: a 200-point gap-down pierced the May low by 30-40 points, then a 350-point short-covering rally; FIIs sold 7000+ crore even so; IT led (TCS +6%) with HDFC Bank turning positive; VIX fell 7% while the market fell 800 intraday - the bottoming tell; RBI policy moved to Friday and expected a non-event.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": -7000, "dii_cr": None},
    [{"claim": "On 02-Jun-2026 Nifty gapped down ~200, broke the May low (23262) by 30-40 points, rallied 350 from the low, fell 150, and recovered 120 - extreme two-way session", "verify": True},
     {"claim": "FIIs sold over 7000 crore on 2-Jun (after ~21000 Friday and ~3000 Monday) yet the market recovered", "verify": True},
     {"claim": "India VIX fell more than 7% (intraday 8%) while Nifty was down about 800 points intraday - divergence signaling a bottom attempt", "verify": True},
     {"claim": "RBI policy shifted to Friday (5-Jun-2026), expected a non-event: no cut (inflation/rupee), hike unlikely", "verify": True}],
    ["When price makes new lows but VIX refuses to spike, smart money is covering - the tape's most reliable bottoming tell",
     "Overreaction gaps (no escalation, no crude spike) are for fading, not joining"],
    "When the market overreacts, that is when smart people cover their shorts.",
    "Repeats; adds double-bottom validation, RBI Friday",
    BASE_LEAKS + ["personal 23000 put saved from stop", "enjoy my evening closing", "dead cat bounce caution"])

with open("/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_090.jsonl", "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("records:", len(R))
