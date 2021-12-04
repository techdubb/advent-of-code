passports = []
idx = 0

def parse_line(line):
    global idx
    if (line == '\n'):
        print('NEW LINE')
        idx += 1
    else:
        if len(passports) == idx:
            passports.append([])
        passports[idx].append(line.strip())

def is_valid(passport):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    present = []

    elements = passport.split(" ")
    for e in elements:
        (k,v) = e.split(":")
        if k != 'cid':
            present.append(k)

    return sorted(req) == sorted(present)


def validate_passports():
    valid_passports = []
    for p in passports:
        valid_passports.append(is_valid(" ".join(p)))

    return valid_passports

f = open("input.txt", "r")
for line in f:
    parse_line(line)

# print(passports)
print("*****")

valid_list = validate_passports()

print(valid_list.count(True))

# print(len(tree_map))
# print(len(tree_map[0]))
