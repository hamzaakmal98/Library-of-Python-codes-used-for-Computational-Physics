def lower_triangular(matrix):
    """
    Returns the lower triangular matrix of a given 3x3 matrix.
    """
    n = len(matrix)
    lower = [[0 for x in range(n)] for y in range(n)]

    # Computing lower triangular matrix
    for i in range(n):
        for j in range(n):
            if i >= j:
                lower[i][j] = matrix[i][j]

    return lower


# Example test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lower = lower_triangular(matrix)
print("Original Matrix:\n", matrix)
print("Lower Triangular Matrix:\n", lower)
