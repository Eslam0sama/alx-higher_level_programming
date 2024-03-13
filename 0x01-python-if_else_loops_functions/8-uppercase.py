#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) in range(65, 91)):
            print(char, end="")
        else:
            char = chr(ord(char) - 32)
            print(char, end="")
