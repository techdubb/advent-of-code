from difflib import SequenceMatcher

f = open("input_2.txt", "r")
ratios = dict()
for line in f:
	f2 = open("input_2.txt", "r")
	for line2 in f2:
		s = SequenceMatcher(None, line, line2)
		ratio = s.ratio()
		ratios[ratio] = (line, line2)

print "*****"
sorted_keys = sorted(list(ratios.keys()))
scnd_last = sorted_keys[-2]

(str1, str2) = ratios.get(scnd_last)
list1 = list(str1)
list2 = list(str2)

solution = list()

for idx in range(0, len(list1) - 1):
	if list1[idx] == list2[idx]:
		solution.append(list1[idx])

print ''.join(solution)