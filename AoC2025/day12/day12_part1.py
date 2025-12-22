from functools import cache
import numpy as np


def main():
    with open("day12_input.txt") as f:
        content = f.read()
        split_content = content.split('\n\n')
        presents = [
            line.splitlines()
            for line in split_content[:-1]
        ]
        presents = np.array([
            [list(present_grid) for present_grid in present[1:]]
            for present in presents
        ])
        regions = split_content[-1].splitlines()
        regions = [(tuple([int(d) for d in region.split(':')[0].split('x')]),
                    tuple([int(quantity) for quantity in region.split(':')[1].split()])) for region in regions]

    # def get_presents_from_region(region):
    #     _, quantities = region
    #     return [presents[index] for index, quantity in enumerate(quantities) if quantity > 0 for _ in range(quantity)]

    def get_all_rotations(present):
        rotations = [present] + [np.rot90(present, k=i) for i in range(1, 4)]
        return rotations

    def get_all_flips(present):
        flips = [present, np.flip(present, 0), np.flip(present, 1)]
        return flips

    def present_to_coords(present):
        present_tuple = tuple([tuple(row) for row in present])
        return present_tuple_to_coords(present_tuple)

    @cache
    def present_tuple_to_coords(present_tuple):
        coords = []
        for x, row in enumerate(present_tuple):
            for y, piece in enumerate(row):
                # print(piece)
                if piece == "#":
                    coords.append((x, y))
        return coords

    def get_all_orientations(present):
        seen_coords = set()
        unique_orientations = []

        for rotated in get_all_rotations(present):
            for flipped in get_all_flips(rotated):
                coords = tuple(sorted(present_to_coords(flipped)))
                if coords not in seen_coords:
                    seen_coords.add(coords)
                    unique_orientations.append(flipped)

        return unique_orientations

    def generate_region_grid(region):
        width, length = region[0]
        return np.array([['.' for _ in range(width)] for _ in range(length)])

    # Backtracking approach - correct, but too slow
    # def solve_region(grid, presents_left, letters=None):
    #     call_counts['solve_region'] += 1
    #     print(f"\nFunction call counts:")
    #     for func, count in call_counts.items():
    #         print(f"{func}: {count}")
    #     if letters is None:
    #         letters = list(string.ascii_uppercase)
    #     if not presents_left:
    #         return True
    #     next_present = presents_left[0]
    #     remaining_presents = presents_left[1:]
    #     for orientated_present in get_all_orientations(next_present):
    #         for x in range(len(grid)):
    #             for y in range(len(grid[0])):
    #                 if can_place(orientated_present, grid, x, y):
    #                     place(orientated_present, grid, x, y, letters.pop(0))
    #                     # print(f"Placed present {np.nonzero(presents == next_present)[0][0]} at ({x}, {y})")
    #                     # print(grid)
    #                     if solve_region(grid, remaining_presents, letters):
    #                         # print(grid)
    #                         return True
    #                     remove(orientated_present, grid, x, y, letters)
    #                 # else:
    #                 # print(f"Cannot place present {np.nonzero(presents == next_present)[0][0]} at ({x}, {y})")
    #     return False

    # Greedy algorithm - didn't work with the example input, but worked with the real input?
    def solve_region(grid, region):
        _, quantities = region
        present_counts = list(quantities)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != '.':
                    continue
                for present_index in range(len(presents)):
                    if grid[y][x] != '.':
                        break
                    if present_counts[present_index] == 0:
                        continue
                    for orientated_present in get_all_orientations(presents[present_index]):
                        if can_place(orientated_present, grid, x, y):
                            place(orientated_present, grid, x, y, "#")
                            present_counts[present_index] -= 1
                            print(f"Placed present {present_index} at ({x}, {y})")
                            break
        return all(count == 0 for count in present_counts)

    def can_place(present, grid, start_x, start_y):
        coords = present_to_coords(present)
        for y, x in coords:
            new_x, new_y = start_x + x, start_y + y
            if new_x < len(grid[0]) and new_y < len(grid):
                if grid[new_y][new_x] != '.':
                    return False
            else:
                return False
        return True

    def place(present, grid, start_x, start_y, letter):
        coords = present_to_coords(present)
        for y, x in coords:
            grid[start_y + y][start_x + x] = letter

    # def remove(present, grid, start_x, start_y, letters):
    #     coords = present_to_coords(present)
    #     letters.insert(0, grid[start_y][start_x])
    #     for y, x in coords:
    #         grid[start_y + y][start_x + x] = "."

    num_successful_regions = 0

    for region in regions:
        print(f"\nSolving region {regions.index(region)}...")
        if solve_region(generate_region_grid(region), region):
            num_successful_regions += 1
            print("Success!")

    print("\nNumber of successful regions:", num_successful_regions)


if __name__ == "__main__":
    main()
