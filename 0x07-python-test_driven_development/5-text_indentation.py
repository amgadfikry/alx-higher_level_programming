#!/usr/bin/python3
""" function split string accoeding specific characters"""


def text_indentation(text):
    """function that split string accord characters . : ?
        Parameters:
            text: input string want to split
        Raises:
            TypeError: if input not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    if text == "":
        print("")
    txt = ""
    for i in text:
        if i in [":", ".", "?"]:
            txt += i
            print(f"{txt.strip()}\n")
            txt = ""
            continue
        txt += i
