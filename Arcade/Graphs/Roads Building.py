def create_matrix(cities, roads):
    matrix = [[False for _ in range(cities)] for _ in range(cities)]
    for road in roads:
        matrix[road[0]][road[1]] = True
        matrix[road[1]][road[0]] = True
    return(matrix)

def roadsBuilding(cities, roads):
    matrix = create_matrix(cities, roads)
    res = []
    for i in range(cities):
        for j in range(cities):
            if i != j and not matrix[i][j]:
                matrix[i][j] = True
                matrix[j][i] = True
                res.append(sorted([i, j]))
    return(res)


roads = [[0, 1], [1, 2], [2, 0]]
roadsBuilding(4, roads)
cities = 4
