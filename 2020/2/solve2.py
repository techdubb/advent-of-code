f = open("input.txt", "r")
valid_passwords = 0

def validate_password(line):
	line_parts = line.split()

	positions_str = line_parts[0]
	positions = positions_str.split('-')

	character = line_parts[1].replace(':', '')
	password = line_parts[2]

	char_count = password.count(character)

	pos_check = []

	for pos in positions:
		pos_check.append(password[int(pos) - 1] == character)

	num_true = pos_check.count(True)
	return (num_true == 1)



for line in f:
	if validate_password(line.strip()):
		valid_passwords += 1

print(valid_passwords)