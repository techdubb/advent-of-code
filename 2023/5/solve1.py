# f = open("input_test.txt", "r")
f = open("input.txt", "r")

seeds = []
maps = []
input = ''
for line in f:
    input += line

sections = input.split("\n\n")

seeds = sections[0].split(' ')[1:]
seeds = [int(x) for x in seeds]
locals = []

for seed in seeds:
    val = seed
    for i in range(1, len(sections)):
    # for i in range(1, 2):
        lines = sections[i].split("\n")
        for m in lines[1:]:
            n = m.split(' ')
            n = [int(x) for x in n]
            # [dest, source, len]
            if n[1] <= val and n[1]+n[2] >= val:
                val = val + (n[0]-n[1])
                break

        # print(val)

    locals.append(val)


print(min(locals))