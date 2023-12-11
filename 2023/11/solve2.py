# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_universe(u):
    for row in u:
        for col in row:
            print(col, end='')
        print()

def expand_universe(u, coords):
    row_sans_g = []
    for r, row in enumerate(u):
        if row.count('#') == 0:
            row_sans_g.append(r)

    transpose = list(map(list, zip(*u)))

    col_sans_g = []
    for r, row in enumerate(transpose):
        if row.count('#') == 0:
            col_sans_g.append(r)

    print(row_sans_g)
    print(col_sans_g)

    exp_v = 999999

    for idx, c in enumerate(coords):
        roff = 0
        for row in row_sans_g:
            if row < c[0]:
                roff += exp_v

        coff = 0
        for col in col_sans_g:
            if col < c[1]:
                coff += exp_v

        coords[idx] = (c[0] + roff, c[1] + coff)

    return coords

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

c = get_coords(universe)
# print_universe(universe)
ec = expand_universe(universe, c)

pairs = get_pairs(range(0, len(ec)))

dists = []
for p in pairs:
    dists.append(step_distance(ec[p[0]], ec[p[1]]))

# print(dists)
print(sum(dists))

