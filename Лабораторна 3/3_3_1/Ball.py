from Figure import Figure
from math import pi

class Ball(Figure):
    def __init__(self, radius):
        super().__init__(dim=3)
        self.radius = radius
    def dimension(self):
        return 3
    def squareSurface(self):
        return 4 * 3.14 * self.radius ** 2
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return 4 / 3 * 3.14 * self.radius ** 3