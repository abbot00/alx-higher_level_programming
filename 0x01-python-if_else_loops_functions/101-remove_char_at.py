#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    i = 0
    new_str = ""
    for ch in range(len(str)):
        if i != n:
            new_str += ch
    return new_str
