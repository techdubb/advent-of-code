p = print

def parse_line(line):
    parsed = []
    paren_depth = 0
    for e in line:
        if e == ' ':
            continue
        elif e == '(':
            p(e)
            # parsed.append(parsed)
        elif e == '+' or e == '*':
            # p(e)
            parsed.append(e)
        else:
            # p(int(e))
            parsed.append(int(e))

def do_math(line):
    eq = list(line)
    total = int(eq[0])
    operator = ''

    for e in eq[1:]:
        if e == ' ':
            pass
        elif e == '+' or e == '*':
            operator = e
        else:
            if operator == '*':
                total *= int(e)
            elif operator == '+':
                total += int(e)

    return total

homework = []
f = open("input_test.txt", "r")
for line in f:
    sline = line.strip()
    homework.append(sline)

sp = homework[5].split('(')

parts = []
for s in sp:
    split = s.strip().split(')')

    if len(split) == 1 and split[0] == '':
        pass
    else:
        parts.append(split)

p(parts)

# for prt in parts:
#     if prt[0].isnumeric() and prt[-1].isnumeric():
#         p(do_math(prt))
#     else:
#         p('didnt do anything')

# p(homework)

# parse_line(homework[1])
