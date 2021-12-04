# f = open("input_test.txt", "r")
f = open("input.txt", "r")
coords = [0,0] # h,d

def apply_cmds(coords, raw_cmd):
    split_cmd = raw_cmd.split()
    direction = split_cmd[0]
    unit = int(split_cmd[1])
    n_coords = coords

    if direction == 'forward':
        n_coords = (n_coords[0] + unit, n_coords[1])
    elif direction == 'up':
        n_coords = (n_coords[0], n_coords[1] - unit)
    elif direction == 'down':
        n_coords = (n_coords[0], n_coords[1] + unit)
    else:
        raise Exception("Unknown Direction")

    return n_coords


for line in f:
    coords = apply_cmds(coords, line.strip())

print(coords[0] * coords[1])