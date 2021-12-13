# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_paper(area):
    for row in area:
        print(''.join(row))

def do_fold(paper, instruction):
    split_ins = instruction.split(' ')
    ins = split_ins[2]
    (axis, unit) = ins.split('=')
    iunit = int(unit)

    max_x = len(paper[0])
    max_y = len(paper)

    if axis == 'y':
        new_paper = [['.' for j in range(max_x)] for i in range((max_y)/2)]
        top = paper[:iunit]
        bottom = paper[(iunit+1):]
        bottom.reverse()

        dot_count = 0
        for i, x in enumerate(new_paper):
            for j, y in enumerate(x):
                if top[i][j] == '#':
                    new_paper[i][j] = '#'
                    dot_count += 1
                elif bottom[i][j] == '#':
                    new_paper[i][j] = '#'
                    dot_count += 1

    elif axis == 'x':
        paper = zip(*paper)
        left = paper[:iunit]
        right = paper[(iunit+1):]
        right.reverse()

        left = zip(*left)
        right = zip(*right)

        new_paper = [['.' for j in range(max_x/2)] for i in range(max_y)]
        dot_count = 0
        for i, x in enumerate(new_paper):
            for j, y in enumerate(x):
                if left[i][j] == '#':
                    new_paper[i][j] = '#'
                    dot_count += 1
                elif right[i][j] == '#':
                    new_paper[i][j] = '#'
                    dot_count += 1

    return (new_paper, dot_count)

def mark_dot(input, paper):
    (x, y) = map(int, input.split(','))
    paper[y][x] = '#'

    return paper

def get_dims(coords):
    max_x = 0
    max_y = 0
    for c in coords:

        (x, y) = c.split(',')

        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)

    return max_x, max_y

instructions = []
dot_coords = []
space = False

for line in f:
    if line == '\n':
        space = True

    if not space:
        dot_coords.append(line.strip())
    else:
        instructions.append(line.strip())

(max_x, max_y) = get_dims(dot_coords)

paper = [['.' for j in range(max_x+1)] for i in range(max_y+1)]
instructions = instructions[1:]

for c in dot_coords:
    paper = mark_dot(c, paper)

dots = []
(new_paper, dot_count) = do_fold(paper, instructions[0])
dots.append(dot_count)
paper = new_paper

print(dots)
