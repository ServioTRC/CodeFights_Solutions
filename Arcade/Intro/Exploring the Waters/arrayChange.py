def arrayChange(inputArray):
    res = 0
    i = 1
    while i < len(inputArray):
        if inputArray[i-1] >= inputArray[i]:
            num = inputArray[i-1] - inputArray[i] + 1
            res += num
            inputArray[i] += num
        else:
            i += 1
    return res
