def areSimilar(a, b):
    for e in b:
        if e not in a:
            return(False)

    change = False
    num = len(a)
    for i in range(num):
        if a[i] != b[i]:
            if not change:
                for j in range(i+1, num):
                    if b[j] == a[i] and b[j] != a[j]:
                        b[j], b[i] = b[i], b[j]
                        break
                    if j == num-1:
                        return(False)
                change = True
            else:
                return(False)
    return(True)
