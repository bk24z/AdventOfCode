import math

# current_pos = 50
current_pos = 50
password = 0
multiplier = 1

with open("day1_input.txt","r") as p1_input:
    rotations = p1_input.read().splitlines()
    for rotation in rotations:
        direction = rotation[0]
        original_distance = int(rotation[1:])
        distance = original_distance%100
        if direction == "L":
            multiplier = -1
        elif direction == "R":
            multiplier = 1
        else:
            pass
        previous_pos = current_pos
        current_pos = previous_pos + multiplier*distance
        # print(current_pos)
        if current_pos < 0 or current_pos > 99:
            print("Out of bounds")
            current_pos = current_pos - multiplier*100
            if previous_pos != 0:
                password += 1
                print("Crossed 0 once")
        elif current_pos == 0:
            print("Equals 0, crossed 0 once")
            password += 1
        if original_distance > 99:
            extra_crosses = math.floor(original_distance/100)
            print(f"Crossed 0 {extra_crosses} times")
            password += extra_crosses
        print(previous_pos,multiplier*distance,current_pos)
        print(f"Password: {password}")
    p1_input.close()

print("Final password:",password)