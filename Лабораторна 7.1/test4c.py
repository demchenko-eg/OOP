def t4c(n):
    if n == 1:
        return 3
    elif n == 2:
        return 3**2 - 2
    else:
        d0 = 3
        d1 = 3**2 - 2
        for i in range(3, n + 1):
            d2 = 3 * d1 - 2 * d0
            d0, d1 = d1, d2
        return d1

n = int(input())
print(len(t4c(n)))
