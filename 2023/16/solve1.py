# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def track_path():
    beams = [(0, 0, '>')]
    energized = []

    while True:
        for idx, b in enumerate(beams):
            (y, x, d) = b
            if y >= len(grid) or x >= len(grid) or x < 0 or y < 0:
                beams.pop(idx)
                continue
            elif (y,x,d) in energized:
                beams.pop(idx)
                continue

            energized.append((y,x,d))
            if grid[y][x] == '.':
                # print('on a dot!')
                if d == '>':
                    beams[idx] = (y, x+1, d)
                elif d == '<':
                    beams[idx] = (y, x-1, d)
                elif d == 'v':
                    beams[idx] = (y+1, x, d)
                elif d == '^':
                    beams[idx] = (y-1, x, d)
            elif grid[y][x] == '/':
                # print('on a frontslash!')
                if d == '>':
                    beams[idx] = (y-1, x, '^')
                elif d == '<':
                    beams[idx] = (y+1, x, 'v')
                elif d == 'v':
                    beams[idx] = (y, x-1, '<')
                elif d == '^':
                    beams[idx] = (y, x+1, '>')
            elif grid[y][x] == '\\':
                # print('on a backslash!')
                if d == '>':
                    beams[idx] = (y+1, x, 'v')
                elif d == '<':
                    beams[idx] = (y-1, x, '^')
                elif d == 'v':
                    beams[idx] = (y, x+1, '>')
                elif d == '^':
                    beams[idx] = (y, x-1, '<')
            elif grid[y][x] == '-':
                # print('on a dash!')
                if d == '>':
                    beams[idx] = (y, x+1, d)
                elif d == '<':
                    beams[idx] = (y, x-1, d)
                elif d == 'v':
                    beams[idx] = (y, x+1, '>')
                    beams.append((y, x-1, '<'))
                elif d == '^':
                    beams[idx] = (y, x+1, '>')
                    beams.append((y, x-1, '<'))
            elif grid[y][x] == '|':
                # print('on a pipe!')
                if d == '>':
                    beams[idx] = (y+1, x, 'v')
                    beams.append((y-1, x, '^'))
                elif d == '<':
                    beams[idx] = (y+1, x, 'v')
                    beams.append((y-1, x, '^'))
                elif d == 'v':
                    beams[idx] = (y+1, x, d)
                elif d == '^':
                    beams[idx] = (y-1, x, d)

        if len(beams) == 0:
            break

    return energized

def print_energized(tiles):
    g = []

    for i in range(0, len(grid)):
        g.append([])
        for j in range(0, len(grid)):
            g[i].append('.')

    for t in tiles:
        (y,x,d) = t
        g[y][x] = '#'

    for r in g:
        print(''.join(r))


grid = []
for line in f:
    grid.append(list(line.strip()))

energized_tiles = track_path()
energized_coords = [(x[0], x[1]) for x in energized_tiles]

print(len(set(energized_coords)))