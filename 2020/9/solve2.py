p = print

def get_contiguous_set(num, space):
    set_size = 2

    while True:
        idx = 0
        while (idx + set_size -1 ) < len(space):
            sub_list = space[idx:set_size + idx]
            # p(sub_list)
            if sum(sub_list) != num:
                idx += 1
            else:
                return sub_list

        set_size += 1

    return None

number_stream = []
# target_sum_idx = 14
target_sum_idx = 520

f = open("input.txt", "r")
for line in f:
    number_stream.append(int(line))

num = number_stream[target_sum_idx]
p(num)
search_space = number_stream[:target_sum_idx]

p("*****")
c_set = get_contiguous_set(num, search_space)
p(c_set)
p(max(c_set) + min(c_set))