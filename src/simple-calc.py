import sys

if __name__ == "__main__":
    result = 0

    def help(): {
        print("input: [value] [operation] [value]\noperations: [ + - . / ]\n")
    }

    if(len(sys.argv) > 1):
            if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
                help()
                sys.exit()
    if(len(sys.argv) == 0):
        help()
        sys.exit()

    if(len(sys.argv) < 4):
        print("not enough arguments\n")
        help()
        sys.exit()
    if(len(sys.argv) > 4):
        print("too many arguments\n")
        help()
        sys.exit()
        
    if(sys.argv[1].isdecimal):
        val1=int(sys.argv[1])

    else:
        print("1st arg should be an integer!")
        help()
        sys.exit()
    if(sys.argv[2].isascii and len(sys.argv[2]) == 1):
        if (not ((sys.argv[2]=="+") or (sys.argv[2]=="-") or (sys.argv[2]==".") or (sys.argv[2]=="/"))):
            print("2nd arg should be an operator [ + - . / ]!\n")
            help()
            sys.exit()
        op=sys.argv[2]
        
    if(sys.argv[3].isdecimal):
        val2=int(sys.argv[3])
    else:
        print("3rd arg should be an integer!")
        help()


    #todo switch case and then operations

    if(op=="+"):
        print(f"{val1} + {val2} = {val1+val2}")

    elif(op=="-"):
        print(f"{val1} - {val2} = {val1-val2}")

    elif(op=="."):
        print(f"{val1} . {val2} = {val1*val2}")

    elif(op=="/"):
        print(f"{val1} / {val2} = {val1/val2}")

    else:
        print(f"'{op}' is not a valid operator")
        sys.exit()
        