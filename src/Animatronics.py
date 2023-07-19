import time
from random import randint
from pygame import mixer


class Animatronics:
    def __init__(self, game, level=0):
        self.name = None
        self.game = game
        self.map = self.game.monitor
        self.path = [None]
        self.path_pos = 0
        self.pos = self.path[self.path_pos]
        self.level: int = level
        self.movement_opportunity: int = 0
        self.just_arrive_at_office: bool = True

        self.scream_sound = mixer.Sound("src/sounds/Scream.wav")
        self.knock_sound = mixer.Sound("src/sounds/KnockingDoor.wav")
        self.light_sound = mixer.Sound("src/sounds/SeeLight.wav")

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
        print(f"{self.name} KILLED YOU")

    def run(self):
        while self.game.running:
            time.sleep(4.5)
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

        self.path = ("Show Stage", "BackStage", "Show Stage",
                     "Left Hall", "office light_left", "office")


class Chica(Animatronics):
    def __init__(self, game, level: int):
        Animatronics.__init__(self, game, level)
        self.name = "chica"
        self.pos = "Show Stage"

        self.path = ("Show Stage", "Dining Area", "Show Stage", "Dining Area",
                     "Right Hall", "office light_right", "office")
