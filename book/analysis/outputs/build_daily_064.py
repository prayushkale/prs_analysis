#!/usr/bin/env python3
import json

R = []

def rec(id, date, type, summary, levels=None, events=None, lessons=None, quote="", dup_flag="", leaks=None):
    R.append({
        "id": id, "date": date, "type": type, "summary": summary,
        "levels": levels or {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
        "events": events or [], "lessons": lessons or [], "quote": quote,
        "dup_flag": dup_flag, "leaks": leaks or [],
    })

rec("2311a", "2024-08-23", "pre_market",
    "Pre-Jackson Hole caution: markets pricing ~50bp cut expectations; low-volume Sensex expiry Friday could see engineered moves; VIX below 13 warns short-dated option sellers; 25,000-25,100 the critical range.",
    {"nifty": 24500, "banknifty": 51000, "vix": 13, "fii_cr": 1400, "dii_cr": 3000},
    [{"claim": "Markets are pricing in a 50 basis point Fed rate cut ahead of the Jackson Hole symposium speech by the Fed chair on 23 Aug 2024", "verify": True},
     {"claim": "Japan's market fell nearly 10-12% in a single day in early August 2024 (the second Friday of the month)", "verify": True},
     {"claim": "On 22 Aug 2024 both FIIs (~1,400 crore) and DIIs (~3,000 crore) were net buyers in cash", "verify": True},
     {"claim": "Bank Nifty option sellers concentrated around 51,000 (straddle ~700 rupees combined); Nifty 24,500 PE / 25,000 CE sold (~100 rupees combined)", "verify": False}],
    ["When VIX is very low, sellers of short-dated options face sudden large-move risk; keep positions light.",
     "Engineered big moves happen where volumes are thinnest - low-volume expiry days are the danger zone."],
    "Manipulation can be done where the volumes are low.",
    "",
    ["sponsored by indelta.itChange (Delta Exchange garble)", "I am flying to Mumbai for workshop... at Radisson Blue Hotel", "my friend, his name is Sharad. So he is my right hand", "from tomorrow, every Saturday, there will be a video, myself, my friend", "Hope you enjoyed watching this video"])

rec("2311b", "2024-06-24", "pre_market",
    "After a correcting week, a 2,000-point Bank Nifty rally (HDFC Bank, ICICI) lifted indices to records while most stocks fell; budget tax speculation on F&O income looms over July; range 23,000-24,000 with negative bias risk.",
    {"nifty": 24000, "banknifty": None, "vix": None, "fii_cr": -1500, "dii_cr": None},
    [{"claim": "Bank Nifty rallied nearly 2,000 points in the week to 21 Jun 2024 led by HDFC Bank and ICICI Bank, contributing ~600 points to Nifty, yet Nifty rose only ~100 points as most Nifty 50 stocks corrected", "verify": True},
     {"claim": "Media reports ahead of Budget 2024 suggested the government may treat F&O income as speculative income and may introduce TDS/TCS on such trades", "verify": True},
     {"claim": "NVIDIA briefly overtook Apple and Microsoft as the world's most valuable company in June 2024 before seeing selling", "verify": True},
     {"claim": "Reserve Bank of Australia governor signalled possible rate hikes if inflation persists; Australian CPI data due 26 Jun 2024", "verify": True}],
    ["A 200-250 point fall from a recent high is the dip to sell puts below, not to panic.",
     "Speculative-income classification would block expense offsets and loss set-off, multiplying F&O tax outgo."],
    "Whether it is Congress or BJP, every finance minister is looking to mobilize more money for the government.",
    "",
    ["sponsored by Delta.exchange", "some marriage celebrations at home", "P. R. Sundar (name variant)", "Hope you enjoyed watching this video"])

rec("2312a", "2024-06-24", "post_market",
    "Huge unexpected intraday swing - 200+ point fall then full recovery; Bank Nifty 1,000-point swings now standard; five straight closes between 23,500-23,600 form a coil; breakout odds high, 23,000 the floor.",
    {"nifty": 23600, "banknifty": 52000, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Nifty closed between 23,500 and 23,600 for five consecutive trading sessions in June 2024", "verify": True},
     {"claim": "India VIX rose more than 6% on 24 Jun 2024 ahead of the Union Budget", "verify": True},
     {"claim": "Both FIIs and DIIs were net sellers in cash on 24 Jun 2024", "verify": True}],
    ["A resistance tested repeatedly weakens each time - coiled ranges resolve in breakouts.",
     "Position for the resolution of a coil, not for a directional guess."],
    "If you keep hammering a tin many times it gets weaker, and finally one hit breaks it.",
    "same coil thesis as 2313 and 2314 next sessions",
    ["sponsored by Delta.Exchange", "I went for some YouTube video shooting", "Hope you enjoyed watching this video"])

rec("2313", "2024-06-25", "pre_market",
    "Profit booking absorbed by retail dip-buyers; rally narrow to large caps (Reliance, banks, IT); path to 24,000 likelier than 23,000; investors advised staggered buying at -10% and -20% corrections.",
    {"nifty": 23500, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Reliance Industries was range-bound 2,800-3,000 and ICICI Bank near 1,100 for months before breaking out in June 2024", "verify": True},
     {"claim": "Nifty has not corrected more than 20% in 25 years except 2004 (BJP election loss), the 2008 Lehman collapse and COVID 2020, each followed by ~100% rebound within a year", "verify": True},
     {"claim": "A US economist forecast the biggest stock market crash coming in 2025", "verify": True}],
    ["Institutional selling absorbed by fast retail dip-buying is the signature of a bullish undercurrent.",
     "For investors, simple staggered buying at -10% and -20% beats complex timing."],
    "Play with futures, you don't have a future; play with options, you have plenty of options.",
    "",
    ["launching two workshops, one in Bengaluru, one in Mumbai, plus online", "sponsored by Delta.exchange", "most of my followers are traders", "Hope you enjoyed watching this video"])

rec("2314", "2024-06-25", "post_market",
    "Breakout above 23,600 despite weak global cues and both institutions selling; 140 of Nifty's 180-point gain came from three banks; Om Birla's speakership read as coalition stability; box shifts to 23,500-24,000.",
    {"nifty": 23500, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "On 25 Jun 2024, 140 of Nifty's 180-point gain came from HDFC Bank, ICICI Bank and Axis Bank while Next 50, midcap and smallcap indices fell", "verify": True},
     {"claim": "Om Birla was elected Lok Sabha Speaker on 26 Jun 2024, signalling coalition partners could not pressure the BJP", "verify": True},
     {"claim": "India's fiscal deficit data released around 24-25 Jun 2024 came in lower", "verify": True}],
    ["Markets want a stable government more than any particular ruling party.",
     "A narrow, heavyweight-led breakout can extend when leadership rotates to the next laggard sector."],
    "No matter who rules the country, what the stock market wants is a stable government.",
    "extends coil/breakout thesis of 2312a-2313",
    ["sponsored by Delta.exchange", "workshop.prsunder.com", "launching workshop in Bangalore and Mumbai", "Hope you enjoyed watching this video"])

