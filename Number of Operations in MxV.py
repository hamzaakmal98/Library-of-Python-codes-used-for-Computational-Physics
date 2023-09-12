# # When multiplying a n × n matrix with a n-dimensional vector, you are carrying out n^2 multiplications and (n^2 -
# n) additions. Therefore, the total number of floating-point operations (
# additions/subtractions/multiplications/divisions) required to perform the matrix-vector multiplication is: # # n^2
# + (n^2 - n) = 2n^2 - n # # So, the total number of floating-point operations required to multiply a n × n matrix
# with a n-dimensional vector is 2n^2 - n.
#
# When multiplying a n × n matrix with a m × m matrix, you are carrying out n^2 × m multiplications and n^2 × (m - 1)
# additions/subtractions. Therefore, the total number of floating-point operations required to perform the
# matrix-matrix multiplication is:
#
# n^2 × m + n^2 × (m - 1) = n^2 × m + n^2 × m - n^2 = 2n^2 × m - n^2
#
# So, the total number of floating-point operations required to multiply a n × n matrix with a m × m matrix is 2n^2 ×
# m - n^2.
