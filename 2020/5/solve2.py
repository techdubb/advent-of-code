import math

seat_map = []
max_row = 127
max_col = 7

for i in range(0, max_row):
    seat_map.append([])
    for j in range (0, max_col):
        seat_map[i].append('.')

def get_seat_score(line):
    line_list = list(line)

    row_data = line_list[:7]
    col_data = line_list[7:10]
    # print(row_data, col_data)

    row = get_row(row_data)
    col = get_col(col_data)

    update_seat_map(row, col)

    return (row * 8) + col

def get_row(data):
    cur_u = max_row
    cur_l = 0

    for d in data:
        diff = cur_u - cur_l
        if d == 'F':
            cur_u -= math.ceil(diff / 2)
        else: #it's B
            cur_l += math.ceil(diff / 2)

    return cur_l

def get_col(data):
    cur_u = max_col
    cur_l = 0

    for d in data:
        diff = cur_u - cur_l
        if d == 'L':
            cur_u -= math.ceil(diff / 2)
        else: #it's R
            cur_l += math.ceil(diff / 2)

    return cur_l
def update_seat_map(r,c):
    seat_map[r-1][c-1] = 'X'

def print_seat_map():
    for row in seat_map:
        print(row)

scores = []

f = open("input.txt", "r")
for line in f:
    scores.append(get_seat_score(line.strip()))

print("*****")
print_seat_map()
scores.sort()
print(scores)

temp_comp_list = list(range(min(scores), max(scores)+1))

print(set(scores).symmetric_difference(set(temp_comp_list)))