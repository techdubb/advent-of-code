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

good_updates = []
for u in updates:
    ulist = u.split(',')
    good = True
    for idx, page in enumerate(ulist):
        rest = ulist[idx+1:]


        for r in rest: 
            if r in rule_dict and page in rule_dict[r]:
                good = False


    if good:
        good_updates.append(ulist)


middles = []
for g in good_updates:
    middles.append(int(g[len(g) // 2]))


print(middles)
print(sum(middles))

