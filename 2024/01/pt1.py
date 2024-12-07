def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = (line.strip()).split()
            i.append(ln)

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

transposed = list(map(list, zip(*input)))
sort = [sorted(i) for i in transposed]
zipped = zip(sort[0], sort[1])

distances = [abs(int(i[0])-int(i[1])) for i in list(zipped)]

print(sum(distances))