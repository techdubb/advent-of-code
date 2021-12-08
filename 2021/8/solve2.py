f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def get_digit_map(sig_pattern):
    segment_pos_per_digit = ['1110111',
                            '0010010',
                            '1011101',
                            '1011011',
                            '0111010',
                            '1101011',
                            '1101111',
                            '1010010',
                            '1111111',
                            '1111011']
    segments_per_digit = [x.count('1') for x in segment_pos_per_digit]
    pos = [[] for _ in range(7)]

    unique_dgts = [1,7,4,8]
    digit_map = {}
    letters_used = set()
    segments_done = set()
    for x in unique_dgts:
        segments_of_x = [i for i, dgt in enumerate(segment_pos_per_digit[x]) if dgt == '1']
        do_segments = set(segments_of_x) - segments_done
        for s in do_segments:
            for p in sig_pattern:
                if len(p) == segments_per_digit[x]:
                    digit_map[x] = ''.join(sorted(p))
                    possible_letters = set(p) - set(letters_used)
                    pos[s].append(list(possible_letters))
                    
        segments_done = segments_done.union(do_segments)
        letters_used = letters_used.union(possible_letters)

    strings_per_digit = {}
    for idx, x in enumerate(segment_pos_per_digit):
        if idx in digit_map.keys():
            continue;
        segments_of_x = [i for i, dgt in enumerate(segment_pos_per_digit[idx]) if dgt == '1']
        possible_chars = []
        for s in segments_of_x:
            possible_chars.append(pos[s])

        built_strings = possible_chars[0][0]
        for p in range(1, len(possible_chars)):
            new_b_s = []
            for c in possible_chars[p][0]:
                for b in built_strings:
                    new_b_s.append(b+c)

            built_strings = new_b_s

        sorted_bs = [''.join(sorted(x)) for x in built_strings]

        strings_per_digit[idx] = sorted_bs

    for s in sig_pattern:
        sorted_pattern = ''.join(sorted(s))
        for k in strings_per_digit:
            if sorted_pattern in strings_per_digit[k]:
                digit_map[k] = sorted_pattern

    return digit_map

output_digits = []
for line in f:
    input = line.strip()
    (sig_pattern, digital_output) = input.split(' | ')
    sig_pattern = sig_pattern.split(' ')
    digital_output = digital_output.split(' ')

    digit_map = get_digit_map(sig_pattern)

    output = []
    for o in digital_output:
        sorted_o = ''.join(sorted(o))
        output.append(digit_map.keys()[digit_map.values().index(sorted_o)])

    strings = [str(i) for i in output]
    strings = "".join(strings)
    output_digits.append(int(strings))

print(output_digits)
print(sum(output_digits))


