from ast import literal_eval

f = open("input_test.txt", "r")
# f = open("input.txt", "r")

version_cnt = 0

def parse_literal(bin_input):
    # print('in parse_literal')
    output = ''
    chunks = [bin_input[i:i+5] for i in range(0, len(bin_input), 5)]
    for c in chunks:
        output += c[1:]
        if c[0] == '0':
            break;

    return output

def parse_packet(bin_input):
    # print(bin_input)
    v = int(bin_input[0:3],2)
    print('version',v)
    global version_cnt
    version_cnt += v
    tid = int(bin_input[3:6],2)
    print('tid', tid)

    result = ''
    if tid == 4:
        result = parse_literal(bin_input[6:])
    else:
        ltid = bin_input[6]
        # print('ltid', ltid)
        if ltid == '0':
            # print('BY LENGTH')
            # print('bin length', bin_input[7:22])
            length = int(bin_input[7:22],2)
            # print('dec length', length)
            parsed_bits = 0
            while parsed_bits < length:
                idx = 22 + parsed_bits
                p = parse_packet(bin_input[idx:])
                if p[1] == 4:
                    print('the p literal', p)
                    bit_groups = len(p[2])/4
                    parsed_bits += (6 + (bit_groups*5))
                    # print('parsed_bits', parsed_bits)
                else:
                    # print('the p operator', p)
                    parsed_bits += len(p[2])

            result = bin_input[0:(22+parsed_bits)]
        elif ltid == '1':
            # print('BY NUM')
            num_sp = int(bin_input[7:18],2)
            # print('num_sp', num_sp)
            parsed_bits = 0
            for n in range(num_sp):
                idx = 18 + parsed_bits
                p = parse_packet(bin_input[idx:])
                if p[1] == 4:
                    print('the p literal', p)
                    bit_groups = len(p[2])/4
                    parsed_bits += (6 + (bit_groups*5))
                    # print('parsed_bits', parsed_bits)
                else:
                    # print('the p operator', p)
                    parsed_bits += len(p[2])

            result = bin_input[0:(18+parsed_bits)]

    return (v, tid, result)

def parse_2_bin(input):
    d = literal_eval('0x'+input)
    str_len = 4 * len(input)
    return format(d, '0'+str(str_len)+'b')

input = [line.strip() for line in f]

parse_packet(parse_2_bin(input[0]))

print(version_cnt)
