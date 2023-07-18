import time
from random import randint


class Animatronics:
    def __init__(self, game, level):
        self.name = None
        self.game = game
        self.map = self.game.monitor
        self.path = [None]
        self.path_pos = 0
        self.pos = self.path[self.path_pos]
        self.level: int = level
        self.movement_opportunity: int = 0

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
        # print(f"{self.name} is MOVING in the {self.pos}!")

    def is_on_office(self):
        if self.pos == "office light":
            self.game.office.left.light.show_anim(self.name)

        if self.pos == "office":
            if (self.name == "bonnie" and self.game.office.left.door.is_open) or (self.name == "chica" and
                                                                                  self.game.office.right.door.is_open):
                self.game.running = False
                print(f"{self.name} KILLED YOU")
        return self.pos == "office"

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
                     "Left Hall", "office light", "office")


class Chica(Animatronics):
    def __init__(self, game, level: int):
        Animatronics.__init__(self, game, level)
        self.name = "chica"
        self.pos = "Show Stage"

        self.path = ("Show Stage", "Dining Area", "Show Stage", "Dining Area",
                     "Right Hall", "office light", "office")
