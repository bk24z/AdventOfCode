with open("day6/day6_input.txt","r") as d6_input:
    rows = d6_input.read().splitlines()
    d6_input.close()

split_rows = [row.split() for row in rows]
# print(split_rows)
problems = list(zip(*split_rows))
total = 0

for problem in problems:
    *numbers, operator = problem
    # print(problem,numbers,operator)
    if operator == '*':
        answer = 1
        for num in numbers:
            answer *= int(num)
    elif operator == '+':
        answer = 0
        for num in numbers:
            answer += int(num)
    # print(answer)
    total += answer

print(total)