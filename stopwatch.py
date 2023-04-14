#!/bin/env python3
from time import localtime, sleep, struct_time, time
import datetime
import sys


class stopwatch:
    def __init__(self) -> None:
        self.start_time = datetime.datetime.now().replace(microsecond=0)

    def display(self) -> None:
        print("started at:\t%s" % self.start_time)
        while True:
            now = datetime.datetime.now().replace(microsecond=0)
            elapsed = (now - self.start_time)
            text0 = ("\rcurrent:\t%s" % now)
            text1 = ("elapsed:\t%s" % elapsed)
            sys.stdout.write('\r' + str(text0+"\t\t"+text1) + "\t" * 3)
            sys.stdout.flush()
            sleep(1)                        

def main():
    try:
        timer = stopwatch()
        timer.display()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
