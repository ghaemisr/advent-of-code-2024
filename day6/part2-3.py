def solve():
    import sys

    grid = [list(line.rstrip("\n")) for line in sys.stdin]
    R = len(grid)
    C = len(grid[0]) if R > 0 else 0

    # Find guard start and direction
    # Directions encoded as indices: 0=up,1=right,2=down,3=left
    dir_map = {'^':0, '>':1, 'v':2, '<':3}
    start_r = start_c = None
    start_d = None

    for r in range(R):
        for c in range(C):
            if grid[r][c] in dir_map:
                start_r, start_c = r, c
                start_d = dir_map[grid[r][c]]
                grid[r][c] = '.'  # replace guard symbol with floor
                break
        if start_r is not None:
            break

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    def in_bounds(r,c):
        return 0 <= r < R and 0 <= c < C

    # Function to simulate the guard's path
    # Returns (exited, visited_cells, visited_states_sequence) where:
    # - exited: True if guard left map, False if ended by detecting a loop (if we run a loop check)
    # - visited_cells: list of (r,c) visited in order
    # - final_state_reached: whether we got stuck in a loop or ended normally
    def simulate(map_grid, start_r, start_c, start_d, detect_loop=True):
        r, c, d = start_r, start_c, start_d
        visited_cells = []
        visited_states = set()

        while True:
            visited_cells.append((r,c))
            state = (r,c,d)
            if detect_loop:
                if state in visited_states:
                    # Loop detected
                    return (False, visited_cells)
                visited_states.add(state)

            # Check forward
            dr,dc = directions[d]
            fr,fc = r+dr, c+dc
            forward_blocked = True
            if in_bounds(fr,fc):
                if map_grid[fr][fc] != '#':
                    forward_blocked = False

            if forward_blocked:
                # turn right
                d = (d+1)%4
            else:
                # move forward
                r,c = fr,fc
                if not in_bounds(r,c):
                    # exited the map
                    return (True, visited_cells)

    # First, simulate without changes to find all visited cells
    _, visited_without_obst = simulate(grid, start_r, start_c, start_d, detect_loop=False)

    # Potential positions for the new obstruction:
    # - Must be visited by the guard
    # - Must not be the starting position
    # - Must be currently empty '.'
    candidates = []
    for (r,c) in visited_without_obst:
        if (r,c) != (start_r,start_c) and grid[r][c] == '.':
            candidates.append((r,c))

    # For each candidate, place an obstruction and check if loop occurs
    loop_count = 0
    for (cr,cc) in candidates:
        # Copy grid
        map_copy = [row[:] for row in grid]
        map_copy[cr][cc] = '#'

        # Simulate with loop detection
        exited, _ = simulate(map_copy, start_r, start_c, start_d, detect_loop=True)
        if not exited:
            # loop detected
            loop_count += 1

    print(loop_count)

solve()