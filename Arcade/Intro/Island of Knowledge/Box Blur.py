def boxBlur(image):
    new_image = []
    for i in range(len(image)):
        res = []
        for j in range(len(image[0])):
            if 0 < i < len(image)-1 and 0 < j < len(image[0])-1:
                suma = 0
                for e in range(-1, 2):
                    for h in range(-1, 2):
                        suma += image[i-e][j-h]
                suma //= 9;
                res.append(suma)
        if len(res) != 0:
            new_image.append(res)
    return(new_image)
