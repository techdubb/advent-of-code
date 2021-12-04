import re

passports = []
idx = 0

def parse_line(line):
    global idx
    if (line == '\n'):
        # print('NEW LINE')
        idx += 1
    else:
        if len(passports) == idx:
            passports.append([])
        passports[idx].append(line.strip())

def check_field_keys(passport):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    present = []

    elements = passport.split(" ")
    for e in elements:
        (k,v) = e.split(":")
        if k != 'cid':
            present.append(k)

    return sorted(req) == sorted(present)

def check_field_values(passport):
    pp_dict = {}

    elements = passport.split(" ")
    for e in elements:
        (k,v) = e.split(":")
        pp_dict[k] = v

    # print (pp_dict['pid'])
    # print (len(pp_dict['pid']))
    hcl_match = re.search(r'#[a-fA-F0-9]{6}$', pp_dict['hcl'])
    if hcl_match is None:
        return False
    elif int(pp_dict['byr']) < 1920 or int(pp_dict['byr']) > 2002:
        return False
    elif int(pp_dict['iyr']) < 2010 or int(pp_dict['iyr']) > 2020:
        return False
    elif int(pp_dict['eyr']) < 2020 or int(pp_dict['eyr']) > 2030:
        return False
    elif pp_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    elif pp_dict['hgt'].find('cm') == -1 and pp_dict['hgt'].find('in') == -1:
        return False
    elif len(pp_dict['pid']) != 9:
        return False
    elif not pp_dict['pid'].isdecimal():
        return False
    elif pp_dict['hgt'].find('cm') > -1: # in cm
        hgt_v = int(pp_dict['hgt'].replace('cm', ''))
        if hgt_v < 150 or hgt_v > 193:
            return False
    elif pp_dict['hgt'].find('in') > -1: # in in
        hgt_v = int(pp_dict['hgt'].replace('in', ''))
        if hgt_v < 59 or hgt_v > 76:
            return False

    return True

def validate_passports():
    valid_passports = []
    valid_field_keys = []
    for p in passports:
        if check_field_keys(" ".join(p)):
            valid_field_keys.append(" ".join(p))

    for p in valid_field_keys:
        if check_field_values(p):
            valid_passports.append(p)

    return valid_passports

f = open("input.txt", "r")
for line in f:
    parse_line(line)

# print(passports)
print("*****")

valid_list = validate_passports()

print("*****")
print("*****")
print("*****")

print(len(valid_list))
# for p in valid_list:
#     print(p)
# print(valid_list.count(True))

