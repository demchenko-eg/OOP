from Rational import Rational
from RationalList import RationalList

def lire(r):
    lst = []
    elem = ''
    for ch in r:
        if ch.isdigit() or ch in '/-':
            elem += ch
        if ch.isspace():
            lst.append(elem)
            elem = ''
    lst.append(elem)
    return lst

def transform(lst):
    new_lst = []
    for el in lst:
        if el == '':
            continue
        try:
            new_lst.append(int(el))
        except ValueError:
            if '/' in el:
                new_lst.append(Rational(el))
            else:
                new_lst.append(el)
    return new_lst

def summ(lst):
    count = 0
    for el in lst:
        count += el
    return count

# r = '-25/5  -9  -2/16  -1  -12/7  13/14  17/7  24  14/2  25/22  2  '
# print(summ(transform(lire(r))))

if __name__ == "__main__":
    with open('input01.txt', 'r') as input_file, open('results01.txt', 'w') as output_file:
        for line in input_file:
            expression = transform(lire(line.strip()))
            result = summ(expression)
            output_file.write(str(result) + '\n')
    with open('input02.txt', 'r') as input_file, open('results02.txt', 'w') as output_file:
        for line in input_file:
            expression = transform(lire(line.strip()))
            result = summ(expression)
            output_file.write(str(result) + '\n')
    with open('input03.txt', 'r') as input_file, open('results03.txt', 'w') as output_file:
        for line in input_file:
            expression = transform(lire(line.strip()))
            result = summ(expression)
            output_file.write(str(result) + '\n')