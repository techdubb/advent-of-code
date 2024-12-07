def parse_textfile(filename):
    i = []
    with open(filename, 'r') as file:
        for line in file:
            ln = (line.strip())#.split()
            i.append(ln)

    return i

# file_name = "ex2.txt"
file_name = "in1.txt"

input = parse_textfile(file_name)

products = []
multipying = True
for inp in input:
    steps = 0

    matches = [i for i in range(len(inp)) if inp.startswith('mul(', i)]

    do_match = [i for i in range(len(inp)) if inp.startswith('do()', i)]
    dont_match = [i for i in range(len(inp)) if inp.startswith("don't()", i)]

    for steps in range(len(inp)):

        if steps in do_match:
            multipying = True
        elif steps in dont_match:
            multipying = False
        elif steps in matches and multipying:
            c = inp[steps+4:steps+12]

            parts = c.split(',')

            if len(parts) > 1:
                if ')' in parts[1]:
                    pp = parts[1].split(')')

                    if parts[0].isdigit() and pp[0].isdigit():
                        products.append(int(parts[0]) * int(pp[0]))

print(products)
print(sum(products))