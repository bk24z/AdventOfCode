import itertools

with open("day4/day4_input.txt","r") as d4_input:
    grid = [list(row) for row in d4_input.read().splitlines()]
    d4_input.close()

# print(grid)

row_length = len(grid[0])
column_length = len(grid)
row_end = row_length-1 # Last valid index of any row
column_end = column_length-1 # Last valid index of any column

num_of_accessible_rolls = 1
num_of_removable_rolls = 0

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

while num_of_accessible_rolls > 0:
    num_of_accessible_rolls = 0
    for row_index, row in enumerate(grid):
        for roll_index, roll in enumerate(row):
            if roll == "@": # If a roll is present in that space
                parameters = (grid,row_index,roll_index)
                adjacent_rolls = list(itertools.chain(
                    rolls_above(*parameters),
                    rolls_below(*parameters),
                    roll_left(*parameters),
                    roll_right(*parameters),
                )) # Combine all of the adjacent rolls into one list
                # print(adjacent_rolls)
                if adjacent_rolls.count("@") < 4: # If there are less than 4 adjacent rolls, the roll is accessible
                    num_of_accessible_rolls += 1
                    grid[row_index][roll_index] = "." # Remove the roll
                    num_of_removable_rolls += 1
    # print(grid)
    print(num_of_accessible_rolls)

print("Removable:",num_of_removable_rolls)