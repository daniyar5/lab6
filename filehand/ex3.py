import os

path_to_file = "c:/Users/user/Desktop/lab6/filehand/ex3.py"
if(os.path.exists(path_to_file)):
    print(os.path.basename(path_to_file))
    print(os.path.basename(os.getcwd()))
else:
    print("File does not exist")