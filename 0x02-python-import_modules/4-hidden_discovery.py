#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    l_name = names.split()
    for word in l_name:
        if word[0] != '_' and word[1] != '_':
            print(word)
