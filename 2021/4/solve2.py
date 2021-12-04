# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def mark_boards(m_boards, n):

    for idx, i in enumerate(m_boards):
        for jdx, j in enumerate(i):
            if n in j:
                ndx = j.index(n)
                m_boards[idx][jdx][ndx] = 'X'

    return m_boards

def check_for_winner(m_boards):
    retval = []
    # check rows
    for idx, i in enumerate(m_boards):
        for jdx, j in enumerate(i):
            row_count = sum('X' in y for y in j)
            if row_count == 5:
                retval.append(idx)

    # check cols
    for idx, i in enumerate(m_boards):
        i_t = zip(*i)
        for jdx, j in enumerate(i_t):
            row_count = sum('X' in y for y in j)
            if row_count == 5:
                retval.append(idx)

    return retval

def get_sum_from_winner(winner):
    sum = 0
    for i in winner:
        for j in i:
            if j != 'X':
                sum += int(j)
    return sum

input = []

for line in f:
    input.append(line.strip())

numbers_called = input[0].split(',')
boards = []

board_idx = -1
for x in range(1, len(input)):
    if input[x] == '':
        board_idx += 1
        boards.append([])
    else:
        line = input[x].split(' ')
        line = [i for i in line if i]
        boards[board_idx].append(line)

marked_boards = boards
previous_winners = []
for num in numbers_called:
    marked_boards = mark_boards(marked_boards, num)
    winner = check_for_winner(marked_boards)
    if winner != -1:
        if len(set(winner)) >= len(boards):
            last_winner = [x for x in set(winner) if x not in set(previous_winners)]
            sum = get_sum_from_winner(marked_boards[last_winner[0]])
            answer = sum*int(num)
            print(answer)
            break;

        previous_winners = winner
