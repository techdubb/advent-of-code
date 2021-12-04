import string

workers = 2
base_task_duration = 0
# workers = 5
# base_task_duration = 60

workload = [[] for i in range(0, workers)]
done_sec = [-1 for i in range(0, workers)]

def parse_step(step):
    (step1, step2) = step.split('step')
    step1 = step1.split('Step')[1].strip()

    return (step1[0], step2.strip()[0])

def get_next_step(steps):
    candidates = list(steps.keys())
    for step_k in steps:
        for step_vs in steps.values():
            if step_k in step_vs:
                if step_k in candidates:
                    candidates.remove(step_k)

    candidates.sort()
    return candidates[:workers]

def build_solution(steps):
    solution = []
    next_steps = steps.copy()
    clock = 0

    next_step = get_next_step(next_steps)
    while len(next_steps) > 0:
        print "CLOCK! " + str(clock)
        for idx, s in enumerate(next_step):
            print "next step"
            print s
            if done_sec[idx] == -1:
                done_sec[idx] = clock + (string.ascii_uppercase.index(s) + 1)
                workload[idx].append(s)
            if clock >= done_sec[idx]:
                done_sec[idx] = -1
                next_steps.pop(s, None)
                if len(next_steps) > 0:
                    next_step = get_next_step(next_steps)

            print "$$"*3

        clock += 1

        print "workload"
        print workload

        print "done"
        print done_sec

    print "CLOCK! " + str(clock)

    return 'foo'


f = open("test_input.txt", "r")
steps = dict()

for line in f:
    s1, s2 = parse_step(line.strip())
    if s1 in steps:
        steps[s1].append(s2)
    else:
        steps[s1] = [s2]

print steps
print "*****"
solution = build_solution(steps)
# print ''.join(solution)
