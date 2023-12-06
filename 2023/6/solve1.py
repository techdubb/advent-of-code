from functools import reduce

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def get_ways(time,dist):
    print(time, dist)

    ways = []

    for x in range(0, time+1):
        print(x)
        rate = x
        time_left = time - x
        if dist < rate * time_left:
            ways.append(x)

    return ways


input = []
for line in f:
    input.append(line.strip())

time = input[0].split(':')[1]
dist = input[1].split(':')[1]

t_data = [int(i) for i in time.split(' ') if i]
d_data = [int(i) for i in dist.split(' ') if i]

ways = []
for idx, t in enumerate(t_data):
    w = get_ways(t, d_data[idx])

    if len(w) > 0:
        ways.append(w)

print(ways)
way_count = [len(i) for i in ways]

print(reduce((lambda x, y: x * y), way_count))
