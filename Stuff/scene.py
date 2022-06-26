import sys
import pygame as pg

from abc import ABC, abstractmethod

class SceneABS(ABC):
    def __init__(self, screen, FPS):
        self.sc = screen
        self.clock = pg.time.Clock()
        self.FPS = 60

        self.widgets = {}
        self.defs =  []
        self.params = []

    def check_event(self, mouse):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            self.check(event, mouse)

    def start(self, data=None):
        self.create_widget()
        self.create_data(data)
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)

        play = True
        while play:
            self.clock.tick(self.FPS)

            mouse = pg.mouse.get_pos()

            self.check_event(mouse)
            self.sc.fill((0,0,0))
            self.update(mouse)
            pg.display.flip()

    @abstractmethod
    def update(self, mouse):
        pass

    @abstractmethod
    def create_data(self, data):
        if not data:
            pass

    @abstractmethod
    def check(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_widget(self):
        pass
