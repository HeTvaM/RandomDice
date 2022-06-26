import pygame as pg
import gamecontroller as gc

from random import randint
from zone import Zone
from constpack import COLORS_TYPES
from constpack import MIN, MAX, CELL_SIZE, ROAD_LEN

class RoadManager:
    def __init__(self, screen):
        self.screen = screen
        self.ready_toChange = None
        self.corners = []

        self.controller = gc.GameController()
        self.roads = pg.sprite.Group()

    def new_road(self, coords, vector2D):
        road = Zone(vector2D, *coords)
        cells = road.create_cells(COLORS_TYPES["ROAD"])
        new_cells = [cell.get_coords() for cell in cells]

        freezones_coords = self.controller.freezones
        for cell in freezones_coords:
            if cell.get_coords() in new_cells:
                freezones_coords.remove(cell)
            
        self.controller.freezones = freezones_coords

        self.roads.add(cells)
        self.corners.append(road.get_corners())
        self.create_freezones(road, vector2D)

    def create_freezones(self, road, vector2D):
        freezones_list = []
        freezones = pg.sprite.Group()
        size = [randint(MIN, MAX) for i in range(2)]
    
        coords = road.get_coords()

        if vector2D[0] == ROAD_LEN: key = 0
        else: key = 1
        
        for i in range(ROAD_LEN):
            vector2D[key] = size[i]
            coords[key] = coords[key]-size[0]*CELL_SIZE if i % 2 == 0 else coords[key]+ROAD_LEN*CELL_SIZE

            freezone = Zone(vector2D, *coords)
            cells = freezone.create_cells(COLORS_TYPES["FREEZONE"])

            for type in range(ROAD_LEN):
                type_coords = self.controller.get_freezones() if type % 2 == 0 else [cell.get_coords() for cell in self.roads]
                for cell in cells:
                    if cell.get_coords() in type_coords:
                        cells.remove(cell)
            
            freezones_list.append(freezone)
            freezones.add(cells)
            coords = road.get_coords()

        self.controller.update_freezones(freezones, freezones_list)
    
    def get_roads(self):
        return self.roads

    def get_corners(self):
        return self.corners

    def update(self):
        self.roads.draw(self.screen)

    def remove(self):
        self.roads = pg.sprite.Group()
        self.corners = []