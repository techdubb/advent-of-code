# f = open("input_test.txt", "r")
f = open("input.txt", "r")
games = {}

def get_max_pull_by_color(p):
    pulls = p.split(';')
    max_pull = {}

    for pull in pulls:
        by_color = pull.split(',')

        for c in by_color:
            c = c.strip()
            (n, color) = c.split(' ')
            if color in max_pull:
                if max_pull[color] < int(n):
                    max_pull[color] = int(n)
            else:
                max_pull[color] = int(n)

    return max_pull


for idx, line in enumerate(f):
    print(line)
    (game, pulls) = line.split(':')

    game_num = game[5:]

    max_by_color = get_max_pull_by_color(pulls.strip())
    games[int(game[5:])] = max_by_color

# 12 red cubes, 13 green cubes, and 14 blue
constraints = {'red': 12, 'green': 13, 'blue': 14}

print(games)
answer = 0

for game in games:
    possible = True
    for c in constraints:
        if c in games[game]:
            if constraints[c] < games[game][c]:
                possible = False

    if possible:
        answer += game

print(answer)


