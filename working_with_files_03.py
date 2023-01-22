#!/usr/bin/env python3


myfile = "file1.txt"
try:
    file = open(myfile, "a")
except FileNotFoundError as e:
    print("The file was not found.")
    print(e)
    exit(1)

movies = ["The Matrix", "The Lord of the Rings", "The Avengers"]

for m in movies:
    file.write(m + "\n")
file.close()