rec("2315a", "2024-08-26", "post_market",
    "Gap filled and second-highest close (~25,010) recovering the whole Japan-carry crash; FIIs buying three straight days; Nifty technically long above 24,975; speaker discloses a synthetic long hedged with a December 26,000 put.",
    {"nifty": 25010, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "By 26 Aug 2024 Nifty had recovered the entire ~1,000-point fall from the early-August Japan carry-trade crash and closed around 25,010", "verify": True},
     {"claim": "FIIs were net cash buyers for three consecutive sessions (22-26 Aug 2024) after selling ~1.5 lakh crore over the prior 8-9 months", "verify": True},
     {"claim": "Cabinet approved the Unified Pension Scheme on 24 Aug 2024", "verify": True}],
    ["Crash-day gaps act as magnets: once the first gap fills, the second follows.",
     "Fresh longs this late in a run need a full edge - hedged structures, not naked exposure."],
    "Technical is only probability, not certainty.",
    "",
    ["sponsored by Delta.exe", "Piers from (name garble)", "Hope you enjoyed watching this video"])

rec("2315b", "2024-06-26", "pre_market",
    "After a 3,000-point six-session Bank Nifty surge with no macro news, expects consolidation; three banks gave 140 of 180 points; FII 3,500 crore sell / DII 5,000 crore buy flip; 23,800 max-OI strike is the magnet.",
    {"nifty": 23800, "banknifty": None, "vix": None, "fii_cr": -3500, "dii_cr": 5000},
    [{"claim": "Bank Nifty rose ~3,000 points across six sessions to 26 Jun 2024, contributing ~1,100 points to Nifty, while Nifty rose only 300-350 points", "verify": True},
     {"claim": "On 25 Jun 2024 FIIs sold about 3,500 crore while DIIs bought about 5,000 crore in cash", "verify": True},
     {"claim": "On 4 Jun 2024 election-results day Nifty fell nearly 10% intraday but recovered to close only 2-3% lower", "verify": True}],
    ["Big news-less narrow rallies tend to consolidate the next day: shorts are covered and buyers are done.",
     "After an outsized move, short options into the follow-through lull."],
    "If the market makes a very big move and you do a straddle or strangle, uniformly the next day you will get some profit.",
    "140/180-points leadership stat repeats from 2314",
    ["sponsored by Delta.Exchange", "what we teach in our workshops", "Hope you enjoyed watching this video"])

