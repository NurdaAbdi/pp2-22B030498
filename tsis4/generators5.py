def down(max = 0):
    n = int(input())
    while n >= max:
        yield n
        n -=1
a = down()
for i in a:
    print(i)