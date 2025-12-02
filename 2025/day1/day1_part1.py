import math

current_pos = 50
password = 0
multiplier = 1

with open("day1_input.txt","r") as p1_input:
    rotations = p1_input.read().splitlines()
    for rotation in rotations:
        direction = rotation[0]
        distance = abs(int(rotation[1:]))%100
        if direction == "L":
            multiplier = -1
        elif direction == "R":
            multiplier = 1
        else:
            pass
        previous_pos = current_pos
        current_pos = current_pos + multiplier*distance
        if current_pos < 0 or current_pos > 99:
            current_pos = current_pos - multiplier*100
        if current_pos == 0:
            password += 1
        print(previous_pos,multiplier*distance,current_pos)
    p1_input.close()

print("Password:",password)