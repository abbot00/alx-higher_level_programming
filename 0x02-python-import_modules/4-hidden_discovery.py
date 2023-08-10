#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    s_name = names.sort()
    for word in s_name:
        if word[0] != '_' and word[1] != '_':
            print(word)
