import os
import pygame as pg
from icecream import ic

import gamecontroller as gc
from Entities.entities import *

class EntityManager:
    def __init__(self, screen):
        self.screen = screen
        self.entity = []
        self.group = pg.sprite.Group()
        self.controller = gc.GameController()

        self.amount = 0
        self.time = 0
        self.n = 0
        self.dead = 0

    def set_params(self, amount, duration):
        self.amount = amount
        self.duration = duration

    def spawn(self):
        def create_entity():
            new = Base(
               50, 5, 10
            )

            self.entity.append(new)
            self.group.add(new)

        if self.n >= self.amount:
            return True

        if self.time >= self.duration:
            create_entity()
            self.time = 0
            self.n += 1

        self.time += 1

    def take_dmg(self, dmg):
        pass

    def update(self):
        self.spawn()
        try:
            first = self.entity[0]
        except IndexError:
            first = None

        for cell in self.group:
            cell.move()

            if cell.is_dead():
                self.dead += 1

                if cell == first:
                    self.entity.pop(0)
                    first = self.entity[0]
                else:
                    self.entity.pop()
                self.group.remove(cell)

                if self.dead == self.amount:
                    self.remove()
                    self.controller.loadlvl()
                    break

            if first.y > 1000:
                self.controller.gamelose()

        if self.dead == self.amount:
            self.remove()
            self.controller.loadlvl()

        self.group.update()
        self.group.draw(self.screen)

    def kill(self):
        self.dead += 1
        self.group.remove(
            self.entity.pop(0)
        )

    def remove(self):
        self.amount = 0
        self.duration = 0
        self.time = 0
        self.n = 0
        self.dead = 0
        self.entity = []
        self.group = pg.sprite.Group()
