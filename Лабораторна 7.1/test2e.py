from math import factorial as f

def t2e(x, n):
    a = 1
    for k in range(1, n + 1):
        a = ((-1) ** k) * (x ** (2*k)) / f(2*k)
    return a

x = int(input('Введіть значення х: '))
n = int(input('Введіть номер члена почлідовності: '))
print(t2e(x, n))