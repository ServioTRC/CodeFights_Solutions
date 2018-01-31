def commonCharacterCount(s1, s2):
    lista1 = [0 for _ in range(26)]
    lista2 = [0 for _ in range(26)]
    res = 0
    for i in s1:
        lista1[ord(i)-97] += 1
    for i in s2:
        lista2[ord(i)-97] += 1
    for i in range(26):
        if lista1[i] != 0 and lista2[i] != 0:
            if lista1[i] > lista2[i]:
                res += lista2[i]
            else:
                res += lista1[i]
    return res
