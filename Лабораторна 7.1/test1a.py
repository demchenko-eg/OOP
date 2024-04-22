from math import sqrt as s

def sqrt2(n):
    a = s(2)
    for i in range(1, n):
        a = s(2 + a)
    return a

n = int(input())
print(sqrt2(n))