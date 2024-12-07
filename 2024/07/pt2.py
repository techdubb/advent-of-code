import itertools

def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            i.append(ln)

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

def math_operator(a, b, op):
    ops = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '|': lambda x, y: int(str(x) + str(y))
    }
    return ops[op](a, b)

fixable = []
for i in input:
    cali, rest = i.split(':')

    vals = rest.strip().split(' ')

    vals = [int(x) for x in vals]
    cali = int(cali)

    operators = '*+|'
    possibilities = list(itertools.product(operators, repeat = (len(vals)-1)))

    for p in possibilities:
        res = vals[0]

        for idx in range(1, len(vals)):
            res = math_operator(res, vals[idx], p[idx-1])

        if res == cali:
            fixable.append(cali)
            break

print(sum(fixable))
