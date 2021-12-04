
def print_sky(sky):
    for row in map(list, zip(*sky)):
        print row

def draw_map(sky_size, min_points, points):
    print sky_size
    (sky_x, sky_y) = sky_size
    (min_x, min_y) = min_points
    sky = []
    for i in range (0, sky_x-abs(min_x)+1):
        row = ['.' for i in range(0, sky_y-abs(min_y)+1)] 
        sky.append(row)

    print "DONE INIT!"
    print "*"*20

    for point in points:
        ((x,y), (vx, vy)) = point
        sky[x-abs(min_x)][y-abs(min_y)] = '#'

    print_sky(sky)

def get_min_points(points):
    min_x = 10000000
    min_y = 10000000
    for p in points:
        ((x,y), (vx, vy)) = p
        if int(x) < min_x:
            min_x = int(x)
        if int(y) < min_y:
            min_y = int(y)

    return (min_x, min_y)

def get_sky_dims(points):
    max_x = -1
    max_y = -1
    for p in points:
        ((x,y), (vx, vy)) = p
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)

    return (max_x, max_y)

def update_points(min_points, points):
    updated_points = list()
    (min_x, min_y) = min_points

    for point in points:
        ((pos_x, pos_y), (vel_x, vel_y)) = point
        upx = int(pos_x) + abs(min_x)
        upy = int(pos_y) + abs(min_y)

        updated_points.append(((upx, upy), (vel_x, vel_y)))

    return updated_points

def fast_forward(points, seconds):
    min_y = 10000000
    min_points = list()
    for sec in range(0, seconds):
        print min_y
        updated_points = list()
        for point in points:
            ((pos_x, pos_y), (vel_x, vel_y)) = point
            upx = int(pos_x) + (int(vel_x) * sec)
            upy = int(pos_y) + (int(vel_y) * sec)

            updated_points.append(((upx, upy), (vel_x, vel_y)))

        sky_x, sky_y = get_sky_dims(updated_points)
        if sky_y < min_y:
            min_y = sky_y
            min_points = updated_points

    return min_points


def parse_line(line):
    split_line = line.split('=')
    pos = split_line[1].split('velocity')[0].strip()
    vel = split_line[2].strip()
    pos_x, pos_y = pos.replace('<', '').replace('>', '').replace(' ', '').split(',')
    vel_x, vel_y = vel.replace('<', '').replace('>', '').replace(' ', '').split(',')

    return ((pos_x, pos_y), (vel_x, vel_y))

f = open("input10.txt", "r")

points = list()
# seconds = 10
seconds = 10400

for line in f:
    points.append(parse_line(line.strip()))

print "*****"
min_x, min_y = get_min_points(points)
print min_x, min_y

# print points
# print min_x, min_y

points = update_points((min_x, min_y), points)

points = fast_forward(points, seconds)

sky_x, sky_y = get_sky_dims(points)
draw_map((sky_x, sky_y), (min_x, min_y), points)
