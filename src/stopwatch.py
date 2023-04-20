#!/usr/bin/env python3

# hard dependencies
import argparse
import time
import datetime
import sys
import time
import curses

# optional dependencies
try:
    import beepy    # pip install beepy
except:
    beepy = None
try:
    from multiprocessing import Process
except:
    Process = None
    

# printing to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Animation:
    X_SIZE = 8
    Y_SIZE = 3
    field = [
        ['>', '>' * (X_SIZE - 2), 'v',],
        ['^', ' ' * (X_SIZE - 2), 'v',] * (Y_SIZE - 2),
        ['^', '<' * (X_SIZE - 2), '<',],
        ]
    def __init__(self) -> None:
        pass

    def tick(self) -> list[str]:
        out_arr: list[str] = []
        for line in self.field:
            out_arr.append(self.__char_array_to_str(line))
        return out_arr

    def __char_array_to_str(self, chars) -> str :
        out_str = ""
        for char in chars:
            out_str += char
        return out_str

class Stopwatch:

    beep_at: int
    beep_at_time: datetime.datetime
    has_beeped: bool = False
    start_time: datetime.datetime
    enable_sound: bool = False
    screen: curses.window
    next_line = 0
    enable_animation: bool
    animation: Animation

    BUFFER_LINE = '=' * 120
    COL0_Y = 0
    COL1_Y = 44
    COL2_Y = 90

    def __init__(self, beep_at, enable_sound, screen: curses.window, enable_animation: bool) -> None:
        self.screen = screen
        self.screen.addstr(0, 0, self.BUFFER_LINE)
        self.next_line += 2
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.enable_animation = enable_animation
        if enable_sound:
            self.enable_sound = enable_sound
        if not beep_at <= 0:
            self.beep_at = beep_at
            self.beep_at_time = self.start_time + datetime.timedelta(minutes=beep_at)
            self.screen.addstr(self.next_line, self.COL0_Y, "Start time:\t%s" % self.start_time)
            self.screen.addstr(self.next_line, self.COL1_Y, "Will beep at:\t%s" % self.beep_at_time)
            self.screen.addstr(self.next_line, self.COL2_Y, "Beeping Time:\t%sm" % beep_at)
            self.next_line += 2
            self.screen.addstr(self.next_line, self.COL0_Y, self.BUFFER_LINE)
            self.next_line += 5
            # content goes here
            self.screen.addstr(self.next_line, self.COL0_Y, self.BUFFER_LINE)
            self.next_line -= 3
        else:
            self.beep_at = 0
            self.beep_at_time = datetime.datetime.now()
            self.screen.addstr(self.next_line, self.COL1_Y, "Start time:\t%s" % self.start_time)
            self.next_line += 6
            # content goes here
            self.screen.addstr(self.next_line, self.COL0_Y, self.BUFFER_LINE)
            self.next_line -= 4


    def display(self) -> None:
        remaining_time_str = ""
        beep_notice_str = ""
        while True:
            nl_store = self.next_line
            now = datetime.datetime.now().replace(microsecond=0)
            elapsed = (now - self.start_time)
            current_time_str = ("\rcurrent:\t%s" % now)
            elapsed_time_str = ("elapsed: %s" % elapsed)
            if self.beep_at > 0 and not self.has_beeped:
                remaining = self.beep_at_time - now
                remaining_time_str = ("remaining: %s" % remaining)
            if elapsed.seconds / 60 >= self.beep_at and not self.has_beeped and not self.beep_at == 0:
                current_time_str += '\a'
                beep_notice_str = "🔔Beep!🔔"
                self.has_beeped = True
                if self.enable_sound and not beepy is None and not Process is None:
                    p = Process(target=beepy.beep, kwargs={"sound": "success"})
                    p.start()
            #sys.stdout.write('\r' + current_time_str+"\t\t"+elapsed_time_str+"\t\t"+remaining_time_str+"\t\t"+beep_notice_str + "\t")
            if self.beep_at > 0:
                self.screen.addstr(self.next_line, self.COL0_Y, "current:\t%s" % (now))
                self.screen.addstr(self.next_line, self.COL2_Y, "elapsed:\t%s" % (elapsed))
                self.next_line += 1
                if not self.has_beeped:
                    self.screen.addstr(self.next_line, self.COL2_Y, "remaining:\t%s" % (remaining))
                else:
                    self.screen.addstr(self.next_line, self.COL2_Y, "overtime:\t%s" % (remaining))
            else:
                self.screen.addstr(self.next_line, self.COL1_Y, "current:\t%s" % (now))
                self.next_line += 2
                self.screen.addstr(self.next_line, self.COL1_Y, "elapsed:\t\t    %s" % (elapsed))

            if self.enable_animation:
                self.next_line -= 1
                if now.second % 4 == 0:
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "$-")
                    self.next_line += 1
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "--")
                elif now.second % 4 == 1:
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "-$")
                    self.next_line += 1
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "--")
                elif now.second % 4 == 2:
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "--")
                    self.next_line += 1
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "-$")
                elif now.second % 4 == 3:
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "--")
                    self.next_line += 1
                    self.screen.addstr(self.next_line, self.COL1_Y + 16, "$-")
            #sys.stdout.flush()
            self.screen.refresh()
            self.next_line = nl_store
            time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(prog="stopwatch", description='Simple CLI stopwatch.')
    # TODO make this weird nargs thing better, generates a bad help page
    parser.add_argument('-b', '--beep', metavar='N', type=float, nargs='+',
                    help='beep after N minutes', default=[0])
    parser.add_argument('-s', '--sound',
                    action='store_true', help="activate sound")
    parser.add_argument('-l', '--legacy-ui',
                    action='store_true', help="Use the old \"inline\" ui instead of the curses ui")
    parser.add_argument('-a', '--no-animation',
                    action='store_true', help="don't show the animation")
    args = parser.parse_args()
    try:
        stdscreen = curses.initscr()
        # copied from my guide, idk what they do:
        curses.noecho()
        curses.cbreak()

        timer = Stopwatch(
                beep_at=args.beep[0], 
                enable_sound=args.sound, 
                screen=stdscreen,
                enable_animation= not args.no_animation
                )
        timer.display()
    except KeyboardInterrupt:
        pass

    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

if __name__ == "__main__":
    main()
