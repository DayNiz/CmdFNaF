from src.Office import Office
from src.Animatronics import Bonnie, Chica, Foxy, Freddy
from src.Camera import Camera
import os
import keyboard
from pygame import mixer
from random import randint
from src.office_state import art_6am


class Game:
    def __init__(self):
        self.view_side: int = 1  # [left = 0, center = 1, right = 2]
        self.clock: int = 0  # 0 = 12AM
        self.comsum: int = 0
        self.batt_level: float = 100.0
        self.office: Office = Office(self.view_side, self)
        self.running: bool = True
        self.monitor = Camera(self)
        self.freddy = Freddy(self, level=0)
        self.bonnie = Bonnie(self, level=0)
        self.chica = Chica(self, level=0)
        self.foxy = Foxy(self, level=0)

        self.is_keyboard_pressed = False

        self.monitor.get_animatronics_position()

        self.end_night_sound = mixer.Sound("src/6AM.wav")

    # Fonction pour effacer l'écran
    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def check_comsum(self):
        self.comsum = 0
        if not self.office.left.door.is_open:
            self.comsum += 1
        if not self.office.right.door.is_open:
            self.comsum += 1
        if self.office.left.light.isOn:
            self.comsum += 1
        if self.office.right.light.isOn:
            self.comsum += 1
        # éviter la surconsommation / sous-consommation
        if self.comsum > 4:
            self.comsum = 4
        if self.comsum < 0:
            self.comsum = 0

    def turn_all_off(self):
        self.office.left.door.opening()
        self.office.right.door.opening()
        self.office.left.light.turn_off()
        self.office.right.light.turn_off()

    def run(self):
        self.office.show(self.clock, self.comsum)
        while self.running:
            self.check_input()
            self.check_comsum()
            if self.office.side == 1 and not self.monitor.isOn:
                self.clear_screen()
                self.office.show(self.clock, self.comsum)
            if self.bonnie.is_on_office() or self.chica.is_on_office():
                self.running = False
                break

    def check_input(self):
        checking_keyboard = keyboard.read_event()
        checking_input = checking_keyboard.name
        try:
            if checking_keyboard.event_type == 'down' and self.batt_level > 0 and self.running:
                self.clear_screen()
                if checking_input == "u":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Show Stage"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "y":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "BackStage"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "h":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Dining Area"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "b":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Left Hall"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "n":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Right Hall"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "g":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Pirate's Cove"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "j":
                    if self.monitor.isOn:
                        self.monitor.current_camera = "Toilets"
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)

                elif checking_input == "s":
                    self.monitor.isOn = not self.monitor.isOn
                    if self.monitor.isOn:
                        self.monitor.show()
                    else:
                        self.office.side = 1
                        self.office.show(self.clock, self.comsum)
                elif checking_input == "q":
                    self.office.side -= 1
                    if self.office.side < 0:
                        self.office.side = 1
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()
                elif checking_input == "d":
                    self.office.side += 1
                    if self.office.side > 2:
                        self.office.side = 1
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()

                elif checking_input == "a":
                    self.office.left.light.toggle()
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()
                elif checking_input == "e":
                    self.office.right.light.toggle()
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()
                elif checking_input == "w":
                    self.office.left.door.toggle()
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()
                elif checking_input == "c":
                    self.office.right.door.toggle()
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                    else:
                        self.monitor.show()
                elif checking_input == "z":
                    self.turn_all_off()
                    if not self.monitor.isOn:
                        self.office.show(self.clock, self.comsum)
                else:
                    if self.monitor.isOn:
                        self.monitor.show()
                    else:
                        self.office.show(self.clock, self.comsum)
        except KeyboardInterrupt:
            self.running = False

    def add_one_hour(self):
        self.clock += 1
        self.clear_screen()
        self.office.show(self.clock, self.comsum)

    def six_am(self):
        """
        function called when it's 6AM
        """
        self.end_night_sound.play()
        print(art_6am)
        self.running = False
