def check_for_both(box_id):
	letter_count = dict()

	for letter in box_id:
		letter_count[letter] = letter_count.get(letter, 0) + 1

	twice = 2 in letter_count.values()
	thrice = 3 in letter_count.values()

	return (twice, thrice)

f = open("input_2.txt", "r")
total_twice = 0
total_thrice = 0
for line in f:
	(tw, th) = check_for_both(line)

	if tw:
		total_twice += 1

	if th:
		total_thrice += 1


print "*****"
print total_twice
print total_thrice
print "*****"
print total_thrice * total_twice
