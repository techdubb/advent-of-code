# f = open("input_test.txt", "r")
f = open("input.txt", "r")
depths = []

for line in f:
    depths.append(int(line.strip()))

increases = 0
triples = []

for i in range(0, len(depths)-2):
    new_triple = depths[i] + depths[i+1] + depths[i+2]
    triples.append(new_triple)

for i in range(1, len(triples)):
    if triples[i] - triples[i-1] > 0:
        increases += 1

print(increases)
