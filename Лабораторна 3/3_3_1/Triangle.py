from Figure import Figure
from math import sqrt

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(dim=2)
        self.a = a
        self.b = b
        self.c = c
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        s = self.perimetr() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))