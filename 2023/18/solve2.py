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

def find_smudge(m):
    for i in range(1, len(m)):
        above = m[:i]
        below = m[i:]

        above.reverse()
        min_len = min([len(above), len(below)])

        cmp_a = above[:min_len]
        cmp_b = below[:min_len]

        err_cnt = 0
        for idx, a in enumerate(cmp_a):
            for jdx, c in enumerate(a):
                if cmp_a[idx][jdx] != cmp_b[idx][jdx]:
                    err_cnt += 1

        if err_cnt == 1:
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
    fold = find_smudge(m)
    if fold:
        total += (fold * 100)
    else:
        # search for vertical fold
        t = list(map(list, zip(*m)))
        fold = find_smudge(t)

        if fold:
            total += fold

print(total)
