# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def do_roll(x, player_pos, player_score):
    player = x % 2
    print('player', player)
    start_value = (x*3)+1
    roll_range = range(start_value, start_value+3)
    print(roll_range)
    roll_total = sum([i % 100 for i in roll_range])
    print('roll', roll_total)

    # if x > 10:
    #     print(x)
    #     print(player_score)
    #     exit()

    pos = player_pos[player] + roll_total
    if pos > 10:
        pos = pos % 10
        if pos == 0:
            pos = 10

    score = player_score[player] + pos

    player_pos[player] = pos
    player_score[player] = score

    print(pos, score)

    print('****'*8)
    return (player_pos, player_score)

player_pos = []
for line in f:
    l = line.strip()
    l_split = l.split(':')
    player_pos.append(int(l_split[1]))

player_score = [0,0]
x = 0
while True:
    # if x > 10:
    #     break
    if any(x >= 1000 for x in player_score) > 0:
        break

    (player_pos, player_score) = do_roll(x, player_pos, player_score)
    x += 1

print(x)
# print(player_pos)
print(min(player_score)*(3*x))