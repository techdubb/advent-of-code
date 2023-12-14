# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def tilt_north(p):
    # print(p)

    for col in p:
        was_move = True
        while was_move:
            was_move = False
            for s in range(1, len(col)):
                if col[s] == 'O' and col[s-1] == '.':
                    col[s] = '.'
                    col[s-1] = 'O'
                    was_move = True

    return p


platform = []
for line in f:
    if line.strip():
        platform.append(list(line.strip()))

t_platform = list(map(list, zip(*platform)))
tilted = list(map(list, zip(*tilt_north(t_platform))))

total = 0
for v in range(len(tilted), 0, -1):
    idx = len(tilted) - v
    cnt = tilted[idx].count('O')
    total += cnt * v

print(total)
