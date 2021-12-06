from itertools import chain


def read_fishes_from_file():
    file = open('a06-data.txt', 'r')
    lines = file.readlines()
    fishes = [int(num) for num in lines[0].strip().split(",")]
    return fishes


def mature_fishes(fishes):
    for i in range(len(fishes)):
        fish = fishes[i]
        fish -= 1
        if fish == -1:
            fish = 6
            fishes.append(8)
        fishes[i] = fish
    return fishes


def main():
    fishes = read_fishes_from_file()
    for i in range(80):
        fishes = mature_fishes(fishes)

    print(len(fishes))


if __name__ == '__main__':
    main()
