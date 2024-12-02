from collections import Counter

def read_and_sort(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.split())) for line in file]

    left_column = sorted(pair[0] for pair in data)
    right_column = sorted(pair[1] for pair in data)
    return left_column, right_column


def calculate_total_distance(left_column, right_column):
    return sum(abs(left - right) for left, right in zip(left_column, right_column))

def calculate_similarity_score(left, right):
    frequency_map = Counter(right)

    return sum(num * frequency_map[num] for num in left)


if __name__ == "__main__":
    left, right = read_and_sort('input')
    distance = calculate_total_distance(left, right)
    similarity_score = calculate_similarity_score(left,right)

    print("Day 1 - Part One :",distance)
    print("Day 1 - Part Two :", similarity_score)



