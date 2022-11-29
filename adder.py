import sys

if __name__ == "__main__":
    result = 0

    for arg in sys.argv:
        if(arg.isdecimal()):
            result += int(arg)
    print(result)