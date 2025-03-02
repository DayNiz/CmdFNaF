##Afton.py:
# A set of methods and fucntion for dealing with curses initialization and usage
import curses

BLACK   = 0
RED     = 1
GREEN   = 2
YELLOW  = 3
BLUE    = 4
MAGENTA = 5
CYAN    = 6
WHITE   = 7

def init() -> curses.window:
    screen = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    __init_color()
    curses.curs_set(0)
    screen.refresh()
    return screen

def __init_color():
    curses.init_pair(BLACK, curses.COLOR_BLACK, -1)
    curses.init_pair(RED, curses.COLOR_RED, -1)
    curses.init_pair(GREEN, curses.COLOR_GREEN, -1)
    curses.init_pair(YELLOW, curses.COLOR_YELLOW, -1)
    curses.init_pair(BLUE, curses.COLOR_BLUE, -1)
    curses.init_pair(MAGENTA, curses.COLOR_MAGENTA, -1)
    curses.init_pair(CYAN,curses.COLOR_CYAN, -1)
    curses.init_pair(WHITE,curses.COLOR_WHITE, -1)

def print(msg_array: list, screen: curses.window) -> int:
    """
    'msg_array' format = [(color: int, art: str), ...]
    return: 0 if success, 1 else.
    """
    if not type(msg_array) == list:
        print("ERR: msg_array must be an list, found", type(msg_array), "!")
        return 1
    for element in msg_array:
        #TODO: rename element to smthg more appropriate.
        if not (type(element) == tuple and len(element) == 2):
            print("ERR: msg_array must be composed of tuple f len 2, found", type(element), "of len", len(element))
            return 1
        if not (type(element[0]) == int and element[0] in range(0,8) and type(element[1]) == str):
            print("ERR: bad format, check your msg_array!")
            return 1
        #Now we're sure the msg_array is correctly formated.
        screen.addstr(element[1], curses.color_pair(element[0]))
        screen.refresh()

def exit():
    curses.curs_set(1)
    curses.endwin()


