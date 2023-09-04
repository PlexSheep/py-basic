import hashlib
import sys
BASE: str = "foobar"
MAX = 1000000
SEARCH = "00"

results: list[str] = []
count = 0

for i in range(0, MAX):
    num: str = ("%06d" % i)
    current = BASE + num
    results.append(hashlib.md5(current.encode()).digest().hex())

for res in results:
    if SEARCH == res[:2]:
        count += 1
        print(res)

print(f"\nFound %d digests matching the search" % count)
