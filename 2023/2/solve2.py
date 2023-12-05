import numpy

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

print(games)
answer = 0

for game in games:
    answer += numpy.prod(list(games[game].values()))

print(answer)


