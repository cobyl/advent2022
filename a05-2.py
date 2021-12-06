from itertools import chain


def read_puzzles_from_file():
    with open("a05-data.txt") as file:
        lines = []
        for line in file:
            coords = line.strip().split(" -> ")
            lines.append(
                ([int(x) for x in coords[0].split(",")], [int(x) for x in coords[1].split(",")])
            )
    return lines


def find_dimension(lines):
    all_from = [i[0] for i in lines]
    all_to = [i[0] for i in lines]

    return max([i[0] for i in all_from + all_to]) + 1, max([i[1] for i in all_from + all_to]) + 1


def dfor(start, end):
    if start == end:
        return [start]

    inc = 1 if start < end else -1
    return range(start, end + inc, inc)


def paint_straight_lines_on_table(table, lines):
    for f, t in lines:
        for x in dfor(f[0], t[0]):
            for y in dfor(f[1], t[1]):
                table[x][y] += 1

    return table


def paint_non_straight_lines_on_table(table, lines):
    for f, t in lines:
        direction_lr = 1 if f[0] < t[0] else - 1
        direction_ud = 1 if f[1] < t[1] else - 1

        length = (f[0] - t[0] + 1) if f[0] > t[0] else (t[0] - f[0] + 1)

        for i in range(length):
            table[f[0] + direction_lr * i][f[1] + direction_ud * i] += 1

    return table


def count_points(table):
    flattened_puzzle = list(chain.from_iterable(table))

    return len(list(filter(lambda x: x > 1, flattened_puzzle)))


def filter_straight_lines(lines):
    return list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))


def filter_non_straight_lines(lines):
    return list(filter(lambda x: x[0][0] != x[1][0] and x[0][1] != x[1][1], lines))


def main():
    lines = read_puzzles_from_file()
    dimension = find_dimension(lines)
    table = [[0] * dimension[0] for _ in range(dimension[1])]

    table = paint_straight_lines_on_table(table, filter_straight_lines(lines))
    table = paint_non_straight_lines_on_table(table, filter_non_straight_lines(lines))
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table]))

    print(count_points(table))


if __name__ == '__main__':
    main()
