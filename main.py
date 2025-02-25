import os
from src.Clocking_Game import Clocking
#TODO: replace by curses
os.system('mode con: cols=65 lines=5')

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
#TODO: Choose the appropriate curses color (0->254) for bgg and fg
# 0 -> Black
# 1 -> White
# 2 -> Blue (bonnie)
# 3 -> Yellow (chica)
# 4 -> Orange/Brown (freddy)
# 5 -> Red (foxy)
# 6 -> Gray
# 7 -> Purple
# TBD: adding more colors? 8 seems enough, no?


if __name__ == '__main__':
    #TODO: replace by mono-thread (see src/Clocking_Game.py)
    Cl_game: Clocking = Clocking()
