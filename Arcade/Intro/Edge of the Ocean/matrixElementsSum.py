def matrixElementsSum(matrix):
    res = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                break
            else:
                res += matrix[j][i]
    return res