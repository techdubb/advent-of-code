# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def do_steps(init, target):
    vx, vy = init
    px, py = (0,0)
    tx, ty = target

    max_y = -99999999
    while (px < tx[0] or py > ty[1]) and py > ty[0]:
        px += vx
        py += vy

        if py > max_y:
            max_y = py

        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1

    success = False
    if px >= tx[0] and px <= tx[1] and py <= ty[1] and py >= ty[0]:
        success = True

    return (success, max_y)

input = [line.strip() for line in f]
(_, _, x, y) = input[0].split(' ')
(_, x_range) = [p.split('..') for p in x.split('=')]
(_, y_range) = [p.split('..') for p in y.split('=')]

x_range = [p.strip(',') for p in x_range]
x_range = map(int, x_range)
y_range = map(int, y_range)

results = []
for x in range(1, 200):
    for y in range(200):
        res = do_steps((x, y), (x_range, y_range))
        if res[0]:
            results.append(res[1])

print(max(results))
