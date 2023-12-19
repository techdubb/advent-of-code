f = open("input_test.txt", "r")
# f = open("input.txt", "r")

city = []
for line in f:
    city.append(list(line.strip()))

for r in city:
    print(r)