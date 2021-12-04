import math

max_row = 127
max_col = 7

def get_seat_score(line):
    line_list = list(line)

    row_data = line_list[:7]
    col_data = line_list[7:10]
    # print(row_data, col_data)

    row = get_row(row_data)
    col = get_col(col_data)

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

scores = []

f = open("input.txt", "r")
for line in f:
    scores.append(get_seat_score(line.strip()))

print("*****")
print(max(scores))
