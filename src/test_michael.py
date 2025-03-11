import Afton
import office_state as ofs
from CameraArt import CameraArt
import time
import random
#just a random testing file, I use it to check how the ASCII art render
#   when I use curses colors...
cam = CameraArt()
all_arts: list = [
    cam.pirate_cove_art[0],
    cam.pirate_cove_art[1],
    cam.pirate_cove_art[2],
    # cam.main_stage_art["BCF"],
    # cam.main_stage_art["F"],
    # cam.main_stage_art["C"],
    # cam.main_stage_art["B"],
    # cam.main_stage_art["BF"],
    # cam.main_stage_art["BC"],
    # cam.main_stage_art["CF"],
    # cam.main_stage_art["BCF"],
    # ofs.art_6am,
    # ofs.art_jump_bonnie,
    # ofs.art_jump_chica,
    # ofs.art_jump_foxy,
    # ofs.art_jump_freddy,
    # ofs.art_jump_golden,
    # ofs.door_art[0],
    # ofs.door_art[1],
    # ofs.light_art["anim"],
    # ofs.light_art["bonnie"],
    # ofs.light_art["chica"],
    # ofs.light_art["on"],
    # ofs.office_gf_art,
]
def main():
    afton = Afton.Afton()
    print(len(all_arts))
    for i in range(len(all_arts)):
        afton.a_print(ofs.office_art)
        afton.refresh_screen()
        time.sleep(0.9)
        afton.a_print(all_arts[i])
        afton.refresh_screen()
        time.sleep(0.7)
    
    afton.exit()
    return

main()
