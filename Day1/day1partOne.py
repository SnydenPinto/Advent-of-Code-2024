def read_and_sort(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.split())) for line in file]

    left_column = sorted(pair[0] for pair in data)
    right_column = sorted(pair[1] for pair in data)
    return left_column, right_column


def calculate_total_distance(left_column, right_column):
    return sum(abs(left - right) for left, right in zip(left_column, right_column))


if __name__ == "__main__":
    left, right = read_and_sort('input')
    distance = calculate_total_distance(left, right)
    print(distance)
