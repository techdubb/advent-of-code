# f = open("input_test.txt", "r")
f = open("input.txt", "r")
ins = list(f.read())

floor = 0

for idx, i in enumerate(ins):
    if i == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(idx+1)
        break;