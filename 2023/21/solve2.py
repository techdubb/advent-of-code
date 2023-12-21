# f = open("input_test.txt", "r")
f = open("input.txt", "r")

possible_steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def do_next_steps(stps):
    # print(stps)
    next_steps = set()

    for s in stps:
        (r, c) = s
        for ps in possible_steps:
            (rd, cd) = ps
            nr = r+rd
            nc = c+cd
            if nr >= 0 and nc >= 0 and nr < max_r and nc < max_c:
                if garden_map[nr][nc] in ['.', 'S']:
                    next_steps.add((nr, nc))

    steps.append(next_steps)


garden_map = []

s = (0,0)
for idx, line in enumerate(f):
    has_s = line.find('S')
    if has_s != -1:
        s = (idx, has_s)
    garden_map.append(list(line.strip()))

max_r = len(garden_map)
max_c = len(garden_map[0])
# print(s)
# for gm in garden_map:
#     print(gm)

steps = [[s]]
steps_left = 64
for s in steps:
    if steps_left == 0:
        break
    do_next_steps(s)

    steps_left -= 1

print(len(steps[-1]))