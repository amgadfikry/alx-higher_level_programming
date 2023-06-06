#!/usr/bin/python3
""" class which looked to dunamic attributes"""


class LockedClass:
    """ class that has no attributes and no dunamic ones"""

    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """check if dynamic attribution set and prevent it
            if not first_name
            Parameters:
                name: name of attribute
                value: value of attribute
            Raises:
                AttributeError: if not equal to attribute in slots
        """
        text = f"'LockedClass' object has no attribute '{name}'"
        if name not in LockedClass.__slots__:
            raise AttributeError(text)
