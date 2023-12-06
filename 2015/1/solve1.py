# f = open("input_test.txt", "r")
f = open("input.txt", "r")
ins = list(f.read())

floor = 0

for i in ins:
    if i == '(':
        floor += 1
    else:
        floor -= 1

print(floor)