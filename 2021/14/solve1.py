# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def count_chars(chain):
    char_count = {}

    for c in chain:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count

def do_step(chain, rules):
    new_chain = []
    pairs = [''.join(pair) for pair in zip(chain[:-1], chain[1:])]

    for p in pairs:
        new_chain.append(p[0]+rules[p])

    return ''.join(new_chain)+chain[-1]

def parse_rules(rules):
    parsed = {}
    for r in rules:
        pair, l = r.split(' -> ')
        parsed[pair] = l

    return parsed

input = [line.strip() for line in f]

template = input[0]
rules = parse_rules(input[2:])

steps = 10
chain = template
for s in range(steps):
    chain = do_step(chain, rules)

count = count_chars(chain)
print(max(count.values()) - min(count.values()))
