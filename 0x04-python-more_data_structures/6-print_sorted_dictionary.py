#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary != 0:
        for key in sorted(a_dictionary):
                print("{}: {}".format(key, a_dictionary[key]))
