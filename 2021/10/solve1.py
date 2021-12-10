from collections import deque

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def check_corrupt(line):
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

    return mismatches

corrupted_by_char = []
for line in f:
    input = line.strip()
    corrupted_by_char += check_corrupt(input)

scoring =   {')': 3, ']': 57, '}': 1197, '>': 25137}
print(sum([scoring[x] for x in corrupted_by_char]))
