with open("day5/day5_input.txt","r") as d5_input:
    d5_input_list = d5_input.read().splitlines()
    print("Read d5_input")
    split_index = d5_input_list.index('') # Find the index of the empty string
    # Split into two lists
    id_range_strs = d5_input_list[:split_index]
    id_strs = d5_input_list[split_index + 1:]
    print("Split to lists")
    d5_input.close()

new_ranges = []
previous_ranges = []
previous_ranges_check = []

for id_range_str in id_range_strs:
    new_ranges.append(tuple(map(int, id_range_str.split("-"))))

new_ranges.sort()
# print(new_ranges)
# print()

while new_ranges != previous_ranges_check:
    previous_ranges = new_ranges.copy()
    previous_ranges_check = new_ranges.copy()
    new_ranges = []
    while previous_ranges != []:
        if len(previous_ranges) == 1:
            new_ranges.append(previous_ranges.pop(0))
        else:
            id_range_1 = previous_ranges.pop(0)
            id_range_2 = previous_ranges.pop(0)
            if id_range_1[0] <= id_range_2[1] and id_range_2[0] <= id_range_1[1]:
                new_ranges.append((
                    min(id_range_1[0],id_range_2[0]),
                    max(id_range_1[1],id_range_2[1])
                ))
            else:
                new_ranges.append(id_range_1)
                previous_ranges.insert(0,id_range_2)
    new_ranges.sort()
    # print(previous_ranges, previous_ranges_check, new_ranges)
    # print()

print(new_ranges)
print("Optimised ranges")

fresh_ids = []
num_fresh_ids = 0

for id_range in new_ranges:
    num_fresh_ids += (id_range[1] + 1) - id_range[0]

# print(fresh_id_range)
fresh_ids = list(set(fresh_ids))
print("Calculated fresh IDs")

print(num_fresh_ids)