def read_crabs_from_file():
    file = open('a07-data.txt', 'r')
    lines = file.readlines()
    fishes = [int(num) for num in lines[0].strip().split(",")]
    return fishes


cache = []


def calculate_cost(line, crabs):
    global cache
    cost = 0
    for crab_line in crabs:
        line = abs(crab_line - line) + 1
        if cache[line] is False:
            line_cost = sum(range(line))
            cache[line] = line_cost
        else:
            line_cost = cache[line]
        cost += line_cost
    return cost


def main():
    global cache
    crabs = read_crabs_from_file()
    max_line = max(crabs)
    costs = [False] * (max_line + 1)
    cache = [False] * (max_line + 1)
    for i, cost in enumerate(costs):
        costs[i] = calculate_cost(i, crabs)


    print(min(costs))


if __name__ == '__main__':
    main()
