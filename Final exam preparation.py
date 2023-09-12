import numpy as np

def ludec(mat_t):
    new_T=np.copy(mat_t)
    UT=new_T.copy()
    LT=np.identity(new_T.shape[0])
    p=0
    for j in range(UT.shape[0]-1):
        k = np.argmax(np.abs(UT[j:,j])) + j
        if k != j:
            p=p+1
            UT[j,:], UT[k,:] = UT[k,:], UT[j,:].copy()
        coefficient=0
        for i in range(j+1,new_T.shape[0]):
            coefficient=UT[i][j]/UT[j][j]
            UT[i]-=coefficient*UT[j]
            LT[i][j]=coefficient
        A=np.diagonal(UT)
        det=(-1)**(p)
        for elements in A:
            det*=elements
    return [UT,LT,det]



def lu_pivot(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.copy(A)
    p = 0  # number of row interchanges
    for j in range(n - 1):
        k = np.argmax(np.abs(U[j:, j])) + j
        if k != j:
            p = p + 1
            U[[j, k], :] = U[[k, j], :]

        for i in range(j + 1, n):
            coeff = U[i,j] / U[j, j]
            U[i] = U[i] - coeff * U[j, j:]
            L[i, j] = coeff

    det = ((-1) ** p)
    for i in range(n):
        det *= U[i, i]

    return L, U, det


B = np.array([[1, 2], [3, 4]])
L, U, det = lu_pivot(B)
print("U:")
print(U)
print("L:")
print(L)
print("det:", det)