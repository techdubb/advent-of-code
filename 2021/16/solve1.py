from ast import literal_eval

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

class LiteralPacket:
    def __init__(self, ver, tid, bin_str):
        self.version = ver
        self.type_id = tid
        self.bin_string = bin_str

    def __str__(self):
        return 'LiteralPacket | ' + str(self.version) + ' | ' + str(self.type_id)

    def __repr__(self):
        return 'LiteralPacket | ' + str(self.version) + ' | ' + str(self.type_id)

class OperatorPacket:
    def __init__(self, ver, tid, bin_str, p):
        self.version = ver
        self.type_id = tid
        self.bin_string = bin_str
        self.inner_packet = p

    def __str__(self):
        return 'OperatorPacket | ' + str(self.version) + ' | ' + str(self.type_id)

    def __repr__(self):
        return 'OperatorPacket | ' + str(self.version) + ' | ' + str(self.type_id)


def parse_literal(bin_input):
    output = ''
    chunks = [bin_input[i:i+5] for i in range(0, len(bin_input), 5)]
    for c in chunks:
        output += c[1:]
        if c[0] == '0':
            break;

    return output

def parse_packet(bin_input):
    v = int(bin_input[0:3],2)
    tid = int(bin_input[3:6],2)

    result = ''
    if tid == 4:
        result = LiteralPacket(v, tid, parse_literal(bin_input[6:]))
    else:
        ltid = bin_input[6]
        if ltid == '0':
            length = int(bin_input[7:22],2)
            parsed_bits = 0
            packets = []
            while parsed_bits < length:
                idx = 22 + parsed_bits
                p = parse_packet(bin_input[idx:])
                packets.append(p)
                if p.type_id == 4:
                    bit_groups = len(p.bin_string)/4
                    parsed_bits += (6 + (bit_groups*5))
                else:
                    parsed_bits += len(p.bin_string)

            result = OperatorPacket(v, tid, bin_input[0:(22+parsed_bits)], packets)
        elif ltid == '1':
            num_sp = int(bin_input[7:18],2)
            parsed_bits = 0
            packets = []
            for n in range(num_sp):
                idx = 18 + parsed_bits
                p = parse_packet(bin_input[idx:])
                packets.append(p)
                if p.type_id == 4:
                    bit_groups = len(p.bin_string)/4
                    parsed_bits += (6 + (bit_groups*5))
                else:
                    parsed_bits += len(p.bin_string)

            result = OperatorPacket(v, tid, bin_input[0:(18+parsed_bits)], packets)

    return result

def get_version_total(packet, total):
    total += packet.version

    if packet.type_id == 4:
        return total

    if len(packet.inner_packet) == 0:
        return total

    for p in packet.inner_packet:
        t = get_version_total(p, 0)
        total += t

    return total

def parse_2_bin(input):
    d = literal_eval('0x'+input)
    str_len = 4 * len(input)
    return format(d, '0'+str(str_len)+'b')

input = [line.strip() for line in f]
p = parse_packet(parse_2_bin(input[0]))

print(get_version_total(p, 0))
