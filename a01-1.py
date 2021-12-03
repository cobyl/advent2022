from functools import reduce
from more_itertools import pairwise
from pprint import pprint

if __name__ == '__main__':
    with open("a01-data.txt") as file:
        lines = [line.strip().split() for line in file]

    increased = pairwise(lines)


    def compare(result, element):
        if element[1] > element[0]:
            result = result + 1
        return result

    print(reduce(compare, list(pairwise(lines)), 0))
