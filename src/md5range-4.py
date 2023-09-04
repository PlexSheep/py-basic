#!/usr/bin/env python3
import hashlib
BASE: str = "foobar"
MAX = 1000000
SEARCH = "2718"

count = 0

for i in range(0, MAX):
    num: str = ("%06d" % i)
    current = BASE + num
    res = hashlib.md5(current.encode()).digest().hex()
    if SEARCH == res[:4]:
        count += 1
        print("%06d | %s" % (i, res))
        break


print(f"\nFound %d digests matching the search" % count)
