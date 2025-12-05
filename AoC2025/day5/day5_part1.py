with open("day5/day5_input.txt","r") as d5_input:
    d5_input_list = d5_input.read().splitlines()
    print("Read d5_input")
    split_index = d5_input_list.index('') # Find the index of the empty string
    # Split into two lists
    id_range_strs = d5_input_list[:split_index]
    id_strs = d5_input_list[split_index + 1:]
    print("Split to lists")
    d5_input.close()

fresh_id_ranges = []
# fresh_ids = []
# spoiled_ids = []
num_fresh_ids = 0

for id_range_str in id_range_strs:
    id_range = tuple(id_range_str.split("-"))
    print(id_range)
    fresh_id_ranges.append(id_range)

# print(fresh_id_range)
print("Calculated fresh ranges")
# print(fresh_id_range)

for id_str in id_strs:
    id = int(id_str)
    for id_range in fresh_id_ranges:
        start = int(id_range[0])
        end = int(id_range[1])
        if id in range(start,end+1):
            # fresh_ids.append(id)
            num_fresh_ids += 1
            break
        # else:
        #     spoiled_ids.append(id)

# print(fresh_ids)
# print(spoiled_ids)
# print(len(fresh_ids))
print(num_fresh_ids)