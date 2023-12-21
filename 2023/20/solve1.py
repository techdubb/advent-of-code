# f = open("input_test.txt", "r")
# f = open("input_test1.2.txt", "r")
f = open("input.txt", "r")

def parse_module(line):
    (n, d) = line.split(' -> ')

    if n == 'broadcaster':
        name = n
        type = 'B'
    else:
        name = n[1:]
        type = n[0]

    return (name, {'t': type, 'd': d.split(', ')})

def do_phase(p):
    # print(p)
    (sender, pulse, sendee) = p
    pulse_cnt[pulse] += 1

    if sendee in modules:
        mod = modules[sendee]
        # print(mod)

        if mod['t'] == 'B':
            for d in mod['d']:
                phases.append((sendee, pulse, d))
        elif mod['t'] == '%':
            if pulse == 'low':
                if states[sendee]:
                    # print('i was true!')
                    for d in mod['d']:
                        phases.append((sendee, 'low', d))
                    states[sendee] = False
                else:
                    # print('i was false!')
                    for d in mod['d']:
                        phases.append((sendee, 'high', d))
                    states[sendee] = True
        elif mod['t'] == '&':
            states[sendee][sender] = pulse
            all_high = True
            for s in states[sendee]:
                all_high = all_high and (states[sendee][s] == 'high')

            for d in mod['d']:
                if all_high:
                    phases.append((sendee, 'low', d))
                else:
                    phases.append((sendee, 'high', d))

modules = {}
for line in f:
    m = parse_module(line.strip())
    modules[m[0]] = m[1]

print(modules)

states = {}
for m in modules:
    if m != 'broadcaster':
        mod = modules[m]
        if mod['t'] == '%':
            states[m] = False
        elif mod['t'] == '&':
            states[m] = {}
            for mm in modules:
                if mm != 'broadcaster':
                    if m in modules[mm]['d']:
                        states[m][mm] = 'low'


pulse_cnt = {'low': 0, 'high': 0}

# for i in range(0, 4):
for i in range(0, 1000):
    # print(i)
    phases = [('button', 'low', 'broadcaster')]
    for p in phases:
        do_phase(p)

print(pulse_cnt)
print(pulse_cnt['low'] * pulse_cnt['high'])