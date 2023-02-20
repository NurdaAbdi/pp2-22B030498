def evens(max = 0):
    n = int(input())
    for i in range(n):
        if i % 2 == 0:
         yield i
a = evens()
for i in a:
    print(i, sep = ", ")
