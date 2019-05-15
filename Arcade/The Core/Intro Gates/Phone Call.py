def phoneCall(min1, min2_10, min11, s):
    res = 0
    while True:
        res += 1
        if res == 1:
            s -= min1
        elif 1 < res <= 10:
            s -= min2_10
        else:
            s-= min11
        
        if s < 0:
            return(res-1)
        elif s == 0:
            return(res)
