def palindromeRearranging(inputString):
    letras = [0 for _ in range(26)]
    for i in inputString:
        letras[ord(i.lower())-97] += 1
    impar = False
    if len(inputString) % 2 != 0:
        impar = True
    for val in letras:
        if val % 2 != 0:
            if impar:
                impar = False
            else:
                return(False)
    return(True)
