n = int(input())
def div(n):
    for i in range(0, n+1):
        if i%3 == 0 or i%4 == 0:
         yield i
         i+=1
a = div(n)
for i in a:
    print(i)
