import pygame as pg

from .constpack import CELL_SIZE

class Cell(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([CELL_SIZE, CELL_SIZE])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def fill(self, color):
        self.image.fill(color)

    def get_coords(self):
        return (self.rect.x, self.rect.y)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x):
        self.rect.x += x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, y):
        self.rect.y += y
