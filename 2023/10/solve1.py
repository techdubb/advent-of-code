f = open("input_test.txt", "r")
# f = open("input_test1.2.txt", "r")
# f = open("input.txt", "r")

next_pipe_coord = [(-1,0), (1, 0), (0, -1), (0, 1)]

ground = []
for line in f:
    ground.append((list(line.strip())))


print(ground[0][0])
print(ground[4][4])

