def avoidObstacles(inputArray):
    salto = 1
    pos = 0
    maximo = max(inputArray)
    while True:
        termino = True
        pos = salto
        while pos <= maximo:
            if pos in inputArray:
                termino = False
                break
            pos += salto
        if termino:
            return(salto)
        else:
            salto += 1
