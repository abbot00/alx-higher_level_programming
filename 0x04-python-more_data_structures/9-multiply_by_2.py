#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic2 = a_dictionary.copy()
    l_keys = list(dic2.keys())
    for i in l_keys:
        dic2[i] *= 2
    return (dic2)
