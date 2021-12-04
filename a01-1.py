from functools import reduce
from more_itertools import pairwise

if __name__ == '__main__':
    with open("a01-data.txt") as file:
        lines = [line.strip().split() for line in file]

    print(reduce(lambda total, element: total + 1 if element[1] > element[0] else total, list(pairwise(lines)), 0))
