from src.Office import Office
from src.Animatronics import Bonnie, Chica
from src.Camera import Camera
import os
import keyboard
from pygame import mixer
from src.office_state import art_6am


class Game:
    def __init__(self):
        self.view_side: int = 1  # [left = 0, center = 1, right = 2]
        self.clock: int = 0  # 0 = 12AM
        self.comsum: int = 0
        self.office: Office = Office(self.view_side)
        self.running: bool = True
        self.monitor = Camera(self)
        self.bonnie = Bonnie(self, level=0)
        self.chica = Chica(self, level=0)

        self.is_keyboard_pressed = False

        self.monitor.get_animatronics_position()

        self.end_night_sound = mixer.Sound("src/sounds/6AM.wav")

    
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
            if self.bonnie.is_on_office() or self.chica.is_on_office():
                self.running = False
                break

    def check_input(self):
        checking_keyboard = keyboard.read_event()
        checking_input = checking_keyboard.name
        try:
            if checking_keyboard.event_type == 'down':
                self.clear_screen()
                if checking_input == "u":
                    self.monitor.current_camera = "Show Stage"
                    self.monitor.show()
                elif checking_input == "y":
                    self.monitor.current_camera = "BackStage"
                    self.monitor.show()
                elif checking_input == "h":
                    self.monitor.current_camera = "Dining Area"
                    self.monitor.show()
                elif checking_input == "b":
                    self.monitor.current_camera = "Left Hall"
                    self.monitor.show()
                elif checking_input == "n":
                    self.monitor.current_camera = "Right Hall"
                    self.monitor.show()
                elif checking_input == "s":
                    self.office.show(self.clock, self.comsum)

                elif checking_input == "q":
                    self.office.side -= 1
                    if self.office.side < 0:
                        self.office.side = 0
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "d":
                    self.office.side += 1
                    if self.office.side > 2:
                        self.office.side = 2
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "a":
                    self.office.left.light.toggle()
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "e":
                    self.office.right.light.toggle()
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "w":
                    self.office.left.door.toggle()
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "c":
                    self.office.right.door.toggle()
                    self.office.show(self.clock, self.comsum)
                elif checking_input == "quit":
                    self.running = False
                elif checking_input == "z":
                    self.turn_all_off()
                    self.office.show(self.clock, self.comsum)
                else:
                    pass
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
        self.clear_screen()
        self.end_night_sound.play()
        print(art_6am)
        self.running = False
