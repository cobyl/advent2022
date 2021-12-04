from functools import reduce
from more_itertools import pairwise

if __name__ == '__main__':
    with open("a01-data.txt") as file:
        lines = [int(line.strip()) for line in file]

    unnoised = [sum(lines[i:i + 3]) for i in range(0, len(lines) - 2)]

    print(reduce(lambda total, element: total + 1 if element[1] > element[0] else total, list(pairwise(unnoised)), 0))
