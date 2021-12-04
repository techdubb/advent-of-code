import copy

p = print

def print_seat_area(area):
    for row in area:
        p(row)

def do_seating_round(area):
    new_area = copy.deepcopy(area)
    area_w = len(area[0])
    area_h = len(area)

    max_dist = max(area_h, area_w)

    the_pounds = 0
    change_count = 0

    for idx_i, i in enumerate(area): #rows
        for idx_j, j in enumerate(i): #cols
            # print(area[idx_i][idx_j])
            if area[idx_i][idx_j] == '.':
                continue #no need to check for the floor

            seats_full = []

            for x in range(1, area_h):
                up = (idx_i - x, idx_j)
                if up[0] >= 0 and area[up[0]][up[1]] != '.':
                    seats_full.append(area[up[0]][up[1]] == '#')
                    break

            for x in range(1, area_h):
                down = (idx_i + x, idx_j)
                if down[0] < area_h and area[down[0]][down[1]] != '.':
                    seats_full.append(area[down[0]][down[1]] == '#')
                    break

            for x in range(1, area_w):
                left = (idx_i, idx_j - x)
                if left[1] >= 0 and area[left[0]][left[1]] != '.':
                    seats_full.append(area[left[0]][left[1]] == '#')
                    break

            for x in range(1, area_w):
                right = (idx_i, idx_j + x)
                if right[1] < area_w and area[right[0]][right[1]] != '.':
                    seats_full.append(area[right[0]][right[1]] == '#')
                    break

            for x in range(1, max_dist):
                up_left = (idx_i - x, idx_j - x)
                if up_left[0] >= 0 and up_left[1] >= 0 and area[up_left[0]][up_left[1]] != '.':
                    seats_full.append(area[up_left[0]][up_left[1]] == '#')
                    break

            for x in range(1, max_dist):
                up_right = (idx_i - x, idx_j + x)
                if up_right[0] >= 0 and up_right[1] < area_w and area[up_right[0]][up_right[1]] != '.':
                    seats_full.append(area[up_right[0]][up_right[1]] == '#')
                    break

            for x in range(1, max_dist):
                down_left = (idx_i + x, idx_j - x)
                if down_left[0] < area_h and down_left[1] >= 0 and area[down_left[0]][down_left[1]] != '.':
                    seats_full.append(area[down_left[0]][down_left[1]] == '#')
                    break

            for x in range(1, max_dist):
                down_right = (idx_i + x, idx_j + x)
                if down_right[0] < area_h and down_right[1] < area_w and area[down_right[0]][down_right[1]] != '.':
                    seats_full.append(area[down_right[0]][down_right[1]] == '#')
                    break

            # p(seats_full)
            if seats_full.count(True) == 0 and area[idx_i][idx_j] != '#':
                # p("currently", new_area[idx_i][idx_j], "changing to #")
                new_area[idx_i][idx_j] = '#'
                change_count += 1
                the_pounds += 1
            elif seats_full.count(True) >= 5 and area[idx_i][idx_j] != 'L':
                # p("currently", new_area[idx_i][idx_j], "changing to L")
                new_area[idx_i][idx_j] = 'L'
                change_count += 1
            else:
                if new_area[idx_i][idx_j] == '#':
                    the_pounds += 1
                # p("no change", seats_full.count(True))

    return (new_area, change_count, the_pounds)

seat_area = []

f = open("input.txt", "r")
for line in f:
    seats = list(line.strip())
    seat_area.append(seats)

print_seat_area(seat_area)

changes = 1
new = seat_area
while changes != 0:
    p('*'*10)
    (new, change_count, the_pounds) = do_seating_round(new)
    changes = change_count
    p(changes)
    p(the_pounds)
    # print_seat_area(new)

