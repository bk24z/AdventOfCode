import csv
from itertools import combinations
from functools import cache


def calc_area(pair) -> float:
    (t1_x, t1_y), (t2_x, t2_y) = pair
    height = abs(t1_y - t2_y) + 1
    width = abs(t1_x - t2_x) + 1
    area = height * width
    # print(pair, area)
    return area


def main():
    with open('day9_input.csv', 'r') as f:
        f_reader = csv.reader(f)
        red_tiles: list[tuple[int, ...]] = [tuple(map(int, row)) for row in f_reader]
        f.close()

    print(f"Red tiles count: {len(red_tiles)}")
    print(f"X range: {min(x for x, y in red_tiles)} to {max(x for x, y in red_tiles)}")
    print(f"Y range: {min(y for x, y in red_tiles)} to {max(y for x, y in red_tiles)}")

    @cache
    def check_if_rectangle_valid(pair: tuple[tuple[int, ...], tuple[int, ...]]):
        t1, t2 = pair
        (t1_x, t1_y), (t2_x, t2_y) = t1, t2
        t3, t4 = (t1_x, t2_y), (t2_x, t1_y)
        # Check corners
        if (not is_point_inside_polygon(*t3) and not is_on_edge(*t3)) or (not is_point_inside_polygon(
                *t4) and not is_on_edge(*t4)):
            return False
        # Check top and bottom edges
        for x in range(min(t1_x, t2_x), max(t1_x, t2_x) + 1):
            if not is_point_inside_polygon(x, t1_y) and not is_on_edge(x, t1_y):
                return False
            if not is_point_inside_polygon(x, t2_y) and not is_on_edge(x, t2_y):
                return False
        # Check left and right edges
        for y in range(min(t1_y, t2_y), max(t1_y, t2_y) + 1):
            if not is_point_inside_polygon(t1_x, y) and not is_on_edge(t1_x, y):
                return False
            if not is_point_inside_polygon(t2_x, y) and not is_on_edge(t2_x, y):
                return False
        # Check the rest of the tiles
        for y in range(min(t1_y, t2_y) + 1, max(t1_y, t2_y)):
            for x in range(min(t1_x, t2_x) + 1, max(t1_x, t2_x)):
                if not is_point_inside_polygon(x, y) and not is_on_edge(x, y):
                    return False
        return True

    @cache
    def is_on_edge(p_x, p_y):
        for i in range(len(red_tiles)):
            t1 = red_tiles[i]
            t2 = red_tiles[(i + 1) % len(red_tiles)]
            t1_x, t1_y = t1
            t2_x, t2_y = t2
            if t1_x == t2_x and p_x == t1_x and p_y in range(min(t1_y, t2_y), max(t1_y, t2_y) + 1):
                return True
            if t1_y == t2_y and p_y == t1_y and p_x in range(min(t1_x, t2_x), max(t1_x, t2_x) + 1):
                return True
        return False

    @cache
    def is_point_inside_polygon(p_x, p_y):
        crossings = 0
        for i in range(len(red_tiles)):
            t1 = red_tiles[i]
            t2 = red_tiles[(i + 1) % len(red_tiles)]
            t1_x, t1_y = t1
            t2_x, t2_y = t2
            if t1_x == t2_x and t1_x < p_x:
                if min(t1_y, t2_y) <= p_y < max(t1_y, t2_y):
                    crossings += 1
        return crossings % 2 == 1

    pairs = combinations(red_tiles, 2)
    pairs_with_areas = [(pair,) + (calc_area(pair),) for pair in pairs]
    print(len(pairs_with_areas))
    pairs_with_areas.sort(key=lambda x: x[-1], reverse=True)
    for pair_with_area in pairs_with_areas:
        print(f"Checking {pair_with_area}")
        pair, _ = pair_with_area
        if check_if_rectangle_valid(pair):
            print(f"Valid {pair_with_area}")
            break


if __name__ == "__main__":
    main()
