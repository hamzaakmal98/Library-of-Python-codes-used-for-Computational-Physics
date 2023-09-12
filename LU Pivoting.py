import numpy as np


def lu_pivot(A):
    n = A.shape[0]
    P = np.eye(n, dtype=np.float64)
    L = np.zeros((n, n), dtype=np.float64)
    U = np.copy(A).astype(np.float64)
    swaps = 0

    for k in range(n):
        # Find pivot index
        i_max = np.argmax(abs(U[k:, k])) + k

        # If pivot is zero, matrix is singular
        if U[i_max, k] == 0:
            raise ValueError("Matrix is singular.")

        # Swap rows to pivot
        if i_max != k:
            P[[k, i_max], :] = P[[i_max, k], :]
            U[[k, i_max], k:] = U[[i_max, k], k:]
            swaps += 1

        # Calculate L and U entries
        L[k:, k] = U[k:, k] / U[k, k]
        U[k + 1:, k:] -= L[k + 1:, k][:, np.newaxis] * U[k, k:]

    # Set diagonal of L to 1
    np.fill_diagonal(L, 1)

    return P, L, U, swaps


def det_pivot(A):
    P, L, U, swaps = lu_pivot(A)
    n = A.shape[0]
    return ((-1) ** swaps) * np.prod(np.diag(U))


# Test case 1
A = np.array([
    [1, 3, 5],
    [2, 4, 7],
    [1, 1, 0]
])

P, L, U, swaps = lu_pivot(A)
print("P =\n", P)
print("L =\n", L)
print("U =\n", U)
print("Number of row swaps:", swaps)

det = det_pivot(A)
print("Determinant of A:", det)

# Test case 2
A = np.array([
    [1, 1, 1],
    [1, 2, 3],
    [1, 3, 6]
])

P, L, U, swaps = lu_pivot(A)
print("P =\n", P)
print("L =\n", L)
print("U =\n", U)
print("Number of row swaps:", swaps)

det = det_pivot(A)
print("Determinant of A:", det)
