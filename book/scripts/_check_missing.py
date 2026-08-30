#!/usr/bin/env python3
import json, glob, os

ROOT = "/home/ubuntu/repos/prs_analysis"
idx = json.load(open(f"{ROOT}/book/events/bulk_verify_queue.json"))

done = set()
for f in glob.glob(f"{ROOT}/book/events/verified_batch_*.jsonl"):
    base = os.path.basename(f)
    try:
        done.add(int(base.split("_")[2].split(".")[0]))
    except (IndexError, ValueError):
        print(f"unexpected file: {f}")

total = (len(idx) + 9) // 10
print(f"Total queue items: {len(idx)}")
print(f"Batches total (10/batch): {total}")
print(f"Done batches: {len(done)}")

missing = [i for i in range(total) if i not in done]
print(f"Missing batches: {len(missing)}")
for i in sorted(missing):
    s = i * 10
    e = min(s + 10, len(idx))
    claims = idx[s:e]
    dates = [c.get("date") or "nodate" for c in claims]
    km = [c["claim"][:60].replace("\n", " ").replace("\r", "") for c in claims]
    print(f"  ver_{i:03d}: {len(claims)} claims, dates={dates[0]}..{dates[-1]}, first-claim: {km[0]}")