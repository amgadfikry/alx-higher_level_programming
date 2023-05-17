#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    h_key = ""
    score = 0
    for key, val in a_dictionary.items():
        if val > score:
            score = val
            h_key = key
    return h_key
