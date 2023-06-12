#!/usr/bin/python3
""" module that get list and print it in sorted one"""


class MyList(list):
    """ class inhertet from list obj
        Inheretance:
            list: list object
    """

    def print_sorted(self):
        """functon print sorted list"""

        print(sorted(self))
