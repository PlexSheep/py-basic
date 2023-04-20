#!/bin/env python3
import beepy    # pip install beepy
from multiprocessing import Process
import argparse
import time
import datetime
import sys
import time


class stopwatch:

    beep_at: int
    beep_at_time: datetime.datetime
    has_beeped: bool = False
    start_time: datetime.datetime
    enable_sound: bool = False

    def __init__(self, beep_at, enable_sound) -> None:
        print('='*120)
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        if enable_sound:
            print("Warning:\tonce the beep time is reached, a sound will play.")
        self.enable_sound = enable_sound
        if not beep_at <= 0:
            self.beep_at = beep_at
            self.beep_at_time = self.start_time + datetime.timedelta(minutes=beep_at)
            print("Start time:\t%s\nWill beep at:\t%s\nBeeping Time:\t%sm" % (self.start_time, self.beep_at_time, beep_at))
        else:
            self.beep_at = 0
            self.beep_at_time = datetime.datetime.now()
            print("Start time:\t%s" % self.start_time)
        print('='*120)


    def display(self) -> None:
        text2 = ""
        text3 = ""
        while True:
            now = datetime.datetime.now().replace(microsecond=0)
            elapsed = (now - self.start_time)
            text0 = ("\rcurrent:\t%s" % now)
            text1 = ("elapsed: %s" % elapsed)
            if self.beep_at > 0 and not self.has_beeped:
                remaining = self.beep_at_time - now
                text2 = ("remaining: %s" % remaining)
            if elapsed.seconds / 60 >= self.beep_at and not self.has_beeped and not self.beep_at == 0:
                text0 += '\a'
                text3 = "🔔Beep!🔔"
                self.has_beeped = True
                if self.enable_sound:
                    p = Process(target=beepy.beep, kwargs={"sound": "success"})
                    p.start()
            sys.stdout.write('\r' + text0+"\t\t"+text1+"\t\t"+text2+"\t\t"+text3 + "\t")
            sys.stdout.flush()
            time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(prog="stopwatch", description='Simple CLI stopwatch.')
    parser.add_argument('-b', '--beep', metavar='N', type=float, nargs='+',
                    help='beep after x minutes', default=[0])
    parser.add_argument('-s', '--sound',
                    action='store_true')
    args = parser.parse_args()
    try:
        timer = stopwatch(args.beep[0], enable_sound=args.sound)
        timer.display()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
