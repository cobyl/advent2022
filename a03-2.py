from collections import Counter


def read_lines_from_file():
    with open("a03-data.txt") as file:
        lines = []
        for line in file:
            lines.append([int(x) for x in line.strip()])
    return lines


def mode(list):
    data = Counter(list)
    most = data.most_common(1)[0]
    least = data.most_common()[-1]
    if least[1] == most[1]:
        raise ValueError
    return most[0]


def convert_bin_array_to_dec(bin_array):
    return int(''.join([str(x) for x in bin_array]), 2)


def find_value(lines, default_value, find_type):
    for i in range(0, len(lines[0])):
        rotated_lines = list(zip(*lines[::-1]))
        try:
            value = mode(list(rotated_lines[i]))
            if find_type == "least_common":
                value = int(not (bool(value)))
        except ValueError:
            value = default_value

        lines = list(filter(lambda x: (x[i] == value), lines))
        if len(lines) == 1:
            break
    return convert_bin_array_to_dec(lines[0])


def main():
    lines = read_lines_from_file()

    oxygen = find_value(lines, 1, "most_common")
    co2 = find_value(lines, 0, "least_common")

    print(oxygen * co2)


if __name__ == '__main__':
    main()
