#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    i = 0
    sum_total = 0
    while i < len(roman_string):
        current = roman_num[roman_string[i]]
        next_num = roman_num[roman_string[i + 1]] if i < len(roman_string) - 1 else 0
        if next_num > current:
            sum_total += next_num - current
            i += 2
        else:
            sum_total += current
            i += 1
    return sum_total
