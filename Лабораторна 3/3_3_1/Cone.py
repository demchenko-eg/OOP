from Circle import Circle
from math import sqrt, pi

class Cone(Circle):
    def __init__(self, radius, h):
        super().__init__(radius)
        self.h = h
        self.radius = radius
    def dimension(self):
        return 3
    def squareSurface(self):
        t = sqrt((self.h**2) + (self.radius**2))
        return pi * self.radius * t
    def squareBase(self):
        return pi * self.radius ** 2
    def height(self):
        return self.h
    def volume(self):
        return (1 / 3) * self.squareBase() * self.h