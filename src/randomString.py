#!/usr/bin/env python3
import random
import string
import sys

def get_random_string(length):
    # choose from all lowercase letter
    alphabet = string.ascii_lowercase
    alphabet += string.ascii_uppercase
    alphabet += "0123456789"
    result_str = ''.join(random.choice(alphabet) for i in range(length))
    return result_str

print(get_random_string(int(sys.argv[1])))