rec("2316a", "2024-06-26", "post_market",
    "Second straight rally: Reliance contributed 85 of 150 points (Jio tariff hopes), Vedanta promoter selling over 10,000 crore weighed; Nifty within sight of 24,000; heavy put OI added at 23,800/23,700.",
    {"nifty": 23850, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Reliance rose more than 4% on 26 Jun 2024 on expected Jio tariff hikes, contributing ~85 of Nifty's 150-point gain", "verify": True},
     {"claim": "Vedanta promoters were selling shares worth more than 10,000 crore in June 2024", "verify": True},
     {"claim": "From the 4 Jun 2024 low to 26 Jun 2024 the Nifty rallied 13-15%", "verify": True}],
    ["HDFC Bank and Reliance together carry about a quarter of Nifty - two strong stocks can hide weak breadth.",
     "Near expiry the same rally decays premiums instead of spiking them - timing changes strategy outcomes."],
    "If tomorrow TCS or Infosys start moving higher, Nifty can easily test 24,000.",
    "",
    ["sponsored by Delta.exchange", "now only I am getting a call from my old friends", "Hope you enjoyed watching this video"])

rec("2316b", "2024-08-27", "pre_market",
    "Flat-to-negative open ahead of NVIDIA results tonight; FIIs buying a third straight day; Nifty technically long (24,975 trigger), Bank Nifty needs 51,800; December straddles price a 24,000-26,000 month.",
    {"nifty": 24975, "banknifty": 51800, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "NVIDIA results due 28 Aug 2024 treated as the key market risk; the stock had earlier fallen ~40% then rebounded ~30%", "verify": True},
     {"claim": "Intel shares fell about 30% in one day after weak results in early August 2024", "verify": True},
     {"claim": "FIIs net cash buyers for the third consecutive day (27 Aug 2024)", "verify": True}],
    ["Technical triggers are tiered: Bank Nifty confirming above 51,800 gates the next index leg.",
     "Before binary results, positioning thins - the surprise lands on a light book."],
    "Markets don't move in one straight line; they move up, down, up, down, then one day break out.",
    "FII 3-day buying streak and NVIDIA caution repeat 2315a/2316a themes",
    ["sponsored by Delta.exe", "Find this is Pia Sundar (name garble)", "Hope you enjoyed watching this video"])

