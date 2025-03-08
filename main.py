import os
from src.Clocking_Game import Clocking

########################
#     COMMANDS         #
# w : left door        #
# c : right door       #
# a : left light       #
# e : right light      #
# q : look left        #
# d : look right       #
# s : monitor          #
# z : reset door&light #
#   FOR CAMERA         #
# y : back stage       #
# u : show/main stage  #
# h : dining area      #
# b : left hall        #
# n : right hall       #
# s : show the office  #
#     in the isOn you #
#     have left it     #
########################

#NOTE: Curses colors
# RED     = 1
# GREEN   = 2
# YELLOW  = 3
# BLUE    = 4
# MAGENTA = 5
# CYAN    = 6
# WHITE   = 7


if __name__ == '__main__':
    #TODO BUG: replace by mono-thread (see src/Clocking_Game.py)
    Cl_game: Clocking = Clocking()
