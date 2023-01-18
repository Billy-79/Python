#!/usr/bin/env python3


while True:
    try:
        age = int(input("Enter your age:\n"))
        break

    except ValueError:
        print("Invalid Input. Please enter a number as your age.\nTry again.")

print("You are " + str(age) + " years old.")

age2 = int(age) + 50

print("In 50 years, you will be " + str(age2) + " years old.")