rec("2317a", "2024-08-27", "post_market",
    "Consolidation just under 25,000 with late-session selling; DIIs booking profits after a long absence while FIIs bought a fourth day; 25,000 straddle (~200 rupees) frames 24,800-25,200; FinNifty expiry volatile.",
    {"nifty": 25000, "banknifty": 51400, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "DIIs booked profits in cash for a fourth straight session on 27 Aug 2024 while FIIs kept buying", "verify": True},
     {"claim": "Nifty fell in the last 45 minutes on 27 Aug 2024 yet closed near 25,000 on a weighted-average basis", "verify": True}],
    ["The last 45 minutes reveals true institutional intent - sell programmes show up at the close.",
     "Watch when DIIs flip to profit-booking at highs; until retail absorbs, upside is capped."],
    "Markets need consolidation so that people can adjust their positions.",
    "",
    ["sponsored by Delta.exchange", "Piers from the (name garble)", "Hope you enjoyed watching this video"])

rec("2317b", "2024-06-27", "pre_market",
    "Monthly expiry day: confusing flows (FII -3,500 crore / DII +5,000 crore); Australian inflation beat expectations; 23,800 PE max OI with 24,000 CE caps expiry between 23,725 and 24,075; rally still narrow.",
    {"nifty": 23800, "banknifty": None, "vix": None, "fii_cr": -3500, "dii_cr": 5000},
    [{"claim": "Australian inflation came in higher than expected on 26 Jun 2024, reviving rate-hike worries", "verify": True},
     {"claim": "On 26 Jun 2024 FIIs sold ~3,500 crore and DIIs bought ~5,000 crore in Indian cash equities", "verify": True},
     {"claim": "For the June 2024 expiry, 23,800 put carried the highest open interest and 24,000 call the highest call OI", "verify": True}],
    ["Expiry-day cash data skews to FII selling because hedges are unwound in futures that day.",
     "Max-OI strangle strikes frame the expiry landing zone: breakevens are strike minus/plus collected premium."],
    "One day FIIs buy, the next day they sell - there is no clear trend; the undercurrent is what matters.",
    "narrow-leadership theme repeats 2314/2315b",
    ["sponsored by Delta.exchange", "Hope you enjoyed watching this video"])

rec("2318a", "2024-06-27", "post_market",
    "Expiry near 24,050 after a 700-point three-session rally rotating banks to Reliance to IT; June series ended +1,500 (Nifty) and +4,000 (Bank Nifty); ICICI Bank +10% in three days after six flat months; July the budget honeymoon.",
    {"nifty": 24050, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "June 2024 series ended with Nifty up more than 1,500 points and Bank Nifty up nearly 4,000 points (27 Jun 2024 expiry)", "verify": True},
     {"claim": "ICICI Bank rallied about 10% in three days in late June 2024 after roughly six months range-bound near 1,100", "verify": True},
     {"claim": "The previous 1,500-point monthly Nifty rally was November 2023, when the BJP won three key state elections", "verify": True},
     {"claim": "Accenture's June 2024 results showed weak forward prospects, capping TCS and Infosys", "verify": True}],
    ["Leadership rotation - banks, then Reliance, then IT - sustains a rally even with negative breadth.",
     "Patient holders get paid in lumps: months of nothing, then a year's return in days."],
    "Real life begins after the honeymoon period; July is still the honeymoon and the budget is the main event.",
    "",
    ["sponsored by Delta dot exchange", "workshop dot P R Sunder dot com", "in person workshop in Bangalore, Mumbai as well as Chennai", "I also have a Bank Nifty 50,000 short straddle for July series", "Hope you enjoyed watching this video"])

