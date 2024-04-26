def t1a(n):
    sum_sn = 0
    a1, a2 = 0, 1
    b1, b2 = 1, 1
    s1 = 2 / (a1 + b1)
    s2 = (2 ** n) / (a2 + b2)
    if n == 1:
        return s1
    elif n == 2:
        return s1 + s2
    else:
        sum_sn = 4
        for k in range(3, n + 1):
            bk = b2 + a2
            ak = a2 / k + a1 * bk
            sum_sn += (2 ** k) / (ak + bk) 
            a1, a2 = a2, ak
            b1, b2 = b2, bk
    return sum_sn


n = int(input('Введіть кількість членів послідовності: '))
print(f'Сума {n} членів послідовності = {t1a(n)}')
