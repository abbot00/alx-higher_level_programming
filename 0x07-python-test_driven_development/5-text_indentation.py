#!/usr/bin/python3
"""function that prints lines"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The text to be processed.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text = "Hello. How are you? I'm good: Thanks!"
        >>> text_indentation(text)
        Hello.
        How are you?
        I'm good:
        Thanks!
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize variables
    special_chars = ['.', '?', ':']
    lines = []
    current_line = ''

    # Process each character
    for char in text:
        current_line += char
        if char in special_chars:
            lines.append(current_line.strip())
            current_line = ''

    # Print formatted lines
    for line in lines:
        print(line)



text_indentation("Holberton School")