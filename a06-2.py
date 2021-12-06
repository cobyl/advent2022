def read_fishes_from_file():
    file = open('a06-data.txt', 'r')
    lines = file.readlines()
    fishes = [int(num) for num in lines[0].strip().split(",")]
    return fishes


cache = []


def kids(days_for_reproduction):
    global cache
    total = 0

    while True:
        total += 1
        days_for_reproduction -= 7
        time_for_kid_reproduction = days_for_reproduction - 2
        if time_for_kid_reproduction >= 0:
            if cache[time_for_kid_reproduction] is False:
                total += kids(time_for_kid_reproduction)
            else:
                total += cache[time_for_kid_reproduction]

        if days_for_reproduction < 0:
            break

    return total


def main():
    global cache

    fishes = read_fishes_from_file()
    max_days = 256

    cache = [False] * (max_days + 1)
    for day, _ in enumerate(cache):
        cache[day] = kids(day)

    sea = []
    for reproduction_start_day in fishes:
        sea.append(1)  # that fish
        fishes = cache[max_days - reproduction_start_day - 1]
        sea.append(fishes)

    print("sum=", sum(sea))


if __name__ == '__main__':
    main()
