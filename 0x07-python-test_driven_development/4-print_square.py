#!/usr/bin/python3
"""Module for method print_square"""


def print_square(size):
    """Method to find area and print a visual square of area"""

    if isinstance(size, (int, float)):
        if isinstance(size, float):
            if size < 0:
                raise TypeError("size must be an integer")
            else:
                for i in range(int(size)):
                    for i in range(int(size)):
                        print("#", end="")
                    print()
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(int(size)):
                for i in range(int(size)):
                    print("#", end="")
                print()
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
