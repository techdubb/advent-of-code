groups = []
group_count = 0

def get_group_data(line):
    global group_count

    if line == '\n':
        group_count += 1
        return
        
    if len(groups) < group_count + 1:
        groups.append([])

    groups[group_count].append(list(line.strip()))


f = open("input.txt", "r")
for line in f:
    get_group_data(line)

total_yes = 0

print("*****")
for g in groups:
    new_set = set()
    for p in g:
        new_set |= set(p)
    total_yes += len(new_set)

print(total_yes)