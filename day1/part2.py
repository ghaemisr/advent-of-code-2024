column1 = []
column2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))


similarity = [column2.count(column1[i]) * column1[i] for i in range(len(column1))]

print(sum(similarity))
