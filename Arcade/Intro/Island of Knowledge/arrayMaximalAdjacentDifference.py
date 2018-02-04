def arrayMaximalAdjacentDifference(inputArray):
    dif = abs(inputArray[0]- inputArray[1])
    for i in range(1, len(inputArray)-1):
        num = abs(inputArray[i]- inputArray[i+1])
        if dif < num:
            dif = num
    return(dif)
