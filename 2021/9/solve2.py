import numpy

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
                low_points.append((i,j))

    return low_points

def get_basin_size(low_point, map):
    basin_points = [low_point]
    rows = len(map)
    cols = len(zip(*map))

    next_points = [low_point]
    while len(next_points) > 0:
        new_next_points = []
        for p in next_points:
            (x,y) = p
            if x != 0:
                if map[x-1][y] != '9' and (x-1, y) not in basin_points:
                    basin_points.append((x-1, y))
                    new_next_points.append((x-1, y))
            if y != 0:
                if map[x][y-1] != '9' and (x, y-1) not in basin_points:
                    basin_points.append((x, y-1))
                    new_next_points.append((x, y-1))
            if x != rows - 1:
                if map[x+1][y] != '9' and (x+1, y) not in basin_points:
                    basin_points.append((x+1, y))
                    new_next_points.append((x+1, y))
            if y != cols - 1:
                if map[x][y+1] != '9' and (x, y+1) not in basin_points:
                    basin_points.append((x, y+1))
                    new_next_points.append((x, y+1))

        next_points = new_next_points

    return len(basin_points)

floor_map = []
for line in f:
    input = line.strip()
    floor_map.append(list(input))

basin_sizes = [get_basin_size(lp, floor_map) for lp in find_low_points(floor_map)]
print(numpy.prod(sorted(basin_sizes, reverse=True)[:3]))
