#!/usr/bin/env python3


import os

print("\n" + "Your current working directory is: " + os.getcwd() + "\n\n")

print("The contents of this directory are:""\n")
os.system("ls -laFh --color=auto")
