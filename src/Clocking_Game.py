import threading
import time
from src.Game import Game
import os
from pygame import mixer
mixer.init()


class Clocking:
    """
    Class de gestion du temps en parallèle / threading du jeu CmdFNaF
    """

    def __init__(self):
        self.game = Game()

        try:
            print()
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

        self.gameThread = GameThread(self.game)
        self.clockThread = ClockThread(self.game)
        self.bonnieThread = AnimatronicThread(self.game.bonnie)
        self.chicaThread = AnimatronicThread(self.game.chica)
        self.foxyThread = AnimatronicThread(self.game.foxy)
        self.soundThread = SoundThread(self.game)
        self.batteryThread = BatteryThread(self.game)

    def run(self):
        os.system('mode con: cols=25 lines=17')
        self.gameThread.start()
        self.clockThread.start()
        self.bonnieThread.start()
        self.chicaThread.start()
        self.foxyThread.start()
        self.soundThread.start()
        self.batteryThread.run()


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
            time.sleep(2.75)
            self.game.batt_level -= self.game.comsum * 0.5
            if self.game.office.side == 1 and not self.game.monitor.isOn and self.game.running:
                self.game.clear_screen()
                self.game.office.show(self.game.clock, self.game.comsum)
