#!/usr/bin/python3

def no_c(my_string):
    chars = ""
    for char in my_string:
        if (char == "c" or char == "C"):
            continue
        chars += char

    return chars
