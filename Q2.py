import math
import numpy as np


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


matrix = [[1, 1], [1, 0]]
newMatrix = [[1, 1], [1, 0]]
print("Here are the first few Fibonacci numbers: \n")
print(matrix[0][0])
print(newMatrix[0][0])

for i in range(10):
    newMatrix = matrix_multiply(newMatrix, matrix)
    print(newMatrix[0][0])

print("\n Here are the Eigen Values and Eigen Vectors of The Matrix F")
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues of F: \n", eigenvalues)
print("Eigenvectors of F: \n", eigenvectors, "\n")

term = 1100
fibonacci = int(matrix_multiply(matrix_multiply(eigenvectors,
np.diag([eigenvalues[0] ** term, eigenvalues[1] ** term])),eigenvectors.T)[0][1])

print("The 1100th Fibonacci number is: ", fibonacci)
