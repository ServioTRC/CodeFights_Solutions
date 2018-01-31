def isLucky(n):
    num = str(n)
    mitad = len(num)//2
    mitad1 = 0
    mitad2 = 0
    for i in range(len(num)):
        if i < mitad:
            mitad1 += int(num[i])
        else:
            mitad2 += int(num[i])
    return (mitad1 == mitad2)
