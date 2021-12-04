p = print

def parse_rules(input):
    rules = {}

    for r in input:
        parts = r.split(':')
        name = parts[0]
        values = parts[1].strip().split('or')

        value_ints = []
        for v in values:
            nums = v.strip().split('-')
            value_ints += list(range(int(nums[0]), int(nums[1])+1))

        rules[name] = value_ints

    return rules

def check_invalid_tickets(input, rules):
    invalid_values = []

    for t in input[1:]:
        vals = t.split(',')
        for v in vals:
            is_found = []
            for r in rules:
                if int(v) not in rules[r]:
                    # p('value', v, 'not found in', rules[r])
                    is_found.append(False)
                else:
                    is_found.append(True)

            if is_found.count(True) == 0:
                invalid_values.append(int(v))

    return invalid_values

input = [[], [], []]
idx = 0

f = open("input.txt", "r")
for line in f:
    sline = line.strip()
    if sline == '':
        idx += 1
        continue

    input[idx].append(sline)

# p(input)

rules = parse_rules(input[0])
# p(rules)

invalid = check_invalid_tickets(input[2], rules)

p(sum(invalid))