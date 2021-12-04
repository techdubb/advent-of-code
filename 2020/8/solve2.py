instructions = []
accumulator = 0
p = print

def get_instructions(line):
    global instructions

    line_split = line.strip().split(' ')

    instructions.append([line_split[0], int(line_split[1])])

def execute(ins):
    global accumulator
    stack_size = len(ins)

    has_execd = []
    idx = 0

    while True:
        if idx in has_execd:
            return 'inf'

        if idx >= stack_size:
            p('execution complete')
            return 'suc'

        i = ins[idx]
        op = i[0]
        arg = i[1]
        has_execd.append(idx)

        if op == 'nop':
            # p('nop')
            idx += 1
        elif op == 'acc':
            # p('acc')
            accumulator += arg
            idx += 1
        else:
            # p(op)
            idx += arg

def defrag():
    global instructions
    global accumulator
    def_idx = 0
    result = ''

    while result != 'suc':
        new_ins = instructions.copy()
        i = new_ins[def_idx]
        op = i[0]
        arg = i[1]

        if op == 'nop':
            new_ins[def_idx] = ['jmp', arg]
        elif op == 'jmp':
            new_ins[def_idx] = ['nop', arg]

        def_idx += 1
        accumulator = 0
        # p(new_ins)
        result = execute(new_ins)


f = open("input.txt", "r")
for line in f:
    get_instructions(line)


defrag()

# p(instructions)
p("*****")
p(accumulator)
