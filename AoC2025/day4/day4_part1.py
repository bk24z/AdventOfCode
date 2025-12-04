import itertools

with open("day4/day4_input.txt","r") as d4_input:
    grid = [list(row) for row in d4_input.read().splitlines()]
    d4_input.close()

# print(grid)

row_length = len(grid[0])
column_length = len(grid)
row_start = column_start = 0
row_end = row_length-1
column_end = column_length-1

num_of_accessible_rolls = 0

def rolls_above(grid,row_index,roll_index):
    if row_index-1 < 0:
        return []
    else:
        rolls = grid[row_index-1][max(0,roll_index-1):min(roll_index+1,row_end)+1]
        # print(rolls)
        # print(grid[row_index][roll_index])
        return rolls
    
def rolls_below(grid,row_index,roll_index):
    if row_index+1 > column_end:
        return []
    else:
        rolls = grid[row_index+1][max(0,roll_index-1):min(roll_index+1,row_end)+1]
        # print(rolls)
        # print(grid[row_index][roll_index])
        return rolls
    
def roll_left(grid,row_index,roll_index):
    if roll_index-1 < 0:
        return []
    else:
        roll = grid[row_index][min(roll_index-1,row_end)]
        # print(roll)
        # print(grid[row_index][roll_index])
        return roll

def roll_right(grid,row_index,roll_index):
    if roll_index+1 > row_end:
        return []
    else:
        roll = grid[row_index][roll_index+1]
        # print(roll)
        # print(grid[row_index][roll_index])
        return roll

for row_index, row in enumerate(grid):
    for roll_index, roll in enumerate(row):
        if roll == "@":
            parameters = (grid,row_index,roll_index)
            adjacent_rolls = list(itertools.chain(
                (rolls_above(*parameters)),
                rolls_below(*parameters),
                roll_left(*parameters),
                roll_right(*parameters),
            ))
            # print(adjacent_rolls)
            if adjacent_rolls.count("@") < 4:
                num_of_accessible_rolls += 1

print(num_of_accessible_rolls)
# test_roll = (grid,column_end-1,row_end-1)

# roll_right(*test_roll)