rec("2318b", "2024-08-28", "pre_market",
    "Day before Nifty expiry with a fresh-record attempt; Infosys ADR +1.6% flags IT strength; aggressive call writing 25,000-25,200 vs ITM 51,300 PE on Bank Nifty; NVIDIA tonight keeps books light; 24,700-25,300 expected hold.",
    {"nifty": 25010, "banknifty": 51300, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Nifty closed around 25,010 on 27 Aug 2024, its second-highest close, just below the record 25,020", "verify": True},
     {"claim": "Infosys ADR rose 1.6% overnight (27 Aug 2024)", "verify": True},
     {"claim": "December-2024 series 25,000 straddle was taken aggressively, pricing a roughly 24,000-26,000 month", "verify": False}],
    ["ITM put OI outpacing OTM call OI is a tell of relative institutional bullishness.",
     "Desks de-risk ahead of NVIDIA-style binary events; expect compressed expiry ranges until the print."],
    "",
    "NVIDIA caution and FII streak repeat 2316b",
    ["sponsored by Delta.exchange", "Pia Sundar (name garble)", "Hope you enjoyed watching this video"])

rec("2319a", "2024-08-28", "post_market",
    "Fresh all-time high near 25,100 led by IT (Infosys +2.5%); DIIs sold into strength late; the two-month 24,000-25,000 box decisively broken so 25,000 flips to support; speaker runs 24,850 PE / 25,250 CE into expiry.",
    {"nifty": 25100, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Nifty set fresh intraday and closing all-time highs around 25,100 on 28 Aug 2024, decisively out of its 24,000-25,000 two-month box", "verify": True},
     {"claim": "Infosys rose about 2.5% on 28 Aug 2024, leading the IT complex", "verify": True},
     {"claim": "Speaker sold the 24,850 put and 25,250 call for the 29 Aug 2024 expiry (personal positioning disclosure)", "verify": False}],
    ["A decisively broken multi-month box turns old resistance into new support.",
     "Even mid-rally, traders de-risk into binary events like NVIDIA results."],
    "You ask me the reason? Simple. I sold the 24,850 put and the 25,250 call, so I wish Nifty closes between them.",
    "",
    ["sponsored by Delta.exchange", "Last week I had workshop in Mumbai", "workshop for US market traders... workshop in Chennai", "I appear on some television channels", "Pierre Sundar (name garble)", "Hope you enjoyed watching this video"])

rec("2319b", "2024-07-01", "pre_market",
    "A 1,000-point tear from Monday's low into the new series; unusual expiry-day FII buying of 7,500+ crore; Jio tariff-hike news supercharges Reliance; July range set at 23,000-25,000 with PCR near 1.5; tax headlines read as trial balloons.",
    {"nifty": 24150, "banknifty": None, "vix": None, "fii_cr": 7500, "dii_cr": None},
    [{"claim": "Reliance Jio raised telecom tariffs around 30 Jun-1 Jul 2024 with Airtel and Vodafone Idea expected to follow", "verify": True},
     {"claim": "FIIs bought more than 7,500 crore in cash on 27 Jun 2024, unusual for an expiry day when hedges unwind", "verify": True},
     {"claim": "Indian index options volumes grew many-fold between 2018 and 2024", "verify": True}],
    ["Expiry-day FII buying instead of the usual hedge-unwind selling signals an unusually strong institutional hand.",
     "Governments float tax trial balloons through planted media stories to soften the eventual blow."],
    "Buy on rumor, sell on news - smart people bought already; the common man buys today.",
    "",
    ["sponsored by Delta.exchange", "PR Sundar... became famous in 2018", "I attended one conference in Mumbai", "that is what we teach in our workshops", "a Tamil movie called Thani Oruvan", "marriage functions in my house", "Hope you enjoyed watching this video"])

