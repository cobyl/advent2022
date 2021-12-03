from functools import reduce
from more_itertools import pairwise
from pprint import pprint

if __name__ == '__main__':
    with open("a02-data.txt") as file:
        lines = [line.strip().split() for line in file]

    aim = horizontal = deep = 0
    for command, num in lines:
        if command == "up":
            aim = aim - int(num)
        if command == "down":
            aim = aim + int(num)
        if command == "forward":
            horizontal = horizontal + int(num)
            deep = deep + aim*int(num)

    print(horizontal*deep)
