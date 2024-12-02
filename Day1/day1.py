from collections import Counter
from helper import read_input



def sort_data(data):
    left_column = sorted(pair[0] for pair in data)
    right_column = sorted(pair[1] for pair in data)
    return left_column, right_column


def calculate_total_distance(left_column, right_column):
    return sum(abs(left - right) for left, right in zip(left_column, right_column))

def calculate_similarity_score(left, right):
    frequency_map = Counter(right)

    return sum(num * frequency_map[num] for num in left)


if __name__ == "__main__":
    data = read_input('day1_input')
    left, right = sort_data(data)
    distance = calculate_total_distance(left, right)
    similarity_score = calculate_similarity_score(left,right)

    print("Day 1 - Part One :",distance)
    print("Day 1 - Part Two :", similarity_score)



