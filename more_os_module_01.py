#!/usr/bin/env python3


import os

file = "myfile.txt"

if os.path.isfile(file):
    print("The file exists.")
else:
    print("The file does not exist.")
