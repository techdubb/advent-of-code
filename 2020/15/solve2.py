from itertools import product

p = print

memory = {}

def decimalToBinary(decimal):
    return bin(decimal).replace("0b", "")

def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return decimal

def get_addresses(floating_address):

    x_count = floating_address.count('X')
    indices = [i for i, x in enumerate(floating_address) if x == 'X']
    addresses = []

    for perm in product([1, 0], repeat = x_count):
        new_address = floating_address.copy()
        for idx, v in enumerate(perm):
            new_address[indices[idx]] = str(v)

        new_address_str = ''.join(new_address)
        new_val = binaryToDecimal(int(new_address_str))
        addresses.append(new_val)

    return addresses


def save_value(mask, input):
    global memory

    input_parts = line.split('=')
    val = input_parts[1].strip()

    mem = input_parts[0].strip().split('[')
    address = mem[1].replace(']', '')

    binary = decimalToBinary(int(address))
    binary = binary.zfill(36)

    new_binary = []

    for i in range(0, len(binary)):
        if mask[i] == '0':
            new_binary.append(binary[i])
        else:
            new_binary.append(mask[i])

    new_binary_str = ''.join(new_binary)
    new_addresses = get_addresses(new_binary)

    for a in new_addresses:
        memory[str(a)] = int(val)

    return True

current_mask = 0

f = open("input.txt", "r")
for line in f:
    if 'mask' in line:
        line_parts = line.split('=')
        current_mask = line_parts[1].strip()
    else:
        save_value(current_mask, line)

p(memory)
p(sum(memory.values()))