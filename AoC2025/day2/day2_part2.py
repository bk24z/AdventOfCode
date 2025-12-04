import re

p_input = "78847-119454,636-933,7143759788-7143793713,9960235-10043487,44480-68595,23468-43311,89-123,785189-1014654,3829443354-3829647366,647009-692765,2-20,30-42,120909-197026,5477469-5677783,9191900808-9191943802,1045643-1169377,46347154-46441299,2349460-2379599,719196-779497,483556-641804,265244-450847,210541-230207,195-275,75702340-75883143,58-84,2152-3237,3367-5895,1552-2029,9575-13844,6048-8966,419388311-419470147,936-1409,9292901468-9292987321"
#p_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

all_ids = []

split_input = p_input.split(",")

for id_range_str in split_input:
    id_range = id_range_str.split("-")
    all_ids.extend([i for i in range(int(id_range[0]),int(id_range[1])+1)])

valid_ids = all_ids.copy()
invalid_ids = []
invalid_pattern = r"^(.+)\1{1,}$"

# print(valid_ids)

for id in all_ids:
    # print(id)
    id_str = str(id)
    matches = re.findall(invalid_pattern,id_str)
    # print(matches)
    if matches != []:
        valid_ids.remove(id)
        invalid_ids.append(id)

invalid_sum = sum(invalid_ids)

# print(split_input)
# print(all_ids)
# print(valid_ids)
# print(invalid_ids)
print(invalid_sum)