
def print_5by5_grid(grid, top_left):
    tl_x, tl_y = top_left
    for x in range (tl_x-1, tl_x+4):
        for y in range (tl_y-1, tl_y+4):
            print grid[x][y]

def get_hundreth(number):
    if number >= 100:
        return number // 10**2 % 10
    else:
        return 0

def calc_power(x, y, grid_serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = get_hundreth(power_level)
    power_level -= 5

    return power_level

def create_grid(grid_size, grid_serial_number):
    grid = []

    # init grid
    for i in range (0, grid_size):
        row = ['.' for i in range(0, grid_size)]
        grid.append(row)

    for x in range (0, grid_size):
        for y in range (0, grid_size):
            grid[x][y] = calc_power((x + 1), (y + 1), grid_serial_number)

    return grid

def calc_total_power(x, y, grid, size):
    total_power = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            total_power += grid[i][j]

    return total_power

def find_max_square(grid_size, grid, size):
    max_square = 0
    max_square_tl = ''
    for x in range (0, grid_size - (size - 1)):
        for y in range (0, grid_size - (size - 1)):
            total_power = calc_total_power(x, y, grid, size)

            if total_power > max_square:
                max_square = total_power
                max_square_tl = (x+1, y+1)
    
    return max_square_tl, max_square


x, y = 33,45
# grid_serial_number = 42
grid_serial_number = 8979
grid_size = 300

grid = create_grid(grid_size, grid_serial_number)

max_for_size = dict()
for size in range(1, 300):
    print size
    max_square_tl, max_square = find_max_square(grid_size, grid, size)
    print max_square_tl, max_square
    print '*******'
    max_for_size[size] = max_square

print max(max_for_size, key=max_for_size.get)
# print grid[x-1][y-1]

# 14
# (235, 118) 166
