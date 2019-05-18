def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])

print(twoTeams([1, 11, 13, 6, 14]))