def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            i.append(list(ln))

    return i

# file_name = "ex2.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

y_max = len(input)
x_max = len(input[0])

def find_letter(c, letter):
    letter_candidates = []
    for p in c:
        y,x,d,cs = p

        cleft = (x-1) >= 0
        cright = (x+1) < x_max
        cup = (y-1) >= 0
        cdown = (y+1) < y_max
 
        #check up left
        if cup and cleft and 'ul' in d:
            if input[y-1][x-1] == letter:
                letter_candidates.append((y-1,x-1,'ul',cs+[(y-1,x-1)]))

        #check up right 
        if cup and cright and 'ur' in d:
            if input[y-1][x+1] == letter:
                letter_candidates.append((y-1,x+1,'ur',cs+[(y-1,x+1)]))

        #check down right 
        if cdown and cright and 'dr' in d:
            if input[y+1][x+1] == letter:
                letter_candidates.append((y+1,x+1,'dr',cs+[(y+1,x+1)]))

        #check down left 
        if cdown and cleft and 'dl' in d:
            if input[y+1][x-1] == letter:
                letter_candidates.append((y+1,x-1,'dl',cs+[(y+1,x-1)]))

    return letter_candidates

candidates = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 'M':
            candidates.append((y,x,'updnltrtulurdrdl',[(y,x)]))

A_candidates = find_letter(candidates, 'A')

S_candidates = find_letter(A_candidates, 'S')

coords = []
for s in S_candidates:
    coords.append(s[3][1])

scoords = sorted(coords, key=lambda x: (x[0], x[1]))

pairs = []
for idx,c in enumerate(scoords):

    if (idx+1) < len(scoords):
        if scoords[idx+1]==c:
            pairs.append(c)
            
print(pairs)
print(len(pairs))