from collections import deque

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def is_corrupt(line):
    mismatches = []
    chars = deque()
    open_char = ('(', '[', '{', '<')
    for c in line:
        if c in open_char:
            chars.append(c)
        else:
            match = chars.pop()
            if (match == '(' and c != ')'):
                mismatches.append(c)
            elif (match == '[' and c != ']'):
                mismatches.append(c)
            elif (match == '{' and c != '}'):
                mismatches.append(c)
            elif (match == '<' and c != '>'):
                mismatches.append(c)

    return len(mismatches) > 0

def get_remaining_char(line):
    chars = deque()
    open_char = ('(', '[', '{', '<')
    for c in line:
        if c in open_char:
            chars.append(c)
        else:
            chars.pop()

    return chars


scoring =   {')': 1, ']': 2, '}': 3, '>': 4}
char_lookup = {'(':')', '[':']', '{':'}', '<':'>'}
scores = []
for line in f:
    score = 0
    input = line.strip()
    if not is_corrupt(input):
        remaining = get_remaining_char(input)
        remaining.reverse()
        for r in remaining:
            score *= 5
            score += scoring[char_lookup[r]]

        scores.append(score)

print(sorted(scores)[(len(scores) - 1)/2])
