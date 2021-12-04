# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def tally_bits(bin_input):
    columns = []

    for bit in bin_input:
        bit_count = {'0':0, '1':0}
        if bit == '0':
            bit_count['0'] += 1
        elif bit == '1':
            bit_count['1'] += 1
        else:
            raise Exception("Unknown bit")

        columns.append(bit_count)

    return columns

tally = []

for line in f:
    tally.append(tally_bits(line.strip()))

col_tally = []
# get column tally
for x in tally[0]:
    col_tally.append({'0':0, '1':0})

for i in tally:
    for idx, j in enumerate(i):
        col_tally[idx]['0'] += j['0']
        col_tally[idx]['1'] += j['1']

# get gamma
gamma = []
for i in col_tally:
    gamma.append(max(i, key=i.get))


# get epsilon
epsilon = []
for i in col_tally:
    epsilon.append(min(i, key=i.get))

gamma_int = int("".join(gamma), 2)
epsilon_int = int("".join(epsilon), 2)


print (epsilon_int*gamma_int)