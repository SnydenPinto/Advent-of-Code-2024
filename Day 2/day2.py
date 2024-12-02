from helper import read_input

report = read_input('day2_input')

def is_increasing_or_decreasing(data):
    return data == sorted(data) or data == sorted(data, reverse=True)


def has_valid_differences(data):
    differ_allowed = [1, 2, 3]
    for i in range(len(data) - 1):
        if abs(data[i] - data[i + 1]) not in differ_allowed:
            return False
    return True


def part_one(report):
    safe = 0
    for data in report:
        if is_increasing_or_decreasing(data) and has_valid_differences(data):
            safe += 1
    return  safe




print("Part 1: Safe reports:",part_one(report))
