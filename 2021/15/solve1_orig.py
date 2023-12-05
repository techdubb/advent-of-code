f = open("input_test.txt", "r")
# f = open("input.txt", "r")

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node | ' + str(self.val)

    def __repr__(self):
        return 'Node | ' + str(self.val)


def find_paths(m, s, e, min_v, path=0):
    # print('*'*8)
    # print('map', m)
    # print('start', s)
    # print('end', e)
    path = path + m[s[1]][s[0]]

    if path > min_v:
        return {}

    # print('*'*8)
    # print('path', path)
    # print('*'*8)

    if s == e:
        return {path}

    paths = set()
    if s[0]+1 <= e[0]:
        s_l = (s[0]+1, s[1])
        paths = set.union(paths, find_paths(m, s_l, e, min_v, path))
    if s[1]+1 <= e[1]:
        s_r = (s[0], s[1]+1)
        paths = set.union(paths, find_paths(m, s_r, e, min_v, path))

    return paths

def parse_rules(rules):
    parsed = {}
    for r in rules:
        pair, l = r.split(' -> ')
        parsed[pair] = l

    return parsed

input = [map(int, list(line.strip())) for line in f]

min_a = sum(input[0])
for x in input[1:]:
    min_a += x[-1]

min_b = sum(input[-1])
for x in input[:-1]:
    min_b += x[-1]

paths = find_paths(input, (0,0), (len(input[0])-1, len(input)-1), min(min_a, min_b))

# print(paths)
print(min(paths)-input[0][0])

