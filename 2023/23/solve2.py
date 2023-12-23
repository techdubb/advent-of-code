f = open("input_test.txt", "r")
# f = open("input.txt", "r")

possible_steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def do_next_steps(paths):
    # print(stps)
    next_paths = paths
    full_paths = []

    while len(next_paths) > 0:
        print(len(next_paths))
        for idx, p in enumerate(next_paths):
            next_paths.pop(idx)
            (r, c) = p[-1]

            for ps in possible_steps:
                np = p.copy()
                (rd, cd) = ps
                nr = r+rd
                nc = c+cd
                if (nr,nc) not in np:
                    if nr >= 0 and nc >= 0 and nr < max_r and nc < max_c:
                        if hiking_map[nr][nc] in ['.', '<', 'v', '>', '^']:

                            np.append((nr,nc))
                            next_paths.append(np)

                            if (nr,nc) == end:
                                full_paths.append(np)

            # print(next_paths)
    lens = []
    for p in full_paths:
        lens.append((len(p)-1))

    return lens

hiking_map = []
for line in f:
    hiking_map.append(list(line.strip()))

max_r = len(hiking_map)
max_c = len(hiking_map[0])

# for hm in hiking_map:
#     print(''.join(hm))

find_s = hiking_map[0].index('.')
start = (0, find_s)
find_e = hiking_map[max_r-1].index('.')
end = (max_r-1, find_e)

lens = do_next_steps([[start]])

print(max(lens))
