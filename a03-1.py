from functools import reduce
from more_itertools import pairwise
from pprint import pprint

if __name__ == '__main__':
    with open("a03-data.txt") as file:
        lines = []
        for line in file:
            lines.append([int(x) for x in line.strip()])

    rotated_lines = list(zip(*lines[::-1]))

    half = len(lines) / 2


    def sum_tuples(result, element):
        return result.__add__([str(int(sum(list(element)) > half))])


    bits = reduce(sum_tuples, rotated_lines, [])
    bits_string = ''.join(bits)
    gamma = eval('0b' + bits_string)
    epsilon = (~gamma & 0b111111111111)

    print(gamma, epsilon, gamma*epsilon)
