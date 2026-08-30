#!/usr/bin/env python3
"""Throttled verifier: uses searchhelper with long gaps, caches to disk."""
import json, os, sys, time, urllib.request

sys.path.insert(0, "/home/ubuntu/repos/prs_analysis/book/scripts")
try:
    from searchhelper import wiki_search, get_json
except Exception as e:
    print("import fail", e)
    sys.exit(1)

CACHE = "/tmp/verify_cache.json"
cache = {}
if os.path.exists(CACHE):
    cache = json.load(open(CACHE))

def cached_search(q):
    if q in cache:
        return cache[q]
    for attempt in range(3):
        try:
            r = wiki_search(q)
            if r and r[0][0] != "ERROR":
                cache[q] = r
                json.dump(cache, open(CACHE, "w"))
                return r
            print("  retry (err)", r)
        except Exception as e:
            print("  retry (exc)", e)
        time.sleep(12)
    return [("ERROR", "rate-limited")]

if __name__ == "__main__":
    q = sys.argv[1]
    for title, snip in cached_search(q):
        print(f"* {title}\n  {snip[:220]}")