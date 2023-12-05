# f = open("input_test.txt", "r")
f = open("input.txt", "r")

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node | ' + str(self.val)

    def __repr__(self):
        return 'Node | ' + str(self.val)


def make_node(m, s, e):
    # print('*'*8)
    # print('map', m)
    # print('start', s)
    # print('end', e)

    new_node = Node(m[s[0]][s[1]])
    if s == e:
        return new_node

    # if s[0]+1 > e[0]:
        # print('HELLLLLLO!@!!!')
    if s[0]+1 <= e[0]:
        s_l = (s[0]+1, s[1])
        new_node.left = make_node(m, s_l, e)
    if s[1]+1 <= e[1]:
        s_r = (s[0], s[1]+1)
        new_node.right = make_node(m, s_r, e)

    return new_node

input = [map(int, list(line.strip())) for line in f]

root = make_node(input, (0,0), (len(input[0])-1, len(input)-1))

print(root)
# print(min(paths)-input[0][0])

