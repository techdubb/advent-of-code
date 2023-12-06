# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def get_ways(time,dist):
    ways = []

    for x in range(0, time+1):
        time_left = time - x
        if dist < (x * time_left):
            ways.append(x)

    return ways


input = []
for line in f:
    input.append(line.strip())

time = input[0].split(':')[1]
dist = input[1].split(':')[1]

t_data = [i for i in time.split(' ') if i]
d_data = [i for i in dist.split(' ') if i]

t = int(''.join(t_data))
d = int(''.join(d_data))
print(t, d)

w = get_ways(t, d)
print(len(w))
