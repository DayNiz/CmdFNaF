from src.office_state import *
from pygame import mixer


class Side:
    def __init__(self):
        self.door: Door = Door()
        self.light: Light = Light()

    def show(self):
        print(self.light.art, self.door.art, sep="")


class Door:
    def __init__(self):
        self.is_open: bool = True
        self.art: str = door_art[self.is_open]
        self.closing_sound = mixer.Sound("src/CloseDoor.wav")
        self.opening_sound = mixer.Sound("src/OpenDoor.wav")

    def toggle(self):
        if self.is_open:
            self.closing()
        else:
            self.opening()

    def closing(self):
        self.is_open = False
        self.closing_sound.play()
        # update display
        self.art: str = door_art[self.is_open]

    def opening(self):
        self.is_open = True
        self.opening_sound.play()
        # update display
        self.art: str = door_art[self.is_open]


class Light:
    def __init__(self):
        self.isOn: bool = False
        self.anim_name: str = ""
        self.art: str = light_art["off"]

    def toggle(self):
        if self.isOn:
            self.turn_off()
        else:
            self.turn_on()

    def show_anim(self, anim_name):
        self.anim_name = anim_name
        self.art = light_art[self.anim_name]

    def turn_off(self):
        self.isOn = False
        # update display
        self.art = light_art["off"]

    def turn_on(self):
        self.isOn = True
        # update display
        self.art = light_art["on"]
        if self.anim_name != "":
            self.art = light_art[self.anim_name]


class Office:
    def __init__(self, side, game):
        self.game = game
        self.side = side
        self.left: Side = Side()
        self.right: Side = Side()

    def show(self, clock, comsum):
        if self.side == 0:
            self.left.show()
        elif self.side == 1:
            print(comsum_art[comsum], show_battery(round(self.game.batt_level)), clock_art[clock], OFFICE_art, sep="")
        elif self.side == 2:
            self.right.show()
