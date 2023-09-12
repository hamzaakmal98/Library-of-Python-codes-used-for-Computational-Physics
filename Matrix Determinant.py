def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det_sum = 0
        for j in range(n):
            sign = (-1) ** j
            sub_matrix = []
            for i in range(1, n):
                row = []
                for k in range(n):
                    if k != j:
                        row.append(matrix[i][k])
                sub_matrix.append(row)
            det_sum += sign * matrix[0][j] * det(sub_matrix)
        return det_sum


matrix = [[1, 2, 2, 1],
          [2, 3, 4, 1],
          [1, 0, 2, 1],
          [2, 1, 2, 2]]

det_matrix = det(matrix)
print(det_matrix)
