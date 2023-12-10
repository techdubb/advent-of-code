# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def check(x):
    return x and [x[0]]*len(x) == x and ( x[0] == 0)

def breakdown(s):
    layers = [s]
    layer = s
    while not check(layer):
        layer = [layer[i+1] - layer[i] for i in range(0, len(layer)-1)]
        layers.append(layer)

    return layers

def get_next_element(b):
    b.reverse()
    next = 0
    for layer in b:
        next = layer[0] - next

    return next

sequences = []
for line in f:
    l = [int(x) for x in line.strip().split(' ')]
    if l:
        sequences.append(l)

breakdowns = [breakdown(s) for s in sequences]

nexts = [get_next_element(b) for b in breakdowns]
print(sum(nexts))

