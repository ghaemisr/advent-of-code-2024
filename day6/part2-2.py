from copy import deepcopy

# Parse the map and find the guard's starting position
def parse_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

    directions = ['^', 'v', '<', '>']
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return grid, (i, j, cell)
    return grid, None

# Simulate the guard's patrol
def simulate_guard(grid, start_state):
    path = []  # Store the sequence of states (row, col, direction)
    seen_paths = set()  # Set of all encountered prefixes of the path
    row, col, direction = start_state

    # Movement rules
    deltas = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    while True:
        # Track the current state
        current_state = (row, col, direction)
        path.append(current_state)

        # Check for loops by detecting repeated sequences in the path
        path_tuple = tuple(path)
        if path_tuple in seen_paths:
            return True  # Loop detected
        seen_paths.add(path_tuple)

        # Determine the next position
        next_row, next_col = row + deltas[direction][0], col + deltas[direction][1]

        # Check if the guard exits the grid
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return False  # Guard exits the map

        # Handle movement
        if grid[next_row][next_col] == '.':
            row, col = next_row, next_col  # Move forward
        elif grid[next_row][next_col] == '#':
            direction = turns[direction]  # Turn right
        else:
            return False  # Guard hits an invalid state or edge

# Find positions where placing an obstacle creates a loop
def find_loop_positions(grid, start_state):
    loop_positions = set()

    # Iterate through all positions in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Only consider open positions
            if grid[row][col] == '.' and (row, col) != (start_state[0], start_state[1]):
                # Place a temporary obstacle
                temp_grid = deepcopy(grid)
                temp_grid[row][col] = '#'

                # Check if the guard loops with this obstacle
                if simulate_guard(temp_grid, start_state):
                    loop_positions.add((row, col))

    return loop_positions

# Parse input and find the solution
file_path = 'input.txt'
grid, start_state = parse_input(file_path)
loop_positions = find_loop_positions(grid, start_state)

# Output the results
print(f"Number of loop-causing positions: {len(loop_positions)}")
# print(f"Loop-causing positions: {sorted(loop_positions)}")
