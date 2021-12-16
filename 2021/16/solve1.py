from ast import literal_eval

f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def parse_literal(bin_input):
    output = ''
    chunks = [bin_input[i:i+5] for i in range(0, len(bin_input), 5)]
    for c in chunks:
        output += c[1:]
        if c[0] == '0':
            break;

    return output

def parse_packet(bin_input):
    print(bin_input)
    v = int(bin_input[0:3],2)
    print(v)
    tid = int(bin_input[3:6],2)
    print(tid)

    if tid == 4:
        result = parse_literal(bin_input[6:])

    return result

def parse_2_bin(input):
    d = literal_eval('0x'+input)
    str_len = 4 * len(input)
    return format(d, '0'+str(str_len)+'b')

input = [line.strip() for line in f]

print(parse_packet(parse_2_bin(input[0])))
