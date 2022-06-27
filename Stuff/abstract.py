import os
import pygame as pg

from abc import ABC, abstractmethod

from .cell import Cell
from .constpack import DICE_TYPES, COORDS, DICE_COLORS
from .constpack import START_X, START_Y
from .constpack import RED

class Obj(ABC, Cell):
    @staticmethod
    def draw(text, coords, value):
        text.change_text(f"{value:2.0f}")
        text.draw_in_obj(*coords)

    def __init__(self, x, y, color=RED):
        super().__init__(x, y)
        self.fill(color)


class Dice(Obj):
    def __init__(
                 self, x, y,
                 type,
                 dmg, duration,
                 effect=None
    ):
        super().__init__(
            x,y,
            DICE_COLORS[DICE_TYPES[type]]
        )

        self.lvl = 1
        self.time = 0

        self.focus = False
        self.dmg = dmg
        self.duration = duration
        self.type = DICE_TYPES[type]

        self.effect = effect

    def duplicate(self, obj):
        if obj.type == self.type \
           and obj.lvl == self.lvl:
           self.dmg += DMG[self.type]
           self.lvl += 1
           return True

        return False

    def focus(self):
        return self.focus()

    def upgrade(self):
        self.dmg += DMG_UPGRADE[self.type]

    @abstractmethod
    def do_ability(self):
        pass

    @abstractmethod
    def attack(self):
        pass

class Entity(Obj):
    def __init__(
                 self,
                 hp, speed, armor
    ):
        super().__init__(
            START_X, START_Y,
            color=RED
        )

        self.hp = hp
        self.speed = speed
        self.armor = armor/100

        self.flag = True

    def move(self):
        self.is_move()

        if self.flag:
            self.y = -self.speed
        else:
            self.x = self.speed

    def is_move(self):
        if self.y <= COORDS[0]:
            self.flag = False

        if self.x >= COORDS[1] and not self.flag:
            self.speed *= -1
            self.flag = True

    def attacked(self, dmg):
        self.hp -= int(dmg * (1 - self.armor))

    def is_dead(self):
        if self.hp <= 0:
            return True

        return False

    @abstractmethod
    def do_ability(self):
        pass
