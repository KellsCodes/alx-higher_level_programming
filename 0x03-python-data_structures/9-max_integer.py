#!/usr/bin/python3

def max_integer(my_list=[]):
    if !my_list:
        return None
    largest = 0
    for num in my_list:
        if num > largest:
            largest = num
        continue
    return largest
