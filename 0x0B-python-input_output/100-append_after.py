#!/usr/bin/python3
""" module search and insert file"""


def append_after(filename="", search_string="", new_string=""):
    """function that search for specific string then
        insert specific string after this line
        Parameters:
            filename: file we search in it
            search_string: string we look if present or not
            new_string: new string will added
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as fi:
        for line in fi.readlines():
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as fi:
        offset = 0
        for i in lines:
            fi.seek(offset, 0)
            fi.write(i)
            offset += len(i)
