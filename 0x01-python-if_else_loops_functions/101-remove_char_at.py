#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    new_str = ""
    for ch in range(len(str)):
        if ch != n:
            new_str += str[ch]
    return new_str
