import re

reports = []
content = open("input.txt", "r").read()
mul_list = re.findall(r"mul\(\d+,\d+\)", content)

res = 0
for item in mul_list:
    nums = item[4:-1].split(',')
    res += int(nums[0]) * int(nums[1])

print(res)
