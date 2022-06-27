import os
import pygame as pg
import gamecontroller as gc
from icecream import ic

from Entities.entities import *

from Stuff.constpack import CELL_SIZE
from Stuff.constpack import HP, SPEED, ARMOR
from PygameWidgets.wPygame.Widgets import Font, Text
from PygameWidgets.wPygame.constpack import WHITE, terminal


FONT = Font(terminal, WHITE, 30)


class EntityManager:
    def __init__(self, screen, group):
        self.screen = screen
        self.entity = []
        self.group = group
        self.controller = gc.GameController()

        self.amount = 0
        self.time = 0
        self.dead = 0
        self.n = 0

        self.text = Text(
            screen, "50", font=FONT,
            text_location="C"
        )
        self.text.location(CELL_SIZE, CELL_SIZE)

    def set_params(self, amount, duration):
        self.amount = amount
        self.duration = duration

    def spawn(self):
        def create_entity():
            new = Base(
               HP, SPEED, ARMOR
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

        for cell in self.group:
            cell.draw(
                self.text,
                cell.get_coords(), cell.hp
            )

    def kill(self):
        self.dead += 1
        self.group.remove(
            self.entity.pop(0)
        )

    def remove(self):
        for i in range(self.n):
            self.group.remove()
        self.amount = 0
        self.duration = 0
        self.time = 0
        self.n = 0
        self.dead = 0
        self.entity = []
