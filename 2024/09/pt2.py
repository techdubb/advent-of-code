def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            i.append(ln)

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

blocks = []
memory = 0
for idx,c in enumerate(input[0]):
    b = []
    if idx % 2 == 0:
        for i in range(int(c)):
            b.append(memory)
        blocks.append(b)
        memory += 1
    else:
        for i in range(int(c)):
            b.append('.')
        blocks.append(b)

def get_next_free(b,cf):
    f = cf + 1
    while '.' not in b[f] or len(b[f]) == 0:
        f += 1

    return f

def get_next_notfree(b,cnf):
    nf = cnf - 1

    while '.' in b[nf] or len(b[nf]) == 0:
        nf -= 1

    return nf

free = get_next_free(blocks, -1) 

all_notfree = []
for b in blocks:
    if '.' not in b and len(b) > 0:
        all_notfree.append(b)

all_notfree.reverse()

for nf in all_notfree:

    notfree = blocks.index(nf)
    free = get_next_free(blocks, -1) 

    while free < notfree:
        if len(blocks[free]) >= len(blocks[notfree]):
            for idx, b in enumerate(blocks[notfree]):
                blocks[notfree][idx], blocks[free][idx] = blocks[free][idx], blocks[notfree][idx]

            if len(blocks[free]) > len(blocks[notfree]):
                dot_idx = blocks[free].index('.')
                new_blocks = [blocks[free][:dot_idx], blocks[free][dot_idx:]]

                blocks.pop(free)
                blocks[free:free] = new_blocks

            break;
        else:
            free = get_next_free(blocks, free) 

intblocks = []

for b in blocks:
    if len(b) > 0:
        for x in b:
            if x != '.':
                intblocks.append(int(x))
            else:
                intblocks.append('.')


checksum = 0
for idx, b in enumerate(intblocks):
    if b == '.':
        continue

    checksum += (b * idx)


print(checksum)