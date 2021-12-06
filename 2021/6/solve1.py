import math

f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def do_next_day(pop):
    new_pop = []
    for idx, p in enumerate(pop):
        if p == 0:
            pop[idx] = 6
            new_pop.append(8)
        else:
            pop[idx] -= 1

    return pop + new_pop


population = []
# days = 18
days = 80

for line in f:
    input = line.strip()

population = input.split(',')
population = [int(x) for x in population]

for d in range(days):
    population = do_next_day(population)

print(len(population))