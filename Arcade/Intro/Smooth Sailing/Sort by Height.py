def sortByHeight(a):
    heights = []
    for i in a:
        if i != -1:
            heights.append(i)
    heights.sort(reverse=True)
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = heights.pop()
    return a
