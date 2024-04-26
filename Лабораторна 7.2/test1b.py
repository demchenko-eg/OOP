def t1b(n):
    sum_sn = 0
    a1, a2 = 1, 1
    s1 = 3 / a1
    s2 = (3 ** n) / a2
    if n == 1:
        return s1
    elif n == 2:
        return s1 + s2
    else:
        sum_sn = 12
        for k in range(3, n + 1):
            ak = a2 / k + a1
            sum_sn += (3 ** k) / ak
            a1, a2 = a2, ak
    return sum_sn

n = int(input('Введіть кількість членів послідовності: '))
print("Сума при n = ", n, ": ", t1b(n), sep='')