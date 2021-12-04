instructions = []
accumulator = 0
p = print

def get_instructions(line):
    global instructions

    line_split = line.strip().split(' ')

    instructions.append([line_split[0], int(line_split[1])])

def execute():
    global accumulator
    stack_size = len(instructions)

    has_execd = []
    idx = 0

    while True:
        if idx in has_execd:
            return 'inf'

        if idx >= stack_size:
            p('execution complete')
            return 'suc'

        i = instructions[idx]
        op = i[0]
        arg = i[1]
        has_execd.append(idx)

        if op == 'nop':
            p('nop')
            idx += 1
        elif op == 'acc':
            p('acc')
            accumulator += arg
            idx += 1
        else:
            p(op)
            idx += arg


f = open("input_test.txt", "r")
for line in f:
    get_instructions(line)

p(execute())

# p(instructions)
p("*****")
p(accumulator)
