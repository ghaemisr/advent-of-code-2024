import re

reports = []

with open("input.txt", "r") as f:
    content = f.read()

mul_list = re.finditer(r"mul\(\d+,\d+\)", content)

actions_list = [(0,1)]

do_list = re.finditer(r"do\(\)", content)
do_indexes = [(i.span()[0], 1) for i in do_list]
actions_list.extend(do_indexes)

do_not_list = re.finditer(r"don't\(\)", content)
do_not_indexes = [(i.span()[0], 0) for i in do_not_list]
actions_list.extend(do_not_indexes)

actions_list = sorted(actions_list)

res = 0
curr_action_index = 0
for item in mul_list:
    if curr_action_index + 1 < len(actions_list) and item.span()[0] >= actions_list[curr_action_index+1][0]:
        curr_action_index += 1
    if actions_list[curr_action_index][1]:
        nums = item.group()[4:-1].split(',')
        res += int(nums[0]) * int(nums[1])

print(res)
