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

similarities = [(transposed[1].count(i) * int(i)) for i in transposed[0]]

print(sum(similarities))

