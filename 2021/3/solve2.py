# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def tally_bits(bin_input):
    columns = []

    for bit in bin_input:
        bit_count = {'0':0, '1':0}
        if bit == '0':
            bit_count['0'] += 1
        elif bit == '1':
            bit_count['1'] += 1
        else:
            raise Exception("Unknown bit")

        columns.append(bit_count)

    return columns

def get_col_tally(tally):
    col_tally = []
    for x in tally[0]:
        col_tally.append({'0':0, '1':0})

    for i in tally:
        for idx, j in enumerate(i):
            col_tally[idx]['0'] += j['0']
            col_tally[idx]['1'] += j['1']

    return col_tally

def remove_nums1(n, col_tally, col):
    if col_tally[col]['0'] == col_tally[col]['1']:
        bit_to_keep = '1'
    else:
        bit_to_keep = max(col_tally[col], key=col_tally[col].get)
    new_nums = []

    for num in n:
        if bit_to_keep == num[col]:
            new_nums.append(num)

    return new_nums

def remove_nums2(n, col_tally, col):
    if col_tally[col]['0'] == col_tally[col]['1']:
        bit_to_keep = '0'
    else:
        bit_to_keep = min(col_tally[col], key=col_tally[col].get)
    print(bit_to_keep)
    new_nums = []

    for num in n:
        if bit_to_keep == num[col]:
            new_nums.append(num)

    return new_nums

tally = []
nums = []
col = 0

for line in f:
    nums.append(line.strip())
    tally.append(tally_bits(line.strip()))

col_tally = get_col_tally(tally)

nums1 = remove_nums1(nums, col_tally, col)
nums2 = remove_nums2(nums, col_tally, col)
print(nums2)

for c in range(1, len(nums1[0])):
    tally = []
    for n in nums1:
        tally.append(tally_bits(n))

    col_tally = get_col_tally(tally)
    print(col_tally)

    nums1 = remove_nums1(nums1, col_tally, c)
    # print(nums1)

    if len(nums1) == 1:
        break

for c in range(1, len(nums2[0])):
    tally = []
    for n in nums2:
        tally.append(tally_bits(n))

    col_tally = get_col_tally(tally)
    print(col_tally)

    nums2 = remove_nums2(nums2, col_tally, c)
    print(nums2)

    if len(nums2) == 1:
        break

print(int(nums1[0],2) * int(nums2[0],2))
