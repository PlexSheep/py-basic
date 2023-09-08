#!/usr/bin/env python3
import argparse
import os
import sys

# 2**30 bytes aka 1 Mebibyte
MAX_SIZE: int = 0x100000



def humanbytes(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)

def main():
    """Dump a file"""
    # arg parsing
    parser = argparse.ArgumentParser(
        prog="hexer",
        description="Dumps data as hex"
    )
    parser.add_argument("file")
    parser.add_argument("-c", "--chars", action="store_true")
    args = parser.parse_args()

    # open file
    try:
        file = open(args.file, "rb")
    except Exception as e:
        print(f"Could not open file '{args.file}': {e}")
        sys.exit(1)

    # check if the file has a reasonable size to dump
    if 0 != os.path.getsize(args.file) > MAX_SIZE:
        print(f"""The file you are trying to dump is larger than 1M.\n\
        Actual size: {humanbytes(os.path.getsize(args.file))}\nrefusing to dump""")
        sys.exit(2)
    # print header
    if args.chars:
        print("Line      Data                                     Text")
        print('=' * 68)
    else:
        print(f"Line      Data")
        print('=' * 48)

    # every line should contain 16 bytes, so we need a loop that get's 16 bytes
    # and then works with them
    next: bytes = bytes(16)
    index: int = 0
    while len(next) == 16:
        next = file.read(16)
        if len(next) == 0:
            # no data left to read
            break

        line: str = f"{index:07x} | "

        # actual hexdumping
        for i in range(16):
            if i % 2 == 0:
                if len(next) > i+1:
                    line += f"{next[i]:02x}{next[i+1]:02x} "
                elif len(next) > i:
                    line += f"{next[i]:02x}   "
                else:
                    line += "     "
            else: continue

        # if chars is enabled, print chars
        if args.chars:
            line += "| "
            for b in next:
                # special case for newline
                if b == 0x0a:
                    line+= '␤' # official unicode symbol representing newlines
                # only print regular characters
                elif b > 0x20 and b < 0x7e:
                    line += chr(b)
                elif b == 0x20:
                    line += '\u2420'
                else:
                    line += '.'

        print(line)
        index += 16


if __name__ == "__main__":
    main()
