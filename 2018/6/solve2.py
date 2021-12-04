import string

large_map = []
# map_size = 10
# distance_less_than = 32
map_size = 500
distance_less_than = 10000

for i in range (0, map_size):    
	row = ['.' for i in range(0, map_size)] 
	large_map.append(row)

def print_map():
	for row in map(list, zip(*large_map)):
		print row

def calc_distances(coords):
	distances = dict()
	for coord in coords:
		distances[coord] = dict()
		c_x = int(coords[coord][0].strip())
		c_y = int(coords[coord][1].strip())
		for idx_x in range(0, map_size):
			for idx_y in range(0, map_size):
				distances[coord][(idx_x, idx_y)] =  abs(c_x - idx_x) + abs(c_y - idx_y)

	return distances

def add_region_to_map(coords, distances):
	for idx_x in range(0, map_size):
		for idx_y in range(0, map_size):
			total_dist = 0
			for coord in coords:
				total_dist += distances[coord][(idx_x, idx_y)]

			if total_dist <= distance_less_than:
				large_map[idx_x][idx_y] = '#'

def region_size():
	size = 0
	for idx_x in range(0, map_size):
		for idx_y in range(0, map_size):
			if large_map[idx_x][idx_y] == '#':
				size += 1

	return size

def update_map(coord, coord_id):
	(x, y) = coord.split(',')
	x = int(x.strip())
	y = int(y.strip())

	large_map[x][y] = coord_id

f = open("input6.txt", "r")
ids = list()
for i in range(1, 5):
	for e in list(string.ascii_uppercase):
		ids.append(e*i)

coord_list = dict()

for idx, line in enumerate(f):
	update_map(line.strip(), ids[idx])	
	coord_list[ids[idx]] = line.strip().split(',')	

print "*****"
print coord_list
print "*****"

distances = calc_distances(coord_list)
add_region_to_map(coord_list, distances)

print region_size()

# print_map()
