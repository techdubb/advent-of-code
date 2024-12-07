def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = (line.strip())#.split()
            i.append(ln)

    return i

# file_name = "ex1.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

products = []
for inp in input:
    matches = [i for i in range(len(inp)) if inp.startswith('mul(', i)]

    chunks = []
    for m in matches:
        chunks.append(inp[m+4:m+12])

    for c in chunks:
        parts = c.split(',')

        if len(parts) > 1:
            if ')' in parts[1]:
                pp = parts[1].split(')')

                if parts[0].isdigit() and pp[0].isdigit():
                    products.append(int(parts[0]) * int(pp[0]))

print(products)
print(sum(products))