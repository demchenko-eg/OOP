from Figure import Figure

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        super().__init__(dim=2)
        self.a = a
        self.b = b
        self.h = h
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.h