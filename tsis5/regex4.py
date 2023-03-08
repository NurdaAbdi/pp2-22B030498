import re
str1 = input()
def sequence(str1):
    pattern = r'[A-Z][a-z]+'
    str2 = re.findall(pattern, str1)
    return str2

print(sequence(str1))