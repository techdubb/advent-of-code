# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_universe(u):
    for row in u:
        for col in row:
            print(col, end='')
        print()

def expand_universe(u):
    new_rows = []
    for row in u:
        new_rows.append(row)
        if row.count('#') == 0:
            new_rows.append(row)

    transpose = list(map(list, zip(*new_rows)))

    new_universe = []
    for row in transpose:
        new_universe.append(row)
        if row.count('#') == 0:
            new_universe.append(row)

    return list(map(list, zip(*new_universe))) 

def get_coords(u):
    coords = []
    for r, row in enumerate(u):
        for c, col in enumerate(row):
            if col == '#':
                coords.append((r,c))

    return coords

def step_distance(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

def get_pairs(indices):
    return [(a, b) for idx, a in enumerate(indices) for b in indices[idx + 1:]]

universe = []
for line in f:
    universe.append(list(line.strip()))

# print_universe(universe)
expanded_u = expand_universe(universe)

print(8*'*')
# print_universe(expanded_u)

c = get_coords(expanded_u)
pairs = get_pairs(range(0, len(c)))

dists = []
for p in pairs:
    dists.append(step_distance(c[p[0]], c[p[1]]))

print(sum(dists))
