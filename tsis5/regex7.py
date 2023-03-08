import re
str1 = input()
def snakeToCamel(str1):
    result = ''.join(x.capitalize() or '_' for x in str1.split('_'))
    print(result)
snakeToCamel(str1)