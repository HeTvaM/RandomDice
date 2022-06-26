#import system libs
import sys
import os
import pygame as pg


from Stuff.constpack import terminal, EMERALD
from Stuff.constpack import CELL_SIZE
from icecream import ic

from Stuff.scene import SceneABS
from gamecontroller import GameController

from PygameWidgets.wPygame.Widgets import Font, Text


class Window(SceneABS):
    def __init__(self, screen, FPS):
        super().__init__(screen, FPS)

        self.controller = GameController()
        self.controller.set_screen(screen)

    def create_widget(self):
        pass

    def create_data(self, data):
        self.controller.start(5, 90)

    def update(self, mouse):
        self.controller.update(mouse)

    def check(self, event, mouse):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1: pass

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.controller.start(5, 90)

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1: pass

def run():
    pg.init()
    screen = pg.display.set_mode((1000, 1000))
    pg.display.set_caption("HERandomDice - 1.0a")
    FPS = 10

    win = Window(screen, FPS)
    ic("WORK")
    win.start()


if __name__=="__main__":
    run()
