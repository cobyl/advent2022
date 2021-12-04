from functools import reduce

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
    gamma = int(bits_string, 2)
    epsilon = (~gamma & 0b111111111111)

    print(gamma, epsilon, gamma * epsilon)
