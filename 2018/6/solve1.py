import string

large_map = []
map_size = 500
# map_size = 10

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


def add_distances_to_map(coords, distances):
	for idx_x in range(0, map_size):
		for idx_y in range(0, map_size):
			min_dist = 10000000
			for coord in coords:
				dist = distances[coord][(idx_x, idx_y)]
				if dist < min_dist:
					large_map[idx_x][idx_y] = coord.lower()
					min_dist = dist
				elif dist == min_dist:
					large_map[idx_x][idx_y] = '.'

def count_spots(coords):
	total_spots = dict()
	for coord in coords:
		for row in large_map:
			total_spots[coord.lower()] = total_spots.get(coord.lower(), 0) + row.count(coord.lower())

	return total_spots

def find_finite_coords(coords):
	infinite_coords = set()

	for idx_x in range(0, map_size):
		infinite_coords.add(large_map[idx_x][0])
		infinite_coords.add(large_map[idx_x][map_size - 1])

	for idx_y in range(0, map_size):
		infinite_coords.add(large_map[0][idx_y])
		infinite_coords.add(large_map[map_size - 1][idx_y])

	if '.' in infinite_coords:
		infinite_coords.remove('.')


	coords_set = set()
	for coord in coords:
		coords_set.add(coord.lower())

	return list(coords_set.difference(infinite_coords))

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
distances = calc_distances(coord_list)
add_distances_to_map(coord_list, distances)

spot_count = count_spots(coord_list)
finite_coords = find_finite_coords(coord_list)

max_spots = 0
for coord in finite_coords:
	if spot_count[coord] > max_spots:
		max_spots = spot_count[coord]

print max_spots

# print_map()
