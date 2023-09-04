import hashlib
import sys
hashed = hashlib.md5(sys.argv[1].encode())
print(hashed.digest().hex())
