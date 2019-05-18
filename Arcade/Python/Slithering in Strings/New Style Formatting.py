import re

def newStyleFormatting(s):
    s = s.replace("%%", "?")
    s2 = re.sub(r'%[bcedfgnosx]', '{}', s)
    return s2.replace("?", "%")
