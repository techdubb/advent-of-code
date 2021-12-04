from datetime import datetime
import collections
from operator import itemgetter

def parse_log(log_line):
	(dt, info) = log_line.split(']')
	return (datetime.strptime(dt[1:], '%Y-%m-%d %H:%M'), info.strip())

def update_row(sleep, wake, row):
	wake_int = int('%02d' % wake.minute)
	sleep_int = int('%02d' % sleep.minute)

	for i in range(sleep_int, wake_int):
		row[i] = '#'

	return row

def analyze_logs(data):
	current_guard = ''
	current_date = ''
	current_sleep_time = ''
	current_wake_time = ''

	analysis = dict()

	for log in data:
		dt = log 
		info = data.get(log)

		current_date = '%02d' % dt.month + '-' + '%02d' % dt.day
		if 'Guard' in info:
			split_info = info.split(' ')
			current_guard = split_info[1]

		if 'falls' in info:
			current_sleep_time = dt
		if 'wake' in info:
			current_wake_time = dt
			if analysis.get((current_date, current_guard)) is None:
				init_list = ['.' for i in range(0, 60)]
				analysis[(current_date, current_guard)] = init_list

			updated = update_row(current_sleep_time, current_wake_time, analysis.get((current_date, current_guard)))
			analysis[(current_date, current_guard)] = updated 

	return analysis

# def find_most_sleepy(analysis):
# 	total_sleep = dict()

# 	for (date, guard_id) in analysis:
# 		sleep_data = analysis.get((date, guard_id))
# 		sleep_time = sleep_data.count('#')

# 		total_sleep[guard_id] = total_sleep.get(guard_id, 0) + sleep_time

# 	return total_sleep

def find_sleepy_minute(analysis):
	total_sleep_by_minute = dict()

	for (date, guard_id) in analysis:
		total_sleep_by_minute[guard_id] = total_sleep_by_minute.get(guard_id, dict())
		sleep_data = analysis.get((date, guard_id))

		for min, val in enumerate(sleep_data):
			if val == '#':
				total_sleep_by_minute[guard_id][min] = total_sleep_by_minute[guard_id].get(min, 0) + 1

	return total_sleep_by_minute

f = open("input4.txt", "r")
log_data = dict()
for line in f:
	(dt, info) = parse_log(line.strip())	
	log_data[dt] = info

ordered_data = collections.OrderedDict(sorted(log_data.items()))

analysis = analyze_logs(ordered_data)

print "*****"
# for (i, e) in analysis:
# 	print (i, e)
# 	print analysis[(i,e)]
 
# sleepy_data = find_most_sleepy(analysis)

sleepy_minute = find_sleepy_minute(analysis)
max_data = list()
for row in sleepy_minute:
	max_data.append((row, max(sleepy_minute[row].values()), max(sleepy_minute[row], key=sleepy_minute[row].get)))

max_data.sort(key=itemgetter(1), reverse=True)

solution_tuple = max_data[0]
print int(solution_tuple[0][1:]) * solution_tuple[2]