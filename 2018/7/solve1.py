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

    return min(candidates)

def build_solution(steps):
    solution = []

    next_steps = steps.copy()    
    next_step = get_next_step(next_steps)
    while len(solution) < len(steps):
        solution.append(next_step)
        next_steps.pop(next_step, None)
        if len(next_steps) > 0:
            next_step = get_next_step(next_steps)

    solution = solution + steps[solution[-1]]

    return solution


f = open("input7.txt", "r")
steps = dict()

for line in f:
    s1, s2 = parse_step(line.strip())  
    if s1 in steps:
        steps[s1].append(s2)
    else:
        steps[s1] = [s2]

print "*****"
solution = build_solution(steps)
print ''.join(solution)
