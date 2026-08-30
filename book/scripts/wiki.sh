#!/bin/bash
# wiki.sh - Wikipedia search; prints top titles + extracts
q="$1"
curl -s --max-time 25 "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&srlimit=5&format=json" \
  -A "Mozilla/5.0 (book-factcheck)" | python3 -c "
import sys, json, re
d = json.load(sys.stdin)
res = d.get('query', {}).get('search', [])
if not res:
    print('NO RESULTS'); sys.exit()
for r in res:
    snip = re.sub('<[^>]+>', '', r.get('snippet', ''))
    print('-', r.get('title'))
    print('  ', snip[:250])
    print()
"