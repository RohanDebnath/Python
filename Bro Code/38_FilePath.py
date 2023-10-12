import os
fpath="C:\\Users\\USER\\Desktop\\textfile.txt"
if os.path.exists(fpath):
    print("File exists")
else:
    print("Don't exists")
if os.path.isfile(fpath):
    print("It is a file")
if os.path.isdir(fpath):
    print("It is a directory")    
