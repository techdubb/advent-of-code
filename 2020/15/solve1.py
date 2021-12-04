p = print

def play_game(nth, start_numbers):
    spoken = {}
    round = len(start_numbers)
    last_num = 0

    for idx, s in enumerate(start_numbers):
        spoken[int(s)] = idx
        last_num = s

    # # add the first zero
    # p('turn', len(start_numbers))
    # last_num = 0
    # p(last_num)
    # p('*'*10)

    for i in range(len(start_numbers), nth):
        # p('turn', i)
        if last_num in spoken.keys():
            last_time = spoken[last_num]
            # p(last_num, 'has been seen before on turn', last_time)
            num = (i - 1) - last_time
            spoken[last_num] = i - 1
            last_num = num
        else:
            # p(last_num, 'is new')
            spoken[last_num] = i - 1
            last_num = 0
        # p('latest number is now:', last_num)
        # p('*'*10)

    return last_num



start_numbers = []

f = open("input.txt", "r")
for line in f:
    nums = line.strip().split(',')
    start_numbers.append(nums)

# p(start_numbers)

# play_game(10, start_numbers[0])
p(play_game(30000000, start_numbers[0]))
