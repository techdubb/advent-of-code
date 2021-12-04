# f = open("input_test.txt", "r")
f = open("input.txt", "r")
depths = []

for line in f:
    depths.append(int(line.strip()))

increases = 0

for i in range(1, len(depths)):
    if depths[i] - depths[i-1] > 0:
        increases += 1

print(increases)