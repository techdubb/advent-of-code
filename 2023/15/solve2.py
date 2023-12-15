# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def aoc_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256

    return val

def update_lenses(p):
    (label, val) = ('','')
    op = ''
    if '=' in p:
        op = '='
    elif '-' in p:
        op = '-'

    (label, val) = p.split(op)

    box = aoc_hash(label)

    if op == '=':
        updated = False
        for idx, l in enumerate(boxes[box]):
            if not l.find(label) == -1:
                boxes[box][idx] = label + ' ' + val
                updated = True

        if not updated:
            boxes[box].append(label + ' ' + val)
    elif op == '-':
        for idx, l in enumerate(boxes[box]):
            if not l.find(label) == -1:
                boxes[box].pop(idx)


sequence = ''
for line in f:
    sequence = line.strip()

parts = sequence.split(',')
hashes = []

boxes = {}
for i in range(0,256):
    boxes[i] = []

for p in parts:
    update_lenses(p)

focus_power = 0
for b in boxes:
    if boxes[b]:
        for idx, lens in enumerate(boxes[b]):
            (label, val) = lens.split(' ')
            focus_power += ((b+1) * (idx+1) * int(val))

print(focus_power)