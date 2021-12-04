# too high: 9687

def trigger_reactions(polymer):
    idx = 0
    for val in polymer:
        if idx >= len(polymer) - 1:
            break
        c0 = polymer[idx]
        c1 = polymer[idx + 1]

        # print c0
        # print c1

        if c0.lower() == c1.lower():
            if c0 != c1:
                print "DESTROY!"
                print c0
                print c1
                print idx
                print idx + 1
                print "*"*10
                del(polymer[idx + 1])
                del(polymer[idx])
            else:
                idx += 1
        else:
                idx += 1

    return polymer


with open("input5.txt", "r") as content_file:
    content = content_file.read().strip()
    # for i in rangle(0, len(content)):
    while True:
        prev_len = len(content)
        content = trigger_reactions(list(content))
        print prev_len
        print len(content)
        print "*"*10
        if prev_len == len(content):
            break
    print len(content)
    print ''.join(content)