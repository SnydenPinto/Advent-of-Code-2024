from helper import read_input

report = read_input('day2_input')

def is_increasing_or_decreasing(data):
    return data == sorted(data) or data == sorted(data, reverse=True)


def has_valid_differences(data):
    differ_allowed = {1, 2, 3}
    return all(abs(data[i] - data[i + 1]) in differ_allowed for i in range(len(data) - 1))


def is_safe(data):
    return is_increasing_or_decreasing(data) and has_valid_differences(data)

safe = 0
unsafe_report = []


for data in report:
    if is_safe(data):
        safe += 1
    else:
        unsafe_report.append(data)


part_two_counter = 0

for data in unsafe_report:
    for i in range(len(data)):
        modified_data = data[:i] + data[i + 1:]
        if is_safe(modified_data):
            part_two_counter += 1
            break

print("Part 1: Safe reports:", safe)
print("Part 2: Safe reports after removal:", part_two_counter + safe )
