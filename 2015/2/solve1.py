f = open("input_test.txt", "r")
# f = open("input.txt", "r")
dims = []

for line in f:
    dims.append(line.strip().split('x'))

print(dims)
# increases = 0

# for i in range(1, len(depths)):
#     if depths[i] - depths[i-1] > 0:
#         increases += 1

# print(increases)