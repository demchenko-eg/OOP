from Triangle import Triangle
from math import sqrt

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h
    def dimension(self):
        return 3
    def squareSurface(self):
        return (1/2) * 3 * self.a * self.h
    def squareBase(self):
        return sqrt(3) * (self.a ** 2) / 4
    def height(self):
        return self.h
    def volume(self):
        return 1 / 3 * self.squareBase() * self.h