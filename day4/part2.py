matrix = []

with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

valid_words = [['M', 'A', 'S'], ['S', 'A', 'M']]

count = 0
num_rows = len(matrix)
num_columns = len(matrix[0])
for i in range(num_rows):
    for j in range(num_columns):
        if 0 <= i + 2 < num_rows and 0 <= j + 2 < num_columns:
            words1 = [matrix[i + a][j + a] for a in range(3)]
            words2 = [matrix[i + 2][j], matrix[i + 1][j + 1], matrix[i][j + 2]]

            if words1 in valid_words and words2 in valid_words:
                count += 1
print(count)
