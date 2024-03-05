import os

f1 = "c:/Users/user/Desktop/lab6/filehand/ex6.py"
f2 = "c:/Users/user/Desktop/lab6/filehand/ex7.py"

fileManager = open(f1, "r")
texts = fileManager.readlines() #we saved content from the first file
fileManager.close()


fileManager = open(f2, "a")
for i in texts: #i is one readline
    fileManager.write("\n" + i) #simply write all realdlines from texts to our second file 
fileManager.close()

