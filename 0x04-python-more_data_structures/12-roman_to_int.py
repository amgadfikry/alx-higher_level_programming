#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for idx, x in enumerate(roman_string):
        for key, val in roman.items():
            if x == key:
                res += roman[key]
                if idx != 0 and roman[roman_string[idx - 1]] < roman[key]:
                    res -= roman[roman_string[idx - 1]] * 2
    return res
