import time
from random import randint, uniform
from pygame import mixer
from src.office_state import art_jump_bonnie, art_jump_chica, art_jump_foxy, art_jump_freddy


class Animatronics:
    def __init__(self, game, level=0):
        self.name: str = ""
        self.game = game
        self.map = self.game.monitor
        self.path: list = [None]
        self.path_pos = 0
        self.pos = self.path[self.path_pos]
        self.level: int = level
        self.movement_opportunity: int = 0
        self.just_arrive_at_office: bool = True
        self.jump_art: str = ""
        self.waiting_time: float = 0

        self.scream_sound = mixer.Sound("src/Scream.wav")
        self.knock_sound = mixer.Sound("src/KnockingDoor.wav")
        self.light_sound = mixer.Sound("src/SeeLight.wav")
        self.walk_sound = mixer.Sound("src/FootWalk.wav")

    def check_movement_opportunity(self):
        self.movement_opportunity = randint(1, 20)
        return self.movement_opportunity <= self.level

    def move(self):
        self.path_pos += 1
        try:
            self.pos = self.path[self.path_pos]
        except IndexError:
            self.path_pos = 0
            self.pos = self.path[self.path_pos]
        if self.pos not in ("office light_left", "office"):
            self.walk_sound.play()

    def is_on_office(self):
        if self.pos == "office light_left":
            self.game.office.left.light.anim_name = self.name
            if self.just_arrive_at_office:
                # ne jouer le son qu'une fois
                self.light_sound.play()
                self.just_arrive_at_office = False
        if self.pos == "office light_right":
            self.game.office.right.light.anim_name = self.name
            if self.just_arrive_at_office:
                # ne jouer le son qu'une fois
                self.light_sound.play()
                self.just_arrive_at_office = False

        if self.pos == "office":
            if self.name == "bonnie" and self.game.office.left.door.is_open:
                self.jumpscare()
            elif self.name == "chica" and self.game.office.right.door.is_open:
                self.jumpscare()
            elif self.name == "bonnie" and not self.game.office.left.door.is_open:
                self.knock_sound.play()
                self.game.office.left.light.anim_name = ""
                self.path_pos = 0
                self.pos = self.path[self.path_pos]
            elif self.name == "chica" and not self.game.office.right.door.is_open:
                self.knock_sound.play()
                self.game.office.right.light.anim_name = ""
                self.path_pos = 0
                self.pos = self.path[self.path_pos]
        return self.pos == "office"

    def jumpscare(self):
        if self.game.running:
            self.scream_sound.play()
            self.game.running = False
            self.game.running = False
            self.game.clear_screen()
            print(self.jump_art)
            time.sleep(0.5)
            print(self.jump_art)

    def run(self):
        while self.game.running:
            time.sleep(self.waiting_time)
            if self.check_movement_opportunity():
                self.move()
            else:
                # print(f"{self.name} didn't move")
                pass
            self.is_on_office()


class Bonnie(Animatronics):
    def __init__(self, game, level: int):
        Animatronics.__init__(self, game, level)
        self.name = "bonnie"
        self.pos = "Show Stage"
        self.jump_art = art_jump_bonnie
        self.waiting_time = 4.97

        self.path = ("Show Stage", "BackStage", "Show Stage",
                     "Dining Area", "Left Hall", "office light_left", "office")


class Chica(Animatronics):
    def __init__(self, game, level: int):
        Animatronics.__init__(self, game, level)
        self.name = "chica"
        self.pos = "Show Stage"
        self.jump_art = art_jump_chica
        self.waiting_time = 4.98

        self.path = ("Show Stage", "Dining Area", "Show Stage", "Toilets",
                     "Right Hall", "office light_right", "office")


class Foxy(Animatronics):
    def __init__(self, game, level: int):
        Animatronics.__init__(self, game, level)
        # le niveau de sortie de Foxy
        # 0 : dedans --> 4 : sorti
        self.stage_out = 0
        self.name = "foxy"
        self.waiting_time = 5.01
        self.power_taking = 1
        self.run_sound = mixer.Sound("src/Run.wav")

        self.jump_art = art_jump_foxy

    def run(self):
        while self.game.running:
            time.sleep(self.waiting_time)
            if not self.game.monitor.isOn:
                if self.check_movement_opportunity():
                    # il se déplace
                    self.stage_out += 1

                    if self.stage_out == 3:
                        self.run_sound.play()
                        time.sleep(2)
                        if self.game.office.left.door.is_open:
                            self.jumpscare()
                        else:
                            self.knock_sound.play()
                            self.game.batt_level -= self.power_taking
                            self.power_taking += 6
                            self.stage_out = 0
            else:
                time.sleep(uniform(0.83, 6.67))


class Freddy(Animatronics):
    def __init__(self, game, level: int):
        super().__init__(game)
        self.name = "freddy"
        self.pos = "Show Stage"
        self.jump_art = art_jump_freddy
        self.waiting_time = 3.02

        self.path = ("Show Stage", "Dining Area", "Show Stage", "Toilets",
                     "Right Hall")

    def countdown(self):
        countdown_value = (1000-(100*self.level))*1.67
        if countdown_value < 0:
            countdown_value = 0
        time.sleep(countdown_value)

    def run(self):
        while self.game.running:
            time.sleep(self.waiting_time)
            # if self.check_movement_opportunity() and self.game.monitor.current_camera != self.pos:
            if self.check_movement_opportunity():
                self.countdown()
                self.move()
            self.is_on_office()

    def move(self):
        if self.game.monitor.isOn and self.game.monitor.current_camera == self.pos:
            # he can't move cuz we watch him
            time.sleep(self.waiting_time)  # he waits a little
        else:
            self.path_pos += 1
        try:
            self.pos = self.path[self.path_pos]
        except IndexError:
            self.path_pos = 0
            self.pos = self.path[self.path_pos]

    def is_on_office(self):
        # freddy ne rentre pas dans l'office, mais reste dans le right hall
        if self.pos == "Right Hall":
            if self.game.office.right.door.is_open and self.game.monitor.isOn \
                    and self.game.monitor.current_camera != self.pos:
                self.countdown()
                self.jumpscare()

            else:
                self.game.office.right.light.anim_name = ""
                self.path_pos = 4  # he never leaves the corner
                self.pos = self.path[self.path_pos]
