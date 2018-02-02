def addBorder(picture):
    marco = "*"*(len(picture[0])+2)
    complete_pic = [marco]
    for i in picture:
        complete_pic.append("*"+i+"*")
    complete_pic.append(marco)
    return complete_pic
