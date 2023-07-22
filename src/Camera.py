from pygame import mixer


class Camera:
    def __init__(self, game):
        """
         5 rooms viewable on the cams
         "b" "Left Hall"
         "n" "Right Hall"
         "h" "Dining Area"
         "y" "BackStage"
         "u" "MainStage"
         "o" "Office"
        """

        self.game = game
        self.position_bonnie = None
        self.position_chica = None
        self.all_cam_art = CameraArt()
        self.animatronics_on_camera = 0
        self.art: str = self.all_cam_art.main_stage_art[self.animatronics_on_camera]

        self.all_cam: dict = {"o": "office", "b": "left_hall", "n": "right_hall",
                              "h": "dining_area", "y": "backstage", "u": "main_stage"}

        self.current_camera: str = "Show Stage"
        self.changing_sound = mixer.Sound("src/Camera.wav")

    def get_animatronics_position(self):
        self.position_chica = self.game.chica.pos
        self.position_bonnie = self.game.bonnie.pos

        if self.position_chica == self.current_camera:
            if self.position_bonnie == self.current_camera:
                # both on camera
                self.animatronics_on_camera = "BC"
            else:
                # only chica on cam
                self.animatronics_on_camera = "C"
        elif self.position_bonnie == self.current_camera:
            # only bonnie on cam
            self.animatronics_on_camera = "B"
        else:
            self.animatronics_on_camera = 0
            # none are visible

    def show(self):
        self.changing_sound.play()
        self.get_animatronics_position()
        if self.current_camera == "Show Stage":
            print(self.all_cam_art.main_stage_art[self.animatronics_on_camera])
        elif self.current_camera == "BackStage":
            print(self.all_cam_art.backstage_art[self.animatronics_on_camera])
        elif self.current_camera == "Dining Area":
            print(self.all_cam_art.dining_area_art[self.animatronics_on_camera])
        elif self.current_camera == "Left Hall":
            print(self.all_cam_art.left_hall_art[self.animatronics_on_camera])
        elif self.current_camera == "Right Hall":
            print(self.all_cam_art.right_hall_art[self.animatronics_on_camera])


class MainStage(Camera):
    def __init__(self, game):
        super().__init__(game)
        self.art = self.all_cam_art.main_stage_art


class BackStage(Camera):
    def __init__(self, game):
        super().__init__(game)
        self.art = self.all_cam_art.backstage_art


class DiningArea(Camera):
    def __init__(self, game):
        super().__init__(game)
        self.art = self.all_cam_art.dining_area_art


class RightHall(Camera):
    def __init__(self, game):
        super().__init__(game)
        self.art = self.all_cam_art.right_hall_art


class LeftHall(Camera):
    def __init__(self, game):
        super().__init__(game)
        self.art = self.all_cam_art.left_hall_art


