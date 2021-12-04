large_cloth = []
cloth_size = 1000

for i in range (0, cloth_size):    
	row = []
	for i in range (0, cloth_size):
		row.append(0) 

	large_cloth.append(row)

def print_cloth():
	for row in large_cloth:
		print row

def count_overlaps():
	overlaps = 0
	for idx_x in range(0, cloth_size):
		for idx_y in range(0, cloth_size):
			if large_cloth[idx_y][idx_x] > 1:
				overlaps += 1

	return overlaps

def parse_claim(claim):
	(claim_num, info) = claim.split('@')
	(coords, dim) = info.strip().split(':')
	(x, y) = coords.strip().split(',')
	(w, h) = dim.strip().split('x')

	return ((int(x),int(y)), (int(w),int(h)))

def update_cloth(claim):
	((x,y), (w,h)) = parse_claim(claim)
	# print range(x, x+w)
	# print range(y, y+h)

	for idx_x in range(x, x+w):
		for idx_y in range(y, y+h):
			large_cloth[idx_y][idx_x] += 1

f = open("input3.txt", "r")
for line in f:
	update_cloth(line.strip())	

print "*****"
print count_overlaps()