#!/usr/bin/python3
"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """Method to print first and last name to stdout"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
