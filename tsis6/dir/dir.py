import os
path = '/Users/Admin/pp2-22B030498'
files = os.listdir(path)
print(len(files))




n = int(5)
print([i for i in range (10,10000000) if i%n==0])