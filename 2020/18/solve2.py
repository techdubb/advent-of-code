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
    invalid_tickets = []

    for t in input:
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
                invalid_tickets.append(t)

    return invalid_tickets

def determine_fields(input, rules):
    found_list = {}
    for t in input:
        vals = t.split(',')
        for idx, v in enumerate(vals):
            is_found = {}
            if idx not in found_list:
                found_list[idx] = []
            for r in rules:
                if r not in is_found:
                    is_found[r] = []
                if int(v) not in rules[r]:
                    # p('value', v, 'not found in', r)
                    is_found[r].append(False)
                # else:
                    # is_found.append((r,True))

            found_list[idx].append(is_found)


    possible_fields = {}
    for f in found_list:
        if f not in possible_fields:
            possible_fields[f] = []
        rules_bools = {}

        for i in found_list[f]:
            for r in i:
                if r not in rules_bools:
                    rules_bools[r] = True

                if len(i[r]) > 0:
                    rules_bools[r] = False
                else:
                    rules_bools[r] = rules_bools[r] and True

        for r in rules_bools:
            if rules_bools[r]:
                possible_fields[f].append(r)

    return possible_fields

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

other_tickets = input[2][1:]
invalid = check_invalid_tickets(other_tickets, rules)

for i in invalid:
    other_tickets.remove(i)

# p(other_tickets)

possible = determine_fields(other_tickets, rules)

spossible = {k: v for k, v in sorted(possible.items(), key=lambda item: len(item[1]))}

# p(spossible)

mapping = {}

taken = []
for f in spossible:
    if f not in mapping:
        mapping[f] = ""
    for o in spossible[f]:
        if o in taken:
            continue
        else:
            mapping[f] = o
            taken.append(o)

p(mapping)

the_indices = []
for m in mapping:
    if mapping[m].find('departure') != -1:
        the_indices.append(int(m))

p(the_indices)

my_ticket_data = input[1][1:]
my_ticket = my_ticket_data[0].split(',')

the_values = []
for i in the_indices:
    the_values.append(int(my_ticket[i]))

p(the_values)

from functools import reduce
import operator
p(reduce(operator.mul, the_values, 1))
