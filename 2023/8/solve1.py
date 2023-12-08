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

instruct_len = len(instruct)
current = 'AAA'
goal = 'ZZZ'
steps = 0

while current != goal:
    ins = instruct[(steps % instruct_len)]
    print(ins)
    if ins == 'L':
        current = nodes[current][0]
    elif ins == 'R':
        current = nodes[current][1]
    steps += 1

print(steps)