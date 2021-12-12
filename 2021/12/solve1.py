# f = open("input_test3.txt", "r")
f = open("input.txt", "r")

def find_paths(g, s, e, lc_used=[], path=[]):
    path = path + [s]

    if s == e:
        return [path]
    if not g.has_key(s):
        return []
    if not s.isupper() and s not in ('start', 'end'):
        lc_used = lc_used + [s]

    paths = []
    for n in g[s]:
        if n not in lc_used:
            new_paths = find_paths(g, n, e, lc_used, path)
            for np in new_paths:
                paths.append(np)

    return paths

cave_map = {}
for line in f:
    (n1, n2) = line.split('-')
    n2 = n2.strip()
    if n2 == 'start':
        if n2 in cave_map:
            cave_map[n2].append(n1)
        else:
            cave_map[n2] = [n1]
    elif n1 == 'end':
        if n2 in cave_map:
            cave_map[n2].append(n1)
        else:
            cave_map[n2] = [n1]
    else:
        if n1 in cave_map:
            cave_map[n1].append(n2)
        else:
            cave_map[n1] = [n2]

        if n1 not in ('start', 'end') and n2 not in ('start', 'end'):
            if n2 in cave_map:
                cave_map[n2].append(n1)
            else:
                cave_map[n2] = [n1]

print(cave_map)
print('*'*8)
paths = find_paths(cave_map, 'start', 'end')
unique_paths = set(tuple(row) for row in paths)

# for p in unique_paths:
#     print(p)
print(len(unique_paths))
