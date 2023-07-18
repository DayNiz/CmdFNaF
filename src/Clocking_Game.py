import threading
import time
from Game import Game
import os


class Clocking:
    """
    Class de gestion du temps en parallèle / threading du jeu CmdFNaF
    """

    def __init__(self):
        self.game = Game()
        self.game.bonnie.level = int(input("A quel niveau mets-tu l'IA de BONNIE? (0 à 20)"))
        if self.game.bonnie.level > 20:
            self.game.bonnie.level = 20
        if self.game.bonnie.level < 0:
            self.game.bonnie.level = 0
        self.game.chica.level = int(input("A quel niveau mets-tu l'IA de CHICA? (0 à 20)"))
        if self.game.chica.level > 20:
            self.game.chica.level = 20
        if self.game.chica.level < 0:
            self.game.chica.level = 0
        self.gameThread = GameThread(self.game)
        self.clockThread = ClockThread(self.game)
        self.bonnieThread = AnimatronicThread(self.game.bonnie)
        self.chicaThread = AnimatronicThread(self.game.chica)

    def run(self):
        os.system('mode con: cols=25 lines=16')
        self.gameThread.start()
        self.clockThread.start()
        self.bonnieThread.start()
        self.chicaThread.start()


class ClockThread(threading.Thread):
    def __init__(self, game: Game):
        threading.Thread.__init__(self)
        self.game: Game = game
        self.hour: int = self.game.clock

    def run(self):
        while self.game.running:
            if self.hour == 6:
                self.game.running = False
                self.game.six_am()
            else:
                time.sleep(60)
                self.hour += 1
                self.game.add_one_hour()


class GameThread(threading.Thread):
    def __init__(self, game: Game):
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
