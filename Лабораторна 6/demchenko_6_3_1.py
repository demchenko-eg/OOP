from Rational import Rational
from RationalList import RationalList
from RationalIterator import RationalIterator

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
            new_lst.append(Rational(int(el), 1))
        except ValueError:
            if '/' in el:
                new_lst.append(Rational(el))
            else:
                new_lst.append(el)
    return new_lst

def sort_rational(lst):
    def sort_key(x):
        if type(x) == Rational:
            return (-x.n, x.d)
        else:
            return (0, 0)
    sorted_lst = sorted(lst, key=sort_key)
    return sorted_lst

if __name__ == "__main__":
    with open('input01.txt', 'r') as input_file, open('results01.txt', 'w') as output_file:
        new = []
        for line in input_file:
            sr = sort_rational(transform(lire(line)))
            r_list = RationalList(sr)
            iterator = RationalIterator(r_list)
            for rat in iterator:
                new.append(rat)
                output_file.write(str(rat) + ' ')
            output_file.write('\n')
    with open('input02.txt', 'r') as input_file, open('results02.txt', 'w') as output_file:
        new = []
        for line in input_file:
            sr = sort_rational(transform(lire(line)))
            r_list = RationalList(sr)
            iterator = RationalIterator(r_list)
            for rat in iterator:
                new.append(rat)
                output_file.write(str(rat) + ' ')
            output_file.write('\n')
    with open('input03.txt', 'r') as input_file, open('results03.txt', 'w') as output_file:
        new = []
        for line in input_file:
            sr = sort_rational(transform(lire(line)))
            r_list = RationalList(sr)
            iterator = RationalIterator(r_list)
            for rat in iterator:
                new.append(rat)
                output_file.write(str(rat) + ' ')
            output_file.write('\n')