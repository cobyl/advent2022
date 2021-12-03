from functools import reduce
from more_itertools import pairwise
from pprint import pprint

if __name__ == '__main__':
    with open("a01-data.txt") as file:
        lines = [int(line.strip()) for line in file]

    unnoised = []
    for i in range(0, len(lines)-2):
        unnoised.append(lines[i]+lines[i+1]+lines[i+2])

    increased = pairwise(unnoised)
    def compare(result, element):
        if element[1] > element[0]:
            result = result + 1
        return result

    print(reduce(compare, list(pairwise(unnoised)), 0))
