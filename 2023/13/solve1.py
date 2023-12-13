# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def find_fold(m):
    for i in range(1, len(m)):
        above = m[:i]
        below = m[i:]

        above.reverse()
        min_len = min([len(above), len(below)])

        if above[:min_len] == below[:min_len]:
            return i

maps = []
m = []
for line in f:
    if line.strip():
        m.append(list(line.strip()))
    else:
        maps.append(m)
        m = []
maps.append(m)

total = 0
for m in maps:
    # search for horizonal fold
    fold = find_fold(m)
    if fold:
        total += (fold * 100)
    else:
        # search for vertical fold
        t = list(map(list, zip(*m)))
        fold = find_fold(t)

        if fold:
            total += fold

print(total)
