# define a test matrix
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# calculate the Euclidean norm
sum_of_squares = 0
for row in test_matrix:
    for element in row:
        sum_of_squares += element**2

euclidean_norm = sum_of_squares**0.5

# print the result
print("The Euclidean norm of the test matrix is:", euclidean_norm)
