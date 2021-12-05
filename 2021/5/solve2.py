import math

sign = lambda a: (a>0) - (a<0) #thanks internet!

# f = open("input_test.txt", "r")
f = open("input.txt", "r")
# max_dim = 10
max_dim = 1000

def print_ocean_floor(area):
    for row in zip(*area):
        print(row)

def parse_input(input):
    parsed = input.split(' -> ')
    parsed = [tuple(map(int, i.split(','))) for i in parsed]

    return parsed

def mark_path(input, ocean_floor):
    parsed = parse_input(input)
    (x1, y1) = parsed[0]
    (x2, y2) = parsed[1]

    xm = min(x1, x2)
    xd = int(math.fabs(x1 - x2))
    ym = min(y1, y2)
    yd = int(math.fabs(y1 - y2))

    if x1 == x2:
        for i in range(ym, ym+yd+1):
            ocean_floor[x1][i] += 1
    elif y1 == y2:
        for i in range(xm, xm+xd+1):
            ocean_floor[i][y1] += 1
    elif xd == yd:
        xcoords = []
        xrang = range(xm, xm+xd+1)
        if sign((x1 - x2)) == -1:
            xrang.reverse()
        for i in xrang:
            xcoords.append(i)

        ycoords = []
        yrange = range(ym, ym+yd+1)
        if sign((y1 - y2)) == -1:
            yrange.reverse()
        for i in yrange:
            ycoords.append(i)
        
        for i in zip(xcoords, ycoords):
            ocean_floor[i[0]][i[1]] += 1


    return ocean_floor

ocean_floor = []
ocean_floor = [[0 for i in range(max_dim)] for i in range(max_dim)]

for line in f:
    ocean_floor = mark_path(line.strip(), ocean_floor)

flattened_floor = [val for sublist in ocean_floor for val in sublist]
print(len([i for i in flattened_floor if i >= 2]))