rec("2320a", "2024-06-28", "post_market",
    "Week of five straight up sessions (+4%) ends in consolidation: Reliance gained on telecom-tariff news while private banks profit-booked after 10% runs; breadth finally positive with mid/small caps leading; close decisively above 24,000.",
    {"nifty": 24030, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "US PCE inflation data released 28 Jun 2024 evening was the key weekend risk", "verify": True},
     {"claim": "Telecom tariff hikes announced in late June 2024: Reliance rallied while Bharti Airtel and Vodafone Idea sold off on the news", "verify": True},
     {"claim": "ICICI Bank and Reliance each rose more than 10% in the week to 28 Jun 2024", "verify": True}],
    ["Buy on rumor, sell on news splits one event into winners and losers within the same sector.",
     "Friday profit-booking before US data is routine - the dip is the trade, not the exit."],
    "This is the week the bulls can never forget.",
    "wraps up the same week narrated in 2314-2318a",
    ["sponsored by delta.exchange", "PR Sunder (name garble)", "Hope you enjoyed watching this video"])

rec("2320b", "2024-08-29", "pre_market",
    "NVIDIA results out: good numbers, stock -7% on pricing-to-perfection; US VIX fell 8.5%; first session of the September series; FIIs accelerating buyers, DIIs back too; speaker discloses a December 25,000/26,000 call ratio.",
    {"nifty": 25000, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "NVIDIA reported good results on 28 Aug 2024 but the stock still fell about 7%, having been priced to perfection", "verify": True},
     {"claim": "The US VIX fell about 8.5% after NVIDIA results (28-29 Aug 2024)", "verify": True},
     {"claim": "August 2024 series: Nifty opened the month around 24,400, jumped 400 points on day one and closed ~600 points higher near 25,000", "verify": True}],
    ["A great print can still sell off when expectations are priced to perfection.",
     "First sessions of a series trend disproportionately - wait out the first half before positioning."],
    "Priced to perfection - a small disappointment and the stock falls so much.",
    "",
    ["sponsored by Delta Data Exchange", "Pierre Sunderr (name garble)", "Hope you enjoyed watching this video"])

rec("2321b", "2024-08-29", "post_market",
    "Expiry-day chaos: Reliance 1:1 bonus at the AGM spiked Nifty toward 25,200 then violent swings - the speaker flipped from 5 lakh profit to 20 lakh loss on jumped stop-losses; Nifty still closed at a record ~25,150.",
    {"nifty": 25150, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "Reliance Industries announced a 1:1 bonus issue at its AGM on 29 Aug 2024", "verify": True},
     {"claim": "On 29 Aug 2024 Nifty swung ~800-1,000 points intraday, closing at a fresh record near 25,150", "verify": True},
     {"claim": "Haryana and Jammu & Kashmir election results were due in early October 2024 (speaker says 4 October)", "verify": True}],
    ["Around blockbuster news, stop-losses jump past their triggers - size down instead of trusting stops.",
     "1,000-point expiry swings destroy intraday traders; positional books with adjustments survive."],
    "Stop loss jumps - that is how a 5 lakh profit became a 20 lakh loss.",
    "",
    ["sponsored by Delta.exchange", "Piers from the (name garble)", "Hope you enjoyed watching this video"])

rec("2322b", "2024-08-30", "pre_market",
    "First session of the September series: Nifty technically long, FIIs+DIIs bought ~6,000 crore combined, NVIDIA risk passed with US VIX -8.5%; supports 24,800/24,650/24,500, target 26,000; warns the first session trends.",
    {"nifty": 24500, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "FIIs and DIIs together bought about 6,000 crore in cash on 29 Aug 2024", "verify": True},
     {"claim": "August 2024 series: Nifty started at 24,400, jumped 400 points on the first session and gained ~750 points for the month", "verify": True}],
    ["First sessions of a monthly series trend disproportionately; keep the first half light.",
     "In a confirmed technical uptrend, sell puts at support rather than chase longs 200 points above the trigger."],
    "Easy to make money, easier to lose money - better safe than sorry.",
    "September-series framing repeats from 2321b",
    ["sponsored by Delta.exchange", "we are not SEBI-registered", "that is what we teach in our workshop", "Pierre Sunde (name garble)", "Hope you enjoyed watching this video"])

