# create a 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# create a new matrix to store the transpose
transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# iterate through rows of the original matrix
for i in range(len(matrix)):
    # iterate through columns of the original matrix
    for j in range(len(matrix[0])):
        # assign the element at position (i,j) to the element at position (j,i) in the transpose matrix
        transpose[j][i] = matrix[i][j]

# print the transpose matrix
for row in transpose:
    print(row)
