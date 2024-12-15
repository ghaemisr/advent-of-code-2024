robots = []

with open('input.txt', 'r') as file:
    machine = {}
    for line in file:
        line = line.strip().split(' ')
        # parse int the tuple
        position = tuple(map(int, line[0].split('=')[1].split(',')))
        velocity = tuple(map(int, line[1].split('=')[1].split(',')))
        robots.append({
            'p': position,
            'v': velocity
        })
print(robots)

# 7x11 grid
# 0,0 is top left
len_x = 11
len_y = 7
initial_map = [[0 for _ in range(11)] for _ in range(7)]

for robot in robots:
    initial_map[robot['p'][1]][robot['p'][0]] += 1

print('\n')
for point in initial_map:
    print(point, '\n')

# move the robots for 100 seconds
for _ in range(100):
    for robot in robots:
        new_x = (robot['p'][0] + robot['v'][0]) % len_x
        new_y = (robot['p'][1] + robot['v'][1]) % len_y

        robot['p'] = (new_x, new_y)

final_map = [[0 for _ in range(len_x)] for _ in range(len_y)]
for robot in robots:
    print(robot)
    final_map[robot['p'][1]][robot['p'][0]] += 1


print('\n')
for point in final_map:
    print(point, '\n')

# first quarter
q1_start = (0, 0)
q1_end = (len_x // 2 - 1, len_y // 2 - 1)
print(q1_start, q1_end)

# total number of points in the first quarter
q1_count = 0
for i in range(q1_start[1], q1_end[1] + 1):
    for j in range(q1_start[0], q1_end[0] + 1):
        q1_count += final_map[i][j]
print(q1_count)

# second quarter
q2_start = (len_x // 2 + 1, 0)
q2_end = (len_x - 1, len_y // 2 - 1)
print(q2_start, q2_end)

# total number of points in the second quarter
q2_count = 0
for i in range(q2_start[1], q2_end[1] + 1):
    for j in range(q2_start[0], q2_end[0] + 1):
        q2_count += final_map[i][j]

# third quarter
q3_start = (0, len_y // 2 + 1)
q3_end = (len_x // 2 - 1, len_y - 1)
print(q3_start, q3_end)

# total number of points in the third quarter
q3_count = 0
for i in range(q3_start[1], q3_end[1] + 1):
    for j in range(q3_start[0], q3_end[0] + 1):
        q3_count += final_map[i][j]

# fourth quarter
q4_start = (len_x // 2 + 1, len_y // 2 + 1)
q4_end = (len_x - 1, len_y - 1)
print(q4_start, q4_end)

# total number of points in the fourth quarter
q4_count = 0
for i in range(q4_start[1], q4_end[1] + 1):
    for j in range(q4_start[0], q4_end[0] + 1):
        q4_count += final_map[i][j]

print(q1_count, q2_count, q3_count, q4_count)
print(q1_count * q2_count * q3_count * q4_count)
