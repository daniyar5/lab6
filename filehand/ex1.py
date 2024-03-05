import os 

dirs_list = os.listdir()
print("Only directories: ")
for dir in dirs_list:
    if os.path.isdir(dir):
        print(dir)
    
print("All files and directories: ", os.listdir())

dirs_list = os.listdir()
print("Files with specified path: ")
for dir in dirs_list:
    if os.path.isfile(dir):
        print(os.path.realpath(dir))
        print("-------")
    