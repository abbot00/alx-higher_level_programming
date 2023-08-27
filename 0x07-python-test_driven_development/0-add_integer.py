#!/usr/bin/python3
"""
Adds two integers.

    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Default is 98.

    Returns:
    int: The sum of a and b, after casting to integers if necessary.

    Raises:
    TypeError: If a or b is not an integer or float.

    Example:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    """


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
