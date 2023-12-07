from functools import cmp_to_key

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

labels = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
types = ['HC', '1P', '2P', '3K', 'FH', '4K', '5K']

def get_type(h):
    mult_occ = {}
    res = types[0]
    for char in labels:
        count = h.count(char)
        if count > 1:
            mult_occ[char] = count

    if 5 in mult_occ.values():
        res = types[6]
    elif 4 in mult_occ.values():
        res = types[5]
    elif 3 in mult_occ.values() and 2 in mult_occ.values():
        res = types[4]
    elif 3 in mult_occ.values():
        res = types[3]
    elif 2 in mult_occ.values():
        pair_cnt = list(mult_occ.values()).count(2)
        if pair_cnt == 2:
            res = types[2]
        elif pair_cnt == 1:
            res = types[1]

    return res

def compare(hand1, hand2):
    ht1 = types.index(hand_type[hand1])
    ht2 = types.index(hand_type[hand2])

    if ht1 == ht2:
        for idx, c in enumerate(hand1):
            if labels.index(c) < labels.index(hand2[idx]):
                return -1
            elif labels.index(c) > labels.index(hand2[idx]):
                return 1
    if ht1 < ht2:
        return -1
    else:
        return 1

hand_bet = {}
hand_type = {}
for line in f:
    (hand, bet) = line.split(' ')

    hand_bet[hand] = bet.strip()
    hand_type[hand] = get_type(hand)

print(8*'*')
print(hand_bet)
print(hand_type)

compare_key = cmp_to_key(compare)
hands = list(hand_type.keys())
hands = sorted(hands, key=compare_key)
print(hands)

bets_math = []
for idx, h in enumerate(hands):
    bets_math.append((int(hand_bet[h])*(idx+1)))

print(sum(bets_math))