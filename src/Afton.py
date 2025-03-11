##Afton.py:
# A set of methods and fucntion for dealing with curses initialization and usage
import curses

# We define the colors outside of the class for simplicity
RED     = 1
GREEN   = 2
YELLOW  = 3
BLUE    = 4
MAGENTA = 5
CYAN    = 6
WHITE   = 7

class Afton:
    def __init__(self):
        self.screen = curses.initscr()
        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        self.__init_color()
        self.screen.clear()

    def __init_color(self):
        curses.init_pair(RED, curses.COLOR_RED, -1)
        curses.init_pair(GREEN, curses.COLOR_GREEN, -1)
        curses.init_pair(YELLOW, curses.COLOR_YELLOW, -1)
        curses.init_pair(BLUE, curses.COLOR_BLUE, -1)
        curses.init_pair(MAGENTA, curses.COLOR_MAGENTA, -1)
        curses.init_pair(CYAN,curses.COLOR_CYAN, -1)
        curses.init_pair(WHITE,curses.COLOR_WHITE, -1)

    def a_print(self, msg_array) -> int:
        """
        'msg_array' format = [(color: int, art: str), ...]
        return: 0 if success, 1 else.
        """
        #for msg_array in msg_array_args:
        if not type(msg_array) == list:
            print("ERR: msg_array must be an list, found", type(msg_array), "!")
            return 1
        for element in msg_array:
            #TODO: rename element to smthg more appropriate.
            if not (type(element) == tuple and len(element) == 2):
                print("ERR: msg_array must be composed of tuple f len 2, found", type(element), "of len", len(element))
                print("while looking at element ", element)
                return 1
            if not (type(element[0]) == int and element[0] in range(1,9) and type(element[1]) == str):
                print("ERR: bad format, check your msg_array!")
                print("while looking at element ", element)
                return 1
            #Now we're sure the msg_array is correctly formated.
            self.screen.addstr(element[1], curses.color_pair(element[0]))

    def refresh_screen(self):
        self.screen.refresh()
        self.screen.clear()

    def exit(self):
        self.screen.keypad(0)
        curses.echo()
        curses.curs_set(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()


