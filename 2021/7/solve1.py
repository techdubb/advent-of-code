f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def get_fuel_cost(crab_pos, target):
    costs = [abs(target - x) for x in crab_pos]
    return sum(costs)

for line in f:
    input = line.strip()

crab_pos = input.split(',')
crab_pos = [int(x) for x in crab_pos]

max_pos = max(crab_pos)
min_pos = min(crab_pos)

costs = []
for x in range(min_pos, max_pos+1):
    costs.append(get_fuel_cost(crab_pos, x))

print(min(costs))
