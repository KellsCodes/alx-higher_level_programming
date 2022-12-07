#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    for num in uniq(my_list):
        sum += num
    return sum

def uniq(my_list=[]):
    uniq_nums = []
    for current in my_list:
        count = 0
        for check in uniq_nums:
            if current == check:
                count += 1
        if not count:
            uniq_nums.append(current)
    return uniq_nums
