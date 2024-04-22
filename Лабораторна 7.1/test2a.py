def t2a(x, n):
    a = x
    for k in range(2, n + 1):
        a = (x ** k) / k
    return a

def t2a_generator(x, n):
    a = x
    for k in range(2, n + 1):
        a = (x ** k) / k
        yield a

x = int(input('Введіть значення х: '))
n = int(input('Введіть номер члена почлідовності: '))
print(t2a(x, n))

s = list(t2a_generator(x, n))
print(s[n-2])