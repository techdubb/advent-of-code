f = open("input_1_1.txt", "r")
freq = 0

for line in f: 
	freq = freq + int(line)

print freq