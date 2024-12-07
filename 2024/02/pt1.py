def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = (line.strip()).split()
            i.append([int(i) for i in ln])

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

safe = []
for i in input:
    r = [a - b for a, b in zip(i, i[1:])]
    if all(num < 0 for num in r) and all(num >= -3 for num in r):
        safe.append(r)
    if all(num > 0 for num in r) and all(num <= 3 for num in r):
        safe.append(r)

print(len(safe))