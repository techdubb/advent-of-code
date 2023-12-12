import time

# f = open("input_test.txt", "r")
# f = open("input_test1.2.txt", "r")
f = open("input.txt", "r")

def find_loop(g):
    start = ''
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if col == 'S':
                start = (r, c)

    loop = [start]
    ground_max = len(g)
    (row, col) = start

    while loop.count(start) < 2:
        # time.sleep(1)
        # print(loop)
        c = ground[row][col]
        if col > 0 and c in ['S', '-', 'J', '7']: #look left
            n = ground[row][col-1]
            # print('looking left', n)
            if n == 'S' and len(loop) > 2: break
            if ((row, col-1) not in loop) and n in ['-', 'F', 'L']:
                # print('looked left', n)
                col = col-1
                loop.append((row, col))
                continue
        if col < ground_max - 1 and c in['S', '-', 'F', 'L']: #look right
            n = ground[row][col+1]
            # print('looking right', n)
            if n == 'S' and len(loop) > 2: break
            if ((row, col+1) not in loop) and n in ['-', 'J', '7']:
                # print('looked right', n)
                col = col+1
                loop.append((row, col))
                continue
        if row > 0 and c in ['S', '|', 'J', 'L']: #look up
            n = ground[row-1][col]
            # print('looking up', n)
            if n == 'S' and len(loop) > 2: break
            if ((row-1, col) not in loop) and n in ['|', 'F', '7']:
                # print('looked up', n)
                row = row-1
                loop.append((row, col))
                continue
        if row < ground_max - 1 and c in ['S', '|', 'F', '7']: #look down
            n = ground[row+1][col]
            # print('looking down', n)
            if n == 'S' and len(loop) > 2: break
            if ((row+1, col) not in loop) and n in ['|', 'L', 'J']:
                # print('looked down', n)
                row = row+1
                loop.append((row, col))
                continue

    return loop

ground = []
for line in f:
    ground.append((list(line.strip())))

full_loop = find_loop(ground)

print(len(full_loop))
print(len(full_loop)/2)