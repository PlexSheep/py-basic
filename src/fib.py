#!/usr/bin/env python3
import sys
def fib(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    print(fibs)
    return fibs[n]
fib(int(sys.argv[1]))
