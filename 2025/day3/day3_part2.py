total_output = 0
with open("day3_input.txt","r") as d3_input:
    # banks = [d3_input.read().splitlines()[2]]
    banks = d3_input.read().splitlines()
    bank_length = len(banks[0])
    num_to_remove = bank_length - 12
    for bank in banks:
        batteries = list(bank)
        remaining = 12
        result = []
        start_index = 0
        while remaining > 0:
            search_end = bank_length - remaining
            max_digit = -1
            max_index = -1
            for i in range(start_index, search_end + 1):
                if int(batteries[i]) > max_digit:
                    max_digit = int(batteries[i])
                    max_index = i
            print(f"Position {12-remaining}: searching [{start_index}:{search_end+1}], found {max_digit} at index {max_index}")
            max_digit_str = str(max_digit)
            result.append(max_digit_str)
            remaining -= 1
            start_index = max_index + 1
        print(result)
        total_output += int("".join(result))
        print(total_output)


                


# print(total_output)