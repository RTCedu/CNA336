import os

rel_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(rel_path, "../")

file = 0
try:
    file = open(path, "r")
    print (file.read())
except FileNotFoundError:
    print("File not found, it will be created.")
    file = open(path, "w")
    file.write("")
    file.close()
file = open(path, "r")
print (file.read())
