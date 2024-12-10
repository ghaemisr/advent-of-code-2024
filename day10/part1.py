from collections import deque

map = []

with open('input.txt', 'r') as file:
    for line in file:
        map.append([int(char) for char in line.strip()])

print(''.join([''.join(f"{row}") + '\n' for row in map]))

trailheads = []

for i, row in enumerate(map):
    for j, cell in enumerate(row):
        if cell == 0:
            trailheads.append((i, j))
print(trailheads)


def bfs(matrix, start):
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()

    while queue:
        i, j = queue.popleft()
        if matrix[i][j] == 9:
            reachable_nines.add((i, j))
            continue
        
        for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= i2 < len(matrix)  and 0 <= j2 < len(matrix[0]):
                if (i2, j2) not in visited and matrix[i2][j2] == matrix[i][j] + 1:
                    queue.append((i2, j2))
                    visited.add((i2, j2))

    return len(reachable_nines)

total_score = 0
for trailhead in trailheads:
    total_score += bfs(map, trailhead)
print(total_score)