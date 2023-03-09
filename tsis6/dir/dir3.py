import os
path = '\Users\Admin\pp2-22B030498'
if os.path.exists(path):
    print(f'{path} exists')  


    filename = os.path.basename(path)
    directory = os.path.dirname(path)


    print(f'Filename {filename}')
    print(f'dirname {directory}')
    

else:
    print(f'{path} does not exist')