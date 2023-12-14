import itertools

# f = open("input_test.txt", "r")
# f = open("input_test1.2.txt", "r")
f = open("input.txt", "r")


def get_combinations(chars, length):
     yield from itertools.product(*([chars] * length)) 

def is_valid_record(record, check):
    sums = []
    for part in record.split('.'):
        if part:
            sums.append(len(part))

    return check == sums

def get_options(record):
    errors = record.count('?')
    return get_combinations('.#', errors)

springs = []
for line in f:
    springs.append(line.strip().split(' '))

total = 0
for record in springs:
    opts = get_options(record[0])
    check = [int(x) for x in record[1].split(',')]
    preped_record = record[0].replace('?', "%s")
    for o in opts:
        si = preped_record%tuple(o)
        if is_valid_record(si, check):
            total += 1

print(total)