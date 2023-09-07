#!/usr/bin/env python3
import sys

def internal(text: str, key: int) -> str:
    cyphertext: str = ""
    for c in text:
        if ord(c) >= 65 and ord(c) <= 90: # uppercase letters
            ci = ord(c) - ord('A')
            add = ord('A')
            #print(f"{c} is uppercase")
        elif ord(c) >= 97 and ord(c) <= 122: # uppercase letters
            ci = ord(c) - ord('a')
            add = ord('a')
            #print(f"{c} is lowercase")
        else:
            #print(f"not a letter: {c} ({ord(c)})")
            # character is not a letter, just skip it
            cyphertext += c
            continue
        ci += key
        ci %= 26    # only 23 letters in the alphabet
        #print(f"ci for {c}: {ci}")
        cyphertext += chr(ci + add)

    return cyphertext


if len(sys.argv) <= 2 or len(sys.argv) >= 5:
    print("Takes two arguments: <SOURCE> <KEY> [-e]")
    exit(1)

source: str = sys.argv[1]
target: str = ""
key = int(sys.argv[2])

if len(sys.argv) >= 4 and sys.argv[3] == "-e":
    print("encrypting...")
    target = internal(source, -key)


else:
    print("decrypting...")
    target = internal(source, key)

print("=" * 80)
print("%s" % target)
