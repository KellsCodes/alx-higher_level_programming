#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    key = ""

    for k, v in a_dictionary.items():
        if v > score:
            key, score = k, v
    return key
