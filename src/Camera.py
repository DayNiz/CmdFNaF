from pygame import mixer
from random import randint
from src.CameraArt import CameraArt


class Camera:
    def __init__(self, game):
        """
         6 rooms viewable on the cams
         "b" "Left Hall"
         "n" "Right Hall"
         "j" "Toilets"
         "g" "Pirate's Cove
         "h" "Dining Area"
         "y" "BackStage"
         "u" "MainStage"
         "o" "Office"
        """

        self.game = game
        self.position_bonnie = None
        self.position_chica = None
        self.position_freddy = None
        self.all_cam_art = CameraArt()
        self.animatronics_on_camera = 0
        self.art: str = self.all_cam_art.main_stage_art[self.animatronics_on_camera]

        self.all_cam: dict = {"o": "office", "b": "left_hall", "n": "right_hall", "g": "pirate_cove",
                              "h": "dining_area", "j": "toilets", "y": "backstage", "u": "main_stage"}

        self.current_camera: str = "Show Stage"
        self.changing_sound = mixer.Sound("src/Camera.wav")
        self.itsme_chance: bool = False
        self.isOn = False

    def get_animatronics_position(self):
        self.position_chica = self.game.chica.pos
        self.position_bonnie = self.game.bonnie.pos
        self.position_freddy = self.game.freddy.pos

        if self.position_chica == self.current_camera:
            if self.position_bonnie == self.current_camera:
                if self.position_freddy == self.current_camera:
                    # the three on camera
                    self.animatronics_on_camera = "BCF"
                else:
                    # bonnie et chica on camera
                    self.animatronics_on_camera = "BC"
            elif self.position_freddy == self.current_camera:
                # freddy et chica on camera
                self.animatronics_on_camera = "CF"
            else:
                # only chica on cam
                self.animatronics_on_camera = "C"
        elif self.position_bonnie == self.current_camera:
            if self.position_freddy == self.current_camera:
                # Bonnie et Freddy on camera
                self.animatronics_on_camera = "BF"
            else:
                # only bonnie on cam
                self.animatronics_on_camera = "B"
        elif self.position_freddy == self.current_camera:
            self.animatronics_on_camera = "F"
        else:
            self.animatronics_on_camera = 0
            # none are visible

    def show(self):
        self.changing_sound.play()
        self.get_animatronics_position()
        if self.current_camera == "Show Stage":
            self.game.afton.a_print(self.all_cam_art.main_stage_art[self.animatronics_on_camera])
        elif self.current_camera == "BackStage":
            self.game.afton.a_print(self.all_cam_art.backstage_art[self.animatronics_on_camera])
        elif self.current_camera == "Dining Area":
            self.game.afton.a_print(self.all_cam_art.dining_area_art[self.animatronics_on_camera])
        elif self.current_camera == "Left Hall":
            self.game.afton.a_print(self.all_cam_art.left_hall_art[self.animatronics_on_camera])
        elif self.current_camera == "Right Hall":
            self.game.afton.a_print(self.all_cam_art.right_hall_art[self.animatronics_on_camera])
        elif self.current_camera == "Pirate's Cove":
            self.itsme_chance = randint(1, 100) == 1
            if self.itsme_chance:
                self.game.afton.a_print(self.all_cam_art.pirate_cove_art["its_me"])
            else:
                self.game.afton.a_print(self.all_cam_art.pirate_cove_art[self.game.foxy.stage_out])
        elif self.current_camera == "Toilets":
            self.game.afton.a_print(self.all_cam_art.toilets_art[self.animatronics_on_camera])
        
        self.game.afton.refresh_screen()
