#!/usr/bin/python3
def roman_to_int(roman_string):
    dec, int = 0, 0
    if roman_string and type(roman_string) is str:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(roman_string) - 1, -1, -1):
            if rom[roman_string[i]] >= dec:
                int += rom[roman_string[i]]
            else:
                int -= rom[roman_string[i]]
            dec = rom[roman_string[i]]
        return int
    return int
