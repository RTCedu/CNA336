# This script opens a file for reading. If it doesn't exist it creates the file and then opens it.
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018
import os

file_name = "test.txt"

file = 0
try:
    file = open(file_name, "r")
    print (file.read())
except FileNotFoundError:
    print("File not found, it will be created.")
    file = open(file_name, "w")
    file.write("")
    file.close()
file = open(file_name, "r")
print (file.read())
