class Rational:
    def __init__(self, *args):
        if len(args) == 1:
            n, d = map(int, args[0].split('/'))
        elif len(args) == 2:
            n, d = args

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        cd = gcd(n, d)
        self.n = n // cd
        self.d = d // cd

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if type(other) == Rational:
            return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
        elif type(other) == int:
            return Rational(self.n + other * self.d, self.d)

    def __sub__(self, other):
        if type(other) == Rational:
            return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
        elif type(other) == int:
            return Rational(self.n - other * self.d, self.d)
        
    def __mul__(self, other):
        if type(other) == Rational:
            return Rational(self.n * other.n, self.d * other.d)
        elif type(other) == int:
            return Rational(self.n * other, self.d)

    # def __truediv__(self, other):
    # #Функція не допрацьована для ділення цілого числа на раціональне
    #     if type(self) == Rational and type(other) == Rational:
    #         if other.d == 0 or self.d == 0:
    #             # raise ValueError("Ділення на нуль")
    #             return "На нуль ділити не можна"
    #         return Rational(self.n * other.d, self.d * other.n)
    #     elif type(self) == int:
    #         if other.d == 0 or self == 0:
    #             # raise ValueError("Ділення на нуль")
    #             return "На нуль ділити не можна"
    #         return Rational(self * other.d, other.n)
    #     elif type(other) == int:
    #         if other == 0 or self.d == 0:
    #             # raise ValueError("Ділення на нуль")
    #             return "На нуль ділити не можна"
    #         return Rational(self.n, self.d * other)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        elif key == 'd':
            return self.d
    
    def __radd__(self, other):
        if type(other) == Rational:
            return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
        elif type(other) == int:
            return Rational(self.n + other * self.d, self.d)
    def __rsub__(self, other):
        if type(other) == int:
            return Rational(other * self.d - self.n, self.d)
        elif type(other) == Rational:
            return Rational(other.n * self.d - self.n * other.d, self.d * other.d)
    def __rmul__(self, other):
        if type(other) == Rational:
            return Rational(self.n * other.n, self.d * other.d)
        elif type(other) == int:
            return Rational(self.n * other, self.d)
    


# if __name__ == "__main__":
#     r1 = Rational(11, 2)
#     r2 = Rational(1, 5)
#     i = 5
#     i2 = 2
#     r = i - r1
#     # print(r['n'])
#     # print(r['d'])
#     # print(r())
#     r*=r2
#     r+=r1
#     print(r)