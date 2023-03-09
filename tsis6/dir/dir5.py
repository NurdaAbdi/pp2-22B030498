file_path = '/Users/Admin/pp2-22B030498/tsis6/text.txt'

list = ['anime', 'nothing']

with open(file_path, 'w') as file:
    for word in list:
        file.write(word + ', ')

print('COMPLETED')