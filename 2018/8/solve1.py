class Node(object):
    def __init__(self, data):
        self.num_children, self.num_metadata = data
        self.children = []
        self.metadata = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_metadata(self, obj):
        self.metadata.extend(obj)

    def p(self):
        print self.num_children
        print self.num_metadata
        print self.metadata
        print '*'*8
        for c in self.children:
            c.p()
        print '*'*8

    def check1(self):
        self.sum = sum(self.metadata)
        for c in self.children:
            self.sum += c.check1()

        return self.sum

    def check2(self):
        self.sum = 0
        if self.num_children == 0:
            self.sum += sum(self.metadata)
        else:
            for i in self.metadata:
                idx = i - 1
                if idx < len(self.children):
                    self.sum += self.children[idx].check2()
                else:
                    self.sum += 0

        return self.sum

def get_node(nodes):
    node = Node((nodes[0], nodes[1]))
    nodes = nodes[2:]
    for i in range(node.num_children):
        child, nodes = get_node(nodes)
        node.add_child(child)

    if node.num_metadata > 0:
        node.add_metadata(nodes[:node.num_metadata])
        nodes = nodes[node.num_metadata:]

    return node, nodes

with open("input8.txt", "r") as content_file:
# with open("test_input.txt", "r") as content_file:
    content = content_file.read().strip()

    nodes = content.split(' ')
    nodes = map(int, nodes)

    root, n = get_node(nodes)

    print "*****"
    # root.p()

    print root.check2()

# solution = build_solution(steps)
# print ''.join(solution)
