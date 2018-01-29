def checkPalindrome(inputString):
    if len(inputString) == 1:
        return(True)
    j = len(inputString)-1
    for i in range(len(inputString)):
        if i > j:
            return(True)
            break
        else:
            if inputString[i] != inputString[j]:
                return(False)
                break
            else:
                j -= 1