rec("2323a", "2024-08-30", "post_market",
    "Friday trending risk played out: +250 spike then -100 fade; MSCI's ~$6 billion inflow talk failed to lift HDFC Bank - banking lag since Budget day persists; DIIs sold 3,200 crore vs FII 5,300 crore buying; 25,000-26,000 the bull path.",
    {"nifty": 25300, "banknifty": None, "vix": None, "fii_cr": 5300, "dii_cr": -3200},
    [{"claim": "MSCI rebalancing was expected to bring about $6 billion into Indian equities around 30 Aug 2024, with HDFC Bank a major recipient", "verify": True},
     {"claim": "On 30 Aug 2024 FIIs bought ~5,300 crore while DIIs sold ~3,200 crore in cash", "verify": True},
     {"claim": "Bank Nifty lagged roughly 2,000 points (about 4%) below its all-time high as of 30 Aug 2024", "verify": True}],
    ["Reported passive inflows do not guarantee same-day index behavior - the mechanism works over days.",
     "Bank Nifty catching up its 2,000-point lag alone hands Nifty ~600 points toward 26,000."],
    "If the first trading day is a trending day, its low often holds for the entire series.",
    "",
    ["sponsored by Delta.exchange", "Pias on that (name garble)", "I had some pre-budget discussion in one television channel", "Hope you enjoyed watching this video"])

rec("2323b", "2024-07-01", "pre_market",
    "After Friday's profit-booking despite in-line US inflation, Monday re-risks; flow signals flip-flop daily while retail does the profit-booking; budget likely 25-26 July and IT results start 11 July; PCR near 1.5 counsels downside caution.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": -100, "dii_cr": 6000},
    [{"claim": "US inflation data released 28 Jun 2024 came in line with expectations and lower than prior months", "verify": True},
     {"claim": "Parliament session set for 24 Jul-9 Aug 2024, implying the Union Budget on 25-26 Jul 2024", "verify": True},
     {"claim": "TCS results scheduled for 11 Jul 2024 and HCL Tech 12 Jul 2024, starting Q1 earnings season", "verify": True},
     {"claim": "Infosys had not held campus hiring for about two years as of mid-2024, signalling IT-sector stress", "verify": True}],
    ["Retail, not institutions, now does the profit-booking at highs - flows read differently in this regime.",
     "A put-call ratio near 1.5 is comfort on rallies but fragility on bad news."],
    "I have a right to be wrong.",
    "flow flip-flop narrative repeats 2317b/2323a",
    ["sponsored by Delta.exchange", "P. R. Sundar (name variant)", "Hope you enjoyed watching this video"])

rec("2324a", "2024-07-01", "post_market",
    "Monday continuation: mid-cap IT (Wipro, Tech Mahindra) led sectoral rotation into beaten-down tech; Bank Nifty fell 700-800 then recovered ~500; OI stacks supports every 500 points to 23,000 with 25,000 the lone resistance; PCR eased to 1.46.",
    {"nifty": None, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "On 1 Jul 2024 midcap IT stocks (Wipro, Tech Mahindra) led a sectoral rotation while heavyweight banks fell 700-800 points intraday then recovered ~500 from the low", "verify": True},
     {"claim": "The midcap index hit a fresh all-time high on 1 Jul 2024", "verify": True}],
    ["Bull markets rotate: money leaves the freshly up-10% sector for the beaten-down laggard.",
     "Put-call ratio easing from 1.49 to 1.46 shows profit-taking that keeps rallies sustainable."],
    "In a bull market, sectoral rotation keeps the party going.",
    "same-day companion to 2323b",
    ["sponsored by Delta.Exchange", "P. R. Sundar (name variant)", "Hope you enjoyed watching this video"])

