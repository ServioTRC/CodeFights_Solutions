def isIPv4Address(inputString):
    dirs = inputString.split(".")
    if len(dirs) != 4:
        return(False)
    else:
        for i in dirs:
            if i == "" or not i.isnumeric():
                return(False)
            elif 0 <= int(i) <= 255:
                continue
            else:
                return(False)
    return(True)
