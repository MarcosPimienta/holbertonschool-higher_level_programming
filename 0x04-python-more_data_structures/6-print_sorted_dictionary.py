#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydictio = a_dictionary
    for key in sorted(mydictio.keys()):
        print("{}: {}".format(key, mydictio[key]))
