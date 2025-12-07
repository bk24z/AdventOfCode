from functools import cache


def main():
    with open("day7_input.txt") as f:
        grid = [list(row) for row in f.read().splitlines()]
        # print(grid)
        f.close()

    last_row_idx = len(grid) - 1
    start_col_idx = grid[0].index("S")

    @cache
    def calculate(row_idx, col_idx):
        if row_idx == last_row_idx:
            return 1
        if grid[row_idx + 1][col_idx] == ".":
            return calculate(row_idx + 1, col_idx)
        if grid[row_idx + 1][col_idx] == "^":
            return calculate(row_idx + 1, col_idx - 1) + calculate(row_idx + 1, col_idx + 1)
        return None

    print(calculate(0, start_col_idx))


if __name__ == "__main__":
    main()
