import copy

def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = (line.strip()).split()
            i.append([int(i) for i in ln])

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"


input = parse_textfile(file_name)

def is_safe(diffs):
    if all(num < 0 for num in diffs) and all(num >= -3 for num in diffs):
        return True
    if all(num > 0 for num in diffs) and all(num <= 3 for num in diffs):
        return True

    return False 


safe = []
for i in input:
    d = [a - b for a, b in zip(i, i[1:])]
    if is_safe(d):
        safe.append(d)
    else:
        all_singles = []

        chm3 = list(filter(lambda x: x < -3, d))
        if 1 == len(chm3):
            if d.index(chm3[0]) == 0 or d.index(chm3[0]) == (len(d)-1):
                all_singles += chm3

        chp3 = list(filter(lambda x: x > 3, d))
        if 1 == len(chp3):
            if d.index(chp3[0]) == 0 or d.index(chp3[0]) == (len(d)-1):
                all_singles += chp3

        chn = list(filter(lambda x: x < 0, d))
        if 1 == len(chn):
            all_singles += chn

        chp = list(filter(lambda x: x > 0, d))
        if 1 == len(chp):
            all_singles += chp

        chz = list(filter(lambda x: x == 0, d))
        if 1 == len(chz):
            all_singles += chz

        for a in all_singles:
            idx = d.index(a)
            i1 = copy.deepcopy(i)
            i2 = copy.deepcopy(i)
            i1.pop(idx)
            i2.pop(idx+1)
            d1 = [a - b for a, b in zip(i1, i1[1:])]
            d2 = [a - b for a, b in zip(i2, i2[1:])]
            if is_safe(d1) or is_safe(d2):
                safe.append(d)
                break


print(len(safe))