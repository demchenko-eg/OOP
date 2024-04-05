from Rational import Rational

def lire(r):
    lst = []
    elem = ''
    for ch in r:
        if ch.isdigit() or ch == '/':
            elem += ch
        if ch in '+-*':
            lst.append(elem)
            lst.append(ch)
            elem = ''
    lst.append(elem)
    return lst

def rec(lst):
    new_lst = []
    for elem in lst:
        try:
            new_lst.append(int(elem))
        except ValueError:
            if '/' in elem:
                new_lst.append(Rational(elem))
            else:
                new_lst.append(elem)
    return new_lst

def calc(xop):
    result = xop[0]
    for i in range(1, len(xop), 2):
        op1 = xop[i]
        op2 = xop[i + 1]
        if op1 == '+':
            result += op2
        elif op1 == '-':
            result -= op2
        elif op1 == '*':
            result *= op2
    return result

# rr = "93  *  92  *  86/79  +  31  +  20  *  29/23  +  7  +  25  +  44  *  15"
# # print(rec(lire(rr)))
# print(calc(rec(lire(rr))))


if __name__ == "__main__":
    with open('input01_1.txt', 'r') as input_file, open('results_1_1.txt', 'w') as output_file:
        for line in input_file:
            expression = rec(lire(line.strip()))
            result = calc(expression)
            output_file.write(str(result) + '\n')
