def makeArrayConsecutive2(statues):
    statues.sort()
    res = 0
    for i in range(1, len(statues)):
        dif = statues[i] - statues[i-1] 
        if dif > 1:
            res += dif - 1
    return res