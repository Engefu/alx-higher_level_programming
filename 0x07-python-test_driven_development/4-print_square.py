#!/usr/bin/python3
"""
function that prints a square with the character #
size is the size length of the square
size must be an int
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
