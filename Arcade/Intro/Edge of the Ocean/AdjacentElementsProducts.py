def adjacentElementsProduct(inputArray):
    val = inputArray[0]*inputArray[1]
    for pos in range(2,len(inputArray)):
        mul = inputArray[pos-1]*inputArray[pos]
        if mul > val:
            val = mul
    return val
