from Equation import Equation
class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def __str__(self):
        return f"{self.a}x^2 + " + super().__str__()

    def discr(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            d = self.discr()
            if d < 0:
                return ()
            elif d == 0:
                x1 = - self.b / (2 * self.a)
                return (x1, )
            else:
                d_sqr = d ** 0.5
                x1 = (- self.b + d_sqr) / (2 * self.a)
                x2 = (- self.b - d_sqr) / (2 * self.a)
                return (x1, x2)