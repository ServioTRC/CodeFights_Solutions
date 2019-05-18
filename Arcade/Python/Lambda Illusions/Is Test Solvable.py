def isTestSolvable(ids, k):
    digitSum = lambda id: sum([int(x) for x in str(id)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
