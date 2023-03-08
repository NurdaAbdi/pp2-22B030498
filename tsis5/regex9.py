import re
str1 = input()
def insertSpaces(str1):
    str2 = re.sub(r"(?<!^)(?=[A-Z])", " ", str1)
    print(str2)
insertSpaces(str1)