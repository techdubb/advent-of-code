p = print

instructions = []

f = open("input.txt", "r")
for line in f:
    sline = list(line.strip())
    action = sline[0]
    value = int("".join(sline[1:]))
    instructions.append((action, value))

directions_r = ['east', 'south', 'west', 'north']
directions_l = ['east', 'north', 'west', 'south']
direction = 'east'

location_x = (0)
location_y = (0)

for i in instructions:
    if i[0] == 'N':
        location_y += i[1]
    elif i[0] == 'E':
        location_x += i[1]
    elif i[0] == 'W':
        location_x -= i[1]
    elif i[0] == 'S':
        location_y -= i[1]
    elif i[0] == 'R':
        dir_idx = directions_r.index(direction)
        clicks = i[1] / 90

        new_idx = (clicks + dir_idx) % len(directions_r)
        direction = directions_r[int(new_idx)]
    elif i[0] == 'L':
        dir_idx = directions_l.index(direction)
        clicks = i[1] / 90

        new_idx = (clicks + dir_idx) % len(directions_l)
        direction = directions_l[int(new_idx)]
    elif i[0] =='F':
        if direction == 'north':
            location_y += i[1]
        elif direction == 'east':
            location_x += i[1]
        elif direction == 'west':
            location_x -= i[1]
        elif direction == 'south':
            location_y -= i[1]

p(abs(location_x) + abs(location_y))
