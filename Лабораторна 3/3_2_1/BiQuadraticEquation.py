from QuadraticEquation import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

    def solve(self):
        set_solutions = set()
        solutions_quadratic = super().solve()
        if solutions_quadratic == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        for solution in solutions_quadratic:
            if solution >= 0:
                t1 = solution ** 0.5
                t2 = -t1
                set_solutions.add(t1)
                set_solutions.add(t2)

        return tuple(set_solutions)