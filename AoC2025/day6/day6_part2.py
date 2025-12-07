from itertools import zip_longest, chain
import math

with open("day6/day6_input.txt","r") as d6_input:
    rows = d6_input.read().splitlines()
    d6_input.close()

# problems = list(zip(*split_rows))

row_length = len(rows[0])
column_length = len(rows)
print(row_length,column_length)
rows = [row.ljust(row_length) for row in rows]
# print(rows)
columns = []
for column_idx in range(row_length):
    column = [row[column_idx] for row in rows]
    columns.append(column)
    # print(f"column {column_idx}: {column}")
# print(columns)

total = 0
separator = [' ' for _ in range(column_length)]
print(separator)

while columns != []:
    # print(columns)
    c_column = None
    c_problem = []
    while c_column != separator and columns != []:
        c_column = columns.pop(0)
        # print(c_column)
        # print(len(columns))
        if c_column != separator:
            c_problem.append(c_column)
            if separator not in columns:
                c_problem = c_problem + columns
                columns = []
                break
    # print(c_problem)
    
    operator = None
    nums = []

    for num_list in c_problem:
        if '+' in num_list:
            operator = '+'
            num_list.remove(operator)
        elif '*' in num_list:
            operator = '*'
            num_list.remove(operator)
        # print(num_list)
        num_str = "".join(num_list).strip()
        # print(num_str)
        num = int(num_str)
        nums.append(num) 
    
    # print(nums,operator)

    if operator == '*':
        answer = math.prod(nums)
    elif operator == '+':
        answer = sum(nums)
    
    # print(answer)
    total += answer

print(total)