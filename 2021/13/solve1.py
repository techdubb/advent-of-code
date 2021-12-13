import math

f = open("input_test.txt", "r")
# f = open("input.txt", "r")
max_dim = 15
# max_dim = 1500

def print_paper(area):
    for row in zip(*area):
        print(''.join(row))

def do_fold(paper, instruction):
    print(instruction)

    return None

def mark_dot(input, paper):
    (x, y) = map(int, input.split(','))
    paper[x][y] = '#'

    return paper

paper = [['.' for i in range(max_dim)] for i in range(max_dim)]
print_paper(paper)
instructions = []
space = False

for line in f:
    print(line)
    if line == '\n':
        print("SPACER")
        space = True

    if not space:
        paper = mark_dot(line.strip(), paper)
    else:
        instructions.append(line.strip())

instructions = instructions[1:]

print_paper(paper)

do_fold(paper, instructions[0])

# flattened_floor = [val for sublist in ocean_floor for val in sublist]
# print(len([i for i in flattened_floor if i >= 2]))