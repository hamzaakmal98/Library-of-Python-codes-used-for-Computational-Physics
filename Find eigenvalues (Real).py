import numpy as np

# Define an mxm matrix
matrix = [[3, -2, 0], [4, -1, 0], [0, 1, 2]]

# Define a function to find the eigenvalues of an mxm matrix
def find_eigenvalues(matrix):
    m = len(matrix)
    # Calculate the characteristic polynomial of the matrix
    def poly(x):
        res = 1
        for i in range(m):
            res *= (matrix[i][i] - x)
        return res
    # Use the bisection method to find the roots of the characteristic polynomial
    def bisection(a, b, tol=1e-6):
        roots = []
        if poly(a) * poly(b) >= 0:
            return roots
        while (b - a) >= tol:
            c = (a + b) / 2
            if poly(c) == 0:
                roots.append(c)
                return roots
            if poly(c) * poly(a) < 0:
                b = c
            else:
                a = c
        roots.append(a)
        roots.append(b)
        return roots
    # Find all the eigenvalues
    eigenvalues = []
    for i in range(m):
        for j in range(i+1, m):
            roots = bisection(matrix[i][i], matrix[j][j])
            for root in roots:
                if root is not None:
                    print(root)
                    eigenvalues.append(root)
    return eigenvalues

# Test the function
eigenvalues = find_eigenvalues(matrix)
print("Matrix:\n", np.array(matrix))
print("Eigenvalues:", eigenvalues)
