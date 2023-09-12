# Define two vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Define a scalar
scalar = 2

# Define a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Define a function to add two vectors
def add_vectors(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result

# Define a function to multiply a vector by a scalar
def scalar_multiply(scalar, vector):
    result = []
    for i in range(len(vector)):
        result.append(scalar * vector[i])
    return result

# Define a function to multiply a matrix by a vector
def matrix_vector_multiply(matrix, vector):
    result = []
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix[0])):
            row_sum += matrix[i][j] * vector[j]
        result.append(row_sum)
    return result

# Define a function to multiply two matrices
def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element_sum = 0
            for k in range(len(matrix2)):
                element_sum += matrix1[i][k] * matrix2[k][j]
            row.append(element_sum)
        result.append(row)
    return result

# Test the functions
print(add_vectors(vector1, vector2))         # Output: [5, 7, 9]
print(scalar_multiply(scalar, vector1))      # Output: [2, 4, 6]
print(matrix_vector_multiply(matrix, vector1))# Output: [14, 32, 50]
print(matrix_multiply(matrix, matrix))       # Output: [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
