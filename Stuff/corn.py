from constpack import CELL_SIZE

class Corner:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def __sub__(self, corner):
        new = Corner((abs(self.x - corner.x), abs(self.y-corner.y)))
        return new
    
    def get_coords(self):
        return (self.x, self.y)

    def equal(self, *corner):
        return corner.x == self.x and corner.y == self.y 
    
    def x(self):
        return self.x
    
    def y(self):
        return self.y

