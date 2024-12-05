matrix = []

with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1)
]

valid_words = [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]

count = 0
num_rows = len(matrix)
num_columns = len(matrix[0])
for i in range(num_rows):
    for j in range(num_columns):
        for dir_i, dir_j in directions:
            if 0 <= i + 3 * dir_i < num_rows and 0 <= j + 3 * dir_j < num_columns:
                words = [matrix[i + dir_i * a][j + dir_j * a]
                         for a in range(4)]
                if words in valid_words:
                    count += 1
print(count)
