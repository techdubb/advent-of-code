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
min_local = float('inf')

prepped_sections = []

for i in range(1, len(sections)):
# for i in range(1, 2):
    lines = sections[i].split("\n")
    prepped_sections.append([])
    for m in lines[1:]:
        n = m.split(' ')
        n = [int(x) for x in n]
        n.append(n[1]+n[2])
        n.append(n[0]-n[1])
        prepped_sections[i-1].append(n)

# print(prepped_sections)
section_range = [*range(0, len(prepped_sections))]
# print(section_range)

for i,x in enumerate(seeds):
    if i % 2 == 0:
        print('on seed: ', i)
        for seed in range(x, x+seeds[i+1]):
            val = seed
            for ps in prepped_sections:
            # for i in range(1, 2):
                for n in ps:
                    # [dest, source, len]
                    if n[1] <= val and n[3] >= val:
                        val = val + n[4]
                        break

            if val < min_local:
                min_local = val

print(min_local)