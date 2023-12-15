# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def aoc_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256

    return val

sequence = ''
for line in f:
    sequence = line.strip()

parts = sequence.split(',')
hashes = []

for p in parts:
    hashes.append(aoc_hash(p))

print(sum(hashes))
