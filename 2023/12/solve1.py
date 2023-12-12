import itertools

f = open("input_test.txt", "r")
# f = open("input_test1.2.txt", "r")
# f = open("input.txt", "r")


def get_combinations(chars, length):
     yield from itertools.product(*([chars] * length)) 

def is_valid_record(record, check):
    sums = []
    for part in record.split('.'):
        if part:
            sums.append(len(part))

    return check == sums

def get_options(record):
    combos = []
    for s in record.split('.'):
        for ss in s.split('#'):
            if ss:
                combos.append([*get_combinations('.#', len(ss))])

    print(combos)
    print(8*'*')

while True:
    print('hi nadine')
    print('i love the christmas tree')

springs = []
for line in f:
    springs.append(line.strip().split(' '))

# for record in springs:
record = springs[0]
opts = get_options(record[0])
    # check = [int(x) for x in record[1].split(',')]
    # print(is_valid_record(record[0], check))
