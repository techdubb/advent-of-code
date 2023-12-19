import numpy as np

f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def do_digging(instr, start):
    (r,c) = start
    site[r][c] = '#'

    for i in instr:
        (dir, cnt, color) = i

        if dir == 'R':
            print('going right')
            for i in range(0, cnt):
                c += 1
                site[r][c] = '#'
        elif dir == 'L':
            print('going left')
            for i in range(0, cnt):
                c -= 1
                site[r][c] = '#'
        elif dir == 'D':
            print('going down')
            for i in range(0, cnt):
                r += 1
                site[r][c] = '#'
        elif dir == 'U':
            print('going up')
            for i in range(0, cnt):
                r -= 1
                site[r][c] = '#'

def get_coords(instr, start):
    (r,c) = start
    coords = [start]

    for i in instr:
        (dir, cnt, color) = i

        if dir == 'R':
            c += cnt
        elif dir == 'L':
            c -= cnt
        elif dir == 'D':
            r += cnt
        elif dir == 'U':
            r -= cnt

        coords.append((r,c))

    return coords

def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    print(x)
    y = x_y[:,1]
    print(y)

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

instr = []
w = h = 0
for line in f:
    l = line.strip()
    (dir, cnt, color) = l.split(' ')
    cnt = int(cnt)
    instr.append((dir, cnt, color))

    if dir == 'R':
        w += cnt
    elif dir == 'D':
        h += cnt

site_dim = max(w, h)
site = []
for r in range(0, site_dim):
    site.append([])
    for c in range(0, site_dim):
        site[r].append('.')

coords = get_coords(instr, (1,1))
coords.reverse()
# print(coords)
print(shoelace(coords))

# # print(inst)
# do_digging(instr, (0,0))

# for s in site:
#     print(''.join(s))