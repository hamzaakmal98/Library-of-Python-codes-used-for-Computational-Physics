def upper_triangular(matrix):
    """
    Returns the upper triangular matrix of a given 3x3 matrix.
    """
    n = len(matrix)
    upper = [[0 for x in range(n)] for y in range(n)]

    # Computing upper triangular matrix
    for i in range(n):
        for j in range(n):
            if i <= j:
                upper[i][j] = matrix[i][j]

    return upper


# Example test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
upper = upper_triangular(matrix)
print("Original Matrix:\n", matrix)
print("Upper Triangular Matrix:\n", upper)
