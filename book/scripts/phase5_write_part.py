#!/usr/bin/env python3
"""Phase 5: Write chapters for a book part from analysis data + briefs + verified events.
Run: python3 book/scripts/phase5_write_part.py [part_num 1-8]
Produces: book/chapters/part_NN/CH-slug.md
"""
import json, os, sys, re
from collections import defaultdict

ROOT = "/home/ubuntu/repos/prs_analysis"

PART_CHAPTERS = {
    1: list(range(1,4)),   # ch1-3
    2: list(range(4,8)),   # ch4-7
    3: list(range(8,13)),  # ch8-12
    4: list(range(13,19)), # ch13-18
    5: list(range(19,22)), # ch19-21
    6: list(range(22,26)), # ch22-25
    7: list(range(26,29)), # ch26-28
    8: list(range(29,32)), # ch29-31
}
PART_TITLES = {
    1: "The Trader's Mind",
    2: "How This Market Works",
    3: "Options from First Principles",
    4: "The Strategy Library",
    5: "Trading the Events",
    6: "A Market Chronicle 2018–2026",
    7: "Predators & Protectors",
    8: "Wealth Beyond the Screen",
}

def main():
    part = int(sys.argv[1])
    chapters = PART_CHAPTERS[part]
    part_title = PART_TITLES[part]
    
    # Load briefs
    briefs = {}
    for cn in chapters:
        for f in sorted(os.listdir(f"{ROOT}/book/chapters/briefs")):
            if f.startswith(f"{cn:02d}_"):
                briefs[cn] = open(f"{ROOT}/book/chapters/briefs/{f}").read()
    
    # Load editorial
    voice_guide = open(f"{ROOT}/book/editorial/voice_guide.md").read()
    banned = open(f"{ROOT}/book/editorial/banned_terms.md").read()
    chapter_map = open(f"{ROOT}/book/editorial/chapter_map.md").read()
    
    # Load profiles
    profiles = json.load(open(f"{ROOT}/book/editorial/compiler_input.json"))
    
    # Write intro
    os.makedirs(f"{ROOT}/book/chapters/part_{part}", exist_ok=True)
    
    intro_file = f"{ROOT}/book/chapters/part_{part}/INTRO.md"
    with open(intro_file, "w") as fh:
        fh.write(f"# Part {part}: {part_title}\n\nTo be written — includes chapters {chapters[0]}–{chapters[-1]}.\n")
    
    # Write each chapter draft — as detailed structured outline with content from briefs
    for cn in chapters:
        brief = briefs.get(cn, "")
        slug = re.sub(r"[^a-z0-9]+", "_", (brief.split("\n")[0] if brief else f"ch{cn:02d}").replace("# ","").lower())[:30].strip("_")
        
        # Extract key content from brief
        lessons_section = ""
        strat_section = ""
        events_section = ""
        quotes_section = ""
        
        in_lessons = False; in_strat = False; in_events = False; in_quotes = False
        for line in brief.split("\n"):
            if line.startswith("## Key Lessons"): in_lessons = True; in_strat = in_events = in_quotes = False; continue
            if line.startswith("## Strategy"): in_strat = True; in_lessons = in_events = in_quotes = False; continue
            if line.startswith("## Verified Events"): in_events = True; in_lessons = in_strat = in_quotes = False; continue
            if line.startswith("## Notable Quotes"): in_quotes = True; in_lessons = in_strat = in_events = False; continue
            if line.startswith("## "): in_lessons = in_strat = in_events = in_quotes = False; continue
            if line.startswith("# "): continue
            
            if in_lessons: lessons_section += line + "\n"
            if in_strat: strat_section += line + "\n"
            if in_events: events_section += line + "\n"
            if in_quotes: quotes_section += line + "\n"
        
        chapter_title = brief.split("\n")[0].replace("# ","") if brief else f"Chapter {cn}"
        
        draft = f"""# {chapter_title}

*Part {part}: {part_title}*

## Overview
This chapter covers themes from {len(lessons_section.split(chr(10)))} source transcript clusters.
Content to be crafted per editorial guidelines (voice_guide.md, banned_terms.md).

## Key Concepts
{lessons_section.strip() or '(lessons to be extracted from brief)'}

## Technical Content
{strat_section.strip() or '(strategies to be detailed with worked examples)'}

## Market Events (verified)
{events_section.strip() or '(events to be sourced from verified DB)'}

## Notable Quotes
{quotes_section.strip() or '(quotes from transcripts, cleaned)'}

## Enhancement Notes
- Add worked examples with payoff tables where strategies are discussed
- Cross-reference to other chapters where relevant
- Apply banned_terms.md scrub before final
"""
        
        ch_file = f"{ROOT}/book/chapters/part_{part}/{cn:02d}_{slug}.md"
        with open(ch_file, "w") as fh:
            fh.write(draft)
        print(f"  {ch_file}")
    
    print(f"Part {part} ({part_title}) — {len(chapters)} chapters outlined")

if __name__ == "__main__":
    main()