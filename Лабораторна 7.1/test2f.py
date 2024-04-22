from math import factorial as f

def t2f(x, n):
    a = x
    for k in range(1, n + 1):
        a = (x ** (2*k + 1)) / f(2*k + 1)
    return a

x = int(input('Введіть значення х: '))
n = int(input('Введіть номер члена почлідовності: '))
print(t2f(x, n))