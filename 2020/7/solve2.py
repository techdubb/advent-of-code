bag_rules = {}
p = print

def get_bag_rules(line):
    global bag_rules

    line_split = line.split('contain')

    parent = line_split[0].replace('bags', '').strip()
    children = line_split[1].replace('.', '').replace('bags', '').replace('bag', '').strip()

    children = children.split(',')
    if children[0] == 'no other':
        children = []

    bag_rules[parent] = {}

    for c in children:
        c_s = c.split(None, 1)
        bag_rules[parent][c_s[1].strip()] = c_s[0]

def get_bag_count(bag_color):
    global bag_rules
    bag_count = 0

    p('we are in', bag_color)
    if len(bag_rules[bag_color]) == 0:
        # p('end case')
        return 1
    else:
        child_val = []
        for bag in bag_rules[bag_color]:
            bc = get_bag_count(bag)
            # p("*****")
            # print(bag_rules[bag_color][bag])
            # print(bc)
            # p("*****")
            child_val.append(int(bag_rules[bag_color][bag]) * bc)

        return sum(child_val) + 1




f = open("input.txt", "r")
for line in f:
    get_bag_rules(line)

p("*****")
bag_count = get_bag_count('shiny gold')

p(bag_count - 1)
