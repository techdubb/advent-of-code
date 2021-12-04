p = print
preamble_size = 25

def get_first_not_sum():
    checking = preamble_size

    while checking < len(number_stream):
        if find_sum(checking):
            checking += 1
        else:
            return number_stream[checking]

    return None

def find_sum(idx):
    num = number_stream[idx]
    # p('*****')
    # p('checking', num)

    for i in range(idx - preamble_size, idx):
        for j in range(idx - preamble_size, idx):
            if i == j:
                break
            elif number_stream[i] + number_stream[j] == num:
                # p(number_stream[i], number_stream[j])
                return True

    return False


number_stream = []

f = open("input.txt", "r")
for line in f:
    number_stream.append(int(line))

# p(number_stream)

p("*****")
first_num = get_first_not_sum()

p(first_num)
