#!/usr/bin/python3
""" this module contains an
illustration of inheritance in python"""


class MyList(list):
    """ class that inherits from the list class"""
    def print_sorted(self):
        """prints the list in ascending sorted order
        """

        sorted_list = sorted(self)
        print(sorted_list)
