def read_crabs_from_file():
    file = open('a07-data.txt', 'r')
    lines = file.readlines()
    fishes = [int(num) for num in lines[0].strip().split(",")]
    return fishes


def calculate_cost(line, crabs):
    cost = 0
    for crab_line in crabs:
        cost += sum(range(abs(crab_line - line) + 1))
    return cost


def main():
    crabs = read_crabs_from_file()
    max_line = max(crabs)
    costs = [False] * (max_line + 1)
    for i, cost in enumerate(costs):
        costs[i] = calculate_cost(i, crabs)

    print(costs)
    print(min(costs))


if __name__ == '__main__':
    main()
