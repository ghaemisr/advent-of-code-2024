input = []

with open('input.txt', 'r') as file:
    for line in file:
        input = [int(char) for char in line.strip()]

blocks = []
queue = []
for i in range(0, len(input), 2):
    nums = [int(i/2)]*input[i]
    blocks.extend(nums)
    queue.extend(nums)
    if i+1 < len(input):
        blocks.extend([None]*input[i+1])

len_nums = len(queue)
for index, value in enumerate(blocks):
    # print(index, value)
    if len(blocks) == len_nums:
        break
    if value is None:
        # print('pop', queue[-1])
        blocks[index] = queue.pop()
        blocks.pop()
        while blocks[-1] == None:
            blocks.pop()

total = 0
for index, value in enumerate(blocks):
    total += index*value

print(total)