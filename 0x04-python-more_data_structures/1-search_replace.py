#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = list(my_list)
    for idx, i in enumerate(my_list):
        if i == search:
            newlist[idx] = replace
    return (newlist)
