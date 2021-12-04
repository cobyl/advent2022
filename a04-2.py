import re
from functools import reduce
from itertools import chain
from types import SimpleNamespace


def read_puzzles_from_file():
    file = open('a04-data.txt', 'r')
    lines = file.readlines()
    bingo_numbers = [int(num) for num in lines[0].strip().split(",")]
    number_of_puzzles = (len(lines) - 1) / 6
    if not number_of_puzzles.is_integer():
        raise ValueError
    number_of_puzzles = int(number_of_puzzles)
    file_row = 2
    puzzles = []
    for i in range(0, number_of_puzzles):
        puzzle = []
        for row in range(0, 5):
            puzzle.append([(int(num), False) for num in re.split(r"\s+", lines[file_row].strip())])
            file_row = file_row + 1
        puzzles.append(puzzle)
        file_row = file_row + 1
    return SimpleNamespace(bingo_numbers=bingo_numbers, puzzles=puzzles, number_of_puzzles=number_of_puzzles)


def mark_number(puzzle, number):
    for row in range(0, 5):
        puzzle[row] = list(
            map(lambda x: (x[0], True) if x[0] == number else x, puzzle[row]))


def check_bingo(puzzle):
    def count_marked_in_row(row):
        return reduce(lambda sum, element: sum if (element[1] is False) else sum + 1, row, 0)

    rotated_puzzle = list(zip(*puzzle[::-1]))
    for row in range(0, 5):
        row_bingo = count_marked_in_row(puzzle[row])
        if row_bingo == 5:
            return True
        column_bingo = count_marked_in_row(rotated_puzzle[row])
        if column_bingo == 5:
            return True
    return False


def sum_unmarked(puzzle):
    flattened_puzzle = chain.from_iterable(puzzle)
    return reduce(lambda sum, element: sum if (element[1] is True) else sum + element[0], flattened_puzzle, 0)


def main():
    data = read_puzzles_from_file()

    last_sum = None
    winning = []
    for bingo_number in data.bingo_numbers:
        for i in range(0, data.number_of_puzzles):
            puzzle = data.puzzles[i]
            mark_number(puzzle, bingo_number)
            if check_bingo(puzzle) is True and not winning.__contains__(i):
                winning.append(i)
                last_sum = (bingo_number * sum_unmarked(puzzle))
    print(last_sum)


if __name__ == '__main__':
    main()
