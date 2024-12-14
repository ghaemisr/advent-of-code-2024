machines = []

with open('input.txt', 'r') as file:
    machine = {}
    for line in file:
        if line == '\n':
            machines.append(machine)
            machine = {}
            continue
        line = line.strip().split(': ')
        values = line[1].split(', ')
        if line[0] == 'Button A':   
            machine['A'] = (int(values[0].split('+')[1]), int(values[1].split('+')[1]))
        elif line[0] == 'Button B':
            machine['B'] = (int(values[0].split('+')[1]), int(values[1].split('+')[1]))
        elif line[0] == 'Prize':
            machine['P'] = (int(values[0].split('=')[1]), int(values[1].split('=')[1]))
    if machine:
        machines.append(machine)

total_cost = 0
for machine in machines:

    C = machine['A'][1] * machine['B'][0] - machine['B'][1] * machine['A'][0]
    D = machine['P'][1] * machine['B'][0] - machine['B'][1] * machine['P'][0]

    if C == 0 or D % C != 0:
        continue
    
    a = D // C

    if (machine['P'][0] - machine['A'][0] * a) % machine['B'][0] != 0:
        continue

    b = (machine['P'][0] - machine['A'][0] * a) // machine['B'][0]

    if a < 0 or b < 0:
        continue

    # Calculate cost
    result = a * 3 + b * 1

    if result is not None:
        print(f"Worked! Cost: {result}")
        total_cost += result
    else:
        print("No solution for this machine.")

print(f"Total cost: {total_cost}")
