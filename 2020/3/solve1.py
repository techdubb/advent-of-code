tree_map = []
slope = (3,1)

def print_map():
    for row in tree_map:
        print(row)

def update_map(line, x):
    tree_map.append(list(line) * x)

def travel():
    tree_count = 0
    pos = (0,0)

    new_pos = (pos[0] + slope[0], pos[1] + slope[1])
    pos = new_pos
    while pos[1] < len(tree_map):
        # print(pos)
        if tree_map[new_pos[1]][new_pos[0]] == '#':
            # tree_map[new_pos[1]][new_pos[0]] = 'X'
            tree_count += 1

        # print_map()
        # print(tree_count)
        new_pos = (pos[0] + slope[0], pos[1] + slope[1])
        pos = new_pos

    return tree_count

f = open("input.txt", "r")
for line in f:
    update_map(line.strip(), 3)

# print_map()

print("*****")

# print(len(tree_map))
# print(len(tree_map[0]))
print(travel())
