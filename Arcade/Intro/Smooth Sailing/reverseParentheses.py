def reverseParentheses(s):
    parentesis = []
    num = len(s)
    s1 = list(s)
    for i in range(num):
        if s1[i] == "(":
            parentesis.append(i)
        elif s1[i] == ")":
            pos = parentesis.pop()
            s1[pos+1:i] = s1[i-1:pos:-1]
    for i in range(num):
        if s1[i] == "(" or s1[i] == ")":
            s1[i] = ""
    return(''.join(s1))
 