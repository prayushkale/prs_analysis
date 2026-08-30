#!/usr/bin/env python3
"""Convert the manuscript markdown to Typst-native .typ format."""
import re, sys
text = open('/home/ubuntu/repos/prs_analysis/book/final/manuscript.md').read()
# headings: ## -> = (level 2) etc.
text = re.sub(r'^### (.*)$', r'==== \1', text, flags=re.M)
text = re.sub(r'^## (.*)$', r'=== \1', text, flags=re.M)
text = re.sub(r'^# (.*)$', r'== \1', text, flags=re.M)
# bold: **text** -> *text*
text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', text)
# italic: *text* -> _text_
text = re.sub(r'(?<!\*)\*(?!\*)(.+?)\*\*(?!\*)', r'_\1_', text)  # broken, just use regex
# Actually simpler: ** -> *, * -> _ (single asterisk italic, double bold)
# But there are mixed patterns. Let me do two passes.
text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
text = re.sub(r'(?<!\*)\*(?![* ])(.+?)(?<!\*)\*(?!\*)', r'_\1_', text)
# remove stray * that are emoji or escaped
# tables: convert markdown tables to typst tables
def table_replace(m):
    rows = m.group(0).split('\n')
    # header separator
    out = '#table(\n  columns: ' + str(len(rows[0].split('|')) - 2) + ',\n'
    # header row
    headers = [h.strip() for h in rows[0].split('|') if h.strip()]
    out += '  ' + ', '.join(f'[{h}]' for h in headers) + ',\n'
    for row in rows[2:]:  # skip separator
        if not row.strip(): continue
        cells = [h.strip() for h in row.split('|') if h.strip()]
        if cells:
            out += '  ' + ', '.join(f'[{c}]' for c in cells) + ',\n'
    out += ')'
    return out
text = re.sub(r'\|.+\|\n\|[-:| ]+\|\n(\|.+\|\n)+', table_replace, text)
# footnotes/endnotes: [^N] -> typst footnote
text = re.sub(r'\[\^(\d+)\]', r'#footnote[\1]', text)
# Footnote definition lines: [^N]: text -> remove (typst handles inline)
text = re.sub(r'^\[\^(\d+)\]: (.*)$', r'', text, flags=re.M)
# code blocks: ``` -> ``` but inside we also have backticks -> typst raw blocks
text = re.sub(r'```(\w*)\n(.*?)```', r'```typ\n\2\n```' if False else r'```\n\2\n```', text, flags=re.S)
# Actually just keep as ``` for raw
# lists: - item -> - item (typst supports this)
# auto-build type: preamble
text = text.strip()
# remove multiple blank lines
text = re.sub(r'\n{3,}', '\n\n', text)
open('/home/ubuntu/repos/prs_analysis/book/final/build/chapters.typ', 'w').write(text)
print("converted to chapters.typ")