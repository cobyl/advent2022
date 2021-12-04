import re
from functools import reduce
from itertools import chain

if __name__ == '__main__':
    file = open('a04-data.txt', 'r')
    lines = file.readlines()
    bingo_numbers = [int(num) for num in lines[0].strip().split(",")]
    puzzle_num = (len(lines) - 1) / 6
    if not puzzle_num.is_integer():
        raise ValueError
    puzzle_num = int(puzzle_num)

    row = 2
    puzzles = []
    for i in range(0, puzzle_num):
        puzzle = []
        for j in range(0, 5):
            puzzle.append([(int(num), False) for num in re.split(r"\s+", lines[row].strip())])
            row = row + 1
        puzzles.append(puzzle)
        row = row + 1


    def mark_number(bingo_number, puzzle_number):
        for j in range(0, 5):
            puzzles[puzzle_number][j] = list(
                map(lambda x: (x[0], True) if x[0] == bingo_number else x, puzzles[puzzle_number][j]))


    def check_bingo(puzzle_number):
        rotated_puzzle = list(zip(*puzzles[puzzle_number][::-1]))
        for j in range(0, 5):
            row_bingo = reduce(lambda sum, element: sum if (element[1] is False) else sum + 1,
                               puzzles[puzzle_number][j], 0)
            if row_bingo == 5:
                return True

            column_bingo = reduce(lambda sum, element: sum if (element[1] is False) else sum + 1, rotated_puzzle[j], 0)
            if column_bingo == 5:
                return True

        return False


    def sum_unmarked(puzzle_number):
        flattened_puzzle = chain.from_iterable(puzzles[puzzle_number])
        return reduce(lambda sum, element: sum if (element[1] is True) else sum + element[0], flattened_puzzle, 0)


    for bingo_number in bingo_numbers:
        for i in range(0, puzzle_num):
            mark_number(bingo_number, i)
            if check_bingo(i) is True:
                print(bingo_number * sum_unmarked(i))
                quit()
