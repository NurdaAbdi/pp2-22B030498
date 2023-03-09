import os
path = '\Users\Admin\pp2-22B030498'

print('Directories:')
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

print('\nFiles:')
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)
print('\nAll directories and files:')
for item in os.listdir(path):
    print(item)
