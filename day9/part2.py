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

while blocks[-1] is None:
    blocks.pop()
last_index = blocks[-1]


for number in range(last_index, -1, -1):
    start_index = None
    end_index = None

    for i, num in enumerate(blocks):
        if num == number:
            if start_index is None:
                start_index = i
            end_index = i
        elif start_index is not None:  # Exit early since the list is ordered
            break
    temp = blocks[start_index:end_index+1]
    temp_len = end_index - start_index + 1
    for j in range(start_index):
        if blocks[j:j+temp_len] == [None]*temp_len:
            blocks = blocks[:j] + temp + blocks[j+temp_len:]
            blocks[start_index:end_index+1] = [None]*temp_len
            break

total = 0
for index, value in enumerate(blocks):
    if value is not None:
        total += index*value

print(total)