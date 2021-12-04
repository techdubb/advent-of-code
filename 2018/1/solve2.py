freq = 0
prev_freq = dict()
count = 0

def check_freq_two(pf):
	return 2 in pf.values()

prev_freq[0] = 1

while (not check_freq_two(prev_freq)):	
#for n in range(0,5):
	f = open("input_1_1.txt", "r")
	for line in f:
		count += 1
		freq = freq + int(line)
		prev_freq[freq] = prev_freq.get(freq, 0) + 1
		#print freq
		#print check_freq_two(prev_freq)
		if count % 10 == 0 and check_freq_two(prev_freq):
			break

print "*****"
print freq
print check_freq_two(prev_freq)

for freq, count in prev_freq.items():
    if count == 2:
        print(freq)