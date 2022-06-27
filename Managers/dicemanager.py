import os

from Dices.dices import *
from .zonemanager import ZoneManager
from Stuff.wrapper import check_amount

class DiceManager:
    def __init__(self, screen, group):
        self.screen = screen

        self.zManager = ZoneManager()
        self.amount = 0

        self.group = group

    def attack(self):
        pass

    @check_amount
    def build(self):
        coords = self.zManager.get_coords()

    def upgrade(self):
        pass

    def click(self):
        pass

    def update(self):
        pass

    def remove(self):
        self.zManager.remove()
        self.amount = 0
        self.group.clear()
