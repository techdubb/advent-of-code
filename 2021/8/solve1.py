# f = open("input_test.txt", "r")
f = open("input.txt", "r")

def get_unique_outputs(output):
    unique_lengths = [2,4,3,7]
    costs = [1 if (len(x) in unique_lengths) else 0 for x in output]
    return sum(costs)

outputs = []
for line in f:
    input = line.strip()
    (sig_pattern, digital_output) = input.split(' | ')
    digital_output = digital_output.split(' ')
    outputs.append(digital_output)

print(sum([get_unique_outputs(x) for x in outputs]))
