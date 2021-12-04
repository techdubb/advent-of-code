p = print

adapters = []

f = open("input.txt", "r")
for line in f:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(max(adapters) + 3)
p(adapters)

p("*****")

diffs = []
for a in range(1, len(adapters)):
    diffs.append(adapters[a] - adapters[a-1])

ones = diffs.count(1)
threes = diffs.count(3)

p(ones, threes)
p(ones * threes)
