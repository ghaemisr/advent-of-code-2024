from copy import deepcopy

original_map = []

with open('input.txt', 'r') as file:
    for line in file:
        original_map.append(list(line.strip()))
print(original_map)
def find_character(matrix, char):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == char:
                return (i, j)

chars = ['^', 'v', '<', '>']
for char in chars:
    position = find_character(original_map, char)
    if position:
        break
original_position = position
print(position)

no_obstacle_chars = ['.', '|', '-', '+']

def traverse_map(map, start_position):
    new_map = deepcopy(map)

    visited_states = set()
    in_map = True

    while in_map:
        no_obstacle = True
        while no_obstacle:
            # current_state = (start_position[0], start_position[1], new_map[start_position[0]][start_position[1]])
        
            # # Check if this state has been visited before
            # if current_state in visited_states:
            #     return True, new_map  # Guard is in a loop
            # visited_states.add(current_state)


            next = None
            if new_map[start_position[0]][start_position[1]] == '^':
                next = (start_position[0] - 1, start_position[1])
            elif new_map[start_position[0]][start_position[1]] == 'v':
                next = (start_position[0] + 1, start_position[1])
            elif new_map[start_position[0]][start_position[1]] == '<':
                next = (start_position[0], start_position[1] - 1)
            elif new_map[start_position[0]][start_position[1]] == '>':
                next = (start_position[0], start_position[1] + 1)
            if next[0] < 0 or next[0] >= len(new_map) or next[1] < 0 or next[1] >= len(new_map[0]):
                in_map = False
                no_obstacle = False
                if cur_char == '^' or cur_char == 'v':
                    new_map[start_position[0]][start_position[1]] = '|'
                else:
                    new_map[start_position[0]][start_position[1]] = '-'
                start_position = next
                return False, new_map
            elif new_map[next[0]][next[1]] == '|' and (new_map[start_position[0]][start_position[1]] == '^' or new_map[start_position[0]][start_position[1]] == 'v'):
                return True, new_map
            elif new_map[next[0]][next[1]] == '-' and (new_map[start_position[0]][start_position[1]] == '<' or new_map[start_position[0]][start_position[1]] == '>'):
                return True, new_map
            
            if new_map[next[0]][next[1]] in no_obstacle_chars:
                no_obstacle = True
                cur_char = new_map[start_position[0]][start_position[1]]
                if cur_char == '^' or cur_char == 'v':
                    new_map[start_position[0]][start_position[1]] = '|'
                else:
                    new_map[start_position[0]][start_position[1]] = '-'
                start_position = next
                new_map[start_position[0]][start_position[1]] = cur_char
            else:
                no_obstacle = False
                curr_char = new_map[start_position[0]][start_position[1]]
                new_map[start_position[0]][start_position[1]] = '+'
                new_position = ()
                new_direction = ''
                if curr_char == '^':
                    new_position = (start_position[0], start_position[1] + 1)
                    new_direction = '>'
                elif curr_char == 'v':
                    new_position = (start_position[0], start_position[1] - 1)
                    new_direction = '<'
                elif curr_char == '<':
                    new_position = (start_position[0] - 1, start_position[1])
                    new_direction = '^'
                elif curr_char == '>':
                    new_position = (start_position[0] + 1, start_position[1])
                    new_direction = 'v'
                new_map[new_position[0]][new_position[1]] = new_direction
                start_position = new_position
                # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in map]))

count = 0
for i_index, i in enumerate(original_map):
    for j_index, j in enumerate(i):
        if (i_index, j_index) != original_position and original_map[i_index][j_index] == '.':
            temp_map = deepcopy(original_map)
            temp_map[i_index][j_index] = '#'  # Place obstacle
            is_loop, _ = traverse_map(temp_map, original_position)
            if is_loop:
                count += 1

            
print(count)
     