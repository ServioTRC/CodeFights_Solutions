def minesweeper(matrix):
    matrix_res = []
    for i in range(len(matrix)):
        res = []
        for j in range(len(matrix[0])):
            suma = 0
            if matrix[i][j] == 1:
                suma -= 1
            for e in range(-1, 2):
                for h in range(-1, 2):
                    if 0 <= (i-e) < len(matrix) and 0 <= (j-h) < len(matrix[0]) and matrix[i-e][j-h] == 1:
                        suma += 1
            res.append(suma)
        matrix_res.append(res)
    return(matrix_res)
