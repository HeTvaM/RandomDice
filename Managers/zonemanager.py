import os

from random import choice
from icecream import ic
from Stuff.constpack import CELL_SIZE
from Stuff.constpack import MATRIX, MATRIX_COORDS, MATRIX_STEP

class ZoneManager:
    def __init__(self):
        self.matrix = MATRIX
        self.coords = MATRIX_COORDS
        self.step = MATRIX_STEP

        self.cells = []
        self.create()

    def create(self):
        x, y = self.coords
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                Ox = x + (CELL_SIZE+self.step)*j
                Oy = y + (CELL_SIZE+self.step)*i
                self.cells.append((Ox, Oy))

    def get_coords(self):
        value = choice(self.cells)
        i, j = value - self.coords
        while self.matrix[j][i]:
            value = choice(self.cells)
            i, j = value - self.coords

        self.matrix[j][i] =1
        return value

    def remove(self):
        self.matrix = MATRIX
        self.cells = []
