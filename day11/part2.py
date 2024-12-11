from collections import defaultdict

with open('input.txt', 'r') as file:
    for line in file:
        stones = list(map(int, line.strip().split(' ')))

stone_counts = defaultdict(int)
for stone in stones:
    stone_counts[stone] += 1
print(stone_counts)

for i in range(75):
    new_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            half_len = len(str(stone)) // 2
            left = int(str(stone)[:half_len])
            right = int(str(stone)[half_len:])
            new_counts[left] += count
            new_counts[right] += count
        else:
            new_counts[stone * 2024] += count
    stone_counts = new_counts

total_stones = sum(stone_counts.values())
print("length is", total_stones)
