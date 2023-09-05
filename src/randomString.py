#!/usr/bin/env python3
import random
import string
import math
import sys

alphabet = string.ascii_lowercase
alphabet += string.ascii_uppercase
alphabet += "0123456789"

def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice(alphabet) for i in range(length))
    return result_str

print(get_random_string(int(sys.argv[1])))
if len(sys.argv) >= 3 and sys.argv[2] == "-v":
    security = math.log2(len(alphabet)**int(sys.argv[1]))
    print(f"The alphabets size is {len(alphabet)}")
    print(f"Security bits: {security}")
