import os
PATH = "E:\\Musikote"

for file in os.walk(PATH):
    print(file)
    break