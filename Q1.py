def upper_triangular(matrix):
    n = len(matrix)
    upper = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                upper[i][j] = matrix[i][j]
    return upper


def lower_triangular(matrix):
    n = len(matrix)
    lower = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if i >= j:
                lower[i][j] = matrix[i][j]
    return lower


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

upper = upper_triangular(matrix)
lower = lower_triangular(matrix)
print("Original Matrix:\n", matrix)
print("Upper Triangular Matrix:\n", upper)
print("Lower Triangular Matrix:\n", lower)

matrix2 = [[7, 0, -1],
           [0, -2, 5],
           [0, 0, 8]]
upper = upper_triangular(matrix2)
lower = lower_triangular(matrix2)
print("Original Matrix:\n", matrix2)
print("Upper Triangular Matrix:\n", upper)
print("Lower Triangular Matrix:\n", lower)

matrix3 = [[7, 1, ],
           [6, -2, ]]
upper = upper_triangular(matrix3)
lower = lower_triangular(matrix3)
print("Original Matrix:\n", matrix3)
print("Upper Triangular Matrix:\n", upper)
print("Lower Triangular Matrix:\n", lower)
