#!/usr/bin/env python3


def my_function():
    """This is a sample function.
    We're going to declare a variable 
    inside this function.
    """
    global message
    message = "Hello World!"
    print(message)

my_function()

print(message)
