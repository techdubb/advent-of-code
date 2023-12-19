# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def track_path(start):
    beams = [start]
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

grid = []
for line in f:
    grid.append(list(line.strip()))


energized_lengths = []
for i in range(0, len(grid)):
    print("working all sides from i=", i)

    # check from top
    energized_tiles = track_path((0, i, 'v'))
    energized_coords = [(x[0], x[1]) for x in energized_tiles]
    energized_lengths.append(len(set(energized_coords)))

    # check from bottom
    energized_tiles = track_path((len(grid)-1, i, '^'))
    energized_coords = [(x[0], x[1]) for x in energized_tiles]
    energized_lengths.append(len(set(energized_coords)))

    # check from left
    energized_tiles = track_path((i, 0, '>'))
    energized_coords = [(x[0], x[1]) for x in energized_tiles]
    energized_lengths.append(len(set(energized_coords)))

    # check from right
    energized_tiles = track_path((i, len(grid)-1, '<'))
    energized_coords = [(x[0], x[1]) for x in energized_tiles]
    energized_lengths.append(len(set(energized_coords)))

print(max(energized_lengths))