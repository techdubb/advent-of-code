import math

# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def do_next_day(pop):
    new_pop = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for k in pop:
        if k == 0 and pop[k] > 0:
            new_pop[8] += pop[k]
            new_pop[6] += pop[k]
        elif pop[k] > 0:
            new_pop[k-1] += pop[k]

    return new_pop

def get_dict(pop):
    pop_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for p in pop:
        if p in pop_dict:
            pop_dict[p] += 1
        else:
            pop_dict[p] = 1

    return pop_dict

population = []
# days = 18
# days = 80
days = 256

for line in f:
    input = line.strip()

population = input.split(',')
population = [int(x) for x in population]

pop_dict = get_dict(population)

for d in range(days):
    pop_dict = do_next_day(pop_dict)

print(sum(pop_dict.values()))
