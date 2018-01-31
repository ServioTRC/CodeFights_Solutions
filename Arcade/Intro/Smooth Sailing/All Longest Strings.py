def allLongestStrings(inputArray):
    current_length = len(inputArray[0])
    res = []
    res.append(inputArray[0])
    for i in range(1, len(inputArray)):
        length = len(inputArray[i])
        if current_length < length:
            current_length = length
            res.clear()
            res.append(inputArray[i])
        elif current_length == length:
            res.append(inputArray[i])
    return res
