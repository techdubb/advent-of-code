large_cloth = []
non_overlapping = []
cloth_size = 1000

for i in range (0, cloth_size):    
	row = []
	for i in range (0, cloth_size):
		row.append('.') 

	large_cloth.append(row)

def print_cloth():
	for row in large_cloth:
		print row

def count_overlaps():
	overlaps = 0
	for idx_x in range(0, cloth_size):
		for idx_y in range(0, cloth_size):
			if large_cloth[idx_y][idx_x] == 'X':
				overlaps += 1

	return overlaps

def parse_claim(claim):
	(claim_num, info) = claim.split('@')
	(coords, dim) = info.strip().split(':')
	(x, y) = coords.strip().split(',')
	(w, h) = dim.strip().split('x')

	return (claim_num.strip(), (int(x),int(y)), (int(w),int(h)))

def update_cloth(claim):
	does_not_touch = True

	(cn, (x,y), (w,h)) = parse_claim(claim)

	for idx_x in range(x, x+w):
		for idx_y in range(y, y+h):
			if large_cloth[idx_y][idx_x] != '.':
				does_not_touch = False
				if large_cloth[idx_y][idx_x] != 'X':
					if large_cloth[idx_y][idx_x] in non_overlapping:
						non_overlapping.remove(large_cloth[idx_y][idx_x])

				large_cloth[idx_y][idx_x] = 'X'
			if large_cloth[idx_y][idx_x] == '.':
				large_cloth[idx_y][idx_x] = cn

	if does_not_touch:
		non_overlapping.append(cn)

f = open("input3.txt", "r")
for line in f:
	update_cloth(line.strip())	

print "*****"
print count_overlaps()
# print print_cloth()
print non_overlapping