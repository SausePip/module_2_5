def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)

        matrix.append(row)

    return matrix

n = 3
m = 3
value = 5

Matrix = get_matrix(n, m, value)
for row in Matrix:
    print(row)

