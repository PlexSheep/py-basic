#!/usr/bin/env python3
import re
import sys

if len(sys.argv) != 2:
    print("takes only a file path as argument")
    exit(1)

textfile = open(sys.argv[1])
text = textfile.read()

regex = r"\b[a-z][AEIOUaeiou]([a-w]|[A-W])"
matches = re.finditer(regex, text, re.MULTILINE)
counter = 0
for i, match in enumerate(matches, start=1):
    print(f"{i:03} | \"{match}\"")
    counter += 1
print(f"found {counter}.")
