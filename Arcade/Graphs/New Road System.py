def adding(roads):
    rows = []
    columns = []
    for i in range(len(roads)):
        count = 0
        for j in range(len(roads[i])):
            if roads[i][j]:
                count += 1
        rows.append(count)
    
    for i in range(len(roads[i])):
        count = 0
        for j in range(len(roads)):
            if roads[j][i]:
                count += 1
        columns.append(count)
    return rows, columns

def newRoadSystem(roadRegister):
    rows, columns = adding(roadRegister)
    for i in range(len(roadRegister)):
        if rows[i] != columns[i]:
            return False
    return True


roadRegister = [[False, True,  False, False],
                [False, False, True,  False],
                [True,  False, False, True ],
                [False, False, True,  False]]
roadRegister = [[False, True,  False],
                [False, False, False],
                [True,  False, False]]
print(newRoadSystem(roadRegister))