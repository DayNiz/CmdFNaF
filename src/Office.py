from office_state import *


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

    def toggle(self):
        if self.is_open:
            self.closing()
        else:
            self.opening()

    def closing(self):
        self.is_open = False
        # update display
        self.art: str = door_art[self.is_open]

    def opening(self):
        self.is_open = True
        # update display
        self.art: str = door_art[self.is_open]


class Light:
    def __init__(self):
        self.state: str = "off"
        self.anim_name: str = ""
        self.art: str = light_art[self.state]

    def toggle(self):
        if self.state == "off":
            self.turn_on()
        elif self.state == "on":
            self.turn_off()

    def show_anim(self, anim_name):
        self.anim_name = anim_name
        self.art = light_art[self.anim_name]

    def turn_off(self):
        self.state = "off"
        # update display
        self.art = light_art[self.state]

    def turn_on(self):
        self.state = "on"
        # update display
        self.art = light_art[self.state]


class Office:
    def __init__(self, side):
        self.side = side
        self.left: Side = Side()
        self.right: Side = Side()

    def show(self, clock, comsum):
        if self.side == 0:
            self.left.show()
        elif self.side == 1:
            print(comsum_art[comsum], clock_art[clock], OFFICE_art, sep="")
        elif self.side == 2:
            self.right.show()
