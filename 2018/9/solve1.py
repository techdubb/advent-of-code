def parse_input(input):
    split_input = input.split(' ')
    return split_input[0], split_input[6]

def get_current_player(current_player, total_players):
    player = current_player % int(total_players)
    if player == 0:
        return total_players
    else:
        return player



# input = '13 players; last marble is worth 7999 points'
input = '471 players; last marble is worth 72026 points'
# input = '9 players; last marble is worth 25 points'
# input = '471 players; last marble is worth 7202600 points'

total_players, total_marbles = parse_input(input)

current_marble = 1
current_index = 1
current_player = 1
the_circle = [0, 1]
scores = dict()

while current_marble < int(total_marbles):
    current_marble += 1
    current_player += 1
    player = get_current_player(current_player, total_players)

    if (current_marble % 23) == 0:
        current_index -= 7
        if current_index < 0:
            current_index = current_index + len(the_circle)
        popped_marble = the_circle.pop(current_index)
        scores[player] = scores.get(player, 0) + current_marble + popped_marble
    else:
        current_index += 2
        
        if current_index > len(the_circle):
            current_index = current_index - len(the_circle)
        the_circle.insert(current_index, current_marble)

print "*****"

print 'High Score!'
print max(scores.values())