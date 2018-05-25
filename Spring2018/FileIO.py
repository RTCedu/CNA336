# This script opens a file for reading. If it doesn't exist it creates the file and then opens it.
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018
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
