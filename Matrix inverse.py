def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [[A[i][k] for k in range(n) if k != j] for i in range(1, n)]
            det += (-1)**j * A[0][j] * determinant(minor)
        return det


def invert_matrix(A):
    n = len(A)
    det = determinant(A)
    if det == 0:
        return None
    # create an identity matrix of the same size as A
    B = [[0.0] * n for i in range(n)]
    for i in range(n):
        B[i][i] = 1.0
    # perform row operations on A and B to turn A into the identity matrix
    for i in range(n):
        # find the row with the largest absolute value in column i
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        # swap row i with the row with the largest absolute value in column i
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            B[i], B[max_row] = B[max_row], B[i]
        # normalize row i to have a leading 1
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        for j in range(n):
            B[i][j] /= factor
        # use row i to eliminate the leading entries in all other rows
        for j in range(n):
            if i != j:
                factor = A[j][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                for k in range(n):
                    B[j][k] -= factor * B[i][k]

    return B


# Test case
A = [[1, 2, 1],
     [2, 1, 2],
     [-1, 2, 1]]

print("Original matrix A:")
for row in A:
    print(row)

B = invert_matrix(A)

if B is None:
    print("Matrix is not invertible")
else:
    print("Inverse of matrix A:")
    for row in B:
        print([round(elem, 3) for elem in row])
