from functools import reduce
from more_itertools import pairwise
from pprint import pprint

if __name__ == '__main__':
    with open("a02-data.txt") as file:
        lines = [line.strip().split() for line in file]


    def count_deep(result, element):
        if element[0] == "up":
            result = result - int(element[1])
        if element[0] == "down":
            result = result + int(element[1])
        return result


    forward = reduce(lambda total, element: total + int(element[1]) if element[0] == "forward" else total, lines, 0)
    deep = reduce(count_deep, lines, 0)

    print(forward * deep)
