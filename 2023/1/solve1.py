#f = open("input_test.txt", "r")
f = open("input.txt", "r")
numbers = []

for idx, line in enumerate(f):
    print(line)
    numbers.append([])
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
