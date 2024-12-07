def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip()
            i.append(list(ln))

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

y_max = len(input)
x_max = len(input[0])

def find_letter(c, letter):
    letter_candidates = []
    for p in c:
        y,x,d = p

        cleft = (x-1) >= 0
        cright = (x+1) < x_max
        cup = (y-1) >= 0
        cdown = (y+1) < y_max

        #check up
        if cup and 'up' in d:
            if input[y-1][x] == letter:
                letter_candidates.append((y-1,x,'up'))

        #check down
        if cdown and 'dn' in d:
            if input[y+1][x] == letter:
                letter_candidates.append((y+1,x,'dn'))

        #check left
        if cleft and 'lt' in d:
            if input[y][x-1] == letter:
                letter_candidates.append((y,x-1,'lt'))

        #check right
        if cright and 'rt' in d:
            if input[y][x+1] == letter:
                letter_candidates.append((y,x+1,'rt'))
 
        #check up left
        if cup and cleft and 'ul' in d:
            if input[y-1][x-1] == letter:
                letter_candidates.append((y-1,x-1,'ul'))

        #check up right 
        if cup and cright and 'ur' in d:
            if input[y-1][x+1] == letter:
                letter_candidates.append((y-1,x+1,'ur'))

        #check down right 
        if cdown and cright and 'dr' in d:
            if input[y+1][x+1] == letter:
                letter_candidates.append((y+1,x+1,'dr'))

        #check down left 
        if cdown and cleft and 'dl' in d:
            if input[y+1][x-1] == letter:
                letter_candidates.append((y+1,x-1,'dl'))

    return letter_candidates

candidates = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 'X':
            candidates.append((y,x,'updnltrtulurdrdl'))

M_candidates = find_letter(candidates, 'M')

A_candidates = find_letter(M_candidates, 'A')

S_candidates = find_letter(A_candidates, 'S')
print(len(S_candidates))
