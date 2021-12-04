f = open("input.txt", "r")
valid_passwords = 0

def validate_password(line):
	line_parts = line.split()

	num_range_str = line_parts[0]
	num_range = num_range_str.split('-')

	character = line_parts[1].replace(':', '')
	password = line_parts[2]

	char_count = password.count(character)

	return char_count >= int(num_range[0]) and char_count <= int(num_range[1])



for line in f:
	if validate_password(line.strip()):
		valid_passwords += 1

print(valid_passwords)