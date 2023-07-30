import threading
import time
from src.Game import Game
from src.office_state import art_jump_golden, OFFICE_GF_art, OFFICE_art
import os
from pygame import mixer
from random import randint
mixer.init()


class Clocking:
    """
    Class de gestion du temps en parallèle / threading du jeu CmdFNaF
    """

    def __init__(self):
        self.game = Game()

        self.init_night()

        if self.game.freddy.level == 1 and self.game.bonnie.level == 9 \
                and self.game.chica.level == 8 and self.game.foxy.level == 7:
            self.game.clear_screen()
            os.system('mode con: cols=25 lines=17')
            print(art_jump_golden)
            time.sleep(5)
        else:
            self.gameThread = GameThread(self.game)
            self.clockThread = ClockThread(self.game)
            self.freddyThread = AnimatronicThread(self.game.freddy)
            self.bonnieThread = AnimatronicThread(self.game.bonnie)
            self.chicaThread = AnimatronicThread(self.game.chica)
            self.foxyThread = AnimatronicThread(self.game.foxy)
            self.goldenThread = GoldenThread(self.game)
            self.soundThread = SoundThread(self.game)
            self.batteryThread = BatteryThread(self.game)

            self.run()

    def run(self):
        os.system('mode con: cols=25 lines=17')
        self.gameThread.start()
        self.clockThread.start()
        self.freddyThread.start()
        self.bonnieThread.start()
        self.chicaThread.start()
        self.foxyThread.start()
        self.goldenThread.start()
        self.soundThread.start()
        self.batteryThread.run()

    def init_night(self):
        try:
            self.game.freddy.level = int(input("A quel niveau mets-tu l'IA de FREDDY? (0 à 20) - def 0 -->"))
        except ValueError:
            self.game.freddy.level = 0

        if self.game.freddy.level > 20:
            self.game.freddy.level = 20
        if self.game.freddy.level < 0:
            self.game.freddy.level = 0

        try:
            self.game.bonnie.level = int(input("A quel niveau mets-tu l'IA de BONNIE? (0 à 20) - def 0 -->"))
        except ValueError:
            self.game.bonnie.level = 0

        if self.game.bonnie.level > 20:
            self.game.bonnie.level = 20
        if self.game.bonnie.level < 0:
            self.game.bonnie.level = 0

        try:
            self.game.chica.level = int(input("A quel niveau mets-tu l'IA de CHICA? (0 à 20) - def 0 -->"))
        except ValueError:
            self.game.chica.level = 0
        if self.game.chica.level > 20:
            self.game.chica.level = 20
        if self.game.chica.level < 0:
            self.game.chica.level = 0

        try:
            self.game.foxy.level = int(input("A quel niveau mets-tu l'IA de FOXY? (0 à 20) - def 0 -->"))
        except ValueError:
            self.game.foxy.level = 0

        if self.game.foxy.level > 20:
            self.game.foxy.level = 20
        if self.game.foxy.level < 0:
            self.game.foxy.level = 0


class ClockThread(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game: Game = game
        self.hour: int = self.game.clock

    def run(self):
        while self.game.running:
            if self.hour == 6:
                self.game.running = False
                time.sleep(0.5)
                self.game.running = False
                self.game.six_am()
            else:
                time.sleep(60)
                self.hour += 1
                self.game.add_one_hour()


class GameThread(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game

    def run(self):
        self.game.run()


class AnimatronicThread(threading.Thread):
    def __init__(self, animatronic):
        threading.Thread.__init__(self)
        self.animatronic = animatronic

    def run(self):
        self.animatronic.run()


class SoundThread(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game
        self.music = mixer.music
        self.music.load("src/Vent.wav")

    def run(self):
        while self.game.running:
            self.music.play()
        self.music.stop()


class BatteryThread(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game

    def run(self):
        while self.game.running:
            time.sleep(3)
            self.game.batt_level -= 1
            self.game.batt_level -= self.game.comsum * 0.5
            if self.game.office.side == 1 and not self.game.monitor.isOn and self.game.running:
                self.game.clear_screen()
                self.game.office.show(self.game.clock, self.game.comsum)


class GoldenThread(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game
        self.has_appeared = False
        self.scream_sound = mixer.Sound("src/GFScream.wav")

    def run(self):
        while not self.has_appeared:
            time.sleep(1)
            appear_chance: bool = randint(1, 1000) == 1
            waited_time = 0
            if appear_chance:
                self.game.office.desk_art = OFFICE_GF_art
                self.has_appeared = True
                while not self.game.monitor.isOn:
                    time.sleep(0.1)
                    waited_time += 0.1
                    if waited_time >= 3:
                        self.scream_sound.play()
                        print(art_jump_golden)
                        self.game.running = False
                        break
                self.game.office.desk_art = OFFICE_art
            else:
                self.game.office.desk_art = OFFICE_art
