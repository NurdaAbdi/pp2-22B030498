file_path = '/Users/Admin/pp2-22B030498/tsis6/text.txt'
file_name = '/Users/Admin/pp2-22B030498/tsis6/text_copy.txt'
with open(file_path, 'r') as file,open(file_name, 'w') as file1:
    file1.write(file.read())
print('Completed succesfully')