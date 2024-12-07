import copy
from collections import Counter

def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            i.append(list(ln))

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

y_max = len(input)
x_max = len(input[0])

location = ''
direction = ''
for ydx, y in enumerate(input):
    for xdx, x in enumerate(y):
        if input[ydx][xdx] in ['<','>','v','^']:
            start_point = (ydx,xdx)
            location = (ydx,xdx)
            start_direction = input[ydx][xdx]
            direction = input[ydx][xdx]

def print_map(m):
    for y in m:
        print(''.join(y))

def off_map(l):
    y,x = l

    if y < 0 or x < 0 or y >= y_max or x >= x_max:
        return True

    return False

spots = [location]
while True:
    y, x = location

    if direction == '<':
        next_spot = (y, x-1)

        if off_map(next_spot):
            break;

        if input[next_spot[0]][next_spot[1]] == '#':
            direction = '^'
        else:
            location = next_spot
            spots.append(location)

    elif direction == '>':
        next_spot = (y, x+1)

        if off_map(next_spot):
            break;

        if input[next_spot[0]][next_spot[1]] == '#':
            direction = 'v'
        else:
            location = next_spot
            spots.append(location)

    elif direction == '^':
        next_spot = (y-1, x)

        if off_map(next_spot):
            break;

        if input[next_spot[0]][next_spot[1]] == '#':
            direction = '>'
        else:
            location = next_spot
            spots.append(location)

    elif direction == 'v':
        next_spot = (y+1, x)

        if off_map(next_spot):
            break;

        if input[next_spot[0]][next_spot[1]] == '#':
            direction = '<'
        else:
            location = next_spot
            spots.append(location)

    

def is_looped(s):
    counts = Counter(s)

    vals = list(counts.values())
    if max(vals) >= 6:
        return True

    return False

new_obstacles = []
spots = [(124, 66)]
for s in set(spots):
    spots2 = [start_point]
    location = start_point
    direction = start_direction
    the_map = copy.deepcopy(input)
    the_map[s[0]][s[1]] = '#'

    while True:
        y, x = location

        if is_looped(spots2):
            new_obstacles.append(s)
            break

        if direction == '<':
            next_spot = (y, x-1)

            if off_map(next_spot):
                break;

            if the_map[next_spot[0]][next_spot[1]] == '#':
                direction = '^'
            else:
                location = next_spot
                spots2.append(location)

        elif direction == '>':
            next_spot = (y, x+1)

            if off_map(next_spot):
                break;

            if the_map[next_spot[0]][next_spot[1]] == '#':
                direction = 'v'
            else:
                location = next_spot
                spots2.append(location)
        elif direction == '^':
            next_spot = (y-1, x)

            if off_map(next_spot):
                break;

            if the_map[next_spot[0]][next_spot[1]] == '#':
                direction = '>'
            else:
                location = next_spot
                spots2.append(location)
        elif direction == 'v':
            next_spot = (y+1, x)

            if off_map(next_spot):
                break;

            if the_map[next_spot[0]][next_spot[1]] == '#':
                direction = '<'
            else:
                location = next_spot
                spots2.append(location)

print(new_obstacles)
print(len(new_obstacles))
