import csv
from itertools import combinations


def calc_area(pair):
    (t1_x, t1_y), (t2_x, t2_y) = pair
    height = abs(t1_y - t2_y) + 1
    width = abs(t1_x - t2_x) + 1
    return height * width


def main():
    with open('day9_input_test.csv', 'r') as f:
        f_reader = csv.reader(f)
        red_tiles = [tuple(map(int, row)) for row in f_reader]
        f.close()

    pairs = combinations(red_tiles, 2)
    pairs_with_areas = [pair + (calc_area(pair),) for pair in pairs]
    pairs_with_areas.sort(key=lambda x: x[-1], reverse=True)
    # print(pairs_with_areas)
    largest_area = pairs_with_areas[0][-1]
    print(largest_area)


if __name__ == "__main__":
    main()
