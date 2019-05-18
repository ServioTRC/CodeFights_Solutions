def constructShell(n):
    return [[0 for _ in range(i)] for i in range(1, n+1)] + [[0 for _ in range(i)] for i in range(n-1, 0, -1)]
print(constructShell(3))