f = open("input_test.txt", "r")
# f = open("input.txt", "r")

def add_sf_nums(sf_num, new_num):
    number = []
    number.append(sf_num)
    number.append(new_num)

    return number

def depth(L): return isinstance(L, list) and max(map(depth, L))+1

sf_nums = []
for line in f:
    new_num = line.strip()
    sf_nums.append(new_num)

print(sf_nums)
sf_number = literal_eval(sf_nums[0])
print()

for n in range(1, len(sf_nums)):
    num = literal_eval(sf_nums[n])
    sf_number = add_sf_nums(sf_number, num)

    print(sf_number)
    print(depth(sf_number))
