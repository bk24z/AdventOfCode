total_output = 0
with open("day3_input.txt","r") as d3_input:
    banks = d3_input.read().splitlines()
    for bank in banks:
        highest_joltage = 0
        batteries = list(bank)
        # print(batteries)
        for b_index, i in enumerate(batteries):
            # print(b_index,i)
            for j in batteries[b_index+1:]:
                joltage = int(i+j)
                # print(joltage)
                if joltage > highest_joltage:
                    highest_joltage = joltage
        total_output += highest_joltage

print(total_output)