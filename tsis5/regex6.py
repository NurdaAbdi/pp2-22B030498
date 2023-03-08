import re
str1 = input()
pattern = '\s+'
pattern1 = '\,'
pattern2 = '\.'
replace = ':'
str2 = re.sub(pattern, replace, str1)
str2 = re.sub(pattern1, replace, str2)
str2 = re.sub(pattern2, replace, str2)
print(str2)