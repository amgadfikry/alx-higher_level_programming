#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    tup = (len_str, char)
    return tup
