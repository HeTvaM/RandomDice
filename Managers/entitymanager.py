import os
import pygame as pg
from icecream import ic

from Entities.entities import *

class EntityManager:
    def __init__(self, screen):
        self.screen = screen
        self.entity = []
        self.group = pg.sprite.Group()

        self.amount = 0
        self.time = 0

    def set_params(self, amount, duration):
        self.amount = amount
        self.duration = duration

    def spawn(self):
        def create_entity():
            new = Base(
               50, 2, 10
            )

            self.entity.append(new)
            self.group.add(new)

        if len(self.entity) >= self.amount:
            return True

        if self.time >= self.duration:
            self.time = 0
            create_entity()

        self.time += 1

    def take_dmg(self, dmg):
        pass

    def update(self):
        self.spawn()

        for cell in self.group:
            cell.move()
            ic(cell.coords())
        self.group.update()

        self.group.draw(self.screen)
