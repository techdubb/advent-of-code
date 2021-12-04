from operator import itemgetter

p = print

input = []

f = open("input.txt", "r")
for line in f:
    input.append(line.strip())

soonest_departure = int(input[0])
busses = input[1]

p(soonest_departure, busses)

departure_mod_diffs = []
actual_busses = []
for b in busses.split(','):
    if b == 'x':
        continue
    else:
        departure_mod_diffs.append(int(b) - (soonest_departure % int(b)))
        actual_busses.append(int(b))

min_idx = min(enumerate(departure_mod_diffs), key=itemgetter(1))[0]

p(departure_mod_diffs[min_idx] * actual_busses[min_idx])