class CameraArt:
    def __init__(self):
        self.main_stage_art = {"BC": "~~~~~~~~~~~~[Y][U]~~\n\
~~MAIN~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~*~~~~~~~~~~~~~*~~~\n\
~***~~~~~~~~~~~***~~\n\
~***~~~~~~~~~~~~*~~~\n\
~~* 3 3 ~~ _44_ ~~~~\n\
~~~ 3_3 ~~'&  &'~~~~\n\
~~~'@ @'~~' ^^ '~~~~\n\
~~~' = '~~' \\/ '~~~~\n\
~~~ --- ~~'____'~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~",
                               "B": "~~~~~~~~~~~~[Y][U]~~\n\
~~MAIN~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~*~~~~~~~~~~~~~*~~~\n\
~***~~~~~~~~~~~***~~\n\
~***~~~~~~~~~~~~*~~~\n\
~~* 3 3 ~~~~~~~~~~~~\n\
~~~ 3_3 ~~~~~~~~~~~~\n\
~~~'@ @'~~~~~~~~~~~~\n\
~~~' = '~~~~~~~~~~~~\n\
~~~ --- ~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~",
                               "C": "~~~~~~~~~~~~[Y][U]~~\n\
~~MAIN~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~*~~~~~~~~~~~~~*~~~\n\
~***~~~~~~~~~~~***~~\n\
~***~~~~~~~~~~~~*~~~\n\
~~*~~~~~~~~ _44_ ~~~\n\
~~~~~~~~~~~'&  &'~~~\n\
~~~~~~~~~~~' ^^ '~~~\n\
~~~~~~~~~~~' \\/ '~~~\n\
~~~~~~~~~~~'____'~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~",
                               0: "~~~~~~~~~~~~[Y][U]~~\n\
~~MAIN~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~*~~~~~~~~~~~~~*~~~\n\
~***~~~~~~~~~~~***~~\n\
~***~~~~~~~~~~~~*~~~\n\
~~*~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~"}

        self.backstage_art = {"B": "~~~~~~~~~~~~[Y][U]~~\n\
~~BACK~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~.__.~~~~~~~~~~~~~~~\n\
~|__|~~~~~~~ 3 3 ~~~\n\
~~||~~~~~~~~ 3_3 ~~~\n\
\\-||-/~~~~~~'@ @'~~~\n\
~~||~~~~~~~~' = '~~~\n\
~|--|~~~~~~~ --- ~~~\n\
_|  |_~~~~~~~~~~~~~~\n\
____________________\n\
--------------------",
                              0: "~~~~~~~~~~~~[Y][U]~~\n\
~~BACK~~~~~~~[H]~~~~\n\
~STAGE~~~~~[B]{}[N]~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~.__.~~~~~~~~~~~~~~~\n\
~|__|~~~~~~~~~~~~~~~\n\
~~||~~~~~~~~~~~~~~~~\n\
\\-||-/~~~~~~~~~~~~~~\n\
~~||~~~~~~~~~~~~~~~~\n\
~|--|~~~~~~~~~~~~~~~\n\
_|  |_~~~~~~~~~~~~~~\n\
____________________\n\
--------------------"}

        self.dining_area_art = {"C": "~~~~~~~~~~~[7]~~[9]~\n\
~DINING~~~~[4]~~[6]~\n\
~AREA~~~~~~[B]{}[N]~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~ _44_ ~~~~~~~~~~~~\n\
~~'&  &'~_______~~~~\n\
~~' ^^ '~|     |~~~~\n\
~~' \\/ '~~~~~~~~~~~~\n\
~~'____'~~~______~~~\n\
~~_____~~~~|    |~~~\n\
~~|   |~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
        ~~~~~~~~~~~~~~~~~~~~",
                                0: "~~~~~~~~~~~[7]~~[9]~\n\
~DINING~~~~[4]~~[6]~\n\
~AREA~~~~~~[B]{}[N]~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~_______~~~~\n\
~~~~~~~~~|     |~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~______~~~\n\
~~~~~~~~~~~|    |~~~\n\
~~|   |~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~\n\
~~~~~~~~~~~~~~~~~~~~"}

        self.left_hall_art = {"B": "~~~~~~~~~~~~[Y][U]~~\n\
~~LEFT~~~~~~~[H]~~~~\n\
~~HALL~~~~~[B]{}[N]~\n\
|/~  3     3  ~~~~/|\n\
||~ 333   333 ~~~~||\n\
||~ 333___333 ~~~~||\n\
||~ /       \\ ~~~~||\n\
||~| @@   @@ |~~~~||\n\
||~|         |~~~~||\n\
||~|\\       /|~~~~||\n\
||~~\\]-_-_-[/ ~~~\\\\\\\n\
||~~~.-----.~~~~~~\\\\\n\
||\\~~~~~~~~~~~~~~~~\\",
                              0: "~~~~~~~~~~~~[Y][U]~~\n\
~~LEFT~~~~~~~[H]~~~~\n\
~~HALL~~~~~[B]{}[N]~\n\
|/~~~~~~~~~~~~~~~~/|\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~\\\\\\\n\
||~~~~~~~~~~~~~~~~\\\\\n\
||\\~~~~~~~~~~~~~~~~\\"}

        self.right_hall_art = {"C": "~~~~~~~~~~~~[Y][U]~~\n\
~~RIGHT~~~~~~[H]~~~~\n\
~~HALL~~~~~[B]{}[N]~\n\
|\\~~~~~~~~~~~~~~~~\\|\n\
||~~ /\\_/_\\_/\\ ~~~||\n\
||~~/ __   __ \\~~~||\n\
||~~| @@   @@ |~~~||\n\
||~~|         |~~~||\n\
||~~|   /_\\   |~~~||\n\
||~~ \\  \\_/  / ~~~||\n\
///~   -----   ~~~||\n\
//~~~~~~~~~~~~~~~~||\n\
/~~~~~~~~~~~~~~~~/||",
                               0: "~~~~~~~~~~~~[Y][U]~~\n\
~~RIGHT~~~~~~[H]~~~~\n\
~~HALL~~~~~[B]{}[N]~\n\
|\\~~~~~~~~~~~~~~~~\\|\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
||~~~~~~~~~~~~~~~~||\n\
///~~~~~~~~~~~~~~~||\n\
//~~~~~~~~~~~~~~~~||\n\
/~~~~~~~~~~~~~~~~/||"}
