import re
str1 = input()
def split(str1):
    str2 = re.findall('[A-Z][^A-Z]*', str1)
    return ' '.join(str2)
print(split(str1))