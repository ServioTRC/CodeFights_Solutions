import re

def getCommit(commit):
    return re.sub(r"([0\?+!]*)", "", commit)

print(getCommit("0??+0+!!someCommIdhsSt"))