rec("2325b", "2024-07-02", "pre_market",
    "Second session: DIIs bought ~10,000 crore over two days vs token FII selling; Bank Nifty 53,180 ATH then -1,000 correction; 53,000 call max OI caps expiry; Adani-Hindenburg round two expected as a 2-5% non-event, not a January-2023 repeat.",
    {"nifty": None, "banknifty": 53000, "vix": None, "fii_cr": -450, "dii_cr": 10000},
    [{"claim": "On 30 Jun-1 Jul 2024 DIIs bought nearly 10,000 crore across two sessions while FIIs sold less than 450 crore", "verify": True},
     {"claim": "Bank Nifty hit a fresh all-time high of 53,180 in early July 2024 before correcting almost 1,000 points", "verify": True},
     {"claim": "Hindenburg published a new report (a reply to SEBI) on the Adani group on 1-2 Jul 2024; speaker expects a 2-5% reaction versus the ~20-25% fall of January 2023", "verify": True},
     {"claim": "India manufacturing PMI and GST collections for June 2024 came in strong", "verify": True}],
    ["Markets do not react to the same bad news twice with equal force - repetition breeds immunity.",
     "At highs, prefer selling puts at supports over chasing calls that decay."],
    "First time is a surprise; second time it is not a surprise.",
    "",
    ["sponsored by delta.exchange", "P. R. Sunder (name variant)", "Hope you enjoyed watching this video"])

rec("2326a", "2024-09-02", "pre_market",
    "Flat open with US closed (Labor Day); Friday's Q1 FY25 GDP of 6.7% (vs ~8.3% a year earlier) and weak auto sales clash with euphoric price action - 10 IPOs last week, one SME asking 12 crore drew ~5,000 crore; Fed's 18 Sep cut hopes underpin.",
    {"nifty": 25700, "banknifty": None, "vix": None, "fii_cr": 5000, "dii_cr": -3000},
    [{"claim": "India Q1 FY25 GDP growth came in at 6.7% on 30 Aug 2024, down from about 8.3% a year earlier", "verify": True},
     {"claim": "About 10 IPOs launched in the week ending 30 Aug 2024; one SME IPO seeking 12 crore received about 5,000 crore of subscription", "verify": True},
     {"claim": "Maruti, Hyundai and others posted lower auto sales in August 2024 ahead of the festival season; TVS was the exception", "verify": True},
     {"claim": "The US Fed was expected to cut rates by up to 50 basis points at the 18 September 2024 meeting", "verify": True}],
    ["When price euphoria diverges from softening fundamentals (GDP, autos, IPO froth), book partial profits in speculative pockets.",
     "Large caps cushion both ways; the froth lives in SMEs and microcaps."],
    "Clearly this market is not for investors, it is for traders.",
    "",
    ["sponsored by Delta.exe", "P.S. from the (name garble)", "Hope you enjoyed watching this video"])

rec("2326b", "2024-07-03", "pre_market",
    "HDFC Bank's FII holding slipping below 55% triggers MSCI-weight increase expectations (est. $3-4 billion inflows); ADR +4.5% pre-open; insider front-running suspected in Tuesday's 1.5% rise; the day belongs to HDFC Bank.",
    {"nifty": 24120, "banknifty": None, "vix": None, "fii_cr": None, "dii_cr": None},
    [{"claim": "HDFC Bank's shareholding pattern showed FII ownership below 55%, triggering expectations of a higher MSCI weight and an estimated $3-4 billion index inflow", "verify": True},
     {"claim": "HDFC Bank's US ADR rose about 4.5% on 2 Jul 2024", "verify": True},
     {"claim": "HDFC Bank made a 52-week low on 14 Feb 2024 and was ~30% above it by July 2024", "verify": True},
     {"claim": "When the RBI reopened the FII buying window for HDFC Bank (around 2019-20), the stock gapped up about 10% the next day", "verify": True}],
    ["Index-weight mechanics turn ownership-threshold crossings into large mechanical passive flows.",
     "Good company plus hated price equals the long-term buying window; markets overreact both ways."],
    "If a good company with a good promoter is falling for the wrong reasons, that is the time to buy.",
    "",
    ["sponsored by Delta.exchange", "P. A. Sundar (name garble)", "Hope you enjoyed watching this video"])

OUT = "/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_064.jsonl"
with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(R), "records to", OUT)
