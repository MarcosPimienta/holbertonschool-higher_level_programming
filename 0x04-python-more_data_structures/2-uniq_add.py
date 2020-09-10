#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumnum = 0
    nlist = set(list(my_list))
    for i in nlist:
        sumnum = sumnum + i
    return (sumnum)
