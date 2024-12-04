column1 = []
column2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))
column1.sort()
column2.sort()


differences = [abs(column1[i] - column2[i]) for i in range(len(column1))]

print(sum(differences))
