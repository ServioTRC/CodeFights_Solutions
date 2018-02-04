def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft >= yourRight:
        val = yourLeft
        valO = yourRight
    else:
        val = yourRight
        valO = yourLeft
    if friendsLeft >= friendsRight:
        val2 = friendsLeft
        valO2 = friendsRight
    else:
        val2 = friendsRight
        valO2 = friendsLeft
    return (val==val2) and (valO == valO2)
