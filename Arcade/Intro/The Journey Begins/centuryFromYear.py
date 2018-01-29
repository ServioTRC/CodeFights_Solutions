def centuryFromYear(year):
    extra = year // 100
    if year % 100 != 0:
        extra += 1
    return extra