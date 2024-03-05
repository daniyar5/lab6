import os
path = "c:/Users/user/Desktop/lab6/myfile.txt"

if os.access(path, os.F_OK) and os.access(path, os.R_OK):
  os.remove(path)
else:
  print("The file does not exist")
