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

def get_all_parental(bag_color):
    global bag_rules
    parental_list = set()
    to_check = {bag_color}

    while len(to_check) > 0:
        checking = to_check.pop()
        for bag in bag_rules:
            if checking in bag_rules[bag].keys():
                to_check.add(bag)
                parental_list.add(bag)

        # p(parental_list)
        # p(to_check)

    return list(parental_list)

f = open("input.txt", "r")
for line in f:
    get_bag_rules(line)


# p(bag_rules)
p("*****")
parents = get_all_parental('shiny gold')

p(len(parents))
