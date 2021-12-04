import re

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def update_plant_count(pots, leftmost_pot):
    count = 0

    for idx, c in enumerate(pots):
        if c == '#':
            count += (idx + leftmost_pot)

    return count

def add_buffer(pots, leftmost_pot):
    front_buffer = ''
    end_buffer = ''
    new_leftmost = leftmost_pot

    for i in range(0, 4):
        if pots[i] == '#':
            front_buffer = '.'*(5 - i)
            new_leftmost -= (5 - i)
            break

    for i in range(1, 5):
        if pots[(i * -1)] == '#':
            end_buffer = '.'*(6 - i)
            break

    return (front_buffer + pots + end_buffer, new_leftmost)

def do_generation(notes, pots):
    next_gen_grow = []
    next_gen_no = []

    for note in notes:
        pattern, result = note
        if result == '#':
            next_gen_grow += findall(pattern, pots)
        elif result == '.':
            next_gen_no += findall(pattern, pots)


    row = ['.' for i in range(0, len(pots))]

    for idx in next_gen_grow:
        row[idx + 2] = '#'

    return ''.join(row)

def parse_note(line):
    split_line = line.split(' => ')
    return split_line[0], split_line[1]

# init = '#..#.#..##......###...###'
# f = open('test_input.txt', 'r')
init = '##.######...#.##.#...#...##.####..###.#.##.#.##...##..#...##.#..##....##...........#.#.#..###.#'
f = open('input12.txt', 'r')
notes = []
# generations = 20
generations = 50000000000
plant_count = 0
leftmost_pot = 0

for line in f:
    notes.append(parse_note(line.strip()))

print "*****"

# print '0: ' + init
pots, leftmost_pot = add_buffer(init, leftmost_pot)
for i in range(0, generations):
    pots = do_generation(notes, pots)
    pots, leftmost_pot = add_buffer(pots, leftmost_pot)
    # print leftmost_pot
    # print str(i + 1) + ': ' + pots

print update_plant_count(pots, leftmost_pot)
