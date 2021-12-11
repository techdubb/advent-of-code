from collections import deque

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_map(map):
    for row in map:
        print(row)
    print('*'*20)

def do_step(om):
    for i, x in enumerate(om):
        for j, y in enumerate(x):
            om[i][j] += 1

    return om

def do_flashes(om):
    flashes = 0
    new_flashes = True
    rows = len(om)
    cols = len(zip(*om))

    while new_flashes:
        new_flashes = False
        for i, x in enumerate(om):
            for j, y in enumerate(x):
                if om[i][j] > 9:
                    new_flashes = True
                    flashes += 1
                    om[i][j] = 0
                    if i != 0 and om[i-1][j] != 0:
                        om[i-1][j] += 1
                    if j != 0 and om[i][j-1] != 0:
                        om[i][j-1] += 1
                    if i != rows - 1 and om[i+1][j] != 0:
                        om[i+1][j] += 1
                    if j != cols - 1 and om[i][j+1] != 0:
                        om[i][j+1] += 1
                    if i != 0 and j != 0 and om[i-1][j-1] != 0:
                        om[i-1][j-1] += 1
                    if i != rows - 1 and j != cols - 1 and om[i+1][j+1] != 0:
                        om[i+1][j+1] += 1
                    if i != 0 and j != cols - 1 and om[i-1][j+1] != 0:
                        om[i-1][j+1] += 1
                    if i != rows - 1 and j != 0 and  om[i+1][j-1] != 0:
                        om[i+1][j-1] += 1

    return (flashes, om)

octopus_map = [map(int, list(line.strip())) for line in f]
print('OG MAP:')
print_map(octopus_map)

flashes = []
for x in range(0, 500):
    print('AFTER ROUND:', x+1)
    octopus_map = do_step(octopus_map)
    (f, octopus_map) = do_flashes(octopus_map)
    print_map(octopus_map)
    if f == 100:
        print('ALL FLASHED ON STEP:', x+1)
        break;

