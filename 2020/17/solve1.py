p = print

inital_state = []
f = open("input_test.txt", "r")
for line in f:
    sline = line.strip()
    inital_state.append(list(sline))

p(inital_state)
