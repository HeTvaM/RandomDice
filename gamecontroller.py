import pygame as pg
from Stuff.constpack import CELL_SIZE

from Stuff.wrapper import MetaSingleton
from Managers.entitymanager import EntityManager

class GameController(metaclass = MetaSingleton):
    def __init__(self): pass

    def set_screen(self, screen):
        self.screen = screen
        self.eManager = EntityManager(screen)

    def click(self, mouse, key, id=3):
        pass

    def start(self, amount, duration):
        self.eManager.set_params(amount, duration)

    def update(self, mouse):
        self.eManager.update()

    def remove(self):
        pass
