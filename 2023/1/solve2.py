# f = open("input_test2.txt", "r")
f = open("input.txt", "r")
numbers = []

num_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convert_numstrings(string):
	new_str = string
	occs = {}
	
	for idx, num in enumerate(num_strings):
		if num in string:
			print(num)
			print(idx+1)
			occurances = [i for i in range(len(string)) if string.startswith(num, i)]
			print(occurances)
			for occ in occurances:
				occs[occ] = str(idx+1)

	print(8*"*")
	print(occs)

	k = list(occs.keys())
	k.sort()
	print(k)

	inserts = 0
	for key in k:
		occ = key
		val = occs[key]
		new_str = new_str[:(occ+inserts)] + val + new_str[(occ+inserts):]
		inserts += 1
	
	print(new_str)
	return new_str

for idx, line in enumerate(f):
    print(line)
    numbers.append([])
    line = convert_numstrings(line)
    for c in line:
    	if c.isnumeric():
    		numbers[idx].append(c)
    		
print(numbers)

final_nums = []
for x in numbers:
	
	n = x[0] + x[-1]
	final_nums.append(int(n))

print(final_nums)

print(sum(final_nums))
