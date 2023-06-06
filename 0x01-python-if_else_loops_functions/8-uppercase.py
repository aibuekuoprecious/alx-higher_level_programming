#!/usr/bin/python3

def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")

    print('\n', end="")
