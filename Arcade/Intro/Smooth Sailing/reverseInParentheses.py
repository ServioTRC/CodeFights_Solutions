def reverse_inside_parentheses(word):
    stack = []
    last = len(word)
    for index, letter in enumerate(word):
        if letter == "(":
            stack.append(letter)
        elif stack and letter == ")":
            stack.pop()
        if len(stack) == 0 and index - 1 >= 0:
            last = index
            break
    result = list(word[1:last])
    result.reverse()
    for index, letter in enumerate(result):
        if letter == "(":
            result[index] = ")"
        elif letter == ")":
            result[index] = "("
    # print("salida", result)
    return ''.join(result) + word[last+1:]
        

def reverseInParentheses(inputString):
    while True:
        val = inputString.find("(")
        if val <= -1:
            break
        previo = inputString[:val]
        inputString = previo + reverse_inside_parentheses(inputString[val:])
    return inputString
