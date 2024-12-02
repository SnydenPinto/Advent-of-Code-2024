
def read_input(filename):
    with open(filename, 'r') as file:
        data = [list(map(int, line.split())) for line in file]
    return data
