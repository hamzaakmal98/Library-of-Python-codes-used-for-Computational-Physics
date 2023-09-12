import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
C = A + B
print("Matrix addition: \n", C)

# Matrix subtraction
C = A - B
print("Matrix subtraction: \n", C)

# Matrix multiplication
C = A.dot(B)
print("Matrix multiplication: \n", C)

# Matrix transpose
C = A.T
print("Matrix transpose of A: \n", C)

# Matrix inverse
C = np.linalg.inv(A)
print("Matrix inverse of A: \n", C)

# Matrix determinant
C = np.linalg.det(A)
print("Matrix determinant of A: \n", C)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A: \n", eigenvalues)
print("Eigenvectors of A: \n", eigenvectors)
