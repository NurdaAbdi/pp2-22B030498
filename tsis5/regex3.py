import re
str1 = input()
def lower_under(str1):
    pattern = r'[a-z]+_[a-z]+\b'
    str2 = re.findall(pattern, str1)
    return 