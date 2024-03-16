class Equation:

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.b}x + {self.c} = 0"

    def show(self, file=None):
        if file:
            file.write(f"{self}\n")
        else:
            print(self)

            
    INF = "infinity"
    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.INF
            else:
                return ()
        else:
            return (-self.c / self.b,)