import re
str1 = input()
def camel_to_snake(str1):
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', str1).lower()
    print(result)

camel_to_snake(str1)