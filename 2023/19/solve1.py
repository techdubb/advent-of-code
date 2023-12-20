# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def get_workflows(workflows):
    wf = {}
    for w in workflows:
        w = w.strip()
        w_split = w.split('{')

        r = w_split[1].replace('}', '')
        r_split = r.split(',')

        rules = []
        for r in r_split:
            rules.append(r.split(':'))

        wf[w_split[0]] = rules

    return wf

def get_parts(parts):
    built_parts = []

    for p in parts:
        p = p.strip().replace('{', '').replace('}', '')

        bp = {}
        for prop in p.split(','):
            for s in prop.split(','):
                (v, n) = s.split('=')
                bp[v] = int(n)

        built_parts.append(bp)

    return built_parts

def check_part(part):
    # print(part)
    # print(wf)

    curr = 'in'
    while True:
        if curr in ['A', 'R']:
            break
        # print('CURRENT workflow: ', curr)
        # print(wf[curr])
        for rule in wf[curr]:
            if len(rule) == 2:
                check = rule[0]
                res = rule[1]

                lt = check.split('<')
                if len(lt) == 2:
                    (k, v) = lt
                    # print('LT')

                    if part[k] < int(v):
                        curr = res
                        # print('new curr', res)
                        break

                gt = check.split('>')
                if len(gt) == 2:
                    (k, v) = gt
                    # print('GT')

                    if part[k] > int(v):
                        curr = res
                        # print('new curr', res)
                        break

            else:
                curr = rule[0]
                # print('new curr', curr)

    return curr


input = []
for line in f:
    input.append(line)

gap = input.index('\n')
parts = input[(gap+1):]
workflows = input[:gap]

wf = get_workflows(workflows)

bp = get_parts(parts)

accepted = []
for p in bp:
    check = check_part(p)
    if check == 'A':
        accepted.append(p)

total = 0
for a in accepted:
    total += sum(a.values())

print(total)
