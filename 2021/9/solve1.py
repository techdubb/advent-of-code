# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_map(map):
    for row in map:
        print(row)

def find_low_points(map):
    low_points = []

    rows = len(map)
    cols = len(zip(*map))

    for i, r in enumerate(map):
        for j, c in enumerate(r):
            low_point = True
            if i != 0:
                low_point = c < map[i-1][j]
            if j != 0 and low_point:
                low_point = c < map[i][j-1]
            if i != rows - 1 and low_point:
                low_point = c < map[i+1][j]
            if j != cols - 1 and low_point:
                low_point = c < map[i][j+1]

            if low_point:
                low_points.append(int(c))

    return low_points

floor_map = []
for line in f:
    input = line.strip()
    floor_map.append(list(input))

low_points = find_low_points(floor_map)

print(sum([p + 1 for p in low_points]))
