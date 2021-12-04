from operator import itemgetter

p = print

def check_is_time(bus_id_w_idx, max_id_pair, timestamp):
    departing = []
    max_offset = max_id_pair[1]
    for b in bus_id_w_idx:
        check_ts = timestamp + (b[1] - max_offset)
        check = check_ts % b[0] == 0
        departing.append(check)
        if check == False:
            return (check, timestamp - max_offset)

    return (True, timestamp - max_offset)

input = []

f = open("input.txt", "r")
for line in f:
    input.append(line.strip())

bus_id_w_idx = []
max_id = 0

for idx, b in enumerate(input[1].split(',')):
    if b == 'x':
        continue
    else:
        bus_id_w_idx.append((int(b), idx))
        if int(b) > max_id:
            max_id = int(b)
            max_id_pair = (int(b), idx)

p(bus_id_w_idx)
p(max_id_pair)

# exit()

timestamp = 871100667227947
# timestamp = 0

while True:
    timestamp -= max_id

    if (timestamp % 1000000 == 0): p('{:,}'.format(timestamp))

    (good, ts) = check_is_time(bus_id_w_idx, max_id_pair, timestamp)
    if good:
        p(ts)
        break