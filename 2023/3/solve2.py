from numpy import prod

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def print_schematic(s):
    for row in s:
        for i in row:
            print(i, end="")
        print()

def find_numbers(s):
    numbers = []
    nums = []
    start_coord = ''
    last_coord = ''
    cur_num = ''

    for y, n in enumerate(s):
        for x, m in enumerate(n):
            if m.isnumeric():
                if start_coord == '':
                    start_coord = (x,y)
                last_coord = (x,y)
                cur_num += m
            elif cur_num != '':
                numbers.append((cur_num, [start_coord, last_coord]))
                cur_num = ''
                start_coord = ''

    return numbers

def find_gears(n):
    max = len(schematic)
    gears = {}
    for k,v in n:
        sx, sy = v[0]
        ex, ey = v[1]

        print(k, v)
        print(sx, ex)
        print(ey)

        # check top
        if ey > 0:
            for x in range(sx, ex+1):
                print (x, ey-1)
                val = schematic[ey-1][x]
                if val == '*':
                    if (x, ey-1) in gears:
                        gears[(x, ey-1)].append(k)
                    else:
                        gears[(x, ey-1)] = [k]

                    continue
        # check bottom
        if ey < (max - 1):
            for x in range(sx, ex+1):
                print (x, ey+1)
                val = schematic[ey+1][x]
                if val == '*':
                    if (x, ey+1) in gears:
                        gears[(x, ey+1)].append(k)
                    else:
                        gears[(x, ey+1)] = [k]

                    continue
        # check left
        if sx > 0:
            print (sx-1, ey)
            val = schematic[ey][sx-1]
            if val == '*':
                if (sx-1, ey) in gears:
                    gears[(sx-1, ey)].append(k)
                else:
                    gears[(sx-1, ey)] = [k]

                continue
        # check right
        if ex < (max - 1):
            print (ex+1, ey)
            val = schematic[ey][ex+1]
            if val == '*':
                if (ex+1, ey) in gears:
                    gears[(ex+1, ey)].append(k)
                else:
                    gears[(ex+1, ey)] = [k]

                continue
        # check top left
        if ey > 0 and sx > 0:
            print (sx-1, ey-1)
            val = schematic[ey-1][sx-1]
            if val == '*':
                if (sx-1, ey-1) in gears:
                    gears[(sx-1, ey-1)].append(k)
                else:
                    gears[(sx-1, ey-1)] = [k]

                continue
        # check top right
        if ey > 0 and ex < (max - 1):
            print (ex+1, ey-1)
            val = schematic[ey-1][ex+1]
            if val == '*':
                if (ex+1, ey-1) in gears:
                    gears[(ex+1, ey-1)].append(k)
                else:
                    gears[(ex+1, ey-1)] = [k]

                continue
        # check bottom left
        if ey < (max - 1) and sx > 0:
            print (sx-1, ey+1)
            val = schematic[ey+1][sx-1]
            if val == '*':
                if (sx-1, ey+1) in gears:
                    gears[(sx-1, ey+1)].append(k)
                else:
                    gears[(sx-1, ey+1)] = [k]

                continue
        # check bottom right
        if ey < (max - 1) and ex < (max - 1):
            print (ex+1, ey+1)
            val = schematic[ey+1][ex+1]
            if val == '*':
                if (ex+1, ey+1) in gears:
                    gears[(ex+1, ey+1)].append(k)
                else:
                    gears[(ex+1, ey+1)] = [k]

                continue

    return gears

schematic = []
for line in f:
    schematic.append(list(line.strip()))

numbers = find_numbers(schematic)
print(numbers)

gears = find_gears(numbers)
print(gears)

sum = 0
for k,v in gears.items():
    if len(v) == 2:
        int_list = [int(i) for i in v]
        sum += prod(int_list)


print(sum)
# print(sum(valid_nums))
# print_schematic(schematic)
