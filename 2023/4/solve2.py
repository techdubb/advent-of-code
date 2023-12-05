import math

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def parse_card(s):
    numbers = s.split(':')[1]
    numbers = numbers.strip()
    (winning, actual) = numbers.split('|')

    w = winning.strip().split(' ')
    while ('' in w): w.remove('')
    a = actual.strip().split(' ')
    while ('' in a): a.remove('')

    return (w, a)

def get_match_count(c):
    (w, a) = c
    matches = 0
    for x in w:
        l = [i for i in a if i==x]
        matches += len(l)

    return matches

cards = []
matches = []
for line in f:
    card = parse_card(line)
    matches.append(get_match_count(card))
    cards.append(1)

print(cards)
print(matches)
print()

for i in range(0, len(cards)):
    # print(matches[i])
    print(i+1)
    print(i+matches[i]+1)
    for x in range(i+1, i+matches[i]+1):
        cards[x] += cards[i]

    print(cards)

print(sum(cards))