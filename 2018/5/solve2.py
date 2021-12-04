import string

def trigger_reactions(polymer):
    idx = 0
    for val in polymer:
        if idx >= len(polymer) - 1:
            break
        c0 = polymer[idx]
        c1 = polymer[idx + 1]

        if c0.lower() == c1.lower():
            if c0 != c1:
                # print "DESTROY!"
                del(polymer[idx + 1])
                del(polymer[idx])
            else:
                idx += 1
        else:
                idx += 1

    return polymer


with open("input5.txt", "r") as content_file:
    content = content_file.read().strip()
    alphabet = list(string.ascii_lowercase)
    smallest_reation = dict()
    for letter in alphabet:

        cont = content.replace(letter, '').replace(letter.upper(), '')
        while True:
            prev_len = len(cont)
            cont = trigger_reactions(list(cont))
            if prev_len == len(cont):
                break

        print letter
        smallest_reation[letter] = len(cont)

    print min(smallest_reation.values())