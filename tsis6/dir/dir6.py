for i in range(65, 91):
    letter = chr(i)
    file_name = letter + '.txt'
    with open(file_name, 'w') as file:
        file.write(f'This is file {file_name}.\n')
    print(f'File {file_name} created.')
