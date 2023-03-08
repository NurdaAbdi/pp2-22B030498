str1 = input()
def test(str1):
    if re.search("(a)b{2,3}", str1):
        print('Yes')
    else:
        print('No')

test(str1)