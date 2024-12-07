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
            location = (ydx,xdx)
            direction = input[ydx][xdx]

def print_map():
    for y in input:
        print(''.join(y))

def off_map(l):
    y,x = l

    if y < 0 or x < 0 or y >= y_max or x >= x_max:
        return True

    return False

spots = [location]
on_map = True
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

    

print(len(set(spots)))
