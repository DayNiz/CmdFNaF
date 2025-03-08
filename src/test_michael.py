import Afton
import office_state
import time
import random


all_arts: list = [
    office_state.art_6am, 
    office_state.art_jump_bonnie, 
    office_state.art_jump_chica, 
    office_state.art_jump_foxy,
    office_state.art_jump_freddy,
    office_state.art_jump_golden,
    office_state.light_art["anim"],
    office_state.light_art["on"],
    office_state.light_art["off"],
    office_state.light_art["chica"],
    office_state.light_art["bonnie"],
    office_state.door_art[0]
]
afton = Afton.Afton()

afton.a_print(office_state.comsum_art[0], office_state.comsum_art[1])
afton.refresh_screen()
time.sleep(2)

afton.a_print(office_state.comsum_art[2], office_state.comsum_art[3])
afton.refresh_screen()
time.sleep(2)

for i in range(len(all_arts)):
    afton.a_print(all_arts[i])
afton.refresh_screen()

afton.exit()
