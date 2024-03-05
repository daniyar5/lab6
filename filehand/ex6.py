import os
import string
path = "c:/Users/user/Desktop/lab6/filehand/folder2/"
letters = string.ascii_uppercase
for l in letters:
    f = open(path + f"{l}.txt", "x")