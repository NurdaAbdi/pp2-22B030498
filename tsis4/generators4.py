a = int(input())
b = int(input())
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
        i+=1
x = squares(a,b)
for i in x:
    print(i)
