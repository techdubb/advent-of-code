p = print

import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + round(math.cos(angle)) * (px - ox) - round(math.sin(angle)) * (py - oy)
    qy = oy + round(math.sin(angle)) * (px - ox) + round(math.cos(angle)) * (py - oy)

    return int(qx), int(qy)

instructions = []

f = open("input.txt", "r")
for line in f:
    sline = list(line.strip())
    action = sline[0]
    value = int("".join(sline[1:]))
    instructions.append((action, value))

boat_loc_x = (0)
boat_loc_y = (0)

waypoint_loc_x = (10)
waypoint_loc_y = (1)

for i in instructions:
    if i[0] == 'N':
        waypoint_loc_y += i[1]
    elif i[0] == 'E':
        waypoint_loc_x += i[1]
    elif i[0] == 'W':
        waypoint_loc_x -= i[1]
    elif i[0] == 'S':
        waypoint_loc_y -= i[1]
    elif i[0] == 'R':
        (x, y) = rotate((0,0), (waypoint_loc_x, waypoint_loc_y), math.radians(-1 * i[1]))
        waypoint_loc_x = x
        waypoint_loc_y = y
    elif i[0] == 'L':
        (x, y) = rotate((0,0), (waypoint_loc_x, waypoint_loc_y), math.radians(i[1]))
        waypoint_loc_x = x
        waypoint_loc_x = x
        waypoint_loc_y = y
    elif i[0] =='F':
        units_x = waypoint_loc_x * i[1]
        units_y = waypoint_loc_y * i[1]

        boat_loc_x += units_x
        boat_loc_y += units_y

p(abs(boat_loc_x) + abs(boat_loc_y))
