#!/usr/bin/python3

roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    i = 0
    sum = 0
    while i < len(roman_string):
        current = roman_num[roman_string[i]]
        next_num = roman_num[roman_string[i + 1]] if i < len(roman_string) - 1 else 0
        if next_num > current:
            sum += next_num - current
            i += 2
        else:
            sum += current
            i += 1
    return sum
