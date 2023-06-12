#!/usr/bin/python3
""" module class from int with"""


class MyInt(int):
    """class that inheret from int with some manipulation"""

    def __eq__(self, other):
        """ function that check equality"""

        return False

    def __ne__(self, other):
        """function check none equality """

        return True
