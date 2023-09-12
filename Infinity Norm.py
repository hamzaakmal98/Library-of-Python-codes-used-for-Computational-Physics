# define a test matrix
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# calculate the Infinity norm
infinity_norm = 0
for row in test_matrix:
    row_sum = sum(abs(element) for element in row)
    if row_sum > infinity_norm:
        infinity_norm = row_sum

# print the result
print("The Infinity norm of the test matrix is:", infinity_norm)
