import pygame as pg

from icecream import ic
from Stuff.constpack import CELL_SIZE, LVL

from Stuff.wrapper import MetaSingleton
from Managers.entitymanager import EntityManager

class GameController(metaclass = MetaSingleton):
    def __init__(self):
        self.lvl = 0

    @property
    def level(self):
        return self.lvl

    @level.setter
    def level(self, value):
        if self.lvl >=3:
            self.lvl = 0
        else:
            self.lvl += value

    def set_screen(self, screen):
        self.screen = screen
        self.eManager = EntityManager(screen)

    def click(self, mouse, key, id=3):
        pass

    def start(self, amount, duration):
        self.eManager.set_params(amount, duration)

    def update(self, mouse):
        self.eManager.update()

    def gamelose(self):
        self.eManager.remove()

    def loadlvl(self):
        self.start(*LVL[self.lvl])
        ic(self.lvl)
        self.level = 1

    def kill(self):
        self.eManager.kill()

    def remove(self):
        pass
