#!/usr/bin/env python3


age = input("Please enter your age: ")

if int(age) >= 50:
    print("You are 50 or older.")
elif int(age) >= 25:
    print("You are 25 or older.")
elif int(age) >= 18:
    print("You are an adult.")
else:
    print("You are not even an adult.")

print("This will always print.")
