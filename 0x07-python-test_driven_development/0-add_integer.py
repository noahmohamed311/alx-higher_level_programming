#!/usr/bin/python3
"""Module for one function to get sum of two variables
   can be either integers or floats, but floats must
   be casted into integers.
   Returns sums of the two integers.
   """


def add_integer(a, b=98):
    """Method in which to get sum of two integers given
       Checking if a or b is an int or float
       Returning sum casted into an integer"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
