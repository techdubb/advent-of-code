# f = open("input_test.txt", "r")
f = open("input.txt", "r")

seeds = []
maps = []
input = ''
for line in f:
    input += line

def build_map(section):
    print(section)
    map_len = (max([i[3] for i in section]))

    dest = [*range(0, map_len)]
    source = dest.copy()
    # print(dest)

    for s in section:
        for i in range(0, s[2]):
            # print(i)
            dest[s[1]+i] = s[0]+i

    for idx, d in enumerate(dest):
        print(source[idx], d)



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

# print(seeds)
# print(prepped_sections)

# build_map(prepped_sections[0])
build_map(prepped_sections[len(prepped_sections)-1])
# for x in range(len(prepped_sections)-1, -1, -1):
#     ps = prepped_sections[x]
#     build_map(ps)
#     print(ps)