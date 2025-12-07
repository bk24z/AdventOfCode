def main():
    with open("day7_input.txt") as f:
        grid = f.read().splitlines()
        f.close()

    start_col_idx = grid[0].index("S")
    print(start_col_idx)
    beam_idxs = [start_col_idx]

    num_splits = 0

    for row in grid[1:]:
        while "^" in row:
            split_col_idx = row.index("^")
            if split_col_idx in beam_idxs:
                beam_idxs.remove(split_col_idx)
                if split_col_idx - 1 not in beam_idxs:
                    beam_idxs.append(split_col_idx - 1)
                if split_col_idx + 1 not in beam_idxs:
                    beam_idxs.append(split_col_idx + 1)
                row = row.replace("^", "*", 1)
            else:
                row = row.replace("^", "x", 1)
        print(row)
        num_splits += row.count("*")

    print(num_splits)


if __name__ == "__main__":
    main()
