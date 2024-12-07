import copy

def parse_textfile(filename):
    i = [list(), list()]
    x = 0
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            if (ln==''):
                x += 1
            else:
                i[x].append(ln)

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

rules = input[0]
updates = input[1]

rule_dict = {}
for r in rules:
    b,a = r.split('|')

    if b in rule_dict:
        rule_dict[b].append(a)
    else:
        rule_dict[b] = [a]

def is_good(u):
    good = True
    for idx, page in enumerate(u):
        rest = u[idx+1:]

        for r in rest: 
            if r in rule_dict and page in rule_dict[r]:
                good = False

    return good

bad_updates = []
for u in updates:
    ulist = u.split(',')

    if not is_good(ulist):
        bad_updates.append(ulist)

fixed_updates = []
for b in bad_updates:       
    while not is_good(b):
        for idx, page in enumerate(b):
            rest = b[idx+1:]

            for jdx, r in enumerate(rest):
                if r in rule_dict and page in rule_dict[r]:
                    real_jdx = (idx+1)+jdx
                    new = b
                    new[idx], new[real_jdx] = new[real_jdx], new[idx]


middles = []
for b in bad_updates:
    middles.append(int(b[len(b) // 2]))


print(middles)
print(sum(middles))