import os


path_to_file =  "c:/Users/user/Desktop/lab6/filehand/ex2.py"
print(os.path.exists(path_to_file))


f = open(path_to_file, "r")
print(f.read())


f = open(path_to_file, "a")
f.write("\n#This is just a test")
f.close()
#This is just a test

with open(path_to_file, "x") as file:
    pass

#This is just a test



