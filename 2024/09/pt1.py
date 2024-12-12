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
    if idx % 2 == 0:
        for i in range(int(c)):
            blocks.append(memory)
        memory += 1
    else:
        for i in range(int(c)):
            blocks.append('.')

def get_next(bl):
    free = 0
    notfree = 0
    for idx, b in enumerate(bl): 
        if b == '.':
            free = idx
            break

    for b in range(len(bl)-1, 0, -1): 
        if bl[b] != '.':
            notfree = b 
            break

    return (free, notfree)

while True:

    (free, notfree) = get_next(blocks)

    if free > notfree:
        break;

    blocks[free], blocks[notfree] = blocks[notfree], blocks[free]

checksum = 0
for idx, b in enumerate(blocks):
    if b == '.':
        break

    checksum += (b * idx)


print(checksum)
