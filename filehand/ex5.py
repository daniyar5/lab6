import os

path = "myfile.txt"

mylist = ["Daniyar", "Maksim", "Olzhas"]

with open(path, 'w') as file:
        for i in mylist:
            file.write(str(i) + '\n')

