rules = {}

with open('rules.txt', 'r') as file:
    for line in file:
        nums = line.split('|')
        temp = int(nums[0])
        if temp in rules:
            rules[temp].append(int(nums[1]))
        else:
            rules[temp] = [int(nums[1])]

updates = []
with open('updates.txt', 'r') as file:
    for line in file:
        nums = line.split(',')
        updates.append([int(i) for i in nums])

incorrectUpdates = []

for update in updates:
    is_correct = True
    for index, num in enumerate(update):
        if num in rules:
            for i in rules[num]:
                if i in update and i in update[:index]:
                    is_correct = False

    if not is_correct:
        incorrectUpdates.append(update)

def custom_sort_key(page, update, rules):
    count = 0
    for other in update:
        if page in rules and other in rules[page]:
            count += 1
    return count


middle_pages_sum = 0

for update in incorrectUpdates:
    sorted_update = sorted(update, key=lambda page: custom_sort_key(page, update, rules))
    middle_page = sorted_update[len(sorted_update) // 2]
    middle_pages_sum += middle_page

print(middle_pages_sum)
