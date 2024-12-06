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

correctUpdates = []

for update in updates:
    is_correct = True
    for index, num in enumerate(update):
       
        if num in rules:
            for i in rules[num]:
                if i in update and i in update[:index]:
                    is_correct = False
                    break
        if not is_correct:
            break

    if is_correct:
        correctUpdates.append(update)

sum = 0
for update in correctUpdates:
    # find middle number
    middle = update[len(update) // 2]
    sum += middle

print(sum)