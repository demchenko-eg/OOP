def t2b(x, n):
    a = -x
    for k in range(2, n + 1):
        a = ((-1) ** k) * (x ** k) / k
    return a

def t2b_generator(x, n):
    a = x
    for k in range(2, n + 1):
        a = ((-1) ** k) * (x ** k) / k
        yield a


x = int(input('Введіть значення х: '))
n = int(input('Введіть номер члена почлідовності: '))
print(t2b(x, n))

s = list(t2b_generator(x, n))
print(s[n-2])