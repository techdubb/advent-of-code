f = open("input.txt", "r")
target_value = 2020
expenses = []

for line in f:
	expenses.append(int(line.strip()))

val1 = 0
val2 = 0
val3 = 0

for x in expenses:
	val1 = x
	for y in expenses:
		val2 = y
		for z in expenses:
			val3 = z
			if (val1 + val2 + val3) == target_value:
				break
		if (val1 + val2 + val3) == target_value:
			break
	if (val1 + val2 + val3) == target_value:
		break

print(val1 * val2 * val3)