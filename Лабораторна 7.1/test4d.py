def t4d(n):
    # if n == 1:
    #     return 0
    # elif n == 2:
    #     return 1
    # else:
    #     d0 = 0
    #     d1 = 1
    #     for i in range(3, n + 1):
    #         d2 = d0
    #         d0, d1 = d1, d2
    #     return d1

    if n % 2 == 1:
        return 0
    else:
        return 1

n = int(input())
print(t4d(n))
