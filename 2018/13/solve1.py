import string
import operator

def print_track(track):
    for row in track:
        print ''.join(row)

def get_init_carts(track):
    carts = {}
    count = 0
    for idx_x, row in enumerate(track):
        for idx_y, col in enumerate(row):
            if track[idx_x][idx_y] == '<':
                id = string.ascii_uppercase[count]
                carts[id]= ('<', (idx_x, idx_y), 0)
                count += 1
            elif track[idx_x][idx_y] == '>':
                id = string.ascii_uppercase[count]
                carts[id]= ('>', (idx_x, idx_y), 0)
                count += 1
            elif track[idx_x][idx_y] == 'v':
                id = string.ascii_uppercase[count]
                carts[id]= ('v', (idx_x, idx_y), 0)
                count += 1
            elif track[idx_x][idx_y] == '^':
                id = string.ascii_uppercase[count]
                carts[id]= ('^', (idx_x, idx_y), 0)
                count += 1

    return carts

# left the first time, goes straight the second time, turns right the third time
def get_intersection_move(cart_state, cur_turn):
    new_state = ''
    next_turn = cur_turn % 3

    if cart_state == '<':
        if next_turn == 0:
            new_state = 'v'
        elif next_turn == 1:
            new_state = '<'
        elif next_turn == 2:
            new_state = '^'
    elif cart_state == '>':
        if next_turn == 0:
            new_state = '^'
        elif next_turn == 1:
            new_state = '>'
        elif next_turn == 2:
            new_state = 'v'
    elif cart_state == 'v':
        if next_turn == 0:
            new_state = '>'
        elif next_turn == 1:
            new_state = 'v'
        elif next_turn == 2:
            new_state = '<'
    elif cart_state == '^':
        if next_turn == 0:
            new_state = '<'
        elif next_turn == 1:
            new_state = '^'
        elif next_turn == 2:
            new_state = '>'

    return new_state, cur_turn + 1

def move_cart(track, cart, updated_track):
    cart_state, (c_x, c_y), turns = cart
    direction = (0,0)
    replacement = ''

    if track[c_x][c_y] == '<':
        direction = (0, -1)
    elif track[c_x][c_y] == '>':
        direction = (0, 1)
    elif track[c_x][c_y] == 'v':
        direction = (1, 0)
    elif track[c_x][c_y] == '^':
        direction = (-1, 0)

    d_x, d_y = direction
    (new_x, new_y) = (c_x + d_x, c_y + d_y)

    new_coord_state = track[new_x][new_y]
    if new_coord_state == '|':
        updated_track[new_x][new_y] = cart_state
    elif new_coord_state == '-':
        updated_track[new_x][new_y] = cart_state
    elif new_coord_state == '\\':
        if cart_state == '<':
            cart_state = '^'
        elif cart_state == '>':
            cart_state = 'v'
        elif cart_state == 'v':
            cart_state = '>'
        elif cart_state == '^':
            cart_state = '<'
        updated_track[new_x][new_y] = cart_state
    elif new_coord_state == '/':
        if cart_state == '<':
            cart_state = 'v'
        elif cart_state == '>':
            cart_state = '^'
        elif cart_state == 'v':
            cart_state = '<'
        elif cart_state == '^':
            cart_state = '>'
        updated_track[new_x][new_y] = cart_state
    elif new_coord_state == '+':
        new_state, new_turn = get_intersection_move(cart_state, turns)
        cart_state = new_state
        turns = new_turn
        updated_track[new_x][new_y] = cart_state

    return updated_track, (cart_state, (new_x, new_y), turns)

def sorty(cart):
    cart_state, (x, y), turns = cart

    return [x, y]

def sort_carts(carts):
    return sorted(carts, key=lambda cart: sorty(carts[cart]))

def do_click(track, carts):
    new_track = []
    for row in clean_track:
        new_row = []
        for col in row:
            new_row.append(col)
        new_track.append(new_row)

    sorted_carts = sort_carts(carts)
    for cart in sorted_carts:
        new_track, new_cart = move_cart(track, carts[cart], new_track)
        carts[cart] = new_cart
        was_crash(carts)

    return new_track, carts

def get_clean_track(track, carts):
    clean_track = []

    for row in track:
        new_row = []
        for col in row:
            new_row.append(col)
        clean_track.append(new_row)

    for cart in carts:
        state, (c_x, c_y), turns = carts[cart]
        cart_state = track[c_x][c_y]

        if cart_state == '<' or cart_state == '>':
            clean_track[c_x][c_y] = '-'
        elif cart_state == 'v' or cart_state == '^':
            clean_track[c_x][c_y] = '|'

    return clean_track

def was_crash(carts):
    ids = carts.keys()
    for id in ids:
        state, (c_x, c_y), turns = carts[id]
        check_ids = ids[:]
        check_ids.remove(id)
        for id2 in check_ids:
            state, (c_x2, c_y2), turns = carts[id2]

            if c_x == c_x2 and c_y == c_y2:
                print "COLLISION"
                print c_y, c_x
                return True

    return False

f = open("input13.txt", "r")
track = []
has_crashed = False

for line in f:
    track.append(list(line.replace("\n", '')))
# print_track(track)

carts = get_init_carts(track)
clean_track = get_clean_track(track, carts)
click = 0
print "*****"
while True:
# for i in range(0, 6):
    track, carts = do_click(track, carts)
    click += 1
    print "click: " + str(click)
    if was_crash(carts):
        break
    # print_track(track)
    print "*****"
    print "*****"

# solution = build_solution(steps)
# print ''.join(solution)
