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


def dfs(matrix, start, visited):
    i, j = start
    if matrix[i][j] == 9:
        return 1
    visited.add(start)
    total_trails = 0
    for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= i2 < len(matrix) and 0 <= j2 < len(matrix[0]) and (i2, j2) not in visited and matrix[i2][j2] == matrix[i][j] + 1:
            total_trails += dfs(matrix, (i2, j2), visited)
    visited.remove(start)
    return total_trails

# def bfs(matrix, start):
#     queue = deque([start])
#     visited = set([start])
#     reachable_nines = set()

#     while queue:
#         i, j = queue.popleft()
#         if matrix[i][j] == 9:
#             reachable_nines.add((i, j))
#             continue
        
#         for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
#             if 0 <= i2 < len(matrix)  and 0 <= j2 < len(matrix[0]):
#                 if (i2, j2) not in visited and matrix[i2][j2] == matrix[i][j] + 1:
#                     queue.append((i2, j2))
#                     visited.add((i2, j2))

#     return len(reachable_nines)

total_rating = 0
for trailhead in trailheads:
    total_rating += dfs(map, trailhead, set())
print(total_rating)