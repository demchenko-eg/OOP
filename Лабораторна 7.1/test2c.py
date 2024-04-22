from math import factorial as f

def t2c(x, n):
    a = 1
    for k in range(1, n + 1):
        a = ((-1) ** k) * (x ** k) / f((k ** 2) + k)
    return a

def t2c_generator(x, n):
    a = x
    for k in range(2, n + 1):
        a = ((-1) ** k) * (x ** k) / f((k ** 2) + k)
        yield a

x = int(input('Введіть значення х: '))
n = int(input('Введіть номер члена почлідовності: '))
print(t2c(x, n))

s = list(t2c_generator(x, n))
print(s[n-2])