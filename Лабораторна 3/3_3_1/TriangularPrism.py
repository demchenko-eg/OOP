from Triangle import Triangle
from math import sqrt

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h
    def dimension(self):
        return 3
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def square(self):
        p = (self.a + self.b + self.c) / 2
        return self.a * self.b + self.b * self.c + self.a * self.c + 2 * sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def volume(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) * self.h