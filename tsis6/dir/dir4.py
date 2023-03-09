file_path = '\Users\Admin\pp2-22B030498\tsis6\text.txt'
count = 0
with open(file_path, 'r') as file:
    for line in file:
        count+=1

print(f'The number of lines is: {count}')
