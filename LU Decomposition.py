import numpy as np

# define a test matrix
A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

# calculate the LU decomposition of A using scipy.linalg.lu_factor()
from scipy.linalg import lu_factor
lu, piv = lu_factor(A)

# calculate the inverse of A using the LU decomposition
from scipy.linalg import lu_solve
A_inv = lu_solve((lu, piv), np.identity(len(A)))

# print the inverse of A
print("The inverse of A using LU decomposition is:")
print(A_inv)

# calculate the determinant of A using the LU decomposition
det_A = np.prod(np.diag(lu)) * np.prod(np.diag(np.identity(len(A)))) # The determinant of A is equal to the product of the diagonal elements of U.
if piv[-1] != len(A): # Check if the number of row swaps performed during pivoting was even or odd.
    det_A = -det_A
print("The determinant of A using LU decomposition is:", det_A)

# calculate the inverse and determinant of A using numpy functions
A_inv_np = np.linalg.inv(A)
det_A_np = np.linalg.det(A)
print("The inverse of A using numpy.linalg.inv() is:")
print(A_inv_np)
print("The determinant of A using numpy.linalg.det() is:", det_A_np)

# compare the results
print("LU decomposition and numpy.linalg.inv() give the same inverse?", np.allclose(A_inv, A_inv_np))
print("LU decomposition and numpy.linalg.det() give the same determinant?", np.isclose(det_A, det_A_np))
