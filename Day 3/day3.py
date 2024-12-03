import re


def day2(input_text):

    pattern = r"(?:mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)|(do)\(\))"

    part1_sum = 0
    part2_sum = 0
    enabled = True

    matches = re.finditer(pattern, input_text)

    for match in matches:
        num1, num2, dont, do = match.groups()

        if num1 and num2:
            result = int(num1) * int(num2)
            part1_sum += result
            if enabled:
                part2_sum += result
        elif dont:
            enabled = False
        elif do:
            enabled = True

    return part1_sum, part2_sum


with open('day3_input', 'r') as file:
    data = file.read()

part1, part2 = day2(data)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
