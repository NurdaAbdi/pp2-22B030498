import os
file_path = '/Users/Admin/pp2-22B030498/tsis6/dir/text1.txt'
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    os.remove("text1.txt")