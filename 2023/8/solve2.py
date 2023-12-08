from numpy import lcm

# f = open("input_test2.txt", "r")
f = open("input.txt", "r")

input = []
for line in f:
    l = line.strip()
    if l:
        input.append(l)

instruct = ''
nodes = {}
for idx, i in enumerate(input):
    if idx == 0:
        instruct = list(i)
    else:
        split_i = i.split(' = ')
        nexts = split_i[1].split(', ')
        nodes[split_i[0]] = [nexts[0][1:], nexts[1][:-1]]

print(instruct)
print(nodes)

def is_done(currs):
    true_currs = filter(lambda x: x.endswith('Z'), currs)

    return len(list(true_currs)) == len(currs)


instruct_len = len(instruct)
currents = []
for k in nodes.keys():
    if k.endswith('A'):
        currents.append(k)

all_steps = []

for c in currents:
    steps = 0
    while not c.endswith('Z'):
        ins = instruct[(steps % instruct_len)]
        if ins == 'L':
            c = nodes[c][0]
        elif ins == 'R':
            c = nodes[c][1]
        steps += 1
    all_steps.append(steps)

# print(8*'*')
print(all_steps)
print(lcm.reduce(all_steps))