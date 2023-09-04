#!/usr/bin/env python3
import hashlib
import sys
to_hash = "foobar19"
hashed = hashlib.md5(to_hash.encode())
print(hashed.digest().hex())
