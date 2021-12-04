p = print

adapters = []

f = open("input.txt", "r")
for line in f:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(max(adapters) + 3)
# p(adapters)

p("*****")

diffs = []
for a in range(1, len(adapters)):
    diffs.append(adapters[a] - adapters[a-1])

# p(diffs)

pairs = []
for a in range(1, len(diffs)):
    pairs.append(diffs[a] + diffs[a-1])

# p(pairs)

sub_lists = []
sub_list = []

for i in pairs:
    if i != 2:
        sub_lists.append(sub_list)
        sub_list = []
    else:
        sub_list.append(i)

p(sub_lists)

total = 1
for sl in sub_lists:
    l = len(sl)
    if l == 3:
        total *= 7
    elif l == 2:
        total *= 4
    elif l == 1:
        total *= 2

p(total)

