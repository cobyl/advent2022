from collections import Counter

if __name__ == '__main__':
    with open("a03-data.txt") as file:
        lines = []
        for line in file:
            lines.append([int(x) for x in line.strip()])


    def mode(list):
        data = Counter(list)
        most = data.most_common(1)[0]
        least = data.most_common()[-1]
        if (least[1] == most[1]):
            raise ValueError
        return most[0]


    oxygen_lines = lines
    for i in range(0, len(lines[0])):
        oxygen_rotated_lines = list(zip(*oxygen_lines[::-1]))
        try:
            most_common = mode(list(oxygen_rotated_lines[i]))
        except ValueError:
            most_common = 1
        oxygen_lines = list(filter(lambda x: (x[i] == most_common), oxygen_lines))
        if len(oxygen_lines) == 1:
            break

    co2_lines = lines
    for i in range(0, len(lines[0])):
        co2_rotated_lines = list(zip(*co2_lines[::-1]))
        try:
            least_common = int(not (bool(mode(list(co2_rotated_lines[i])))))
        except ValueError:
            least_common = 0
        co2_lines = list(filter(lambda x: (x[i] == least_common), co2_lines))
        if len(co2_lines) == 1:
            break

    oxygen_dec = eval('0b' + ''.join([str(x) for x in oxygen_lines[0]]))
    co2_dec = eval('0b' + ''.join([str(x) for x in co2_lines[0]]))

    print(oxygen_dec, co2_dec, oxygen_dec * co2_dec)
