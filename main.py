import os
from src.Clocking_Game import Clocking
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


if __name__ == '__main__':
    Cl_game: Clocking = Clocking()
