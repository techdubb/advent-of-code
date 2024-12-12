import itertools

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

y_max = len(input)
x_max = len(input[0])

antenna = {}
for idx, y in enumerate(input):
    for jdx, x in enumerate(y):
        if x == '.':
            continue

        if x in antenna:
            antenna[x].append((idx,jdx))
        else:
            antenna[x] = [(idx,jdx)]

antinodes = []
for k in antenna.keys():
    comb = itertools.combinations(antenna[k],2)

    antinodes += antenna[k]

    for c in comb:
        (y1,x1), (y2,x2) = c

        ydiff = y2-y1
        xdiff = x2-x1

        ny1 = y1-ydiff
        nx1 = x1-xdiff

        while nx1 < x_max and nx1 >=0 and ny1 < y_max and ny1 >= 0:
            antinodes.append((ny1, nx1))

            ny1 = ny1-ydiff
            nx1 = nx1-xdiff

        ny2 = y2+ydiff
        nx2 = x2+xdiff

        while nx2 < x_max and nx2 >=0 and ny2 < y_max and ny2 >= 0:
            antinodes.append((ny2, nx2))

            ny2 = ny2+ydiff
            nx2 = nx2+xdiff

print(len(set(antinodes)))