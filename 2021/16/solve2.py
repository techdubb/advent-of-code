# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def count_chars(pairs, final_char):
    char_count = {}

    for p in pairs:
        if p[0] in char_count:
            char_count[p[0]] += pairs[p]
        else:
            char_count[p[0]] = pairs[p]

    char_count[final_char] += 1
    return char_count

def do_step(pairs, rules):
    new_pairs = {}
    for p in pairs:
        parts = [p[0]+rules[p], rules[p]+p[1]]
        for pa in parts:
            if pa in new_pairs:
                new_pairs[pa] += pairs[p]
            else:
                new_pairs[pa] = pairs[p]

    return new_pairs

def parse_rules(rules):
    parsed = {}
    for r in rules:
        pair, l = r.split(' -> ')
        parsed[pair] = l

    return parsed

input = [line.strip() for line in f]

template = input[0]
rules = parse_rules(input[2:])

pairs_list = [''.join(pair) for pair in zip(template[:-1], template[1:])]
pairs = {}
for p in pairs_list:
    if p in pairs:
        pairs[p] += 1
    else:
        pairs[p] = 1

steps = 40
for s in range(steps):
    pairs = do_step(pairs, rules)

count = count_chars(pairs, template[-1])
print(max(count.values()) - min(count.values()))