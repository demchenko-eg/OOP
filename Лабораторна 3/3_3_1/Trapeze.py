from Figure import Figure
from math import sqrt

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(dim=2)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimetr(self):
        if self.a == self.b and self.c != self.d:
            return None
        elif self.a == self.b and self.c == self.d:
            return 2 * (self.a + self.c)
        return self.a + self.b + self.c + self.d
    def square(self):
        if self.a == self.b and self.c != self.d:
            return None
        elif self.a == self.b and self.c == self.d:
            return self.a * self.c
        return (((self.a + self.b) / 2) * sqrt((self.c ** 2) - (((self.a - self.b) ** 2) + (self.c ** 2) - (self.d ** 2)) / (2 * (self.a - self.b)) ** 2))