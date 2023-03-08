import re

string = input("Enter a string: ")
pattern = r'ab*'

if re.match(pattern, string):
    print("found")
else:
    print("not found")