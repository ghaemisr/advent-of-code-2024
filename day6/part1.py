
map = []

with open('input.txt', 'r') as file:
    for line in file:
        map.append(list(line.strip()))
print(map)
def find_character(matrix, char):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == char:
                return (i, j)

chars = ['^', 'v', '<', '>']
for char in chars:
    position = find_character(map, char)
    if position:
        break
print(position)

in_map = True

while in_map:
    no_obstacle = True
    while no_obstacle:
        
        next = None
        if map[position[0]][position[1]] == '^':
            next = (position[0] - 1, position[1])
        elif map[position[0]][position[1]] == 'v':
            next = (position[0] + 1, position[1])
        elif map[position[0]][position[1]] == '<':
            next = (position[0], position[1] - 1)
        elif map[position[0]][position[1]] == '>':
            next = (position[0], position[1] + 1)
        if next[0] < 0 or next[0] >= len(map) or next[1] < 0 or next[1] >= len(map[0]):
            in_map = False
            no_obstacle = False
            map[position[0]][position[1]] = 'X'
            position = next
            break
        if map[next[0]][next[1]] == '.' or map[next[0]][next[1]] == 'X':
            no_obstacle = True
            cur_char = map[position[0]][position[1]]
            map[position[0]][position[1]] = 'X'
            position = next
            map[position[0]][position[1]] = cur_char
        else:
            no_obstacle = False
            curr_char = map[position[0]][position[1]]
            map[position[0]][position[1]] = 'X'
            new_position = ()
            new_direction = ''
            if curr_char == '^':
                new_position = (position[0], position[1] + 1)
                new_direction = '>'
            elif curr_char == 'v':
                new_position = (position[0], position[1] - 1)
                new_direction = '<'
            elif curr_char == '<':
                new_position = (position[0] - 1, position[1])
                new_direction = '^'
            elif curr_char == '>':
                new_position = (position[0] + 1, position[1])
                new_direction = 'v'
            map[new_position[0]][new_position[1]] = new_direction
            position = new_position
            # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in map]))

count_x = 0
for i in map:
    for j in i:
        if j == 'X':
            count_x += 1
print(count_x)